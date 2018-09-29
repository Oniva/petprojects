import smtplib, sys, json, time, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 


with open("#") as read_file:
    data = json.load(read_file)
try:
    while True:
        for worker in data:
            if data[worker]['working'] == "False" and data[worker]['sent'] == "False":
                data[worker]['sent'] == "True"
                with open("#", "w") as write_file:
                    json.dump(data, write_file)

                fromaddr = "#"
                toaddr = "#"
                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg['Subject'] = "Email Service"
                
                body = "{} is done".format(worker)
                msg.attach(MIMEText(body, 'plain'))
                
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(fromaddr, ("PASSWORD HERE"))
                text = msg.as_string()
                server.sendmail(fromaddr, toaddr, text)
                server.quit()
        time.sleep(10)
except KeyboardInterrupt:
    os.system('clear')
    sys.exit()
