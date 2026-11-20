# Qualidade de Dados

Material gratuito do QG da Engenharia de Dados. Você recebeu porque comentou **QUALIDADE**.

Validação automática de um arquivo com o Pandera: separa o que está certo do que está errado e gera um relatório.

## Como usar este material

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Rode a validação:

```bash
python validar.py
```

3. Veja os arquivos gerados em `saida/`:
   `pedidos_validos.csv` → segue no pipeline
   `relatorio_erros.csv` → o que falhou, em qual coluna e por quê

4. Abra [regras.py](regras.py) → é lá que ficam as regras

## O fluxo

```
dados/pedidos.csv → regras (Pandera) → válidos segue no pipeline
                                     → inválidos vai para o relatório
```

## As 6 dimensões de qualidade

| Dimensão | Pergunta | Regra no projeto |
|---|---|---|
| Completude | Tem valor vazio onde não pode? | `cliente` obrigatório |
| Unicidade | Tem chave repetida? | `id` único |
| Validade | O valor segue a regra? | `valor > 0`, `status` na lista |
| Formato | O texto está no padrão? | `email` com @ e domínio |
| Consistência | Os dados batem entre si? | `data_entrega >= data_pedido` |
| Atualidade | O dado é recente? | `data_pedido` não está no futuro |

## Checklist para qualquer pipeline

- [ ] Validar na entrada, antes de transformar
- [ ] Separar inválidos em vez de apagar
- [ ] Gerar relatório com o motivo do erro
- [ ] Parar o pipeline se o erro passar de um limite
- [ ] Avisar o time dono da origem

## Desafio

Faça o `validar.py` parar com erro se mais de 20% das linhas forem inválidas.

## QG da Engenharia de Dados

Este material é uma amostra do que você encontra no QG.

→ Trilha completa do zero ao sênior
→ Projetos reais para o portfólio
→ Comunidade para tirar dúvidas

Acesse → [qg-engenharia-de-dados.com.br](https://qg-engenharia-de-dados.com.br)
YouTube → [@gonzagadosdados](https://www.youtube.com/@gonzagadosdados)
