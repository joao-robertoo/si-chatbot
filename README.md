<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=009688&center=true&vCenter=true&width=600&lines=SI+Imobili%C3%A1rias+%E2%80%94+Chatbot;Assistente+Sofia+%F0%9F%A4%96+%2B+Groq+%2B+LLaMA+3.1;Desenvolvido+por+Jo%C3%A3o+Roberto" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.1-F55036?style=for-the-badge)
![Status](https://img.shields.io/badge/status-live-22c55e?style=for-the-badge)

<br/>

> **Microsserviço de IA com FastAPI e Groq — Conheça a Sofia, sua assistente virtual imobiliária.**

</div>

---

## 🌟 Sobre o Projeto

O microsserviço de IA da **SI Soluções Imobiliárias** implementa a assistente virtual **Sofia** — especializada em negociação imobiliária, gestão de leads e suporte a corretores em tempo real.

Construído em Python com FastAPI, o serviço se comunica com a API da Groq usando o modelo **LLaMA 3.1**, entregando respostas rápidas, contextuais e sempre em português. O histórico da conversa é mantido a cada requisição, garantindo que a Sofia "lembre" o que foi dito anteriormente.

---

## 🤖 Conheça a Sofia

A Sofia não é um chatbot genérico. Ela foi treinada com um **system prompt especializado** para o universo imobiliário:

- 🏠 Dicas de negociação com leads
- 📊 Suporte na gestão de clientes
- 💡 Estratégias para fechar contratos
- 🗣️ Comunicação sempre em português, objetiva e profissional

---

## 🚀 Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 🧠 **LLM via Groq** | Inferência ultrarrápida com LLaMA 3.1 |
| 💬 **Histórico de conversa** | Contexto mantido entre as mensagens |
| 🏠 **System prompt imobiliário** | Sofia especializada no domínio correto |
| ⚡ **FastAPI assíncrono** | Alta performance e baixa latência |
| 🔍 **Health check** | Endpoint `/health` para monitoramento |
| 🌐 **CORS configurado** | Integração com o frontend sem bloqueios |

---

## 🛠️ Stack Tecnológica

```
Microsserviço de IA
├── Python 3.11+        → Linguagem principal
├── FastAPI             → Framework web assíncrono
├── Groq SDK            → Cliente oficial da API Groq
├── LLaMA 3.1 8B        → Modelo de linguagem (llama-3.1-8b-instant)
├── Uvicorn             → Servidor ASGI de alta performance
└── python-dotenv       → Gerenciamento de variáveis de ambiente
```

---

## 🏗️ Arquitetura

```
┌──────────────────────────────────────────┐
│            si-chatbot :8000              │
│                                          │
│  POST /chat                              │
│  ┌────────────────────────────────────┐  │
│  │  1. Recebe mensagem + histórico    │  │
│  │  2. Monta array de mensagens       │  │
│  │  3. Injeta system prompt Sofia     │  │
│  │  4. Envia para Groq API            │  │
│  │  5. Retorna resposta ao cliente    │  │
│  └────────────────────────────────────┘  │
│                                          │
│  GET /health  → { status: "ok" }         │
└──────────────────┬───────────────────────┘
                   │
                   ▼
        ┌──────────────────┐
        │    Groq Cloud    │
        │  LLaMA 3.1 8B    │
        └──────────────────┘
```

---

## 📋 Endpoints

### `GET /health`

```json
{
  "status": "ok",
  "service": "SI ChatBot"
}
```

### `POST /chat`

**Request:**
```json
{
  "message": "Como posso melhorar a negociação com esse lead?",
  "history": [
    {
      "role": "user",
      "content": "Tenho um lead interessado num apartamento de 3 quartos"
    },
    {
      "role": "assistant",
      "content": "Ótimo! Qual é o perfil financeiro dele?"
    }
  ]
}
```

**Response:**
```json
{
  "response": "Para avançar na negociação, sugiro...",
  "model": "llama-3.1-8b-instant"
}
```

---

## 📁 Estrutura de Pastas

```
si-chatbot/
├── main.py              ← Aplicação FastAPI completa
│   ├── FastAPI app + CORS
│   ├── Groq client
│   ├── SYSTEM_PROMPT (Sofia)
│   ├── GET /health
│   └── POST /chat
├── requirements.txt     ← Dependências Python
├── .env                 ← Variáveis de ambiente (não versionado)
└── .env.example         ← Exemplo de configuração
```

---

## ⚙️ Pré-requisitos

- **Python** >= 3.11
- Conta gratuita na [Groq Cloud](https://console.groq.com) para obter a API Key

---

## 📦 Como Rodar Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/si-chatbot.git
cd si-chatbot

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env
# Cole sua GROQ_API_KEY no arquivo .env

# 5. Inicie o servidor
uvicorn main:app --reload --port 8000
```

✅ API disponível em: [http://localhost:8000](http://localhost:8000)

---

## 🔑 Variáveis de Ambiente

```env
# .env
GROQ_API_KEY=sua_chave_groq_aqui
```

> 🆓 Obtenha sua chave **gratuita** em [console.groq.com](https://console.groq.com)

---

## 🔗 Outros Repositórios do Projeto

| Serviço | Repositório | Tecnologia |
|---------|------------|------------|
| 🖥️ Frontend | [si-frontend](https://github.com/SEU_USUARIO/si-frontend) | Next.js + TypeScript |
| ⚙️ Backend | [si-backend](https://github.com/SEU_USUARIO/si-backend) | NestJS + PostgreSQL |
| 🤖 IA | [si-chatbot](https://github.com/SEU_USUARIO/si-chatbot) | Python + FastAPI + Groq |

---

<div align="center">

### 👨‍💻 Desenvolvido por João Roberto

[![GitHub](https://img.shields.io/badge/GitHub-João_Roberto-181717?style=for-the-badge&logo=github)](https://github.com/SEU_USUARIO)

*Case Técnico — Vaga de Estágio Full Stack · SI Soluções Imobiliárias · 2026*

</div>
