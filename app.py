import streamlit as st
from openai import OpenAI
client=OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.set_page_config(page_title="LLM CHATBOT",layout="centered")
st.title("keerthanas chatbot here")
st.markdown("explore ask anything")
if "message" not in st.session_state:
    st.session_state["message"]=[]

for msg in st.session_state["message"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt=st.chat_input("enter message here")
if prompt:
    st.session_state["message"].append({"role":"user","content":prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder=st.empty()
        full_response=""

        stream=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["message"],
            stream=True,
        )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            full_response+=chunk.choices[0].delta.content
            message_placeholder.markdown(full_response+" |")
    message_placeholder.markdown(full_response)    
    st.session_state["message"].append({"role":"assistant","content":full_response})
