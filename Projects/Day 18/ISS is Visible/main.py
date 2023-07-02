import smtplib
import ssl
import requests
from datetime import datetime

my_lat = -140.3007  
my_lng = 20.9143


def is_iss_overhead():
    iss_res = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_res.raise_for_status()
    iss_data = iss_res.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if (my_lat - 5 <= iss_lat <= my_lat + 5) and (my_lng - 5 <= iss_lng <= my_lng + 5):
        return True 


def is_night():

    parameters = {
        "lat":my_lat,
        "lng":my_lng,
        "formatted" : 0,
    }

    sun_req = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_data = sun_req.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if (time_now >= sunset) or (time_now <= sunrise):
        return True



if is_iss_overhead and is_night:
    
    my_mail = "preettaparia@gmail.com"  
    password = "fiankphuuyruaake"

    receiver_email = "meettaparia99@gmail.com"

    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    
    message ="The ISS is visible:"

    simple_email_context = ssl.create_default_context()

    try:
        print("connecting to server..")
        connection = smtplib.SMTP(smtp_server, smtp_port)
        connection.starttls(context = simple_email_context)
        connection.login(my_mail, password)
        print("connected to server")
        print()
        print(f"Sending email to: {my_mail}")
        connection.sendmail(my_mail, my_mail, message)
        print(f"Email succesfully send to: {my_mail}")
        print(f"message: {message}")
        
    except Exception as e:
        print(e)
        
    finally:
        connection.quit()
    
