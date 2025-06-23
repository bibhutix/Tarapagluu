import streamlit as st
from PIL import Image
import os
import base64


st.set_page_config(page_title="Hieeee Deha💗", page_icon="🥺", layout="centered")

# Custom CSS for baby pink background
st.markdown("""
    <style>
        body {
            background-color: #ffe6f0;  /* Baby pink */
        }

        .stApp {
            background-color: #ffe6f0;  /* Baby pink */
        }

        h1, h2, h3, h4, h5, h6, p, div {
            color: #4b2e2e;  /* Optional: change text color to something soft */
        }

        img {
            border-radius: 12px;
        }

        button[kind="primary"] {
            background-color: #ffb6c1;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)


st.title("Hieeee Deha💗")
st.markdown("## Please forgive me... I miss you so much")

# Load a local GIF
def load_gif(gif_path):
    with open(gif_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

gif_path = "gifs/1.gif"  # Replace with your own file path
gif_base64 = load_gif(gif_path)

# Embed in HTML
st.markdown(f"""
<div style="text-align: center;">
    <img src="data:image/gif;base64,{gif_base64}" alt="I'm Sorry" width="70%">
</div>
""", unsafe_allow_html=True)
# Heartfelt message
st.markdown("""
---
<div style="text-align: center; font-size: 18px;">
💌 To My Sweetheart,

I know I made you upset today. I am sorry for saying something so stupid.
There is no excuses why I said it and I am truly sorry for that.
Please forgive meeeee🙁  
*Bibhuti 💖*
""", unsafe_allow_html=True)


# 💫 Another apology GIF before the forgiveness button
def load_gif(gif_path):
    with open(gif_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
gif_path = "gifs/2.gif"  # Replace with your own file path

gif2_base64 = load_gif(gif_path)  # Replace with your own GIF path
st.markdown(f"""
<div style="text-align: center; margin-top: 40px;">
    <img src="data:image/gif;base64,{gif2_base64}" alt="Please forgive me" width="300">
</div>
""", unsafe_allow_html=True)


# 💌 Centered heading
st.markdown("""
<div style="text-align: center; font-size: 24px; font-weight: bold; margin-top: 40px;">
    I miss you Jaaaan 💖
</div>
""", unsafe_allow_html=True)

# 📸 Centered image gallery
photo_folder = "photos"

if os.path.exists(photo_folder):
    photo_files = [f for f in os.listdir(photo_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]

    if photo_files:
        for photo in photo_files:
            image_path = os.path.join(photo_folder, photo)
            with open(image_path, "rb") as f:
                img_base64 = base64.b64encode(f.read()).decode()
            
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 30px;">
                <img src="data:image/jpeg;base64,{img_base64}" width="300" style="border-radius: 12px;"><br>
                <div style="color: #4b2e2e; font-style: italic; margin-top: 8px;">
                    Prettiest bhai 💗
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No photos found in the 'photos' folder. Please add some!")
else:
    st.error("The 'photos' folder doesn't exist. Please create it and add her photos.")



# 💫 Another apology GIF before the forgiveness button
def load_gif(gif_path):
    with open(gif_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
gif_path = "gifs/3.gif"  # Replace with your own file path

gif2_base64 = load_gif(gif_path)  # Replace with your own GIF path
st.markdown(f"""
<div style="text-align: center; margin-top: 40px;">
    <img src="data:image/gif;base64,{gif2_base64}" alt="Please forgive me" width="300">
</div>
""", unsafe_allow_html=True)



# Sweet forgiveness button
if st.button("💞 Yes, I forgive you"):
    st.balloons()
    st.success("Thank you, my love! I’ll never let you down again ❤️")
else:
    st.info("I won't let you down Pleaseeeee")
