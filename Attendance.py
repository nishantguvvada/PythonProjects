import webbrowser
import tkinter

window = tkinter.Tk()

window.title("Attendance Reminder")
window.geometry('300x150')

label_header = tkinter.Label(window, text='Fill Timesheet!', font=('Helvetica 16 underline'))
label_header.pack(pady=5, padx=5)
label_subhead = tkinter.Label(window, text="It's Friday!!", font=('Helvetica 10'))
label_subhead.pack(pady=10, padx=5)

window.mainloop()

webbrowser.open('https://timesheet')
