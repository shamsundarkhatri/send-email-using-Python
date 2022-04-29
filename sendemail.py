import smtplib
port = 587
conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('yourmail@gmail.com', 'emailpassword')
conn.sendmail('yourmail@gmail.com','toemail@gmail.com','Subject: Your Subject \n\n Your message')
conn.quit()
print("Success")
