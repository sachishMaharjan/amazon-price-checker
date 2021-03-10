from bs4 import BeautifulSoup
import requests
from smtplib import SMTP

MY_EMAIL = "YOUR SENDING EMAIL"
PASSWORD = "YOUR PASSWORD"
RECEIVER_EMAIL = "your receiving email"

URL = "https://www.amazon.com.au/Nikon-D5600-18-55mm-70-300mm-851501/dp/B07RMTV67F/?_encoding=UTF8&pd_rd_w=KFapq&pf_rd_p=37a6e77e-e8e8-43c7-9685-b318cfbb9f8b&pf_rd_r=588PEX3F3ZFEG6C0RZ3W&pd_rd_r=9386ed46-3a5a-4a4b-a62f-9d5302518719&pd_rd_wg=GaQWM&ref_=pd_gw_ci_mcx_mr_hp_d"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
response = requests.get(url=URL, headers=headers)
amazon_wpg = response.text
# print(amazon_wpg)

soup = BeautifulSoup(amazon_wpg, "html.parser")
# print(soup.span)

price_tag = soup.find(name="span", id="priceblock_ourprice")
price_string = price_tag.getText().split("$")[1]
prices = price_string.split(",")
total_price = ""
for price in prices:
    total_price += price

price_float = float(total_price)
print(price_float)

if price_float < 1260:
    with SMTP("smtp.gmail.com.") as smtp:
        smtp.starttls()
        smtp.login(user=MY_EMAIL, password=PASSWORD)
        smtp.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject: Amazon Price Alert!, \n\n camera is now {price_float}"
        )