import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title="Language Translator",
    page_icon="💮",
    layout="wide",
    initial_sidebar_state="expanded",
)

status_dict = {
    0: "1-29 days past due",
    1: "30-59 days past due",
    2: "60-89 days overdue",
    3: "90-119 days overdue",
    4: "120-149 days overdue",
    5: "Overdue or bad debts write-offs for more than 150 days",
    7: "Paid off that month",
    6: "No loan for the month"
}


with open("ensemble_model.pkl", 'rb') as model_file:
    loaded_ensemble_model = pickle.load(model_file)



with open("scaler_amt.pkl", 'rb') as model_file2:
    loaded_scaler_amt = pickle.load(model_file2)

with open("scaler_dob.pkl", 'rb') as model_file3:
    loaded_scaler_dob = pickle.load(model_file3)

with open("scaler_days.pkl", 'rb') as model_file4:
    loaded_scaler_days = pickle.load(model_file4)

with open("scaler_occ.pkl", 'rb') as model_file5:
    loaded_scaler_occ = pickle.load(model_file5)

with open("scaler_cnt.pkl", 'rb') as model_file6:
    loaded_scaler_cnt = pickle.load(model_file6)

with open("scaler_mon.pkl", 'rb') as model_file7:
    loaded_scaler_mon = pickle.load(model_file7)



with open("label_encoder_occ.pkl", 'rb') as model_file8:
    loaded_encoder_occ = pickle.load(model_file8)


with open("occ.txt") as o:
    occu = o.read().splitlines()


st.markdown("<h1 style='text-align: centre; color: yellow;'>Banking Fraud Detection</h1>",
                unsafe_allow_html=True)

final_lst = []

st.markdown("<hr>", unsafe_allow_html=True)

gen, car = st.columns(2)

with gen:
    gender = st.radio('Select your Gender', ['Male', 'Female'])
    if gender == 'Male':
        final_lst.append(1)
    else:
        final_lst.append(0)

with car:
    car = st.radio('Do you have a car', ['Yes', 'No'])
    if car == 'Yes':
        final_lst.append(1)
    else:
        final_lst.append(0)

st.markdown("<hr>", unsafe_allow_html=True)

prop, child = st.columns(2)

with prop:
    gender = st.radio('Do you own any property', ['Yes', 'No'])
    if gender == 'Yes':
        final_lst.append(1)
    else:
        final_lst.append(0)

with child:
    ch = st.number_input('How many childers do you have')
    final_lst.append(ch)

st.markdown("<hr>", unsafe_allow_html=True)

inc, dob = st.columns(2)

with inc:
    income = st.number_input('Enter Your Per Annum Income')
    income = loaded_scaler_amt.transform([[income]])
    final_lst.append(income)

with dob:
    date = st.number_input('How many days passed since your Birthday')
    date = -date
    date = loaded_scaler_dob.transform([[date]])
    final_lst.append(date)

st.markdown("<hr>", unsafe_allow_html=True)


emp, mob = st.columns(2)

with emp:
    employ = st.number_input('How many days you got employeed')
    employ = -employ
    employ = loaded_scaler_days.transform([[employ]])
    final_lst.append(employ)

with mob:
    mobile = st.radio('Do you have a mobile phone', ['Yes', 'No'])
    if mobile == 'Yes':
        final_lst.append(1)
    else:
        final_lst.append(0)

st.markdown("<hr>", unsafe_allow_html=True)

work_ph, fg_ph = st.columns(2)

with work_ph:
    work_phone = st.radio('Do you have a work phone', ['Yes', 'No'])
    if work_phone == 'Yes':
        final_lst.append(1)
    else:
        final_lst.append(0)

with fg_ph:
    fg_phone = st.radio('Do you have a another phone', ['Yes', 'No'])
    if fg_phone == 'Yes':
        final_lst.append(1)
    else:
        final_lst.append(0)

st.markdown("<hr>", unsafe_allow_html=True)

