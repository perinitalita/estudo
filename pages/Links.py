import streamlit as st
import background
import estilo
import base64

background.background()
estilo.logo_title()
    
st.markdown(f"""
    <div class="title-container">
        <img src="data:image/webp;base64,{estilo.img_link()}" class="logo-header">
        <h1 class="meu-titulo-customizado">Links</h1>
    </div>
    """, unsafe_allow_html=True)

with st.container(border=True,
                key="container2",
                width=660,
                horizontal=True
                ):
        st.link_button("Tumblr", "https://tumblr.com/")
        st.link_button("Instagram", "https://www.instagram.com/")
        st.link_button("Webtoon", "https://www.webtoons.com/")
        st.link_button("Patreon", "https://www.patreon.com/")
        st.link_button("Ko-fi", "https://ko-fi.com/")
        st.link_button("INPRNT", "https://www.inprnt.com/")
        st.link_button("Tapas", "https://tapas.io/")

with st.container(border=True,
                key="container1",
                width=660,
                horizontal=True
                ):
        st.markdown('''╰┈➤ I've gathered all my corners of the internet here so we can stay in touch. You can find my Patreon and Ko-fi links below to support my creative path and help me dedicate more time to the stories and art. You also can find and support my first webtoon series, Lonely Prince Club, on Tapas and Webtoon. I hope to see you there!''')

st.sidebar.title("A Cosmic Connection!", text_alignment="center")
st.sidebar.write("Thank you for exploring my portfolio. Support my creative path on Patreon and Ko-fi to help me create more stories.")
st.sidebar.title("ฅᨐฅ", text_alignment="center")