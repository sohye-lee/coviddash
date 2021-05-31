import pandas as pd
import requests

# API 
url_countries = "https://covid-193.p.rapidapi.com/countries"
url_history = "https://covid-193.p.rapidapi.com/history"
url_statistics = "https://covid-193.p.rapidapi.com/statistics"


headers = {
    'x-rapidapi-key': "f433e69929msh4d44c939ac0abbcp1187e1jsn3577f2bbadfd",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

query = {"country":"usa","day":"2020-06-02"}

response = requests.request("GET", url_statistics, headers=headers)
res_history = requests.request("GET", url_history, headers=headers, params=query)

# API ENDS


daily_rp = pd.read_csv("data/daily_report.csv")
totals = daily_rp[["Confirmed","Deaths","Recovered","Active"]].sum().reset_index(name="count")
totals = totals.rename(columns={"index":"condition"})
