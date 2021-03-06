
import tkinter as tk
#import tkcalendar
root = tk.Tk()
frame=tk.Frame(root)
def submitButtonClicked(event):
    print("Submit Button CLicked. Callback function called successfully")

def quitButtonClicked(event):
    print("Quit Button Clicked. Callback function called successfully.")
    root.destroy()

tk.Label(root, text="Start Date").grid(row=0, sticky=tk.W)
tk.Label(root, text="Start Time").grid(row=1,sticky=tk.W)
tk.Label(root, text="End Date").grid(row=2, sticky=tk.W)
tk.Label(root, text="End Time").grid(row=3,  sticky=tk.W)
tk.Label(root, text="Change Duration (in hours)").grid(row=4,  sticky=tk.W)
tk.Label(root, text = "Change duration Explanation").grid(row=5, sticky=tk.W)
tk.Label(root, text = "System Name :").grid(row=6,sticky=tk.W)
tk.Label(root, text = "Impact Scope :").grid(row=7,sticky=tk.W)
tk.Label(root, text = "Affected Site(s) :").grid(row=8,sticky=tk.W)
tk.Label(root, text = "HSBC Requester Name :").grid(row=9,sticky=tk.W)
tk.Label(root, text = "Is Testing needed from HSBC? :").grid(row=10,sticky=tk.W) # Name and contact details to be specified
tk.Label(root, text = "Change Request Nature :").grid(row=11,sticky=tk.W)
tk.Label(root, text = "Provide Supporting Ticket :").grid(row=12,sticky=tk.W)
tk.Label(root, text = "To be Implemented by :").grid(row=13,sticky=tk.W)
tk.Label(root, text = "Cisco Project Manager for this Request :").grid(row=14,sticky=tk.W)
tk.Label(root, text = "All affected CI(s) without IP addresses:").grid(row=15,sticky=tk.W)
tk.Label(root, text = "Peer Reviewed By  :").grid(row=16,sticky=tk.W)
tk.Label(root, text = "Number of Configuration Items in scope of the change :").grid(row=17,sticky=tk.W)
#tk.Label(root, text = "HSBC Requester Name :").grid(row=18,sticky=tk.W)


tk.Entry(root).grid(row=0, column=1, sticky=tk.E)
tk.Entry(root).grid(row=1, column=1, sticky=tk.E)
tk.Entry(root).grid(row=2, column=1, sticky=tk.E)
tk.Entry(root).grid(row=3, column=1, sticky=tk.E)
tk.Entry(root).grid(row=4, column=1, sticky=tk.E)
tk.Entry(root).grid(row=5,column=1, sticky = tk.E)
tk.Entry(root).grid(row=6,column=1, sticky = tk.E)
tk.Entry(root).grid(row=7,column=1, sticky = tk.E)
tk.Entry(root).grid(row=8,column=1, sticky = tk.E)
tk.Entry(root).grid(row=9,column=1, sticky = tk.E)
tk.Entry(root).grid(row=10,column=1, sticky = tk.E)
tk.Entry(root).grid(row=11,column=1, sticky = tk.E)
tk.Entry(root).grid(row=12,column=1, sticky = tk.E)
tk.Entry(root).grid(row=13,column=1, sticky = tk.E)
tk.Entry(root).grid(row=14,column=1, sticky = tk.E)
tk.Entry(root).grid(row=15,column=1, sticky = tk.E)
tk.Entry(root).grid(row=16,column=1, sticky = tk.E)
tk.Entry(root).grid(row=17,column=1, sticky = tk.E)


submitButton = tk.Button(root, text="Submit")
submitButton.grid(row=18,column=0)
submitButton.bind("<Button-1>", submitButtonClicked)
submitButton.bind("<Return>",submitButtonClicked)

quitButton = tk.Button(root, text="Quit")
quitButton.grid(row=18,column=1)
quitButton.bind("<Button-1>",quitButtonClicked)
#cal = tkcalendar.Calendar(root)
#cal.grid(row=19)

""" cal = tkcalendar.Calendar(root,selectmode='none')
cal.grid(row=4,column=1)
date = tkcalendar.DateEntry(root)
date.grid(row=7,column=1)
 """
root.mainloop()
