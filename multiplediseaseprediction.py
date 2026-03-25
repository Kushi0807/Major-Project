import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'], default_index=0)

st.title("Multiple Disease Prediction System")

# Background and footer
def set_bg_from_url(url, opacity=1):
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                Made by: <b> ISE </b>
            </p>
        </div>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_from_url("https://images.everydayhealth.com/homepage/health-topics-2.jpg?w=768", opacity=0.875)

# Appointment function
def book_appointment(condition_name):
    st.subheader(f"Book a Hospital Appointment for {condition_name}")
    name = st.text_input("Full Name", key=f'name_{condition_name}')
    contact = st.text_input("Contact Number", key=f'contact_{condition_name}')
    date = st.date_input("Preferred Appointment Date", key=f'date_{condition_name}')
    time = st.time_input("Preferred Time Slot", key=f'time_{condition_name}')

    if st.button("Confirm Appointment", key=f'confirm_{condition_name}'):
        if name and contact:
            st.success(f"Appointment confirmed for {name} on {date} at {time} for {condition_name}.")
        else:
            st.error("Please fill in all the details.")

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.subheader('Diabetes Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0)
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.0)
    with col3:
        BMI = st.number_input('BMI value', min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0)
    with col2:
        Age = st.number_input('Age of the Person', min_value=1, max_value=120, step=1)

    if st.button('Diabetes Test Result'):
        try:
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            diab_prediction = diabetes_model.predict([input_data])
            if diab_prediction[0] == 1:
                st.success('The person is diabetic')
                book_appointment("Diabetes")
            else:
                st.success('The person is not diabetic')
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.subheader('Heart Disease Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=1, max_value=120, step=1)
    with col2:
        sex = st.number_input('Sex (1 = Male, 0 = Female)', min_value=0, max_value=1, step=1)
    with col3:
        cp = st.number_input('Chest Pain types (0-3)', min_value=0, max_value=3, step=1)
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0.0)
    with col2:
        chol = st.number_input('Serum Cholesterol in mg/dl', min_value=0.0)
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)', min_value=0, max_value=1, step=1)
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0-2)', min_value=0, max_value=2, step=1)
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0.0)
    with col3:
        exang = st.number_input('Exercise Induced Angina (1 = yes; 0 = no)', min_value=0, max_value=1, step=1)
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', format="%.1f")
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment (0-2)', min_value=0, max_value=2, step=1)
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy (0-4)', min_value=0, max_value=4, step=1)
    with col1:
        thal = st.number_input('Thal (1 = normal; 2 = fixed defect; 3 = reversible defect)', min_value=1, max_value=3, step=1)

    if st.button('Heart Disease Test Result'):
        try:
            input_data = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg),
                          float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
            heart_prediction = heart_disease_model.predict([input_data])
            if heart_prediction[0] == 1:
                st.success('The person is having heart disease')
                book_appointment("Heart Disease")
            else:
                st.success('The person does not have any heart disease')
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")

# Parkinson's Prediction
if selected == "Parkinsons Prediction":
    st.subheader("Parkinson's Disease Prediction")
    col1, col2, col3, col4, col5 = st.columns(5)

    inputs = []
    fields = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
        'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
        'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]

    for i, field in enumerate(fields):
        col = [col1, col2, col3, col4, col5][i % 5]
        inputs.append(col.text_input(field))

    if st.button("Parkinson's Test Result"):
        try:
            input_data = [float(value) for value in inputs]
            parkinsons_prediction = parkinsons_model.predict([input_data])
            if parkinsons_prediction[0] == 1:
                st.success("The person has Parkinson's disease")
                book_appointment("Parkinson's")
            else:
                st.success("The person does not have Parkinson's disease")
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")
