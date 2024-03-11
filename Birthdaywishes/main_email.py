import smtplib
import pandas as pd
import datetime as dt

my_email = "myemail@gmail.com"
password = "get_password"  # from the sender email security settings

# -------------------import data frame --------------------
df = pd.read_csv("./Input/Names/names.csv")
df['date'] = pd.to_datetime(df['date'])
df['month'] = df.date.dt.month
df['day'] = df.date.dt.day
print(df.head())
now = dt.datetime.now()
now_month = now.month
now_day = now.day
print(now_month, now_day, now)
for index, row in df.iterrows():
    if now_month == row['month'] and now_day == row['day']:
        with open(f'{row['name']}.txt') as birthday_person:
            message = birthday_person.readlines()

        with smtplib.SMPT("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, passwd=password)
            connection.sendmail(to_addrs=f"{row['email']}",
                                from_addr=my_email,
                                msg=f"Subject:Wishes\n\n{message}"
                                )

