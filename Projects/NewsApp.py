import requests 

query= input("Enter The Topic: ")
api= "pub_bfd359ec201f486ea9f7695212d7015b"

url= f"https://newsdata.io/api/1/latest?apikey={api}&q={query}"
print(url)

r= requests.get(url)
data= r.json()
articles = data["results"]
print(data)


for article in articles:
    print("Title: ", article["title"])
    print("Link: ", article["link"])
    print("_" * 50)








