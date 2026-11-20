import pandas as pd
import pandera.pandas as pa

STATUS_VALIDOS = ["pendente", "entregue", "cancelado"]

schema = pa.DataFrameSchema(
    columns={
        "id": pa.Column(int, unique=True),                                   # unicidade
        "cliente": pa.Column(str, nullable=False),                           # completude
        "email": pa.Column(str, pa.Check.str_matches(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$")),  # formato
        "data_pedido": pa.Column(
            "datetime64[ns]", pa.Check.le(pd.Timestamp.now()), coerce=True   # atualidade
        ),
        "data_entrega": pa.Column("datetime64[ns]", coerce=True),
        "status": pa.Column(str, pa.Check.isin(STATUS_VALIDOS)),             # validade
        "valor": pa.Column(float, pa.Check.gt(0)),                           # validade
    },
    checks=[
        # consistência → regra que olha mais de uma coluna
        pa.Check(lambda df: df["data_entrega"] >= df["data_pedido"], name="entrega_depois_do_pedido"),
    ],
)
