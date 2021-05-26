
import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('varunjha1245@gmail.com', 'Varun@2000')
    server.sendmail('varunjha1245@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    sendEmail("varunjha2000@gmail.com", 'Surprise boi')