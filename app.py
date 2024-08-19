import streamlit as st
import os
from constant import Gemini_api
# from MyInfo import resume_prompt
from llama_index.llms.gemini import Gemini
# from llama_index.core import Settings
import time
from llm import resume_engine,agent
from MyInfo import firstResponse



def main():
    st.set_page_config(layout="wide")
    st.markdown(
        """
        <style>
        .center-title {
            text-align: center;
            margin: -50px 0 0 0;
            padding: 20px;
        }
        </style>
        <h1 class="center-title">ResumeBot</h1>
        """,
        unsafe_allow_html=True
    )
    with st.sidebar:
        st.image("image.png", use_column_width=True)
        st.markdown(
        """
        <div style="margin-top:-50px;margin-bottom:15px">
            <h1>Hello,</h1>
            <p> I am <b>Ashish Sharma</b>, an individual with a profound interest in the realm of <i>Generative AI</i>. Currently, I am dedicatedly involved in this field through my professional endeavors.</p>
        </div>
        <div style="margin-bottom:15px">
            <h2>Education</h2>
            <ul>
                <li>BS in Physics from IIT Kanpur (2024)</li>
                <li>12th from OIA (2020)</li>
                <li>10th from DPS (2018)</li>
            </ul>
        </div>
        <div style="margin-bottom:30px">
            <h3>Experience</h2>
            <ul>
                <li>AI engineer at - <i>Valiance Solutions</i></li>
                <li>Machine Learning Engineer at - <i>Xatalyst Labs</i></li>
                <li>Prompt engineer at - <i>Hrrkoin</i></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
        )
    
    # Create a placeholder for the success message
    message_placeholder = st.empty()
    if Gemini_api:
        # If the API key is present in Gemini_api
        os.environ["GOOGLE_API_KEY"] = Gemini_api
        # with message_placeholder.container():
        #     st.success("API key is already set.")
        # time.sleep(2)  # Display the message for 30 seconds
        # message_placeholder.empty()  # Clear the placeholder
    else:
        # If the API key is not present in Gemini_api, prompt user input
        api_key = st.text_input(label="Put your Gemini API here because I am broke", type='password')
        if api_key:
            # Set the environment variable if the user provides it
            os.environ["GOOGLE_API_KEY"] = api_key
            with message_placeholder.container():
                st.success("API key has been set.")
            time.sleep(2)  # Display the message for 30 seconds
            message_placeholder.empty()  # Clear the placeholder
    # st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    llm = Gemini()


    if "messages" not in st.session_state:
        st.session_state.messages = [{"role":"assistant","content":firstResponse}]
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if question := st.chat_input("Ask your query here..."):
        st.chat_message("user").markdown(question)
        st.session_state.messages.append({"role":"user","content":question})

        response= agent.chat(question)

        with st.chat_message("assistant"):
            st.markdown(response)
        
        st.session_state.messages.append({"role":"assistant","content":response})


    




    
    


if __name__=="__main__":
    main()
