"""Valida dados/pedidos.csv e separa válidos de inválidos. Rode: python validar.py"""
from pathlib import Path

import pandas as pd
import pandera.pandas as pa

from regras import schema

df = pd.read_csv("dados/pedidos.csv")
Path("saida").mkdir(exist_ok=True)

try:
    schema.validate(df, lazy=True)       # lazy → junta todos os erros em vez de parar no primeiro
    erros = pd.DataFrame()
except pa.errors.SchemaErrors as e:
    erros = e.failure_cases.copy()
    # Regra que olha várias colunas aparece uma vez por coluna → deixa uma linha só
    erros.loc[erros["schema_context"] == "DataFrameSchema", ["column", "failure_case"]] = ["várias", "linha inteira"]
    erros = erros.drop_duplicates(subset=["column", "check", "index"])[["column", "check", "failure_case", "index"]]

# Linhas com erro (index nulo = erro na coluna inteira, como tipo errado)
linhas_ruins = set(erros["index"].dropna().astype(int)) if not erros.empty else set()

validos = df[~df.index.isin(linhas_ruins)]
validos.to_csv("saida/pedidos_validos.csv", index=False)
erros.to_csv("saida/relatorio_erros.csv", index=False)

print(f"Linhas lidas    → {len(df)}")
print(f"Linhas válidas  → {len(validos)}")
print(f"Linhas com erro → {len(linhas_ruins)}\n")
if not erros.empty:
    print(erros.to_string(index=False))
