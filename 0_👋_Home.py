import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Sam's Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2025***")
    st.write("**Author:** Samantha Alcaraz")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;"> Welcome ✌🏼!</h1></div>""", unsafe_allow_html=True)  

# ----- Profile image file -----
profile_image_file_path = "samsprofile.jpg"      

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Deeply passionate about Nature, Art and Technology"

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- I am Mexican woman in STEM, dedicated to driving Data-Driven Solutions for a more sustainable and greener future ✨🕊️🍃

- B.S. in Sustainable Development Engineering 🎓 and M.Sc. in Big Data and Analytics 📊

- Constantly reflecting on life's big questions, humanity's purpose, and how we can live in greater harmony with nature 🌍

- Developed first business model focused on transforming a community through the production and sale of Dahlias in Mexico 🌸

- I love painting 🎨, reading 📚, and dancing 🪩

- How to reach me 📫 samantha.alcarazgallardo@gmail.com 

- Mexico City, Mexico ✈️  Barcelona, Spain 
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
