import smtplib

def sendmail(text):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    password = "ybxsrytkgqhagbgo"

    server.login("noahgames99@gmail.com", "zzwaljakpbtrbwtq")
    server.sendmail("noahgames99@gmail.com", "5096889826@vtext.com", str(text))
    server.quit()



