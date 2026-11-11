import streamlit as st

st.set_page_config(
    page_title="VEXA AI",
    page_icon="💜",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #090610;
    color: white;
}
h1 {
    color: #a855f7;
}
.stChatMessage {
    background: #1b1029;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("💜 VEXA AI")
st.caption("Твой персональный ИИ-помощник")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Напиши VEXA что-нибудь...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    answer = "Привет! Я V