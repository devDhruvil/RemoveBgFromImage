import streamlit as st
from rembg import remove
from PIL import Image
import io
import base64

# Convert logo to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Page Configuration
st.set_page_config(page_title="Remove Background", layout="centered", page_icon="🖼️")

# Load the logo as base64
logo_base64 = get_base64_image("E:/RemoveBg/logo.svg")

# Custom CSS for styling
st.markdown(f"""
    <style>
        body {{
            background-color: #f7f7f7;
            font-family: 'Arial', sans-serif;
        }}
        .header {{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        .logo {{
            height: 60px;
            margin-right: 10px;
        }}
        .title {{
            font-size: 32px;
            font-weight: bold;
            color: #333;
        }}
        .upload-card {{
            background-color: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-bottom: 20px;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #1f77b4;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            text-decoration: none;
        }}
        .button:hover {{
            background-color: #155a8c;
        }}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
    <div class="header">
        <img src="data:image/svg+xml;base64,{logo_base64}" class="logo">
        <div class="title">Remove Background</div>
    </div>
""", unsafe_allow_html=True)

# Top Banner Ad
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <h3>Advertisement</h3>
        <iframe
            src="https://via.placeholder.com/728x90.png?text=Sample+Ad+Banner+728x90"
            width="728"
            height="90"
            style="border: none;"
            loading="lazy">
        </iframe>
    </div>
""", unsafe_allow_html=True)

# Upload Image Section
st.markdown("<h2 style='text-align: center;'>Remove Image Background</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>100% Automatically and Free</p>", unsafe_allow_html=True)

st.markdown('<div class="upload-card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Remove Background"):
        st.write("Removing background... please wait.")
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="PNG")
        output = remove(image_bytes.getvalue())
        
        result_image = Image.open(io.BytesIO(output)).convert("RGBA")
        st.image(result_image, caption="Image with Background Removed", use_column_width=True)
        
        # Prepare Download Link
        buffered = io.BytesIO()
        result_image.save(buffered, format="PNG")
        b64 = base64.b64encode(buffered.getvalue()).decode()
        download_link = f'<a href="data:image/png;base64,{b64}" download="removed_bg.png" class="button">Download Image</a>'
        st.markdown(download_link, unsafe_allow_html=True)

# Inline Ad after Upload Section
st.markdown("""
    <div style="text-align: center; margin-top: 30px;">
        <h3>Advertisement</h3>
        <iframe
            src="https://via.placeholder.com/300x250.png?text=Sample+Ad+Banner+300x250"
            width="300"
            height="250"
            style="border: none;"
            loading="lazy">
        </iframe>
    </div>
""", unsafe_allow_html=True)
