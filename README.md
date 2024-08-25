
# StockAssist: A Stock Market Analysis Tool
![image](https://github.com/user-attachments/assets/db5b5ddc-bab6-4f66-9665-a1b00a360d69)

Visit Demo: https://youtu.be/VMVPh0ox84k
Visit here: https://stockassist.streamlit.app/

## Overview

**StockAssist** is an AI-powered platform designed to provide real-time stock market analysis, generate actionable insights, and visualize price data, helping investors and businesses make informed decisions. Leveraging the IBM Watson Granite 7B LAB model, StockAssist offers a comprehensive and user-friendly solution for analyzing stock performance, identifying investment opportunities, and mitigating risks.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Target Audience](#target-audience)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Problem Statement

Many individual investors and financial advisors face challenges in effectively analyzing stock performance, identifying potential investment opportunities, and mitigating risks. Stock-related information is often scattered across various third-party apps and websites, making it difficult for investors to gather relevant data. Traditional methods involve complex financial analysis, time-consuming research, and a lack of personalized insights.

## Solution

StockAssist, powered by the IBM Watson Granite 7B LAB model, addresses these challenges by offering a streamlined and user-friendly platform. The application provides comprehensive stock analysis, generates actionable insights, and visualizes price trends—all in one place. It empowers users to make informed investment decisions and serves as a foundation for further consultation if desired.

## Key Features

- **Real-Time Market Analysis:** Continuously monitors the stock market and provides real-time updates on trends, helping investors stay ahead of market shifts.
- **AI-Generated Strategic Recommendations:** Analyzes market data and social media sentiment using AI, generating strategies, insights, and potential risks associated with a stock.
- **User-Friendly Dashboard:** A visually appealing and easy-to-use dashboard that allows users to interact with data and insights seamlessly.
- **Customizable Insights:** Users can input any stock ticker to access its information and view price fluctuation charts within seconds.

## How It Works

1. **User Input:** The user enters a stock ticker into the Streamlit application.
2. **Data Extraction:** The app extracts key metrics from historical data related to the stock.
3. **Data Processing:** A summarized input text is prepared and sent to the IBM Watson Granite 7B LAB model.
4. **AI Analysis:** The model generates insights, strategies, and potential risks based on the input and its internal knowledge.
5. **Results Display:** The results are displayed on the Streamlit app interface, where users can interact with the data and insights.

## Target Audience

- **Individual Investors:** Those looking to invest in the stock market but lacking the expertise or time for in-depth analysis.
- **Financial Advisors:** Professionals aiming to enhance client services by providing data-driven insights and recommendations.
- **Beginners:** Individuals new to investing who need guidance and support in understanding stock market dynamics.

## Technology Stack

- **Frontend:** Streamlit for building the user interface.
- **Backend:** IBM Watson Granite 7B LAB model for AI-powered analysis.
- **Data Sources:** Historical stock data and real-time market information.

## Installation

To run StockAssist locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/stockassist.git
   cd stockassist
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501`.
2. Enter a stock ticker in the input field.
3. View the real-time analysis, strategic recommendations, and visualized data on the dashboard.
4. Customize your insights by exploring different stock tickers.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

