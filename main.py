import pandas as pd

daily_rp = pd.read_csv("data/daily_report.csv")
totals = daily_rp[["Confirmed","Deaths","Recovered","Active"]].sum().reset_index(name="count")
totals = totals.rename(columns={"index":"condition"})
