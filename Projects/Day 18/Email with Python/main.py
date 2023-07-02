import smtplib
import ssl

my_mail = ""  
password = ""

receive_email = ""

smtp_port = 587
smtp_server = "smtp.gmail.com"


message = "Please Work!!"

simple_email_context = ssl.create_default_context()

try:
    print("connecting to server..")
    connection = smtplib.SMTP(smtp_server, smtp_port)
    connection.starttls(context = simple_email_context)
    connection.login(my_mail, password)
    print("connected to server")
    print()
    print(f"Sending email to: {my_mail}")
    connection.sendmail(my_mail, receive_email, message)
    print(f"Email succesfully send to: {receive_email}")
    
    
except Exception as e:
    print(e)
    
finally:
    connection.quit()
    
