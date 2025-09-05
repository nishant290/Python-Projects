import sys
sys.stdout.reconfigure(encoding="utf-8")
import pandas as pd
import requests
from bs4 import BeautifulSoup


watch_name = []
watch_brand = []
watch_price = []
watch_availability = []


for i in range(1,3):
    url = "https://www.flipkart.com/search?q=watches+for+men+under+2000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="+str(i)

    # print(url)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    # print(req)

    soup = BeautifulSoup(req.text, "lxml")

    boxes = soup.find_all("div", class_="DOjaWF gdgoEp")

    for box in boxes:

        name = box.find_all("a", class_="WKTcLC")
        brand = box.find_all("div", class_="syl9yP")
        price = box.find_all("div", class_="Nx9bqj")

        if name and brand and price:
            for i in name:
                name = i.text
                watch_name.append(name)

            for i in brand:
                brand = i.text    
                watch_brand.append(brand)

            for i in price:
                price_clean = i.text.replace("₹", "").replace(",", "").strip()    
                watch_price.append(price_clean)



print(f"Total so far → names: {len(watch_name)}, brands: {len(watch_brand)}, prices: {len(watch_price)}")
# print(f"Total so far → names: {(watch_name)}, brands: {(watch_brand)}, prices: {(watch_price)}")



df = pd.DataFrame({"Watch Name":watch_name,"Watch Brand":watch_brand, "Watch Price":watch_price})
print(df)

df.to_csv("men_watches_under_2000.csv")



