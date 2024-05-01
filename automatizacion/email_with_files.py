
# This script is used to send an email using the Gmail SMTP server

# Import necessary libraries
from email.message import EmailMessage
import ssl
import smtplib
import imghdr # To use files

# Define the email addresses and authentication information
emisor_email = "santiagodavidsanabriavarela@gmail.com"
email_password = 'sdrh xcur qghr gjfz'
receptor_email = "sanabriasanti1237@gmail.com"

# Obtain user input for the email header and body
header = str(input("Type the header: "))
body = str(input("Enter the body: "))

# Create an EmailMessage object
em = EmailMessage()

# Set the email properties
em['From'] = emisor_email
em['To'] = receptor_email
em['Subject'] = header
em.set_content(body)

### Putting files
with open('maxresdefault.jpg', 'rb') as file :# rb is to read the bytes
  file_data = file.read()
  # To have the type of file
  file_type =imghdr.what(file.name)
  file_name = file.name
# To add it
em.add_attachment(file_data,filename = file_name, subtype = file_type, maintype = 'image') ## The first one is the file to send, the second is the name of the file, the third one is the sub type and the last in the principal type


# Create a SSL context for securing the connection
context = ssl.create_default_context()

# Connect to the Gmail SMTP server and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
  server.login(emisor_email, email_password)
  server.sendmail(emisor_email, receptor_email, em.as_string())