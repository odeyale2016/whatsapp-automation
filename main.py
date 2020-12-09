import pywhatkit
import requests
import json
import  time
import datetime
import schedule
def job():
    now = datetime.datetime.now()
    r= requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    a=json.loads(r.text)
    btc_string ="1 bitcoin will cost you"+ str(a["bitcoin"]["usd"]) + "US Dollars. - from Alphatech(The PythonCoder) "
    pywhatkit.sendwhatmsg("+2348104004365",btc_string, now.hour, now.minute+1)
job()
schedule.every().hour.do(job)

while  True:
    schedule.run_pending()
    time.sleep(1)