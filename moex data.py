import requests
import pandas as pd

def moex_data(x, s, e): # Moex Data
  
  if isinstance(x, str):
    x = [x]
  
  dfs = []
  
  for ticker in x:
    
    url = (
      f"https://iss.moex.com/iss/engines/stock/"
      f"markets/shares/securities/{ticker}/candles.json"
      )
      
    params = {
        "from": s,
        "till": e,
        "interval": 24
    }
    
    data = requests.get(url, params=params).json()
    
    columns = data["candles"]["columns"]
    rows = data["candles"]["data"]
    
    df = pd.DataFrame(rows, columns=columns)
    
    df["Date"] = pd.to_datetime(df["begin"]).dt.date
    
    df = df[["close", "Date"]].set_index("Date").rename(
      columns={"close": ticker})
      
    dfs.append(df)
  
  return pd.concat(dfs, axis=1)

moex_data(["SBER", "GAZP"], "2024-01-01", "2024-12-31")
