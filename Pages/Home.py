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
            st.write("I'm learning Python and Streamlit and this is my first Streamlit Site =)")
            st.write("[My previous site](https://ccrypter.github.io/NikitaRas/index.html) based on elderly technology named html and css!")
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
        with st.container():
            st.write("---")
            st.header("My Videos")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image("img/vid1.png")
            with text_column:
                st.subheader("This is the BEST vehicle in GTA San Andreas")
                st.write(
                    """
                    In this video I'll show you what is the BEST vehicle in GTA San Andreas
                    """
                )
                st.markdown("[Watch Video!](https://youtu.be/tVQamY4ewdk?si=dEHytqiwP2YCq-VA)")
        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image("img/vid2.png")
            with text_column:
                st.subheader("Minecraft ReIndev Review!")
                st.write(
                    """
                    Minecraft ReIndev is a global modification for Minecraft Beta 1.7.3!
                    """
                )
                st.markdown("[Watch Video!](https://www.youtube.com/watch?v=OJVoiDkr868)")

