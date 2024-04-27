import streamlit as st
from PIL import Image
st.set_page_config(page_title="About", page_icon="ℹ️",layout="wide",)

st.markdown(f'<h1 style="color:black;font-size:39px; text-align:center;">{"English to Telugu Text Translation System"}</h1>', unsafe_allow_html=True)
#st.markdown(about,unsafe_allow_html=True)
st.markdown(f'<h3 style="color:black;font-size:24px;">{"English to Telugu text translation system using deeplearning techniques, specifically leveraging transformer architectures their past choices and behavior. "}</h3>', unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             #background-image: url("https://img.freepik.com/free-vector/movie-film-strip-blue-background_1017-33458.jpg");
             background-attachment: fixed;
             background-position: center;
             background-repeat:no-repeat;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


#st.write(":milk[👈 Check out the movie icon in the nav-bar!]")
#st.header(':white[Developers:]')
# st.write(f'<h1 style="color:#ffffff;font-size:24px;">{"👈 Check out the movie icon in the nav-bar!"}</h1>', unsafe_allow_html=True)
# st.write(f'<h1 style="color:#ffffff;font-size:35px;">{"Team: Perfect Drive"}</h1>', unsafe_allow_html=True)

# #st.markdown(d,unsafe_allow_html=True)
# st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Koukuntla Komal Reddy        @Project Manager "}</h2>', unsafe_allow_html=True)
# st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Chalumuri Harshitha          @Software Engineer"}</h2>', unsafe_allow_html=True)
# st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Chintada Jagan Mohan Rao     @Quality Assurance Engineer "}</h1>', unsafe_allow_html=True)
# st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Koppaka Yeswanth             @Data Scientist"}</h2>', unsafe_allow_html=True)
# st.write(f'<h2 style="color:#ffffff;font-size:24px;">{" Kalapala Venkata Surya Teja @User Experience Designer"}</h2>', unsafe_allow_html=True)
# st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Asif Ahmad Najar             @Documentation Writer"}</h2>', unsafe_allow_html=True)