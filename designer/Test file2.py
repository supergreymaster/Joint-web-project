from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os

filepath = "/path/to/file"
basename = os.path.basename(filepath)
address = "help.converter@yandex.ru"

# Compose attachment
part = MIMEBase('application', "octet-stream")
part.set_payload(open(filepath, "rb").read())
# Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)

# Compose message
msg = MIMEMultipart()
msg['From'] = address
msg['To'] = address
msg.attach(part)

# Send mail
smtp = SMTP_SSL()
smtp.connect('smtp.yandex.ru')
smtp.login(address, 'password')
smtp.sendmail(address, address, msg.as_string())
smtp.quit()
