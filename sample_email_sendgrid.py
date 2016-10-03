
#
# Claudia Bittmann September 2016
#
# Email: coding.claudia@gmail.com
#
# This program sends emails directly through SendGrid's API
# by importing your email list via a csv, pulling the email addresses and 
# dynamic content, and then inputting that information into the email send request.
# This logic then sends out the emails iteratively every 5 seconds via a where loop 
# using a dataframe via pandas.
#
# API logic via sendgrid.com
#

import sendgrid
import csv
import pandas
import time
import datetime

api_key = #Enter your API Key provided by SendGrid here
sg = sendgrid.SendGridClient(api_key)

path = #Enter the path to your email list csv here -- example: r'\\C:\Users\Claudia\Documents\Python\GitHub\email_list.csv'
email = pandas.read_csv(path)
print (email.columns)
list(df)

x = len(email.index)
z = 0

html = "This is where you paste in your html code"

while z < x:
    EMAIL = email.iloc[z]['email'] #your list of emails
    EMAILlist = str(EMAIL)
    Variable1 = email.iloc[z]['variable1'] #dynamic content within your email
    Variable2 = email.iloc[z]['variable2'] #dynamic content within your email



    time.sleep(5)
    if z == 0:
        message = sendgrid.Mail()
        message.set_from('Your Name <youremail@email.com>') #Update with your from email address and name
        message.set_subject('Amazing Subject Line') #Update with your desired subject line
        message.set_html(html)

# SMTP API
#========================================================#
# Add the recipients
        message.smtpapi.set_tos([
            EMAILlist
,    
            ])

# Substitutions
        subs = {
            "%Variable_1%": [
                str(Variable1)
                ],
    
            "%Variable_2%": [
                Variable2
                ]
                }
        for tag, values in subs.items():
            for value in values:
                message.add_substitution(tag, value)


#========================================================#
# Categories
        categories = [
            "Sample Category" #Sub in your desired category
            ]
        for category in categories:
            message.add_category(category)                



# SEND THE MESSAGE
#========================================================#
        status, msg = sg.send(message)

        print(msg)
        z = z + 1
    else:
        message = sendgrid.Mail()
        message.set_from('Your Name <youremail@email.com>') #Update with your from email address and name
        message.set_subject('Amazing Subject Line') #Update with your desired subject line
        message.set_html(html)

# SMTP API
#========================================================#
# Add the recipients
        message.smtpapi.set_tos([
            EMAILlist
,    
            ])

# Substitutions
        subs = {
            "%Variable_1%": [
                str(Variable1)
                ],
    
            "%Variable_2%": [
                Variable2
                ]
                }
        for tag, values in subs.items():
            for value in values:
                message.add_substitution(tag, value)


#========================================================#
# Categories
        categories = [
            "Sample Category" #Sub in your desired category
            ]
        for category in categories:
            message.add_category(category)                



# SEND THE MESSAGE
#========================================================#
        status, msg = sg.send(message)

        print(msg)
        z = z + 1
