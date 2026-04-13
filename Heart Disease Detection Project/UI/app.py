import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Heart Disease Expert System", layout="wide")

st.title("❤️ Heart Disease Prediction UI")
st.sidebar.header("Patient Health Input")

def get_streamlit_inputs():
    # Age (Numeric)
    age = st.sidebar.number_input("Enter Age", min_value=1, max_value=110, value=50)

    # Sex (Converted to 1 and 0)
    sex = st.sidebar.selectbox("Sex", options=[1, 0], 
                               format_func=lambda x: "Male " if x == 1 else "Female ")

    # Chest Pain (Converted to numbers)
    # High/Medium/Low from your code mapped to 0, 1, 2
    cp = st.sidebar.selectbox("Chest Pain Type", options=[0, 1, 2], 
                              format_func=lambda x: ["Low ", "Medium ", "High "][x])

    # Blood Pressure & Cholesterol (Numeric)
    trestbps = st.sidebar.number_input("Resting Blood Pressure", value=120)
    chol = st.sidebar.number_input("Cholesterol Level", value=200)

    # Fasting Blood Sugar (Normal/High)
    fbs = st.sidebar.selectbox("Fasting Blood Sugar", options=[0, 1], 
                               format_func=lambda x: "Normal " if x == 0 else "High ")

    # Rest ECG (Numeric 0-2)
    restecg = st.sidebar.selectbox("Rest ECG Result", options=[0, 1, 2])

    # Max Heart Rate (Numeric)
    thalach = st.sidebar.slider("Max Heart Rate Achieved", 60, 220, 150)

    # Exercise Induced Angina (Yes/No)
    exang = st.sidebar.selectbox("Exercise Induced Angina", options=[1, 0], 
                                 format_func=lambda x: "Yes " if x == 1 else "No ")

    # Oldpeak (Float)
    oldpeak = st.sidebar.number_input("Oldpeak Value", min_value=0.0, max_value=6.0, value=1.0, step=0.1)

    # Slope, CA, Thal (Numeric 0-3)
    slope = st.sidebar.selectbox("Slope", options=[0, 1, 2])
    ca = st.sidebar.selectbox("Number of Vessels", options=[0, 1, 2, 3])
    thal = st.sidebar.selectbox("Thal Value", options=[0, 1, 2, 3])

    return {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps, "chol": chol,
        "fbs": fbs, "restecg": restecg, "thalach": thalach, "exang": exang,
        "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }

# --- APPLICATION LOGIC ---

data = get_streamlit_inputs()

# Convert dictionary to DataFrame for easy viewing
df = pd.DataFrame(data, index=[0])

st.subheader("Patient Data Preview")
st.table(df)

# Integrate your Expert System Logic
def expert_system(row):
    r = row.iloc[0].values
    # Your specific rules from the notebook:
    # Rule: If age > 30 and sex is Male (1) [Note: check your notebook logic for r[1]]
    if r[0] > 30 and r[1] == 1: 
        return 1
    elif r[2] == 2: # If Chest Pain is 'High' (2)
        return 1
    else:
        return 0

if st.button("Run Prediction"):
    result = expert_system(df)
    
    st.markdown("---")
    if result == 1:
        st.error("### Prediction: Heart Disease Detected")
    else:
        st.success("### Prediction: No Heart Disease Detected")