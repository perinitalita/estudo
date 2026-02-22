import streamlit as st
import base64

    
def logo_title():
    st.markdown("""
        <style>
        /* Estilo para a LOGO REDONDA ao lado do título */
        .logo-header {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #E0E0E0; /* Opcional: uma borda fina */
        }
                
        /* Ajuste para centralizar verticalmente o título com a logo */
        .title-container {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
    
def img_title():
    with open("imagens/cosmic.webp", "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode("utf-8")
    
def img_link():
    with open("imagens/cosmic2.jpeg", "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode("utf-8")
    
def img_webtoon():
    with open("imagens/cosmic3.jpeg", "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode("utf-8")