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

## Criar ambiente virtual no Linux

1. Baixar o ambiente virtual:
    ```bash
    pip install virtualenv
    ```

2. Criar o ambiente virtual:
    ```bash
    virtualenv venv
    ```

3. Ativar o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```

## Rodar a aplicação

```bash
python -m uvicorn <nome-do-arquivo-principal>:app --reload
```

## Models vs Schemas

### Schemas no FastAPI

Frequentemente denominado como Pydantic model, são utilizados para a validação de dados e serialização

Eles definem a estrutura e tipo de dado que sua API espera receber (input) ou envia (output)

Diferente do models, eles não se ligam diretamente ao banco de dados, mas são usados para validare coverte entre tipo Python e JSON

### SQLAlchemy models

SQLAlchemy models, por outro lado, se conecta diretamente ao banco de dados

### Diferenças entre `schema` e `model`

No FastAPI, é comum usar o Pydantic schemas para validar e trasferir dados, enquanto o model lida com as interações com o banco de dados
