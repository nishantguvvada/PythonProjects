import datetime
import os
import win32com.client

path = os.path.expanduser(r'C:\Users\...\Documents')

today = datetime.date.today()

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items

def saveattachemnts(subject):
    for message in messages:
        if message.Subject == subject and message.Senton.date() == today:
            # body_content = message.body
            attachments = message.Attachments
            attachment = attachments.Item(1)
            for attachment in message.Attachments:
                attachment.SaveAsFile(os.path.join(path, str(attachment)))
                if message.Subject == subject and message.Unread:
                    message.Unread = False
                break

saveattachemnts('Test - Subject')
