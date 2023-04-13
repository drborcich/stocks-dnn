# stocks-lr
A script for measuring metrics on SPY data.

Author: Declan R Borcich
Initiated October 2021

1. Program takes daily (not tick-level) financial asset price data via .csv,
2. Converts data to pandas DataFrame with Open, High, Low, Close, Volume data
3. Simple ARIMA (autoregression) model is trained on this historical data, with input layer
  neurons parameterized on: (1) asset return* over trailing 1 day, 2 day, 5 day,
  25 day, 50 day, 250 day periods; (2) volume over the same periods, baselined
  against the average daily volume over the 250 day period; (3) realized volatility 
  (standard deviation, or sqrt(variance)) over the same periods; 
  (4) implied volatiliy for the ~30-day forward period, as described by the
  VIX

*Return Price(t_1) - Price(t_0) / Price(t_0) 
