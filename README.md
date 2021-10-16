# stocks-dnn
A financial asset price prediction program using deep learning

Author: Declan R Borcich
Initiated October 2021

1. Program takes daily (not tick-level) financial asset price data via .csv
2. Converts data to pandas DataFrame with Open, High, Low, Close, Volume data
3. Deep Neural Network is trained on this historical data, with input layer
  neurons parameterized on asset return over trailing 1 day, 2 day, 5 day,
  25 day, 50 day, 250 day periods; also volume 
