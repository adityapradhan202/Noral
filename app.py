import streamlit as st
import os
from PIL import Image
import time
import requests

# Import for db connectivity
from dbutils import appreqs, dbread
from apputils.typewriter_effect import stream_data

temp_folder = "temp_files"
os.makedirs(temp_folder, exist_ok=True)

st.header("Noral 🪥")
st.write("Welcome to NORAL: Where Oral Health Meets the Power of Neural Networks!")

if 'info_submit_status' not in st.session_state:
    st.session_state.info_submit_status = False

with st.sidebar:
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", value=None)
    address = st.text_input("Enter address:")
    phone = st.text_input("Enter phone number:")
    gender = st.radio(label="Choose your gender:",
                      options=["Male", "Female", "Others"], index=None)
    
    submit = st.button(label="Submit information")
    if submit:
        if name and age and address and phone and gender:
            st.session_state.info_submit_status = True
            st.success("Information successfully submited!")
        else:
            st.warning("Enter all the fields in order to proceed!")
    
tab1, tab2 = st.tabs(tabs=["Patient portal", "Doctor's dashboard"])
with tab1:
    uploaded_image = st.file_uploader(label='Upload an image of your teeth', type=['jpg', 'jpeg', 'png'])
    description = st.text_area(
        label="Describe your problem here(Max 300 characters)"
    )

    check_results = st.button(label="Check results", type="primary")
    if check_results:
        if st.session_state.info_submit_status:
            # st.write("All information submitted and code here will work")
            if uploaded_image and description:
                image = Image.open(uploaded_image)
                st.image(image, caption="Uploaded Image", use_column_width=False)
                temp_file_path = os.path.join(temp_folder, "temp_image.jpg")
                image.save(temp_file_path)

                with st.spinner(text='Model is analysing, wait for a few seconds'):
                    time.sleep(3)
                    api_url = "http://127.0.0.1:5000/predict"  # Replace with your deployed Flask API URL
                    with open(temp_file_path, 'rb') as file:
                        response = requests.post(api_url, files={'file': file})
                                      
                # columns
                c1, c2 = st.columns(2)
                # ----

                if response.status_code == 200:
                    result = response.json()
                    with c1:
                        st.write("Prediction done by cnn models:")
                        st.write(result)
                else:
                    st.warning('Some error occured in the cnn model pipeline!')

                nlp_api_url = f"http://127.0.0.1:8000/text-classify/{description}"
                try:
                    response2 = requests.get(nlp_api_url).json()
                    with c2:
                        st.write("Symptopms extracted by nlp model:")
                        st.write(response2)
                except:
                    st.warning("Some error occured in the nlp model api!")

                # Giving suggestions using typewriter effect
                st.write_stream(stream_data(category=result['EFFNET']))

                # DB connectivity here!!
                appreqs.new_request(
                    name=name,
                    age=age, address=address, phone=phone, gender=gender, cnn_result=result['EFFNET']
                )

                st.write("😊 Your information has been stored in our database!")

            else:
                st.warning("Enter both the description and upload the image if you want to make the AI system examine your problem.")
                
        else:
            st.warning("First fill all the information on the sidebar given on the left in order to make the AI system examine your problem!")

with tab2:
    st.write("Doctor's login here...")
    st.write("This part is under development!")

    dash = st.button(label="See dashboard", type='secondary')
    if dash:
        st.write(dbread.display_db())

    


