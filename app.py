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
              
elif (page == "Faqs"):
      st.title("FAQS");
      st.write("""What is sentiment analysis?
                According to Google  Sentiment analysis, also referred to as opinion mining, is an approach to natural language processing 
                (NLP) that identifies the emotional tone behind a body of text. 
                This is a popular way for organizations to determine and categorize opinions about a product, service, or idea.""");
                
      st.write("""How can sentiment anlysis be used?
            Sentiment Analysis can be used to understand public opinions on nearly everything like the review of a product 
            or the working of a company or the way the people are reacting to news. """);
      text_contents = '''
                  Foo, Bar
                  123, 456
                  789, 000
                  '''

      st.download_button('Download CSV', text_contents, 'text/csv')
      st.download_button('Download CSV', text_contents)  # Defaults to 'text/plain'

      with open('myfile.csv') as f:
            st.download_button('Download CSV', f)  # Defaults to 'text/plain'

      # ---
      # Binary files
      binary_contents = b'whatever'
      st.download_button('Download file', binary_contents)  # Defaults to 'application/octet-stream'
      with open('myfile.zip', 'rb') as f:
            st.download_button('Download Zip', f, file_name='archive.zip')  # Defaults to 'application/octet-stream'
      if st.download_button(...):
            st.write('Thanks for downloading!')
       
