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
                           ['Diabetes Prediction', 
                            'Heart Disease Prediction', 
                            'Parkinsons Prediction',
                            'Food Precautions & Safety Measures'],
                           icons=['activity', 'heart', 'person', 'utensils'], default_index=0)


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
            # ---------------- Food Precautions & Safety Measures ----------------
if selected == "Food Precautions & Safety Measures":
    st.subheader("🥗 Food Precautions & Safety Measures")
    st.write("Follow these guidelines for better health and disease prevention:")

    precautions = {
        "General Health": [
            "Eat more fruits and vegetables daily.",
            "Drink at least 8 glasses of water.",
            "Avoid excessive oily and junk food.",
            "Maintain regular meal timings."
        ],
        "Diabetes": [
            "Avoid sugary drinks and sweets.",
            "Prefer whole grains over refined carbs.",
            "Eat fiber-rich foods like oats and beans.",
            "Limit red meat and processed foods."
        ],
        "Heart Disease": [
            "Reduce salt intake.",
            "Avoid deep-fried and high-cholesterol foods.",
            "Eat omega-3 rich foods like fish and flaxseeds.",
            "Exercise regularly and maintain a healthy weight."
        ],
        "Parkinson’s Disease": [
            "Include antioxidant-rich foods (berries, spinach).",
            "Eat foods high in omega-3 fatty acids.",
            "Take smaller, frequent meals.",
            "Limit processed and high-fat foods."
        ],
        "Food Safety": [
            "Always wash vegetables and fruits before eating.",
            "Cook meat and seafood thoroughly.",
            "Avoid storing cooked and raw food together.",
            "Keep kitchen surfaces and utensils clean."
        ]
    }

    for category, tips in precautions.items():
        with st.expander(f"🔹 {category}"):
            for tip in tips:
                st.write(f"- {tip}")

    st.success("✅ Follow these measures to improve your health and prevent diseases.")




import streamlit as st
from datetime import datetime
import pandas as pd

st.title("🏥 Doctor Appointment Booking System - Tiptur")

# Store appointments in session state
if "appointments" not in st.session_state:
    st.session_state.appointments = []

# ---------------- Tiptur Hospital Data ----------------
hospitals = {
    "Government Hospital Tiptur": {"lat": 13.2606, "lon": 76.4775},
    "Shri Raghavendra Hospital": {"lat": 13.2591, "lon": 76.4802},
    "SNR Hospital": {"lat": 13.2625, "lon": 76.4820},
    "Vinayaka Hospital": {"lat": 13.2575, "lon": 76.4750},
    "CSI Mission Hospital": {"lat": 13.2615, "lon": 76.4788},
    "SS Hospital - Hassan Circle": {"lat": 13.2582, "lon": 76.4845},
}

# ---------------- BOOKING FORM ----------------
st.subheader("📅 Book an Appointment")

with st.form("appointment_form", clear_on_submit=True):
    patient_name = st.text_input("Patient Name", key="patient_name")
    contact_number = st.text_input("Contact Number (10 digits)", key="contact_number")

    # Hospital selection
    hospital_name = st.selectbox("🏨 Choose Nearby Hospital", list(hospitals.keys()))

    doctor = st.selectbox("👨‍⚕️ Choose Doctor", [
        "Dr. Kumar - General Physician",
        "Dr. Shilpa - Gynecologist",
        "Dr. Prasad - Cardiologist",
        "Dr. Ramesh - Orthopedic",
        "Dr. Anitha - Pediatrician",
        "Dr. Shivakumar - Physician"
    ])

    date = st.date_input("📅 Select Date", min_value=datetime.today())
    time = st.time_input("⏰ Select Time")

    submitted = st.form_submit_button("Confirm Appointment")

    if submitted:
        if patient_name.strip() == "" or contact_number.strip() == "":
            st.error("⚠ Please enter both patient name and contact number")
        elif not contact_number.isdigit() or len(contact_number) != 10:
            st.error("⚠ Please enter a valid 10-digit contact number")
        else:
            new_appointment = {
                "patient": patient_name,
                "contact": contact_number,
                "hospital": hospital_name,
                "doctor": doctor,
                "date": str(date),
                "time": str(time),
                "lat": hospitals[hospital_name]["lat"],
                "lon": hospitals[hospital_name]["lon"]
            }
            st.session_state.appointments.append(new_appointment)
            st.success(
                f"✅ Appointment booked for {patient_name} "
                f"with {doctor} at {hospital_name} on {date} at {time}"
            )

# ---------------- CONFIRMATION LIST ----------------
st.subheader("📋 Appointment Confirmation List")

