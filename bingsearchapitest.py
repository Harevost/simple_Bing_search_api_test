import requests

subscription_key = "xxxx" # your Bing search API key
# subscription_key_2 = "xxxx"
assert subscription_key

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
search_term = "ip:" + input("Please input an IP address:")

headers = {"Ocp-Apim-Subscription-Key": subscription_key}   # API KEY
params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}  # 搜索参数

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results_all = response.json()

if "webPages" in search_results_all:
    search_results_count = search_results_all["webPages"]["totalEstimatedMatches"]
else:
    print("Can't find any website.")
    exit(1)

print("total count:" + str(search_results_count))   # 搜索总条目数

params = {"q": search_term, "textDecorations": True, "textFormat": "HTML", "count": 50, "offset": 0}
results_counted = 0
results_list = []

while results_counted <= search_results_count:
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results_all = response.json()
    results_list = search_results_all['webPages']['value']
    params["offset"] += 50  # 继续搜索
    results_counted += 50

    for result in results_list:
        print(result['name'] + '   ' + result['url'])
