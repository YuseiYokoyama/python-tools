from pprint import pprint as pp
from pprint import pformat as pf

import os
import yaml
import random
import time
import ssl
from smtplib import SMTP, SMTP_SSL

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.utils import formataddr, formatdate

def createMailMessageMIME(frm, to, subject, message, fpath=None):
    # MIMETextを作成
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = frm
    msg['To'] = to
    #msg.attach(MIMEText(message, 'plain', 'utf-8'))
    msg.attach(MIMEText(message, 'html', 'utf-8'))

    # 添付ファイルの設定
    if fpath:
        with open(fpath, 'rb') as fp:
            attach_file = MIMEApplication(fp.read())
            attach_file.add_header(
                "Content-Disposition", 
                "attachment", 
                filename=os.path.basename(fpath)
            )
            msg.attach(attach_file)
    return msg

def send_email(msg, smtp_config):
    account = smtp_config["account"]
    password = smtp_config["password"]
    host = smtp_config["host"]
    port = smtp_config["port"]
    context = ssl.create_default_context()
    server = SMTP_SSL(host, port, context=context)
    server.login(account, password)
    server.send_message(msg)
    server.quit()

def make_mime(to_email, mail_config):
    sender_name = mail_config["sender_name"]
    sender = mail_config["sender"]
    frm_email = formataddr((sender_name, sender))
    subject = mail_config["subject"]
    message = open(mail_config["fpath_text"], encoding="utf_8_sig").read()
    fpath = mail_config.get("fpath_attachment", None)
    mime = createMailMessageMIME(frm_email, to_email, subject, message, fpath)
    return mime

if __name__ == '__main__':
    parser = argparse.ArgumentParser("cmd", description="This is hogehoge")
    args = parser.parse_args()

    """ config.yml
    mail:
      sender_name: "株式会社ほげ"
      sender: "hoge@rfuga.com"
      subject: "タイトル"
      fpath_text: "html形式のメール本文"
      fpath_attachment: "添付ファイル.pdf"
    smtp:
      account: "hoge@fuga.com"
      password: "piyo"
      host: 'sample.host.ne.jp'
      port: 465
    """

    mime = make_mime("yuuseitori@gmail.com", config["mail"])
    send_email(mime, config["smtp"])

    print('\033[32m' + 'end' + '\033[0m') # ]] fix indent




