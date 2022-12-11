import requests, json
import pandas as pd

req = requests.get(url='https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=csv&limit=1000')
with open('./input/Current_Daily_Price_Of_Various_Commodities_From_Various_Markets_(Mandi).csv', 'wb') as f:
    f.write(req.content)
    
  
df = pd.read_csv('./input/Current_Daily_Price_Of_Various_Commodities_From_Various_Markets_(Mandi).csv')
for i in range(len(df)):
    params = {'query' : f"{df.loc[i, 'Market']}, {df.loc[i, 'District']}, {df.loc[i, 'State']}"}
    req = requests.get(url='http://api.positionstack.com/v1/forward?access_key=18dc02ae1cf902ce1a6d4a74c5366986', params=params)
    dic = json.loads(req.content)
    df.loc[i, 'Latitude'] = dic['data'][0]['latitude']
    df.loc[i, 'Longitude'] = dic['data'][0]['longitude']
    
df.to_csv('./input/Current_Daily_Price_Of_Various_Commodities_From_Various_Markets_(Mandi)_With_Lat_Long.csv')