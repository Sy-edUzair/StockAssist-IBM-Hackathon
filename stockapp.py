import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt 
import io
from dotenv import load_dotenv
import os
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods

load_dotenv()
# IBM Watson credentials and model setup
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": os.getenv("IBM_API_KEY")
}
project_id = os.getenv("IBM_PROJECT_ID")

model_id = ModelTypes.GRANITE_7B_LAB
parameters = {
    GenParams.MIN_NEW_TOKENS: 0,
    GenParams.MAX_NEW_TOKENS: 1000,
    GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
    GenParams.REPETITION_PENALTY: 1.1
}

model = Model(model_id=model_id, params=parameters, credentials=credentials, project_id=project_id)

def get_stock_data(ticker, period='1y'):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)

def get_current_price(ticker):
    data = get_stock_data(ticker)
    return data['Close'].iloc[-1]

def get_volume(ticker):
    data = get_stock_data(ticker)
    return data['Volume'].mean()  # Average trading volume

def get_volatility(ticker):
    data = get_stock_data(ticker)
    return data['Close'].std() 

def analyze_stock(ticker):
    data = get_stock_data(ticker)
    current_price = get_current_price(ticker)
    volume = get_volume(ticker)
    volatility = get_volatility(ticker)


    latest_data = data.tail(100)  # Get the last 100 records for brevity
    mean_price = latest_data['Close'].mean()
    max_price = latest_data['Close'].max()
    min_price = latest_data['Close'].min()
    
    # Prepare a summarized input text for the model
    input_text = (f"Analyze the stock performance of {ticker}. "
                  f"The current price is ${current_price}. "
                  f"Here are the key metrics from the last 100 records:\n"
                  f"Mean Price: ${mean_price:.2f}\n"
                  f"Max Price: ${max_price:.2f}\n"
                  f"Min Price: ${min_price:.2f}\n"
                  f"Average Volume: {volume:.2f}\n"
                  f"Volatility (Standard Deviation): {volatility:.2f}\n"
                  f"Please provide an analysis based on these metrics.Generate Insights or strategies on how to invest as well as mention possible risks."
                  f"First Analyse each provided metric individually first , then give strategies in seperate heading of overall Analysis and then tells risks if any in seperate headings")
    
    # Get a response from the model
    try:
        response = model.generate(prompt=input_text)
        return response
    except Exception as e:
        return f"Error generating response: {e}"
    

def plot_stock_data(ticker,year):
    data = get_stock_data(ticker,year)
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.title(f'{ticker} Stock Price fluctuation ove year(s)')
    plt.xlabel('Date')
    plt.ylabel('Stock Price ($)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    
    # Save the plot to a BytesIO object and return it
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img


# Streamlit UI setup
st.title("Stock Market Analysis with IBM Granite 7B LAB Model")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):")


if ticker:
    ticker=ticker.upper()
    st.write(f"Analyzing {ticker}...")
    analysis_result = analyze_stock(ticker)
    st.write("Analysis Result:")
    response_text = analysis_result['results'][0]['generated_text']
    cleaned_text = response_text.split("<|endoftext|>")[0]
    st.write(cleaned_text)

    options = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    selected_option = st.selectbox("Select an option:", options)

    if st.button('Generate'):
        stock_plot = plot_stock_data(ticker,selected_option)
        st.image(stock_plot, caption=f'{ticker} Stock Price Chart')
