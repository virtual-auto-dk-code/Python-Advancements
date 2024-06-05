email = 'abc@gmail.com,pqr@gmail.com'
emailList1 = ['xyz@gmail.com']
sa_app_recipients = []
# ---------------------------------------------------------------------
sz = 0
sa_app_recipients_list = []
if "," in email:
    sa_app_recipients = email.split(",")
    sz = len(sa_app_recipients)
else:
    sa_app_recipients.append(email)
    sz = 1
print("Total " + str(sz) + " Email ID/IDs associtated with application")
emailList = emailList1 + sa_app_recipients  # (Add External Email of SA) Comment/Uncomment to send/Not to send email to all
# ---------------------------------------------------------------------
# emailList = ["abc@gmail.com"]
print("Email Sent to - \n" + str(emailList))