if st.session_state.appointments:
    for i, appt in enumerate(st.session_state.appointments, start=1):
        st.write(
            f"**{i}.** 👤 {appt['patient']} (📞 {appt['contact']}) → "
            f"🏨 {appt['hospital']} → 👨‍⚕️ {appt['doctor']} "
            f"on {appt['date']} at {appt['time']}"
        )

    # Show hospitals on map
    st.subheader("🗺️ Hospital Locations on Map")
    df = pd.DataFrame(
        [{"lat": appt["lat"], "lon": appt["lon"]} for appt in st.session_state.appointments]
    )
    st.map(df, zoom=13)
else:
    st.info("No appointments booked yet.")


import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="💊 Medicine Reminder & Emergency Consultation", layout="centered")

st.title("🏥 Health Support System")
st.write("Set medicine reminders and connect to a doctor instantly in emergencies.")

# ----------------- Medicine Reminders -----------------
if "reminders" not in st.session_state:
    st.session_state.reminders = []

st.subheader("💊 Add Medicine Reminder")

with st.form("reminder_form", clear_on_submit=True):
    patient = st.text_input("Patient Name")
    medicine = st.text_input("Medicine Name")
    dose = st.text_input("Dosage (e.g., 500 mg)")
    date = st.date_input("Select Date", value=datetime.today())
    time = st.time_input("Select Time", value=datetime.now().time())
    submit = st.form_submit_button("➕ Add Reminder")

    if submit:
        if not patient or not medicine or not dose:
            st.error("⚠ Please fill all fields")
        else:
            reminder = {
                "patient": patient,
                "medicine": medicine,
                "dose": dose,
                "datetime": datetime.combine(date, time),
                "done": False
            }
            st.session_state.reminders.append(reminder)
            st.success(f"✅ Reminder set for {patient}: {medicine} ({dose}) at {date} {time}")

# ----------------- Reminder List -----------------
st.subheader("📋 Upcoming Reminders")

if st.session_state.reminders:
    for i, r in enumerate(st.session_state.reminders, start=1):
        status = "✅ Done" if r["done"] else "⏳ Pending"
        st.write(f"**{i}.** {r['patient']} → {r['medicine']} ({r['dose']}) at {r['datetime'].strftime('%Y-%m-%d %H:%M')} — {status}")

        if not r["done"]:
            if st.button(f"Mark as Done ✅", key=f"done_{i}"):
                r["done"] = True
                st.experimental_rerun()
else:
    st.info("No reminders yet. Add one above.")



import streamlit as st
from datetime import datetime

# ---------------- Initialize Ambulances ----------------
if "ambulances" not in st.session_state:
    st.session_state.ambulances = [
        {"id": "AMB001", "available": True, "equipment": ["Oxygen", "Ventilator"]},
        {"id": "AMB002", "available": True, "equipment": ["First Aid Kit"]},
        {"id": "AMB003", "available": True, "equipment": ["Oxygen", "Defibrillator"]},
    ]

if "ambulance_bookings" not in st.session_state:
    st.session_state.ambulance_bookings = []

st.title("🚑 Ambulance Booking with Equipment Tracking")

# ---------------- Booking Form ----------------
st.subheader("📋 Book an Ambulance")

with st.form("ambulance_form"):
    patient_name = st.text_input("Patient Name")
    contact_number = st.text_input("Contact Number")
    severity = st.selectbox("Severity", ["Critical", "Moderate", "Low"])
    required_equipment = st.multiselect(
        "Required Equipment",
        ["Oxygen", "Ventilator", "Defibrillator", "First Aid Kit"]
    )
    hospital = st.text_input("Destination Hospital")
    submit = st.form_submit_button("Book Ambulance")

    if submit:
        if not patient_name or not contact_number or not hospital:
            st.error("Please fill all mandatory fields!")
        else:
            # Find available ambulance with required equipment
            allocated_ambulance = None
            for amb in st.session_state.ambulances:
                if amb["available"] and all(eq in amb["equipment"] for eq in required_equipment):
                    allocated_ambulance = amb
                    break

            if allocated_ambulance:
                # Allocate ambulance
                allocated_ambulance["available"] = False
                booking = {
                    "patient": patient_name,
                    "contact": contact_number,
                    "severity": severity,
                    "hospital": hospital,
                    "ambulance_id": allocated_ambulance["id"],
                    "equipment": required_equipment,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                st.session_state.ambulance_bookings.append(booking)
                st.success(f"✅ Ambulance {allocated_ambulance['id']} booked successfully!")
                st.info(f"Assigned Equipment: {', '.join(required_equipment)}")
            else:
                st.warning("⚠ No ambulance available with the requested equipment. Added to waitlist.")

# ---------------- Booking History ----------------
st.subheader("📊 Ambulance Booking History")
if st.session_state.ambulance_bookings:
    st.dataframe(st.session_state.ambulance_bookings)
else:
    st.info("No ambulance bookings yet.")

