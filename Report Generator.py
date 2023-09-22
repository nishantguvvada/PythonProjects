import pandas as pd
import tkinter
from tkinter import messagebox
from google.cloud import bigquery
from google.oauth2 import service_account

# create the GUI window
window = tkinter.Tk()

# GUI window title and dimension
window.title("Generate Your Report")
window.geometry('500x200')

label_header = tkinter.Label(window, text='Generate Your Report', font=('Helvetica 16 underline'))
label_header.pack(pady=5, padx=5)
label_subhead = tkinter.Label(window, text='Provide the destination of the report', font=('Helvetica 10'))
label_subhead.pack(pady=5, padx=5)


user_entry = tkinter.Entry(window, width=50)
user_entry.pack(pady=10, padx=10)
user_entry.delete(0, tkinter.END)


def dataextraction(bqpath):
    credentials = service_account.Credentials.from_service_account_file(
    r'C:\Users\...\GCP_authentication.json')

    client = bigquery.Client(credentials=credentials)

    # Perform a query.
    QUERY = (
        """SELECT * FROM `report_tables` 
        WHERE filter_1 = '123' AND filter_2 IN (456) AND filter_3 = '20230301'
        """
    )
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    df = pd.DataFrame(rows)
    df.to_csv(bqpath)


def onclick():
    xpath = user_entry.get()
    dataextraction(xpath)
    tkinter.messagebox.showwarning("COMPLETED!", "Success")


# Create a Button
first_button = tkinter.Button(window, text='Submit', command=onclick, height=1, width=10)
first_button.pack(pady=5, padx=5)

# Set the position of button on the top of window.
first_button.pack()
window.mainloop()
