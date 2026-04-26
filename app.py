import streamlit as st
from model_helper import predict

# Beautiful CSS styling
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }

    /* Main content container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Title styling - SOLID WHITE for better visibility */
    h1 {
        color: white !important;
        font-size: 3rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 2rem;
        letter-spacing: -0.5px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* File uploader label */
    .stFileUploader > label {
        font-size: 1rem !important;
        font-weight: 500 !important;
        color: white !important;
        margin-bottom: 0.5rem !important;
    }

    /* File uploader container */
    .stFileUploader {
        background: rgba(255,255,255,0.1);
        border: 2px solid rgba(255,255,255,0.2);
        border-radius: 15px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }

    .stFileUploader:hover {
        border-color: #ff6b6b;
        background: rgba(255,255,255,0.15);
    }

    /* Upload button */
    .stFileUploader button {
        background: linear-gradient(135deg, #ff6b6b, #ff8e53);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stFileUploader button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(255,107,107,0.3);
    }

    /* Image container */
    .stImage {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 0.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255,255,255,0.2);
    }

    /* Image caption */
    .stImage figcaption {
        color: white !important;
        text-align: center !important;
        margin-top: 0.5rem !important;
    }

    /* Prediction info box - WHITE BACKGROUND with BLACK TEXT */
    .stAlert {
        background: white !important;
        border-left: 5px solid #ff6b6b !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        margin-top: 1rem !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* Prediction text - BLACK */
    .stAlert .stMarkdown {
        color: black !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }

    /* Make all text in info box black */
    .stAlert div, .stAlert p, .stAlert span {
        color: black !important;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #ff6b6b, #ff8e53);
        border-radius: 10px;
    }

    /* Responsive */
    @media (max-width: 768px) {
        h1 {
            font-size: 2rem !important;
        }

        .stAlert .stMarkdown {
            font-size: 1rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="Uploaded File", use_column_width=True)
        prediction = predict(image_path)
        st.info(f"Predicted Class: {prediction}")