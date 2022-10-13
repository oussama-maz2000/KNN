import math
import pandas as pd;
url="./states.csv"
least_distance=list()
x=list()
y=list()
dist=list()



def readDatafromCSV(url):
    names=["name","longitude","latitude"]
    dataset=pd.read_csv(url,usecols=names)
    dataset=dataset.reset_index()    
    return dataset



def calculateDistance(longPharma,latPharma,longClient,latClient):
    count_distance=math.sqrt(((longPharma-longClient)**2)+((latPharma-latClient)**2))
    return count_distance


def getNearsetPharmacy(longitude,latitude,clientDistance):
    data=readDatafromCSV(url)
    for index ,row in data.iterrows():
        lng=row["longitude"]
        lat=row["latitude"]
        distance=calculateDistance(lng,lat,longitude,latitude)
        if distance <= clientDistance:
            least_distance.append(distance)
            x.append(lng)
            y.append(lat)
            dist.append(distance)
    df=pd.DataFrame({'longitude':x,'latitude':y,'distance':dist })
    for index,row in df.iterrows():
        print(row)

getNearsetPharmacy(35.5381401,6.098486,3);
    

    


 
