import streamlit as st
import joblib
import pandas as pd

### Load the model
model = joblib.load("bank_churn_model.joblib")

st.title("Bank Churn Prediction App")
st.write("This app helps predicts customers churn based on certain indicators")

#### Numeric inputs 
Customer_Age = st.number_input("Enter Age", min_value = 18, max_value = 150)
Dependent_count = st.number_input("How many Dependents", min_value = 0, max_value = 15)
Months_on_book = st.number_input("Months on Book", min_value = 0, max_value = 24)
Total_Relationship_Count = st.number_input("Your relationship", min_value = 0, max_value = 10)
Months_Inactive_12_mon = st.number_input("Months inactive in 12 months", min_value = 0, max_value = 12)
Contacts_Count_12_mon = st.number_input("Contact counts in 12 months", min_value = 0, max_value =12)
Credit_Limit = st.number_input("Credit Limit", min_value = 100)
Total_Revolving_Bal = st.number_input("Revolving Balance", min_value = 50)
Total_Amt_Chng_Q4_Q1 = st.number_input("Total Amount in first and 4th quarter", min_value = 0)
Total_Trans_Amt = st.number_input("Transfer Amount", min_value = 0)
Total_Trans_Ct  = st.number_input("Total Ct", min_value = 0)
Total_Ct_Chng_Q4_Q1 = st.number_input("Total Ct in first and 4th quarter", min_value = 0)
Avg_Utilization_Ratio = st.number_input("Average Utilization Ratio", min_value = 0, max_value =1)


### Categorical Inputs
Gender = st.selectbox("Gender", ["M", "F"])
Education_Level = st.selectbox("Education Level", ["Doctorate", "Graduate", "High School", "Post-Graduate", "Uneducated", "Unknown"])
Marital_Status = st.selectbox("Marital Status", ["Married", "Single", "Unknown"])
Income_Category = st.selectbox("Income Category", ["$40K - $60K", "$60K - $80K", "$80K - $120K", "Less than $40K", "Unknown"])
Card_Category = st.selectbox("Card Category", ["Gold", "Platinum", "Silver"])

### convert the categorical inputs to one-hot encoded format

df = {"Customer_Age":Customer_Age, "Gender":1 if Gender == "M" else 0, "Dependent_count":Dependent_count,
      "Months_on_book":Months_on_book, "Total_Relationship_Count":Total_Relationship_Count,
      "Months_Inactive_12_mon":Months_Inactive_12_mon, "Contacts_Count_12_mon":Contacts_Count_12_mon,
      "Credit_Limit":Credit_Limit, "Total_Revolving_Bal":Total_Revolving_Bal,
      "Total_Amt_Chng_Q4_Q1":Total_Amt_Chng_Q4_Q1, "Total_Trans_Amt":Total_Trans_Amt,
      "Total_Trans_Ct":Total_Trans_Ct,"Total_Ct_Chng_Q4_Q1": Total_Ct_Chng_Q4_Q1, "Avg_Utilization_Ratio":Avg_Utilization_Ratio}


#### Add one-hot encoded column 
### Initialize all as 0
for item in ['Education_Level_Doctorate', 'Education_Level_Graduate',
       'Education_Level_High School', 'Education_Level_Post-Graduate',
       'Education_Level_Uneducated', 'Education_Level_Unknown',
       'Marital_Status_Married', 'Marital_Status_Single',
       'Marital_Status_Unknown', 'Income_Category_$40K - $60K',
       'Income_Category_$60K - $80K', 'Income_Category_$80K - $120K',
       'Income_Category_Less than $40K', 'Income_Category_Unknown',
       'Card_Category_Gold', 'Card_Category_Platinum', 'Card_Category_Silver']:
    df[item] = 0

### set the selected category
df[f"Education_Level_{Education_Level}"] = 1
df[f"Marital_Status_{Marital_Status}"] = 1
df[f"Income_Category_{Income_Category}"] = 1
df[f"Card_Category_{Card_Category}"] = 1

## Create our table
churn_input = pd.DataFrame([df])

#st.write(churn_input.head())

### Create the prediction button
if st.button("Click on this button to run your request"):
    predict = model.predict(churn_input)[0]

    if predict == 1:
        label = "Customer won't churn"
    else:
        label = "Customer will churn"
    st.success(f"The {label}")
