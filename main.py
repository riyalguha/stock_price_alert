import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# stock_API_key: "BDX72C1F66C0LUJ8"
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": "BDX72C1F66C0LUJ8",
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response=requests.get(url=STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()
# print(response.status_code)
data=response.json()['Time Series (Daily)']





#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yest_close=float(data['2022-09-16']['4. close'])
# print(yest_close)
#TODO 2. - Get the day before yesterday's closing stock price
yest_yest_close=float(data['2022-09-15']['4. close'])
# print(yest_yest_close)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff=yest_close-yest_yest_close
print(diff)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
per=(diff/yest_yest_close)*100
round_per=round(per,2)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if round_per>=0.0:
    news_params={
        "q":"tesla",
        "from":"2022-08-17",
        "sortBy":"publishedAt",
        "apiKey":"a038d542ead942a1b0b08d244b914953"
    }
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response=requests.get(url=NEWS_ENDPOINT,params=news_params)
    news_response.raise_for_status()
# print(news_response.status_code)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    data=news_response.json()['articles'][:3]
    # print(data)
    new_list=[]
    for i in range(3):
        new_list.append({
            "title" : data[i]['title'],
            "description" : data[i]['description'],
        })



        account_sid = "AC69f76f6a32a4f04846859dc05147e404"
        auth_token = "1afc844b070383f72ffd16603dcb4244"
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: 😘^{round_per}"
                f"Headline :{new_list[i]['title']}"
                f"Brief :{new_list[i]['description']}",
            from_='+16693228238',
            to='+917044488944'
            )
elif round_per<0.0:
    news_params = {
        "q": "tesla",
        "from": "2022-08-17",
        "sortBy": "publishedAt",
        "apiKey": "a038d542ead942a1b0b08d244b914953"
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    data = news_response.json()['articles'][:3]
    # print(data)
    new_list = []
    for i in range(3):
        new_list.append({
            "title": data[i]['title'],
            "description": data[i]['description'],
        })

        account_sid = "AC69f76f6a32a4f04846859dc05147e404"
        auth_token = "1afc844b070383f72ffd16603dcb4244"
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: 😨{round_per} \n"
                 f"Headline :{new_list[i]['title']} \n"
                 f"Brief :{new_list[i]['description']}\n",
            from_='+16693228238',
            to='+917044488944'
        )

#     new_list.append=[{
#         "title" : news['title'],
#         "description" : news['description']
#     }]
# print(new_list)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

