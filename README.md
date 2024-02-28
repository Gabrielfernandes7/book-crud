# CRUD cadastro de livros :book:

## Criar ambiente virtual no Windows

1. Baixar o Python na Microsoft Store

2. Baixar o ambiente virtual por:
    ```bash
    python -m virtualenv venv
    ```
3. Ativar o ambiente virtual no Git bash:
    ```bash
    source venv/Scripts/activate
    ```

## Rodar a aplicação

```bash
python -m uvicorn <nome-do-arquivo-principal>:app --reload
```