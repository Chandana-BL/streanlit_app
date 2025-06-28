# First streamlit app using st and regukar expression to check input name

import streamlit as st
import re

# Initialize session state
if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = 0

# Name validity check
def is_name_valid(name):
    if len(name) < 3:
        if re.search(r'\d',name):
            return False, "Name should be more than 3 character and should not contain numbers"   
        return False,"Name should contain more than 3 char"  
   
    if len(name) > 50:
        if re.search(r'\d',name):
            return False, "Name should be less than 50 character and should not contain numbers"
        return False, "Name should contain less than 50 char"
    
    if re.search(r'\d',name):
        return False, "Name should not contain any number"
    
    return True,""

# Pop-up window func
@st.dialog("Woaw, your are from Intel 4040 times 😄")
def pop_up_window():
    if st.button("Start_Over"):

        #Clears the specific fields
        st.session_state.name = ""
        st.session_state.age = 0
        st.session_state.reset = True

        #Clears all keys stores here
        # for key in st.session_state.keys():
        #     del st.session_state[key]

        st.rerun()

# Main logic func
def main():
    st.title("Welcome to my first streamlit web-app")
    st.header("Please, enter your details:")

    # Input fields
    name = st.text_input("Enter your name :",max_chars=50,value=st.session_state.get("name",""))

    # Using number_input API
    # age = st.number_input("Enter your age:",min_value=1,max_value=120,step=1) 

    #using slider
    age = st.slider("Enter your age:",min_value=0,max_value=120,step=1,value= st.session_state.get("age",0))

    # saving current values in session state
    st.session_state.name = name
    st.session_state.age = age

    if st.button("Go"):
        valid, msg = is_name_valid(name)
        if not valid:
            st.error(msg)
        elif age <= 0:
            st.error("Age should not be zero!")
        else:
            st.success(f'Hello {name}, you are {age} years old')
            if age > 80:               
                pop_up_window()

main()