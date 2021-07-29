import streamlit as st
import pandas as pd

def main():
    st.title('Student Searching Engine')
    st.header('Welcome to the latinoamericano school')
    st.image('background.png')
    st.markdown('Introduce your school class')
    school_class = st.selectbox('Select the school class', ['S2A', 'S3A', 'S4A', 'S5A'])
    operation(school_class)
    

def operation(selection):
    if st.button('Perform Operation'):
        if selection == 'S2A':
            df = pd.read_excel('S2A student list.xlsx')
            st.dataframe(df[['NUMBER LIST','Student Names']])
            #student_number = int(st.text_input('Write the student number list: '))
            student_info = st.button('Click to show student information')
            if student_info:
                #keynumber = student_number - 1
                st.dataframe(df.iloc[1])
            
#def student_info(student_number):
    #if st.button('Show student information'):
        #keynumber = int(student_number) - 1
        #st.dataframe(df.iloc[keynumber])

main()

 