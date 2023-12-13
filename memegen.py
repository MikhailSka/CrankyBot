import requests
params = {"words": 10, "paragraphs": 1, "format": "json"}
response = requests.get(f"https://jokes.p.rapidapi.com/", params=params,
 headers={
   "X-RapidAPI-Host": "jokes.p.rapidapi.com",
   "X-RapidAPI-Key": "b9d29d0c87mshfea21405f5354a8p1be65bjsn8dfcc8df6113"
 }
)
print (type(response.json()))
print(response.json())
