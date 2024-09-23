import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = yf.download('GOOG', start='2020-01-01')
df ['returns'] = np.log(df.Close.pct_change() + 1)

def lagit(df, lags):
    names = []
    for i in range(1, lags+1):
        df['Lag_'+str(i)] = df['returns'].shift(i)
        names.append('Lag_'+str(i))
    return names
    
lagnames = lagit(df, 6)
df.dropna(inplace=True)


model = LinearRegression()

model.fit(df[lagnames], df['returns'])
df['prediction_LR'] = model.predict(df[lagnames])
df['direction_LR'] = [1 if i > 0 else -1 for i in df.prediction_LR]
df['strat_LR'] = df['direction_LR'] * df['returns']




train,test = train_test_split(df, shuffle=False, test_size=0.3, random_state=0)
train = train.copy()
test = test.copy()
model = LinearRegression()
model.fit(train[lagnames], train['returns'])
test['prediction_LR'] = model.predict(test[lagnames])
test['direction_LR'] = [1 if i > 0 else -1 for i in test.prediction_LR]
test['strat_LR'] = test['direction_LR'] * test['returns']
print(np.exp(test[['returns', 'strat_LR']].sum()))

print((test['direction_LR'].diff() != 0).value_counts())