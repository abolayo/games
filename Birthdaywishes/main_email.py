import random
import smtplib
import datetime as dt
my_email = "myemail@gmail.com"
password = "get_password" # from the sender emai security settings

now = dt.datetime.now()
birthdate = "birthdate"
if now - day == 0:
    with open('./ReadyToSend/.txt') as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMPT("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, passwd=password)
        connection.sendmail(to_addrs="gogo@yahoo.com",
                            from_addr=my_email,
                            msg=f"Subject:Hello\n\n{quote}"
                            )
