import streamlit as st 
from textblob import TextBlob 

page = st.selectbox("Choose your page",["About us","Our App","Faqs"]);

if(page == "About us"):
      st.title("About us");
      st.write(""" This is a basic version of the sentiment analysis app
                we are a team of two, Kaushal Tiwari and Shubh Agarwal studying at Nit-Ap""");
elif(page == "Our App"):
        # Title
        st.title("Sentiment Analysis")
        result_sentiment = 2
        # Sentiment Analysis
        st.subheader("Analyse Your Text")

        message = st.text_area("Enter Text")
        if st.button("Analyze"):
              blob = TextBlob(message)
              result_sentiment = blob.sentiment[0]
                    
            
        if result_sentiment > 0.5 and result_sentiment < 1 :
              st.write('Prediction  :')
              st.subheader('Positive')
              st.success(f'Score : {result_sentiment}')

        elif result_sentiment < 0 :
              st.write('Prediction  :')
              st.subheader('Negative')
              st.success(f'Score : {result_sentiment}')

        elif result_sentiment >= 0 and result_sentiment <= 0.5 :
              st.write('Prediction  :')
              st.subheader('Neutral')
              st.success(f'Score : {result_sentiment}')
