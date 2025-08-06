import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("best_model_bagging.pkl", "rb"))

st.set_page_config(page_title="Loan Approval Prediction", layout="centered")
st.title("📊 Loan Approval Prediction")
st.markdown("Enter applicant's information to check if the loan is likely to be approved.")

with st.form("loan_form"):
    st.header("Application Details")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])

    with col2:
        applicant_income = st.number_input("Applicant Income", min_value=0.0)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0)
        loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0.0)
        loan_term = st.number_input("Loan Term (in months)", min_value=0.0)
        credit_history = st.selectbox("Credit History", [1.0, 0.0])

    submitted = st.form_submit_button("Predict Loan Status")

if submitted:
    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0
    dependents = 3 if dependents == "3+" else int(dependents)
    education = 0 if education == "Graduate" else 1
    self_employed = 1 if self_employed == "Yes" else 0

    input_data = np.array([[gender, married, dependents, education, self_employed,
                            applicant_income, coapplicant_income, loan_amount,
                            loan_term, credit_history]])
    
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
