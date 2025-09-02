# Stock Sentiment Analysis for Price Movement Prediction

This project builds an end-to-end data science pipeline to predict the next day's stock price direction (Up or Down) for a given stock (e.g., AAPL) based on the sentiment of financial news headlines.

---
## Key Features
- **Data Collection**: Fetches historical stock prices using `yfinance` and news articles from NewsAPI.
- **Sentiment Analysis**: Uses the pre-trained `FinBERT` model for accurate, domain-specific sentiment scoring of financial text.
- **Feature Engineering**: Combines sentiment scores with technical indicators like Simple Moving Average (SMA) and Relative Strength Index (RSI).
- **Modeling**: An XGBoost classifier is trained on the prepared features to predict price movement.

---
## How to Run This Project
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/Stock-Sentiment-Analysis.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Stock-Sentiment-Analysis
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```
4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Launch Jupyter Lab and run the notebook:**
    ```bash
    jupyter lab your_notebook_name.ipynb
    ```

---
## Project Structure
- `NLP_for_Stock_Forecasting.ipynb`: The main Jupyter Notebook containing all the analysis and modeling steps.
- `requirements.txt`: A list of all Python libraries required to run the project.
- `AAPL_stock_data.csv`: Sample stock data collected.
- `AAPL_news_data.csv`: Sample news data collected.
