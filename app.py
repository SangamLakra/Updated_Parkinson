import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    # Input fields
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
            
    st.success(diab_diagnosis)

    # Suggestions and Remedies
    with st.expander("Suggestions and Remedies"):
        if diab_diagnosis == 'The person is diabetic':
            st.write("### Lifestyle Changes")
            st.write("- **Increase physical activity**: Aim for at least 150 minutes per week.")
            st.write("- **Quit smoking**: Smoking can worsen complications.")
            
            st.write("### Dietary Recommendations")
            st.write("- **Balanced meals**: Include vegetables, lean proteins, and healthy fats.")
            st.write("- **Monitor carbohydrate intake**: Focus on whole grains over refined carbs.")
            st.write("- **Stay hydrated**: Drink water regularly and avoid sugary drinks.")

            st.write("### Medical Advice")
            st.write("- **Regular monitoring**: Check blood sugar levels frequently.")
            st.write("- **Consult a healthcare provider**: Regular checkups are essential.")

        else:
            st.write("### General Health Tips")
            st.write("Continue leading a healthy lifestyle with a balanced diet and regular exercise to prevent diabetes.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    # Input fields
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            
    st.success(heart_diagnosis)

    # Suggestions and Remedies
    with st.expander("Suggestions and Remedies"):
        if heart_diagnosis == 'The person is having heart disease':
            st.write("### Lifestyle Changes")
            st.write("- **Engage in physical activity**: Aim for at least 30 minutes a day.")
            st.write("- **Quit smoking** and limit alcohol intake.")
            
            st.write("### Dietary Recommendations")
            st.write("- **Heart-healthy diet**: Eat more fruits, vegetables, and whole grains.")
            st.write("- **Limit sodium**: High sodium intake can increase blood pressure.")
            
            st.write("### Medical Advice")
            st.write("- **Regular checkups**: Visit a cardiologist as advised.")
            st.write("- **Medication adherence**: Follow prescribed treatments.")

        else:
            st.write("### General Heart Health Tips")
            st.write("Maintain a healthy lifestyle, including a balanced diet and regular exercise.")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    # Add other input fields similarly...

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            
    st.success(parkinsons_diagnosis)

    # Suggestions and Remedies
    with st.expander("Suggestions and Remedies"):
        if parkinsons_diagnosis == "The person has Parkinson's disease":
            st.write("### Lifestyle Adjustments")
            st.write("- **Stay active** with exercises tailored to your condition, like yoga or tai chi.")
            st.write("- **Practice relaxation techniques** to reduce stress.")

            st.write("### Dietary Recommendations")
            st.write("- **Balanced diet**: Ensure meals rich in fiber and antioxidants.")
            st.write("- **Hydration**: Drink plenty of water to prevent dehydration.")
            
            st.write("### Medical Advice")
            st.write("- **Physical therapy**: Consider regular sessions for mobility and flexibility.")
            st.write("- **Medication management**: Work with healthcare providers on suitable treatments.")

        else:
            st.write("### General Health Tips")
            st.write("Maintain a healthy lifestyle to support overall neurological health.")