email, occ = st.columns(2)

with email:
    email = st.radio('Do you have a email', ['Yes', 'No'])
    if email == 'Yes':
        final_lst.append(1)
    else:
        final_lst.append(0)

with occ:
    occupation = st.selectbox('Select your Occupation', (occu))
    occ_int = loaded_encoder_occ.transform([occupation])
    occ_int = loaded_scaler_occ.transform([occ_int])
    final_lst.append(occ_int)  

st.markdown("<hr>", unsafe_allow_html=True)


cnt_fam, cred = st.columns(2)

with cnt_fam:
    cnt_fam = st.number_input('Enter your family members count')
    cnt_fam = loaded_scaler_cnt.transform([[cnt_fam]])
    final_lst.append(cnt_fam)

with cred:
    credit = st.number_input('How Many years back you applied for loan through credit card')
    credit = -credit
    credit = loaded_scaler_mon.transform([[credit]])
    final_lst.append(credit)

st.markdown("<hr>", unsafe_allow_html=True)

inc_type, edu_type = st.columns(2)

with inc_type:
    inc_type_dict = {'Pensioner' : 0, 'State servant' : 0, 'Student' : 0, 'Working' : 0}
    on = st.toggle('Do you earn')
    if on:
        inc_type = st.selectbox("Select Income Type", (inc_type_dict.keys()))
        if inc_type in list(inc_type_dict.keys()):
            inc_type_dict[inc_type] = 1 
        inc_list = list(inc_type_dict.values())
        final_lst.extend(inc_list)

    else:
        final_lst.extend(list(inc_type_dict.values()))

with edu_type:
    edu_type_dict = {'Higher education' : 0, 'Incomplete higher' : 0, 'Lower secondary' : 0, 'Secondary / secondary special' : 0}
    on2 = st.toggle('Are u Educated')
    if on2:
        edu_type = st.selectbox("Select your Education", (edu_type_dict.keys()))
        if edu_type in list(edu_type_dict.keys()):
            edu_type_dict[edu_type] = 1
        edu_list = list(edu_type_dict.values())
        final_lst.extend(edu_list)

    else:
        final_lst.extend(list(edu_type_dict.values()))

st.markdown("<hr>", unsafe_allow_html=True)

# st.write(final_lst)


rel_type, house_type = st.columns(2)

with rel_type:
    rel_type_dict = {'Married' : 0, 'Separated' : 0, 'Single / not married' : 0, 'Widow' : 0}
    on3 = st.toggle('Are u over 18 years?')
    if on3:
        rel_type = st.selectbox("Select Relationship status : ", (rel_type_dict.keys()))
        if rel_type in list(rel_type_dict.keys()):
            rel_type_dict[rel_type] = 1
        rel_list = list(rel_type_dict.values())
        final_lst.extend(rel_list)

    else:
        final_lst.extend(list(rel_type_dict.values()))

with house_type:
    house_type_dict = {'House / apartment' : 0, 'Municipal apartment' : 0, 'Office apartment' : 0, 'Rented apartment' : 0, 'With parents' : 0}
    on4 = st.toggle('Do you have a house')
    if on4:
        house_type = st.selectbox("Select House Type : ", (house_type_dict.keys()))
        if house_type in list(house_type_dict.keys()):
            house_type_dict[house_type] = 1
        house_list = list(house_type_dict.values())
        final_lst.extend(house_list)

    else:
        final_lst.extend(list(house_type_dict.values()))



cred_final_lst = []
for i in final_lst:
    try : 
        cred_final_lst.append(i[0][0])
    except Exception:
        cred_final_lst.append(float(i))


cred_calc = st.button('Calculate Fraudness')

if cred_calc:
    is_eligible = loaded_ensemble_model.predict([cred_final_lst])
    st.write(f'THE CANDIDATE AFTER TAKING A LOAN ON CREDIT CARD IS PROBABLY EXPECTED TO HAVE : "{status_dict[is_eligible[0]]}"')


