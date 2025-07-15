from pprint import pprint as pp
from pprint import pformat as pf

import os
import ssl
from smtplib import SMTP, SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formataddr

def make_mime(sender_name, sender_addr, to_addr, subject, message, subtype="plain"):
    # MIMETextを作成
    mime = MIMEMultipart()
    mime['From'] = formataddr((sender_name, sender_addr))
    mime['To'] = to_addr
    mime['Subject'] = subject
    mime.attach(MIMEText(message, subtype, 'utf-8'))
    return mime

def attach_files(mime, fpath_list):
    # 添付ファイルの設定
    if fpath_list is None:
        return mime
    for fpath in fpath_list:
        with open(fpath, 'rb') as fp:
            attach_file = MIMEApplication(fp.read())
            attach_file.add_header(
                "Content-Disposition",
                "attachment",
                filename=os.path.basename(fpath)
            )
            mime.attach(attach_file)
    return mime

def send_email(mime, smtp_config):
    context = ssl.create_default_context()
    server = SMTP_SSL(smtp_config["host"], smtp_config["port"], context=context)
    server.login(smtp_config["account"], smtp_config["password"])
    server.send_message(mime)
    server.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser("cmd", description="This is hogehoge")
    args = parser.parse_args()

    sender = "hoge@fuga.com"

    sender_name = "株式会社ほげ"
    sender_addr = sender
    to_addr = "piyo@piyo.com"
    subject = "タイトル"
    message = "<b>これは本文です</b>"

    fpath_list = ["添付ファイル.pdf", "添付ファイル2.pdf"]

    smtp_config = {
      "account": sender,
      "password": "piyo",
      "host": 'sample.host.ne.jp',
      "port": 465,
    }

    mime = make_mime(sender_name, sender_addr, to_addr, subject, message, subtype="html")
    attach_files(mime, fpath_list)
    send_email(mime, smtp_config)

    print('\033[32m' + 'end' + '\033[0m') # ]] fix indent

