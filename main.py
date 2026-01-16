#titulo
#input do chat(campo de mensagem)
#a cada mensagem que o usuario enviar:
    #mostrar a mensagem que o usuário enviou no chat
    #pegar a pergunta e enviar para uma IA responder
    #exibir a resposta da IA na tela

import os
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI

# Carregar variáveis de ambiente
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# Configurar cliente OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Erro: OPENAI_API_KEY não encontrada no arquivo .env")
    st.stop()

modelo_ia = OpenAI(api_key=api_key)

st.write("# Chatbot com IA")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem ["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    # mensagem do usuário
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    # resposta da IA
    resposta_ia = modelo_ia.chat.completions.create(
        messages = st.session_state["lista_mensagens"], 
        model="gpt-4o"
        )
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


print(st.session_state["lista_mensagens"])
