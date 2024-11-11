import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Apply custom CSS for background image
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://coolbackgrounds.io/images/backgrounds/white/white-trianglify-b79c7e1f.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Get the current working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved Parkinson's model
parkinsons_model = pickle.load(open(os.path.join(working_dir, 'parkinsons_model.sav'), 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Parkinson Disease Prediction System',
        ['Parkinsons Prediction'],  # Only Parkinson's Prediction option
        menu_icon='hospital-fill',
        icons=['person'],
        default_index=0
    )

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields for Parkinson's prediction
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('Jitter(Abs)')
    with col1:
        RAP = st.text_input('RAP')
    with col2:
        PPQ = st.text_input('PPQ')
    with col3:
        DDP = st.text_input('DDP')
    with col4:
        Shimmer = st.text_input('Shimmer')
    with col5:
        Shimmer_dB = st.text_input('Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('APQ3')
    with col2:
        APQ5 = st.text_input('APQ5')
    with col3:
        APQ = st.text_input('APQ')
    with col4:
        DDA = st.text_input('DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('Spread1')
    with col5:
        spread2 = st.text_input('Spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # Variable to hold diagnosis result
    parkinsons_diagnosis = ''

    # Button for prediction
    if st.button("Parkinson's Test Result"):
        try:
            # Convert input data to float
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            user_input = [float(x) for x in user_input]
            
            # Make a prediction
            parkinsons_prediction = parkinsons_model.predict([user_input])
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
            
            st.success(parkinsons_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all input fields.")

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
