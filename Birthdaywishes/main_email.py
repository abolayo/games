import smtplib
import datetime as dt

my_email = "myemail@gmail.com"
password = "get_password"  # from the sender emai security settings
name = "placeholder"
day = 0
email = "email"

now = dt.datetime.now()
birthdate = "birthdate"
if now - day == 0:
    with open(f'{name}.txt') as birthday_person:
        message = birthday_person.readlines()

    with smtplib.SMPT("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, passwd=password)
        connection.sendmail(to_addrs=f"{email}",
                            from_addr=my_email,
                            msg=f"Subject:Wishes\n\n{message}"
                            )
