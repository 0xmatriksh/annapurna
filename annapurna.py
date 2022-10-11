import requests
import json

search_q = input("Enter query : ")  # get the search query from user
result = []  # store the articles data in this list
page = 1  # page count
prev_l = 0  # to count number of already stored data

# to load the already collected data in previous request if any
try:
    with open(f"{search_q}.json", "r") as openfile:
        json_object = json.load(openfile)
        prev_l = len(json_object)
    result = json_object # to populate with the data of previously collected data
except:
    pass
    

while len(result) < 30:

    url = f"https://bg.annapurnapost.com/api/search?title={search_q}&page={page}"

    res = requests.get(url).json()

    try:
        # to continue adding page untill the number of already collected records is not surpassed (if there is any)
        if prev_l > 0:
            prev_l = prev_l - len(res["data"]["items"])

        # to continue adding the data to the list untill it reach 30
        else:
            for record in res["data"]["items"]:
                if len(record) > 30:
                    break
                result.append(record)

        page += 1

    # if there is no new record in new page break the loop
    except Exception as e:
        break

json_obj = json.dumps(result)

with open(f"{search_q}.json", "w") as outfile:
    outfile.write(json_obj)
