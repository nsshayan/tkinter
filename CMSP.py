import tkinter as tk

PROGRAM_NAME = ' CMSP '
editLines = [3,4,5,7,13,29,34,40,43,55,57,60,62,73,77,84,105,107]
# 105 and 107 - both require system anme
class HSBC:

    def __init__(self, root):
        self.data = []
        self.root = root
        self.root.title(PROGRAM_NAME)
        self.root.geometry(newGeometry='600x600+600+150')
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


        self.startDate = tk.Entry(root)
        self.startDate.grid(row=0, column=1, sticky=tk.E)
        self.startTime = tk.Entry(root)
        self.startTime.grid(row=1, column=1, sticky=tk.E)
        self.endDate = tk.Entry(root)
        self.endDate.grid(row=2, column=1, sticky=tk.E)
        self.endTime = tk.Entry(root)
        self.endTime.grid(row=3, column=1, sticky=tk.E)
        self.changeDuration = tk.Entry(root)
        self.changeDuration.grid(row=4, column=1, sticky=tk.E)
        self.changeDurationExplanation = tk.Entry(root)
        self.changeDurationExplanation.grid(row=5,column=1, sticky = tk.E)
        self.systemName = tk.Entry(root)
        self.systemName.grid(row=6,column=1, sticky = tk.E)
        self.impactScope = tk.Entry(root)
        self.impactScope.grid(row=7,column=1, sticky = tk.E)
        self.affectedSite = tk.Entry(root)
        self.affectedSite.grid(row=8,column=1, sticky = tk.E)
        self.requesterName = tk.Entry(root)
        self.requesterName.grid(row=9,column=1, sticky = tk.E)
        self.testingNeeded = tk.Entry(root)
        self.testingNeeded.grid(row=10,column=1, sticky = tk.E)
        self.requestNature = tk.Entry(root)
        self.requestNature.grid(row=11,column=1, sticky = tk.E)
        self.supportTicket = tk.Entry(root)
        self.supportTicket.grid(row=12,column=1, sticky = tk.E)
        self.implementationBy = tk.Entry(root)
        self.implementationBy.grid(row=13,column=1, sticky = tk.E)
        self.projectManager = tk.Entry(root)
        self.projectManager.grid(row=14,column=1, sticky = tk.E)
        self.affectedSiteWithoutIP = tk.Entry(root)
        self.affectedSiteWithoutIP.grid(row=15,column=1, sticky = tk.E)
        self.peerReviewedBy = tk.Entry(root)
        self.peerReviewedBy.grid(row=16,column=1, sticky = tk.E)
        self.configurationItemsInScope = tk.Entry(root)
        self.configurationItemsInScope.grid(row=17,column=1, sticky = tk.E)


        submitButton = tk.Button(root, text="Submit")
        submitButton.grid(row=18,column=0)
        submitButton.bind("<Button-1>", self.submitButtonClicked)
        submitButton.bind("<Return>", self.submitButtonClicked)

        quitButton = tk.Button(root, text="Quit")
        quitButton.grid(row=18,column=1)
        quitButton.bind("<Button-1>",self.quitButtonClicked)

    def submitButtonClicked(self,event):
        print("Submit Button CLicked. Callback function called successfully")
        self.data.append(self.startDate.get() + ' ' + self.startTime.get())
        self.data.append(self.endDate.get() + ' ' +  self.endTime.get())
        self.data.append(self.changeDuration.get())
        self.data.append(self.changeDurationExplanation.get())
        self.data.append(self.systemName.get())
        self.data.append(self.impactScope.get())
        self.data.append(self.affectedSite.get())
        self.data.append(self.requesterName.get())
        self.data.append(self.testingNeeded.get())
        self.data.append(self.requestNature.get())
        self.data.append(self.supportTicket.get())
        self.data.append(self.implementationBy.get())
        self.data.append(self.projectManager.get())
        self.data.append(self.affectedSiteWithoutIP.get())
        self.data.append(self.peerReviewedBy.get())
        self.data.append(self.configurationItemsInScope.get())
        print(self.data)
        self.writeToFile()

    def quitButtonClicked(self,event):
        print("Quit Button Clicked. Callback function called successfully.")
        self.root.destroy()
    
    def writetoendofline(self,lines,line_no,append_txt):
        lines[line_no] = lines[line_no].replace('\n', '') + append_txt + '\n'


    def writeToFile(self):

        with open('./CMSP_dup.txt', 'r') as txtfile:
            lines = txtfile.readlines()

        for i in range(len(self.data)):
            self.writetoendofline(lines, editLines[i], self.data[i])


        # write the edited content back to the file
        with open('./text', 'w') as txtfile:
            txtfile.writelines(lines)

        # close the file
        txtfile.close()
        self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    HSBC(root)  
    root.mainloop()
