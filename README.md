# 🚗 Vehicle Damage Detection App

## 📋 Overview
This app lets you drag and drop an image of a car and it will tell you what kind of damage it has.
The model is trained on third-quarter front and rear views - please capture the third-quarter front or rear view of a car.

![app](images/app_screenshot.png)

## 🧠 Model Details
- **Architecture**: ResNet50 with transfer learning
- **Training Data**: ~1700 images
- **Target Classes**: 6 categories
  - Front Normal ✅
  - Front Crushed 💥
  - Front Breakage 🔧
  - Rear Normal ✅
  - Rear Crushed 💥
  - Rear Breakage 🔧
- **Validation Accuracy**: ~80%

### 🛠️ Setup

1. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
2. Run the streamlit app:
   ```commandline
   streamlit run app.py
 
## 👨‍💻 Author

Yoseph Negash

📅 2026


![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
  
