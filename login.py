from tkinter import*
#from PIL import ImageTk
class Login_System:
    def __init__(self,root): #constructor
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x800+0+0")
        print("hello")
        
        '''All Images'''
        self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon=PhotoImage(file="images/man-user.png")
        self.pass_icon=PhotoImage(file="images/pass.png")

        title=Label(self.root,text="")

root=Tk()
obj=Login_System(root)
root.mainloop()