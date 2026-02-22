import streamlit as st

def carrousel_home():
    lista_imagens = [
    "imagens/kero_spinel.jpg",
    "imagens/keroandspinel.jpg",
    "imagens/kerinho.jpg"
    ]


    if 'indice_carrossel' not in st.session_state:
        st.session_state.indice_carrossel = 0
    st.markdown("""
        <style>
                
        /* Estilo para as IMAGENS DA GALERIA (Altura igual e cantos arredondados) */
        [data-testid="stImage"] img {
            height: 300px;
            width: 100%;
            object-fit: cover;
            border-radius: 15px;
        }
                

        .carrossel-img img {
            height: 400px; /* Altura maior para o destaque do carrossel */
            object-fit: cover;
            border-radius: 20px;
            border: 2px solid #700B97; /* Cor cósmica */
        }
        .stButton>button {
            width: 100%;
            border-radius: 50px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    col_voltar, col_img, col_avancar = st.columns([1, 5, 1], vertical_alignment="center")

    with col_voltar:
        if st.button("❮"):
            st.session_state.indice_carrossel = (st.session_state.indice_carrossel - 1) % len(lista_imagens)

    with col_avancar:
        if st.button("❯"):
            st.session_state.indice_carrossel = (st.session_state.indice_carrossel + 1) % len(lista_imagens)

    with col_img:
        st.image(lista_imagens[st.session_state.indice_carrossel], use_container_width=True)
        st.write(f"<p style='text-align: center;'>{st.session_state.indice_carrossel + 1} / {len(lista_imagens)}</p>", unsafe_allow_html=True)



def carrousel_webtoon():
    lista_imagens = [
        "imagens/banner.jpeg",
        "imagens/banner2.jpg"
    ]


    if 'indice_carrossel' not in st.session_state:
        st.session_state.indice_carrossel = 0
    st.markdown("""
        <style>
                
        /* Estilo para as IMAGENS DA GALERIA (Altura igual e cantos arredondados) */
        [data-testid="stImage"] img {
            height: 400px;
            width: 100%;
            object-fit: cover;
            border-radius: 15px;
        }
                

        .carrossel-img img {
            height: 400px; /* Altura maior para o destaque do carrossel */
            object-fit: cover;
            border-radius: 20px;
            border: 2px solid #700B97; /* Cor cósmica */
        }
        .stButton>button {
            width: 100%;
            border-radius: 50px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    col_voltar, col_img, col_avancar = st.columns([1, 5, 1], vertical_alignment="center")

    with col_voltar:
        if st.button("❮"):
            st.session_state.indice_carrossel = (st.session_state.indice_carrossel - 1) % len(lista_imagens)

    with col_avancar:
        if st.button("❯"):
            st.session_state.indice_carrossel = (st.session_state.indice_carrossel + 1) % len(lista_imagens)

    with col_img:
        st.image(lista_imagens[st.session_state.indice_carrossel], use_container_width=True)
        st.write(f"<p style='text-align: center;'>{st.session_state.indice_carrossel + 1} / {len(lista_imagens)}</p>", unsafe_allow_html=True)