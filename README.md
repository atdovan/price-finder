# Stock Trading Strategy using LassoCV

This project implements a stock trading strategy for Google (`GOOG`) using a LassoCV model. The strategy is based on predictive modeling of stock returns using technical indicators and lagged returns. The model predicts future stock price direction, and trades are executed based on these predictions.

## Project Structure

- **Data Collection**: Stock price data is downloaded from Yahoo Finance using the `yfinance` library.
- **Feature Engineering**: The project creates lagged features and technical indicators such as SMA, Volatility, Momentum, and RSI.
- **Modeling**: A LassoCV model is trained to predict stock returns based on these features.
- **Trading Strategy**: Trades are made based on the predicted direction of the stock price (long or short).
- **Performance Evaluation**: The strategy is backtested on the test set, and cumulative returns are compared to the market's returns.

## Key Components

- **yfinance**: To download stock data.
- **scikit-learn**: Used for training the LassoCV model and scaling the data.
- **pandas**: For data manipulation and feature engineering.
- **matplotlib**: For plotting the cumulative returns of both the market and strategy.

## How It Works

1. **Download Stock Data**:
   - Google (`GOOG`) stock data is downloaded from Yahoo Finance from January 1, 2020.

2. **Feature Engineering**:
   - Lagged returns (`Lag_1`, `Lag_2`, ..., `Lag_5`) are created to capture previous stock price movements.
   - Technical indicators like `SMA_5`, `SMA_10`, `Volatility`, `Momentum`, and `RSI` are calculated.

3. **Modeling**:
   - A `LassoCV` model is trained on the features to predict the future stock returns.
   - The model uses cross-validation to find the best regularization parameter for generalization.

4. **Trading Strategy**:
   - Based on the model's predicted returns, a trading signal is generated (`1` for long, `-1` for short).
   - The strategy calculates returns based on the direction and logs the cumulative return.

5. **Performance Evaluation**:
   - Cumulative returns are calculated for both the strategy and the market.
   - The Mean Squared Error (MSE) of the model is also displayed.

## Performance

The strategy's cumulative returns are calculated and compared against the market returns. Both are plotted for easy comparison.

```bash
Lasso Model MSE: [model error]
Cumulative Returns (Market): [market returns]
Cumulative Returns (Strategy): [strategy returns]
