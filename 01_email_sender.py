import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com",port = 587)
    server.starttls()

    # receiver email
    receiver_email = input("Enter the receiver email : ")

    # mail credentials
    senders_email = "madhur09.trinity@gmail.com"
    password = "whxh vlvn fljl ocev"

    #login
    server.login(senders_email, password)

    # sending mail
    subject = input("Enter the subject : ")
    body = input("Enter the body : ")
    message = f"Subject : {subject}  \n\n {body}"
    server.sendmail(senders_email, receiver_email, message)
    print("email send successfully")

    server.quit()
except Exception as e:
    print("Failed to send email : ", e)