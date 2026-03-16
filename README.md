# 🛒 Retail Analytics API

Uma API backend profissional que permite que empresas enviem dados de vendas e recebam análises automáticas sobre o negócio. O sistema funciona como um mini **Business Intelligence**, processando dados de vendas e gerando insights automaticamente.

---

## 🧠 Problema que resolve

Pequenos negócios geralmente têm seus dados de vendas em Excel, CSV ou sistemas simples, mas não sabem analisar esses dados. Esse sistema permite:

1. Enviar dados de vendas
2. Armazenar no banco de dados
3. Processar os dados com Pandas
4. Gerar insights automaticamente

---

## 🚀 Tecnologias utilizadas

- **FastAPI** — framework web
- **PostgreSQL** — banco de dados
- **SQLAlchemy** — ORM
- **Pandas** — análise de dados
- **JWT** — autenticação
- **Passlib + Bcrypt** — hash de senhas

---

## 📦 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/ThiagoZanuz/RetailAnalyticsAPI.git
cd RetailAnalyticsAPI
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/retail_analytics
SECRET_KEY=sua_chave_secreta
```

### 5. Crie o banco de dados

Crie um banco de dados chamado `retail_analytics` no PostgreSQL.

### 6. Rode o servidor

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`

A documentação interativa estará em `http://127.0.0.1:8000/docs`

---

## 🔐 Autenticação

A API utiliza autenticação JWT. Para acessar os endpoints protegidos:

1. Registre um usuário em `POST /auth/register`
2. Faça login em `POST /auth/login`
3. Use o token retornado no header `Authorization: Bearer {token}`

---

## 📋 Endpoints

### Auth
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/auth/register` | Registrar usuário |
| POST | `/auth/login` | Login e geração de token |

### Products
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/products` | Cadastrar produto |
| GET | `/products` | Listar todos os produtos |
| GET | `/products/{id}` | Buscar produto por ID |

### Sales
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/sales` | Registrar uma venda |
| GET | `/sales` | Listar todas as vendas |
| POST | `/sales/upload` | Upload de vendas via CSV |

### Analytics
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/analytics/revenue` | Faturamento total |
| GET | `/analytics/top-products` | Produtos mais vendidos |
| GET | `/analytics/daily-sales` | Vendas por dia |
| GET | `/analytics/average-ticket` | Ticket médio |
| GET | `/analytics/revenue-by-period` | Faturamento por período |
| GET | `/analytics/trend` | Tendência de faturamento por mês |

---

## 📊 Exemplo de CSV para upload

```
date,product,quantity
2026-03-01,Coca-Cola,10
2026-03-02,Coca-Cola,3
```

> O produto precisa estar cadastrado no banco antes do upload. O preço utilizado é o cadastrado no sistema.

---

## 📁 Estrutura do projeto

```
app/
├── main.py
├── api/
│   ├── routes_auth.py
│   ├── routes_products.py
│   ├── routes_sales.py
│   └── routes_analytics.py
├── models/
│   ├── product.py
│   ├── sale.py
│   └── user.py
├── schemas/
│   ├── product_schema.py
│   ├── sale_schema.py
│   └── user_schema.py
├── services/
│   ├── auth_service.py
│   ├── sales_service.py
│   └── analytics_service.py
└── database/
    ├── connection.py
    └── session.py
```

---

## 🔄 Fluxo da aplicação

```
empresa envia dados de vendas
        ↓
API recebe e valida
        ↓
dados são salvos no banco
        ↓
Pandas analisa os dados
        ↓
API retorna métricas e insights
```
