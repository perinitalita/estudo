import streamlit as st
import estilo
import background

st.set_page_config(
    initial_sidebar_state="expanded",
    page_title="Cosmic Pouttine",
    page_icon="🌌",
    layout="centered"
)

background.background()
estilo.logo_title()

st.markdown(f"""
    <div class="title-container">
        <img src="data:image/webp;base64,{estilo.img_title()}" class="logo-header">
        <h1 class="meu-titulo-customizado">Cosmic Pouttine Atelier</h1>
        
    </div>
    """, unsafe_allow_html=True)

with st.container(border=True,
                  width=700,
                  horizontal=True,
                  horizontal_alignment="center"
                  ):
    st.markdown('''
        ╰┈➤ Step into my world, where ethereal beings come to life with delicate lines and vibrant colors. From peaceful portraits to dynamic action scenes, my illustrations are all about connection—drawing you in and making you feel something deeper. Every character I create is a window into a cosmic world of beauty and mystery.
    ''', unsafe_allow_html=True)

st.image("imagens/1.jpeg", width="stretch")
st.image("imagens/2.jpeg", width="stretch")
st.image("imagens/3.jpeg", width="stretch")
st.image("imagens/4.jpeg", width="stretch")
st.image("imagens/5.jpeg", width="stretch")


st.sidebar.title("My Art Style!", text_alignment="center")
st.sidebar.write("Ethereal beings, delicate lines, and vibrant colors. Every character is a window into a world of mystery.")
st.sidebar.title("ฅᨐฅ", text_alignment="center")
