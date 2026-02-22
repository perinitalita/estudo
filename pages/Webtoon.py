import streamlit as st
import background
import estilo
import base64
import carrousel


background.background()
estilo.logo_title()
    
st.markdown(f"""
    <div class="title-container">
        <img src="data:image/webp;base64,{estilo.img_webtoon()}" class="logo-header">
        <h1 class="meu-titulo-customizado">Webtoon</h1>
    </div>
    """, unsafe_allow_html=True)

with st.container(border=True,
                  key="container1"):
    st.markdown('''
                ## Lonely Prince Club ''', text_alignment="center")
    st.markdown('''
        ╰┈➤ A human boy changes his name and ends up being selected to represent human kind in a magical school for princes of every mythological and cryptid realm. Welcome to the Regium Academy.
    ''')


st.markdown('''**Read the chapters here:**''', text_alignment="center")
col_esq, col_centro, col_dir = st.columns([1, 2, 1]) 

with col_centro:
    c1, c2, c3 = st.columns([1, 0.1, 1])
    with c1:
        st.link_button("Tapas", "https://tapas.io/", use_container_width=True)
    with c2:
        st.write("|")
    with c3:
        st.link_button("Webtoon", "https://www.webtoons.com/", use_container_width=True)

carrousel.carrousel_webtoon()

st.sidebar.title("This is my webtoon!", text_alignment="center")
st.sidebar.write("Creating series like Lonely Prince Club is a labor of love, and having a community that cheers me on makes all the difference in the world.")
st.sidebar.title("ฅᨐฅ", text_alignment="center")