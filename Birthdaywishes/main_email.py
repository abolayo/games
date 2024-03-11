import smtplib
import pandas as pd
import datetime as dt

my_email = "myemail@gmail.com"
password = "get_password"  # from the sender email security settings


# -------------------import data frame --------------------
df = pd.read_csv("./Input/Names/names.csv")
df['date'] = pd.to_datetime(df['date'])

day = df.date.dt.day
month = df.date.dt.month
date = df.date
name = df['name']
email = df["email"]
now = dt.datetime.now().month
birthdate = "birthdate"
print(day, month,date, now)


# if now - day == 0:
#     with open(f'{name}.txt') as birthday_person:
#         message = birthday_person.readlines()
#
#
#     with smtplib.SMPT("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, passwd=password)
#         connection.sendmail(to_addrs=f"{email}",
#                             from_addr=my_email,
#                             msg=f"Subject:Wishes\n\n{message}"
#                             )
