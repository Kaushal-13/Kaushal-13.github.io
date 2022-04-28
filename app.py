import streamlit as st 
import pandas as pd;
from streamlit_option_menu import option_menu
#do using vader
from textblob import TextBlob 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def score(sentence):
    obj = SentimentIntensityAnalyzer()
    sentiment_dict = obj.polarity_scores(sentence);
    ''' to map the value bw 0 - 5 we use f(x) = 2.5(x+1)'''
    val = sentiment_dict['compound'] + 1;
    val = val*2.5;
    #return val if you need to map bw 0 and 5;
    return sentiment_dict['compound'];
    
with st.sidebar:
    choose = option_menu("App Gallery", ["About us", "Our App", "Faqs", "Advanced Version"],
                         icons=['house', 'file', 'quora', 'file-fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
if(choose == "About us"):
      st.title("About us");
      st.write(""" This is a basic version of the sentiment analysis app
                we are a team of two, Kaushal Tiwari and Shubh Agarwal studying at Nit-Ap.
                The goal of this app is to track people's opinion """);
elif(choose == "Our App"):
        # Title
        st.title("Sentiment Analysis")
        result_sentiment = 2
        # Sentiment Analysis
        st.subheader("Analyse Your Text")

        message = st.text_area("Enter Text")
        if st.button("Analyze"):
              result_sentiment = score(message)
            
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
              
elif (choose == "Faqs"):
      st.title("FAQS");
      st.write("""What is sentiment analysis? \n
                According to Google  Sentiment analysis, also referred to as opinion mining, is an approach to natural language processing 
                (NLP) that identifies the emotional tone behind a body of text. 
                This is a popular way for organizations to determine and categorize opinions about a product, service, or idea.""");
                
      st.write("""How can sentiment anlysis be used?\n
            Sentiment Analysis can be used to understand public opinions on nearly everything like the review of a product 
            or the working of a company or the way the people are reacting to news. """);
elif(choose == "Advanced Version"):
      st.title("This is the advanced version It can accept datasets");
      uploadedFile = st.file_uploader("Upload File",type=['csv','xlsx'],accept_multiple_files = False,key = "fileUploader");
      if uploadedFile is not None and uploadedFile.type == "csv":
            st.write('Prediction  :')
            df1 = pd.read_csv(uploadedFile);
            sum = 0;
            for index,row in df.iterrows():
                sum = sum + score(row["tweet']);
        if st.button("Analyze"):
              result_sentiment = sum
            
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
            
