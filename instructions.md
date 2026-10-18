# Currency Analytics Engine

A Python desktop application for **real-time currency conversion, historical exchange-rate analysis, and basic statistical forecasting**.

This project demonstrates practical skills in **Python development, REST API integration, data processing, statistical analysis, GUI development, input validation, and exception handling**.

## Features

- Real-time currency conversion
- Historical exchange-rate retrieval
- 45-day exchange-rate analysis
- 7-day moving average
- Annualised volatility calculation
- Linear regression-based next-rate forecasting
- Tkinter graphical user interface
- Input validation
- API and network error handling

## Technologies

- **Python 3.12**
- **Tkinter / ttk**
- **Requests**
- **Frankfurter API**
- **Statistics module**
- **Math module**
- **REST API**
- **JSON data processing**
- **Statistical analysis**

## Key Implementation

### REST API Integration

The application integrates with the Frankfurter API to retrieve current and historical exchange-rate data.

The implementation includes:

- HTTP GET requests
- API parameter handling
- JSON response processing
- HTTP status validation
- Network exception handling

### Currency Conversion

Users can enter an amount and select the source and target currencies. The application retrieves the latest exchange rate and calculates the converted value.

Supported currencies:

`USD` `EUR` `GBP` `MYR` `JPY` `AUD` `SGD`

### Historical Exchange-Rate Analysis

The application retrieves approximately 45 days of historical exchange-rate data and performs several statistical calculations.

#### 7-Day Moving Average

Calculates the average exchange rate across the latest seven observations to provide a simple indication of the recent exchange-rate level.

#### Annualised Volatility

Daily percentage changes are calculated from the historical rates. The standard deviation of these returns is then annualised using:

```text
Annualised Volatility = Daily Standard Deviation × √252
```

#### Next-Rate Forecast

A simple linear regression calculation is used to estimate the next exchange-rate value based on historical observations.

This is a basic statistical forecasting method intended for analytical and demonstration purposes.

## Error Handling

The application includes handling for:

- Invalid numerical input
- Negative amounts
- Missing currency selections
- Invalid currency pairs
- Network connection failures
- HTTP/API errors
- Invalid API data
- Insufficient historical data

User-friendly error messages are displayed through the graphical interface.

## Project Structure

```text
Currency-Analytics-Engine/
│
├── se_currency_converter.py
└── README.md
```

## Requirements

- Python 3.12 or later
- Internet connection
- `requests` package

## Installation

Install the required Python dependency:

```bash
py -3.12 -m pip install requests
```

## Running the Application

Run the application from the project directory:

```bash
py -3.12 se_currency_converter.py
```

The Tkinter graphical interface will open after the application starts.

## Usage

### Currency Conversion

1. Enter the amount.
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

## Skills Demonstrated

- Python programming
- REST API integration
- JSON data processing
- GUI development with Tkinter
- Data validation
- Exception handling
- Statistical analysis
- Basic linear regression
- External API consumption
- User-focused application development

## Limitations

The forecasting feature uses a simple linear regression approach and is not intended to provide guaranteed predictions of future currency prices or professional financial advice.

The application also requires an active internet connection because exchange-rate data is retrieved from an external API.

## Future Improvements

- Interactive exchange-rate charts
- Additional currency support
- Configurable historical periods
- More advanced forecasting models
- CSV export
- Automated unit testing
- Improved GUI design

## Project Status

**Completed**

This project demonstrates an end-to-end Python application combining GUI development, REST API integration, data processing, statistical analysis, basic forecasting, and error handling.
