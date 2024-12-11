import streamlit as st
from streamlit_lottie import st_lottie

class Home:
    def __int__(self):
        pass
    def app(self):
        with st.container():
            lottie_animation = "https://lottie.host/91be4f3b-2f30-4b1f-bb78-5acfb14060f7/4P4uMo4mp1.json"
            st.subheader('Hi, I am Nick :wave:')
            st.title('A Data Analyst from Eshkerya')
            st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings.")
            st.write("[My previous site](https://ccrypter.github.io/NikitaRas/index.html) based on elderly techology named html and css!")
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.write("##")
                st.write("On my Youtube channel I made some fun and interesting videos about games.")
                st.write(
                        """
                        One of my favorite games:
                        - GTA San Andreas
                        - Minecraft
                        - Tanki Online
                        - Terraria
                        - Castle Crashers
                        """
                )
                st.write("and more =)")
                st.write("For all my people very big respect from Saint-Tropez")
                st.write("[My YouTube Channel](https://www.youtube.com/@ccrypter):camera:")
            with right_column:
                st_lottie(lottie_animation, height=300, key="coding")
                st.image("img/saintropez.png")