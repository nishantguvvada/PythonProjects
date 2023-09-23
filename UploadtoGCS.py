from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import os
import tkinter
from tkinter import messagebox

# Line 32 to 51 pertains to the code for uploading files to GCS bucket
# Instantiating tkinter
window = tkinter.Tk()

# GUI window title and dimension
window.title("Upload to GCS")
window.geometry('500x250')

label_header = tkinter.Label(window, text='Upload to Google Cloud Storage Bucket', font=('Helvetica 16 underline'))
label_header.pack(pady=5, padx=5)
label_subhead = tkinter.Label(window, text='Provide the source path of the file', font=('Helvetica 10'))
label_subhead.pack(pady=5, padx=5)

user_entry1 = tkinter.Entry(window, width=50)
user_entry1.pack(pady=10, padx=10)
user_entry1.delete(0, tkinter.END)

label_subhead = tkinter.Label(window, text='Provide the bucket name', font=('Helvetica 10'))
label_subhead.pack(pady=5, padx=5)

user_entry2 = tkinter.Entry(window, width=30)
user_entry2.pack(pady=10, padx=10)
user_entry2.delete(0, tkinter.END)


# upload_to_gcs is a function taking path of file to be uploaded and destination bucket's name
def upload_to_gcs(filename, bucket):
    # Setting the environment variable GOOGLE_APPLICATION_CREDENTIALS to the .json file containing credentials
    # To obtain the .json file : IAM -> Service Accounts -> Click on a service account -> Keys -> Add Key (key will be auto downloaded)
    os.environ[
        'GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\nish3395\OneDrive - Rackspace Inc\Documents\Python_Automation\rax-enterprisebi-dev-e994aa08b90b.json'

    credentials = GoogleCredentials.get_application_default()  # getting key from environment variable and saving into credentials variable
    service = discovery.build('storage', 'v1', credentials=credentials)

    # filename = r'C:\Users\nish3395\OneDrive - Rackspace Inc\Documents\Dashboard\ITS Project\Remediation_data - Test.csv'
    # bucket = 'tableau_source_files'

    body = {'name': 'Remediation_data - Test'}
    req = service.objects().insert(bucket=bucket, body=body, media_body=filename)
    resp = req.execute()
    print(f"File {filename} uploaded to {bucket}.")


# onclick function calls the upload_to_gcs function and triggers "completed" message upon completion
def onclick():
    xpath = user_entry1.get()
    xbucket = user_entry2.get()
    upload_to_gcs(xpath, xbucket)
    tkinter.messagebox.showwarning("COMPLETED!", "Success")


# Create a Button that will trigger the onclick function when the button is pressed
first_button = tkinter.Button(window, text='Submit', command=onclick, height=1, width=10)
first_button.pack(pady=5, padx=5)

# Set the position of button on the top of window.
first_button.pack()
window.mainloop()
