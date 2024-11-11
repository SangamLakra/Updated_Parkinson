# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Parkinsons Prediction'],  # Only include Parkinsons Prediction
                           menu_icon='hospital-fill',
                           icons=['person'],  # Keep only one icon
                           default_index=0)

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
