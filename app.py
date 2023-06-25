# import main libraries

import os
import pandas as pd
import numpy as np
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from pandasai.middlewares.streamlit import StreamlitMiddleware
import streamlit as st
# import matplotlib
# matplotlib.use('TkAgg')



# instantiate LLM with PandasAI

llm = OpenAI(api_token='sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', engine='gpt-3.5-turbo')

pandas_ai = PandasAI(llm, middlewares=[StreamlitMiddleware()], verbose=False)



## streamlit app

# streamlt app page config

st.set_page_config(page_title='Google Analytics Dataset Chatbot with PandasAI', page_icon='🤖', layout='wide')

# title

st.title('📉 Google Analytics Dataset Chatbot with PandasAI')

# subtitle

st.subheader('A conversational AI chatbot that can answer questions about your Google Analytics data.')

# dataset info and download link

st.info('The dataset used is a Google Analytics public dataset provided through Bigquery that can be downloaded from [Here](https://console.cloud.google.com/marketplace/product/obfuscated-ga360-data/obfuscated-ga360-data?project=hotelcustomerdata).')

st.success('Please upload your Google Analytics data in excel format. After the file is uploaded, you will see the first 5 rows of the dataset. Then, you will see an input text area wher you can ask a questions about the dataset and get an answer from the chatbot.')

# upload file

uploaded_file = st.file_uploader('Upload your Google Analytics data in excel format', type=['xlsx'])

# check if file is uploaded

if uploaded_file is not None:
    # store the file in a Pandas dataframe
    df = pd.read_excel(uploaded_file)
    
    # describe the dataframe
    
    st.warning('Showing the 5 first rows of the dataframe.')
    
    # show the first 5 rows of the dataframe
    st.write(df.head())
    
    # create an input text box to start asking questions about the dataset and get answers from the chatbot
    
    st.subheader('Ask a question about your Google Analytics data and get an answer from the chatbot.')
    
    # create an input text box to start asking questions about the dataset and get answers from the chatbot
    
    question = st.text_input(label='Ask a question')
    
    # check if the question is not empty
    
    if st.button('Generate Response'):
        if question:
            with st.spinner('Generating response, please wait...'):
                # get the response from the chatbot
                #pandas_ai.run(df,question, is_conversational_answer=True)
                # show the response
                st.write(pandas_ai.run(df,question, is_conversational_answer=True))
        else:
            st.warning('Please ask a question.')
        
