import streamlit as st


def background():
    st.markdown("""
        <style>
        /* 1. Torna o header transparente em vez de escondê-lo totalmente */
        /* Isso mantém o botão de abrir/fechar a sidebar visível */
        header[data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
            border-bottom: none;
        }

        /* 2. Esconde especificamente o botão roxo de Deploy */
        .stAppDeployButton {
            display: none;
        }

        /* 3. Esconde o rodapé (Made with Streamlit) */
        footer {
            visibility: hidden;
        }

        /* 4. Aplica o degradê no fundo total e define a cor do texto */
        .stApp {
            background: linear-gradient(135deg, #a5ccf1 0%, #629acf 50%, #206cb4 100%);
            color: white;
        }
        
        /* 5. Ajuste da sidebar para ser translúcida e combinar com o fundo */
        [data-testid="stSidebar"] {
            background-color: rgba(255, 255, 255, 0.05);
        }

        /* 6. Força o ícone da sidebar a ficar branco para aparecer no fundo escuro */
        button[kind="header"] {
            color: white !important;
        }
        </style>
        """, unsafe_allow_html=True)