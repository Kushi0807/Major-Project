📌 Description

This project is an AI-based healthcare web application developed using Python and Streamlit.
It predicts diseases at an early stage using Machine Learning models and provides essential healthcare services like doctor appointment booking, medicine reminders, ambulance booking, and disease awareness videos.

🎯 Objectives

Early detection of major diseases using AI

Reduce manual diagnosis effort

Provide quick healthcare assistance through a single platform

Create awareness about diseases using educational videos

🔍 Disease Prediction Modules

Diabetes Prediction

Heart Disease Prediction

Parkinson’s Disease Prediction

Each module supports:

Full Input Mode (all medical parameters)

Quick Prediction Mode (important parameters only)

Graphical probability output

🏥 Additional Features

Doctor Appointment Booking (Tiptur hospitals)

Medicine Reminder System

Ambulance Booking System

Disease Awareness Videos (YouTube API)

🛠 Technologies Used

Python

Streamlit

Machine Learning (Scikit-learn)

Pandas & NumPy

Pickle

YouTube Data API

📂 Project Structure
AI-Healthcare-Platform/
│
├── app.py
├── diabetes_model.sav
├── heart_disease_model.sav
├── parkinsons_model.sav
├── diabetes.csv
├── heart.csv
├── parkinsons.csv
├── requirements.txt
└── README.md

⚙ Installation Steps

Clone the repository

git clone <repository-url>


Install required libraries

pip install -r requirements.txt


Run the application

streamlit run app.py

📊 Output

Disease risk displayed as Low Risk / High Risk

Probability visualization using bar charts

Interactive and user-friendly UI

📈 Future Enhancements

Login & authentication system

SMS / WhatsApp reminders

Cloud database integration

More disease prediction models

🎓 Academic Information

Project Type: Final Year Major Project

Domain: Artificial Intelligence & Healthcare

Application Type: Web Application