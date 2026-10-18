# Currency Analytics Engine

A Python-based currency conversion and analytics application with a graphical user interface (GUI).

The application retrieves live and historical exchange-rate data from online APIs and performs basic statistical analysis, including moving averages, volatility calculation, and next-rate forecasting.

## Features

- Live currency conversion
- Historical exchange-rate retrieval
- 7-day moving average
- Annualised volatility calculation
- Simple statistical next-rate forecasting
- Tkinter graphical user interface
- Input validation and error handling
- API and network error handling

## Technologies Used

- **Python 3.12**
- **Tkinter** — GUI development
- **Requests** — HTTP/API communication
- **Frankfurter API** — exchange-rate and historical data
- **Statistics module** — mean and standard deviation calculations
- **Math module** — mathematical calculations

## Prerequisites

Before running the application, make sure you have:

- Python 3.12 or later
- An active internet connection

The application requires an internet connection because exchange-rate data is retrieved from online APIs.

## Installation

Open **Command Prompt** and install the required dependency:

```bash
py -3.12 -m pip install requests
```

## Running the Application

Navigate to the project folder containing the Python file.

Then run:

```bash
py -3.12 se_currency_converter.py
```

## Usage

### Currency Conversion

1. Enter the amount to convert.
2. Select the **From Currency**.
3. Select the **To Currency**.
4. Click **Convert**.
5. The application retrieves the latest exchange rate and displays the converted amount.

### 45-Day Analytics

1. Select the **From Currency**.
2. Select the **To Currency**.
3. Click **Run 45-Day Analytics**.
4. The application retrieves historical exchange-rate data.
5. The application calculates:
   - Latest exchange rate
   - 7-day moving average
   - Annualised volatility
   - Next-rate forecast

## Analytics Methods

### 7-Day Moving Average

The application calculates the average exchange rate across the most recent seven observations.

This provides a simple measure of the recent exchange-rate level.

### Annualised Volatility

The application calculates daily percentage changes in the exchange rate and uses their standard deviation to estimate annualised volatility.

The calculation uses:

```text
Annualised Volatility = Daily Standard Deviation × √252
```

### Next-Rate Forecast

A simple linear regression model is used to estimate the next exchange-rate value based on historical observations.

This is a basic statistical forecasting approach implemented for analytical purposes.

## Error Handling

The application includes handling for:

- Invalid numerical input
- Missing currency selections
- Unsupported currency pairs
- Network connection problems
- Invalid or unexpected API data

## Project Structure

```text
se_currency_converter.py
README.md
```

## Important Note

The forecasting feature provides a **simple statistical estimate based on historical exchange-rate trends**. It is not intended to provide guaranteed predictions of future currency prices or professional financial advice.

## Project Status

**Completed**

The current version includes currency conversion, historical data retrieval, statistical analysis, forecasting, GUI development, API integration, and error handling.
