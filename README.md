# 🤖 Chatbot com IA

Um chatbot interativo construído com Streamlit e OpenAI GPT-4o que permite conversas em tempo real com inteligência artificial.

## 📋 Descrição

Este projeto é um chatbot web que utiliza a API da OpenAI para fornecer respostas inteligentes às mensagens dos usuários. A interface é construída com Streamlit, proporcionando uma experiência de conversa fluida e intuitiva.

## 🚀 Funcionalidades

- 💬 Interface de chat interativa e responsiva
- 🤖 Integração com OpenAI GPT-4o
- 💾 Histórico de conversas mantido durante a sessão
- 🔒 Segurança: chaves API protegidas via variáveis de ambiente

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI com acesso à API
- Chave de API da OpenAI

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/chatbot-ia-streamlit.git
cd chatbot-ia-streamlit
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`:
   ```bash
   copy .env.example .env
   ```
   - Edite o arquivo `.env` e adicione sua chave da OpenAI:
   ```
   OPENAI_API_KEY=sua_chave_api_aqui
   ```

## ▶️ Como executar

Execute o seguinte comando no terminal:

```bash
streamlit run main.py
```

O aplicativo será aberto automaticamente no seu navegador padrão, geralmente em `http://localhost:8501`.

## 📝 Como usar

1. Abra o aplicativo no navegador
2. Digite sua mensagem no campo de texto na parte inferior
3. Pressione Enter ou clique para enviar
4. Aguarde a resposta da IA
5. Continue a conversa normalmente!

## 🔐 Segurança

⚠️ **Importante**: Nunca compartilhe sua chave de API publicamente. O arquivo `.env` está no `.gitignore` e não será commitado no repositório.

## 🛠️ Tecnologias utilizadas

- [Streamlit](https://streamlit.io/) - Framework para criação de aplicações web
- [OpenAI API](https://platform.openai.com/) - API de inteligência artificial
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Gerenciamento de variáveis de ambiente

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👤 Autor

Criado como parte da Jornada Python 2026

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
