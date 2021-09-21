import requests
from twilio.rest import Client

api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = 'ACb58335d64b490ff0a69ff7c7614b212b'
auth_token = '082712f89404b62e4ba406e4d1a9a63d'

param = {
    'lat':36.59,
    'lon':153.51,
    'exclude':'current,minutely,daily',
    'appid':api_key

}
connection = requests.get('https://api.openweathermap.org/data/2.5/onecall',params=param)
connection.raise_for_status()

data = connection.json()

bring_an_umbrella = False

for hour in range(0,12):

    if bring_an_umbrella != True:
        if data['hourly'][hour]['weather'][0]['id'] < 700:
            bring_an_umbrella = True

if bring_an_umbrella:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="It's going to rain like cats and dogs today."
             "Make sure to bring an umbrella!☔",
        from_='+17175848967',
        to='+9779843487701'
    )

    print(message.status)



