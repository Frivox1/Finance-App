# Stock Chart App

This is a simple web application that allows users to visualize stock closing prices over a specified number of days.

## Getting Started

To get started, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/VOTRE_UTILISATEUR/VOTRE_PROJET.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `config.py` file at the root of your project and add your Alpha Vantage API key:

    ```python
    # config.py
    api_key = 'VOTRE_CLE_API'
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

Visit `http://127.0.0.1:5000/` in your browser to use the Stock Chart App.

## Important Note

This application uses the Alpha Vantage API for fetching stock data. Please note that the free Alpha Vantage API key has limitations, and you are allowed a limited number of requests (e.g., 25 requests per day). If you encounter issues with data fetching, consider upgrading to a premium key.

## Alpha Vantage API Key

You can obtain your free API key from [Alpha Vantage](https://www.alphavantage.co/). Update the `api_key` variable in `config.py` with your key.

## Limitations

The free Alpha Vantage API key has the following limitations:

- **Requests Limit:** The free key allows a limited number of requests per day (e.g., 25 requests).
- **Data Retrieval:** Due to the limitations, historical data retrieval may be affected.

Consider upgrading to a premium key if you require more extensive usage.
