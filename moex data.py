import requests
import pandas as pd

def moex_data(x, s, e):
  
  url = (
    f"https://iss.moex.com/iss/engines/stock/"
    f"markets/shares/securities/{x}/candles.json"
    )

  params = {
      "from": s,
      "till": e,
      "interval": 24
  }
  
  r = requests.get(url, params=params)
  data = r.json()
  
  columns = data["candles"]["columns"]
  rows = data["candles"]["data"]
  
  df = pd.DataFrame(rows, columns=columns)
  
  return df

moex_data("SBER", "2024-01-01", "2024-12-31")
