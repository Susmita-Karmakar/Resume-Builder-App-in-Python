from tkinter import*
from dbhelper import DBhelper
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import Tk,Frame,Label
import shutil,os


class Login:
    def __init__(self):
        self.db=DBhelper()
        self.root = Tk()

        self.root.title("Resume App")

        self.root.configure(background="#6A9113")

        self.root.minsize(600, 600)
        self.root.maxsize(600, 600)
        self.load_gui()

    def load_gui(self):
        self.clear()

        self.label1=Label(self.root, text="Wanna write a resume?? Login here",fg="white",bg="#6A9113")
        self.label1.configure(font=("Times",15,"bold"))
        self.label1.pack(pady=(20,30))

        self.frame1=Frame(self.root,bg="#6A9113")
        self.frame1.pack()
        self.label2 = Label(self.frame1, text="Email:", fg="black", bg="#6A9113")
        self.label2.configure(font=("Times", 20, "italic"))
        self.label2.pack(ipadx=30,side='left')

        self.email = Entry(self.frame1)
        self.email.pack(side='left', ipadx=50, ipady=7)

        self.frame2 = Frame(self.root, bg="#6A9113")
        self.frame2.pack(pady=(20,5))
        self.label3 = Label(self.frame2, text="Password:", fg="black", bg="#6A9113")
        self.label3.configure(font=("Times", 20, "italic"))
        self.label3.pack(ipadx=10,side='left')

        self.password = Entry(self.frame2)
        self.password.pack(side='left',pady=(10,5), ipadx=50, ipady=7)

        self.login = Button(self.root, text="Click here to Login", bg="grey",fg="black",command=lambda :self.btn_click())
        self.login.configure(font=("Times", 12, "bold"))
        self.login.pack(pady=(40,30),ipadx=30)

        self.frame3 = Frame(self.root, bg="#6A9113")
        self.frame3.pack(pady=(100, 5))
        self.label4 = Label(self.frame3, text="Not a member? Register here :", fg="white", bg="#6A9113")
        self.label4.configure(font=("Times", 14, "italic"))
        self.label4.pack(side='left',ipadx=10)

        self.register = Button(self.frame3, text="Sign Up", bg="grey",fg="black",command=lambda :self.register_gui())
        self.register.configure(font=("Times", 12, "bold"))
        self.register.pack(side='left',ipadx=15)



        self.root.mainloop()

    def register_gui(self):
        self.clear()

        self.label0 = Label(self.root, text="Register here to proceed !!", fg="white", bg="#6A9113")
        self.label0.configure(font=("Times", 15, "bold"))
        self.label0.pack(pady=(5, 5))

        self.frame1 = Frame(self.root, bg="#6A9113")
        self.frame1.pack(pady=(60, 5))
        self.label1 = Label(self.frame1, text="Name:", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 20, "italic"))
        self.label1.pack(side='left',ipadx=32)

        self.name = Entry(self.frame1)
        self.name.pack(side='left', ipadx=45, ipady=5)

        self.frame2 = Frame(self.root, bg="#6A9113")
        self.frame2.pack(pady=(20, 5))
        self.label2 = Label(self.frame2, text="Email:", fg="black", bg="#6A9113")
        self.label2.configure(font=("Times", 20, "italic"))
        self.label2.pack(side='left',ipadx=30)

        self.email = Entry(self.frame2)
        self.email.pack(side='left', ipadx=45, ipady=5)

        self.frame3 = Frame(self.root, bg="#6A9113")
        self.frame3.pack(pady=(20, 5))
        self.label3 = Label(self.frame3, text="Password:", fg="black", bg="#6A9113")
        self.label3.configure(font=("Times", 20, "italic"))
        self.label3.pack(side='left',ipadx=10)

        self.password = Entry(self.frame3)
        self.password.pack(side='left', ipadx=45, ipady=5)

        self.register = Button(self.root, text="Sign Up", bg="grey", command=lambda: self.reg_submit())
        self.register.configure(font=("Times", 12, "bold"))
        self.register.pack(pady=(35, 10), ipadx=30, ipady=2)

        self.frame4 = Frame(self.root, bg="#6A9113")
        self.frame4.pack(pady=(70, 5))
        self.label4 = Label(self.frame4, text="After signing up Login here!", fg="white", bg="#6A9113")
        self.label4.configure(font=("Times", 15, "italic"))
        self.label4.pack(side='left',ipadx=10)

        self.login = Button(self.frame4, text="Login", bg="grey", command=lambda: self.load_gui())
        self.login.configure(font=("Times", 12, "bold"))
        self.login.pack(side='left', ipadx=20, ipady=4)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def btn_click(self):
        email=self.email.get()
        password=self.password.get()
        self.data=self.db.check_login(email,password)


        if len(self.data)>0:
            messagebox.showinfo("Successfully Logged in","You may proceed now")
            self.clear()
            self.proceed = Button(self.root, text="Click here to proceed", bg="grey", fg="white",command=lambda: self.cont_details())
            self.proceed.configure(font=("Times", 12, "bold"))
            self.proceed.pack(pady=(200, 10), ipadx=10, ipady=2)
            self.user_id=self.data[0][0]
        else:
            messagebox.showerror("Error","Incorrect email/Password")

        return self.data

    def reg_submit(self):
        login_name=self.name.get()
        login_email=self.email.get()
        password=self.password.get()

        if len(login_name)!=0 and len(login_email)!=0 and len(password)!=0:
            response = self.db.insert_user(login_name,login_email, password)
            messagebox.showinfo("Successfully Registered as a member", "You may login now")

        else:
            messagebox.showerror("Error", "Enter valid input!")


    def navbar(self ,mode=None):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)

        if mode==1:
            menu.add_cascade(label="Edit", menu=filemenu)
            filemenu.add_command(label="Contact Details",command=lambda :self.cont_details())
            filemenu.add_command(label="Education",command=lambda : self.education())
            filemenu.add_command(label="Career Objective",command=lambda :self.career_ob())
            filemenu.add_command(label="Skills",command=lambda: self.skills())
            filemenu.add_command(label="Projects", command=lambda: self.projects())
            filemenu.add_command(label="Others", command=lambda: self.others())
            filemenu.add_command(label="Personal Details", command=lambda: self.personal_details())
            filemenu.add_command(label="LogOut", command=lambda: self.logout())

        else:
            filemenu.destroy()

    def logout(self):
        self.navbar(mode=0)
        self.user_id = ''
        self.user_data = ''

        self.load_gui()

    def cont_details(self):
        self.clear()
        self.navbar(mode=1)

        self.label0 = Label(self.root, text="Contact Details", fg="white", bg="#6A9113")
        self.label0.configure(font=("Times", 15, "bold"))
        self.label0.pack(pady=(5, 5))

        self.frame1 = Frame(self.root, bg="#6A9113")
        self.frame1.pack(pady=(20, 5))
        self.label1 = Label(self.frame1, text="Your Full Name:", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 15, "italic"))
        self.label1.pack(side='left',ipadx=10)

        self.name = Entry(self.frame1)
        self.name.pack(side='left', ipadx=50, ipady=5)

        self.frame2 = Frame(self.root, bg="#6A9113")
        self.frame2.pack(pady=(20, 5))
        self.label2 = Label(self.frame2, text="A valid Email:", fg="black", bg="#6A9113")
        self.label2.configure(font=("Times", 15, "italic"))
        self.label2.pack(side='left',ipadx=20)

        self.email = Entry(self.frame2)
        self.email.pack(side='left', ipadx=50, ipady=5)

        self.frame3 = Frame(self.root, bg="#6A9113")
        self.frame3.pack(pady=(20, 5))
        self.label3 = Label(self.frame3, text="Contact No:", fg="black", bg="#6A9113")
        self.label3.configure(font=("Times", 15, "italic"))
        self.label3.pack(side='left',ipadx=28)

        self.contact_no = Entry(self.frame3)
        self.contact_no.pack(side='left', ipadx=50, ipady=5)

        self.frame4 = Frame(self.root, bg="#6A9113")
        self.frame4.pack(pady=(20, 5))
        self.label4 = Label(self.frame4, text="GitHub Profile:", fg="black", bg="#6A9113")
        self.label4.configure(font=("Times", 15, "italic"))
        self.label4.pack(side='left',ipadx=14)

        self.github = Entry(self.frame4)
        self.github.pack(side='left', ipadx=50, ipady=5)

        self.frame5 = Frame(self.root, bg="#6A9113")
        self.frame5.pack(pady=(20, 5))
        self.label5 = Label(self.frame5, text="LinkedIn Profile:", fg="black", bg="#6A9113")
        self.label5.configure(font=("Times", 15, "italic"))
        self.label5.pack(side='left',ipadx=8)

        self.linked = Entry(self.frame5)
        self.linked.pack(side='left', ipadx=50, ipady=5)

        frame = Frame(self.root)
        frame.pack(pady=(30, 5))

        clear = Button(frame, text="Clear",command=lambda:self.cont_details())
        clear.pack(side="left",ipadx=25, ipady=5)

        save = Button(frame, text="Save",command=lambda:self.app_cont_details())
        save.pack(side="left",ipadx=25, ipady=5)

        self.next = Button(self.root, text="Next", bg="grey", command=lambda: self.education())
        self.next.configure(font=("Times", 12, "bold"))
        self.next.pack(pady=(20, 10), ipadx=20, ipady=4)

    def app_cont_details(self):

        name=self.name.get()
        email=self.email.get()
        contact_no=self.contact_no.get()
        github= self.github.get()
        linked=self.linked.get()

        info=[name,email,contact_no,github,linked]

        response = self.db.contact(self.user_id,info)

        if response!=0:
            messagebox.showinfo("Great","Proceed to the next")
        else:
            messagebox.showerror("Error","Enter valid input!")


    def education(self):
        self.clear()

        self.label0 = Label(self.root, text="Educational Qualification", fg="white", bg="#6A9113")
        self.label0.configure(font=("Times", 15, "bold"))
        self.label0.pack(pady=(5, 5))

        self.frame1 = Frame(self.root, bg="#6A9113")
        self.frame1.pack(pady=(20, 5))
        self.label1 = Label(self.frame1, text="Course / Degree", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 15, "italic"))
        self.label1.pack(side='left',ipadx=23)

        self.courses = Entry(self.frame1)
        self.courses.pack(side='left', ipadx=50, ipady=5)

        self.frame2 = Frame(self.root, bg="#6A9113")
        self.frame2.pack(pady=(20, 5))
        self.label2 = Label(self.frame2, text="School / University", fg="black", bg="#6A9113")
        self.label2.configure(font=("Times", 15, "italic"))
        self.label2.pack(side='left',ipadx=12)

        self.institutes = Entry(self.frame2)
        self.institutes.pack(side='left', ipadx=50, ipady=5)

        self.frame3 = Frame(self.root, bg="#6A9113")
        self.frame3.pack(pady=(20, 5))
        self.label3 = Label(self.frame3, text="Grade / Percentage", fg="black", bg="#6A9113")
        self.label3.configure(font=("Times", 15, "italic"))
        self.label3.pack(side='left',ipadx=10)

        self.scores = Entry(self.frame3)
        self.scores.pack(side='left', ipadx=50, ipady=5)

        self.frame4 = Frame(self.root, bg="#6A9113")
        self.frame4.pack(pady=(20, 5))
        self.label4 = Label(self.frame4, text="Year of passing", fg="black", bg="#6A9113")
        self.label4.configure(font=("Times", 15, "italic"))
        self.label4.pack(side='left',ipadx=26)

        self.years = Entry(self.frame4)
        self.years.pack(side='left', ipadx=50, ipady=5)

        frame = Frame(self.root)
        frame.pack(pady=(25, 5))

        previous = Button(frame, text="Previous", command=lambda: self.cont_details())
        previous.pack(side="left", ipadx=5, ipady=5)

        clear = Button(frame, text="Clear",command=lambda:self.education())
        clear.pack(side="left",ipadx=10, ipady=5)

        save = Button(frame, text="Save",command=lambda:self.app_education())
        save.pack(side="left",ipadx=10, ipady=5)

        self.next = Button(self.root, text="Next", bg="grey", command=lambda: self.education2())
        self.next.configure(font=("Times", 12, "bold"))
        self.next.pack(pady=(15, 10), ipadx=20, ipady=4)

    def app_education(self):
        course=self.courses.get()
        institute=self.institutes.get()
        score=self.scores.get()
        year= self.years.get()

        info=[course,institute,score,year]

        response = self.db.educational(self.user_id,info)

        if response!=0:
            messagebox.showinfo("Great","Proceed to the next")
        else:
            messagebox.showerror("Error","Enter valid input!")

    def education2(self):
        self.clear()

        self.label0 = Label(self.root, text="Educational Qualification_2", fg="white", bg="#6A9113")
        self.label0.configure(font=("Times", 15, "bold"))
        self.label0.pack(pady=(5, 5))

        self.frame1 = Frame(self.root, bg="#6A9113")
        self.frame1.pack(pady=(20, 5))
        self.label1 = Label(self.frame1, text="Course / Degree", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 15, "italic"))
        self.label1.pack(side='left',ipadx=23)

        self.courses = Entry(self.frame1)
        self.courses.pack(side='left', ipadx=50, ipady=5)

        self.frame2 = Frame(self.root, bg="#6A9113")
        self.frame2.pack(pady=(20, 5))
        self.label2 = Label(self.frame2, text="School / University", fg="black", bg="#6A9113")
        self.label2.configure(font=("Times", 15, "italic"))
        self.label2.pack(side='left',ipadx=12)

        self.institutes = Entry(self.frame2)
        self.institutes.pack(side='left', ipadx=50, ipady=5)

        self.frame3 = Frame(self.root, bg="#6A9113")
        self.frame3.pack(pady=(20, 5))
        self.label3 = Label(self.frame3, text="Grade / Percentage", fg="black", bg="#6A9113")
        self.label3.configure(font=("Times", 15, "italic"))
        self.label3.pack(side='left',ipadx=10)

        self.scores = Entry(self.frame3)
        self.scores.pack(side='left', ipadx=50, ipady=5)

        self.frame4 = Frame(self.root, bg="#6A9113")
        self.frame4.pack(pady=(20, 5))
        self.label4 = Label(self.frame4, text="Year of passing", fg="black", bg="#6A9113")
        self.label4.configure(font=("Times", 15, "italic"))
        self.label4.pack(side='left',ipadx=26)

        self.years = Entry(self.frame4)
        self.years.pack(side='left', ipadx=50, ipady=5)

        frame = Frame(self.root)
        frame.pack(pady=(25, 5))

        previous = Button(frame, text="Previous", command=lambda: self.education())
        previous.pack(side="left", ipadx=5, ipady=5)

        clear = Button(frame, text="Clear",command=lambda:self.education2())
        clear.pack(side="left",ipadx=10, ipady=5)

        save = Button(frame, text="Save",command=lambda:self.app_education2())
        save.pack(side="left",ipadx=10, ipady=5)

        self.next = Button(self.root, text="Next", bg="grey", command=lambda: self.education3())
        self.next.configure(font=("Times", 12, "bold"))
        self.next.pack(pady=(15, 10), ipadx=20, ipady=4)

    def app_education2(self):
        course2=self.courses.get()
        institute2=self.institutes.get()
        score2=self.scores.get()
        year2= self.years.get()

        info=[course2,institute2,score2,year2]

        response = self.db.educational2(self.user_id,info)

        if response!=0:
            messagebox.showinfo("Great","Proceed to the next")
        else:
            messagebox.showerror("Error","Enter valid input!")

    def education3(self):
        self.clear()

        self.label0 = Label(self.root, text="Educational Qualification_3", fg="white", bg="#6A9113")
        self.label0.configure(font=("Times", 15, "bold"))
        self.label0.pack(pady=(5, 5))

        self.frame1 = Frame(self.root, bg="#6A9113")
        self.frame1.pack(pady=(20, 5))
        self.label1 = Label(self.frame1, text="Course / Degree", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 15, "italic"))
        self.label1.pack(side='left', ipadx=23)

        self.courses = Entry(self.frame1)
        self.courses.pack(side='left', ipadx=50, ipady=5)

        self.frame2 = Frame(self.root, bg="#6A9113")
        self.frame2.pack(pady=(20, 5))
        self.label2 = Label(self.frame2, text="School / University", fg="black", bg="#6A9113")
        self.label2.configure(font=("Times", 15, "italic"))
        self.label2.pack(side='left', ipadx=12)

        self.institutes = Entry(self.frame2)
        self.institutes.pack(side='left', ipadx=50, ipady=5)

        self.frame3 = Frame(self.root, bg="#6A9113")
        self.frame3.pack(pady=(20, 5))
        self.label3 = Label(self.frame3, text="Grade / Percentage", fg="black", bg="#6A9113")
        self.label3.configure(font=("Times", 15, "italic"))
        self.label3.pack(side='left', ipadx=10)

        self.scores = Entry(self.frame3)
        self.scores.pack(side='left', ipadx=50, ipady=5)

        self.frame4 = Frame(self.root, bg="#6A9113")
        self.frame4.pack(pady=(20, 5))
        self.label4 = Label(self.frame4, text="Year of passing", fg="black", bg="#6A9113")
        self.label4.configure(font=("Times", 15, "italic"))
        self.label4.pack(side='left', ipadx=26)

        self.years = Entry(self.frame4)
        self.years.pack(side='left', ipadx=50, ipady=5)

        frame = Frame(self.root)
        frame.pack(pady=(25, 5))

        previous = Button(frame, text="Previous", command=lambda: self.education2())
        previous.pack(side="left", ipadx=5, ipady=5)

        clear = Button(frame, text="Clear", command=lambda: self.education3())
        clear.pack(side="left", ipadx=10, ipady=5)

        save = Button(frame, text="Save", command=lambda: self.app_education3())
        save.pack(side="left", ipadx=10, ipady=5)

        self.next = Button(self.root, text="Next", bg="grey", command=lambda: self.career_ob())
        self.next.configure(font=("Times", 12, "bold"))
        self.next.pack(pady=(15, 10), ipadx=20, ipady=4)

    def app_education3(self):
        course3 = self.courses.get()
        institute3 = self.institutes.get()
        score3 = self.scores.get()
        year3 = self.years.get()

        info = [course3, institute3, score3, year3]

        response = self.db.educational3(self.user_id, info)

        if response != 0:
            messagebox.showinfo("Great", "Proceed to the next")
        else:
            messagebox.showerror("Error", "Enter valid input!")

    def career_ob(self):
        self.clear()

        self.label1 = Label(self.root, text="Career Objective", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 25, "italic"))
        self.label1.pack(pady=(50, 5))

        self.careers = Entry(self.root)
        self.careers.pack(pady=(20,10), ipadx=50, ipady=100)

        frame = Frame(self.root)
        frame.pack(pady=(50, 5))

        previous = Button(frame, text="Previous", command=lambda: self.education())
        previous.pack(side="left", ipadx=5, ipady=5)

        clear = Button(frame, text="Clear", command=lambda: self.career_ob())
        clear.pack(side="left", ipadx=10, ipady=5)

        save = Button(frame, text="Save", command=lambda: self.app_career())
        save.pack(side="left", ipadx=10, ipady=5)

        self.next = Button(self.root, text="Next", bg="grey", command=lambda: self.skills())
        self.next.configure(font=("Times", 12, "bold"))
        self.next.pack(pady=(15, 10), ipadx=20, ipady=4)

    def app_career(self):
        career=self.careers.get()

        response = self.db.career_ob(self.user_id,career)

        if response!=0:
            messagebox.showinfo("Great","Proceed to the next")
        else:
            messagebox.showerror("Error","Enter valid input!")

    def skills(self):
        self.clear()

        self.label1 = Label(self.root, text="Your Technical skills", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 20, "italic"))
        self.label1.pack(pady=(50, 5))

        self.skillss = Entry(self.root)
        self.skillss.pack(pady=(20,10), ipadx=50, ipady=100)

        frame = Frame(self.root)
        frame.pack(pady=(40, 5))

        previous = Button(frame, text="Previous", command=lambda: self.career_ob())
        previous.pack(side="left", ipadx=5, ipady=5)

        clear = Button(frame, text="Clear", command=lambda: self.skills())
        clear.pack(side="left", ipadx=10, ipady=5)

        save = Button(frame, text="Save", command=lambda: self.app_skills())
        save.pack(side="left", ipadx=10, ipady=5)

        self.next = Button(self.root, text="Next", bg="grey", command=lambda: self.projects())
        self.next.configure(font=("Times", 12, "bold"))
        self.next.pack(pady=(5, 10), ipadx=20, ipady=4)

    def app_skills(self):
        skills = self.skillss.get()

        response = self.db.abt_skills(self.user_id,skills)

        if response != 0:
            messagebox.showinfo("Great", "Proceed to the next")
        else:
            messagebox.showerror("Error", "Enter valid input!")

    def projects(self):
        self.clear()

        self.label1 = Label(self.root, text="Projects you have done", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 20, "italic"))
        self.label1.pack(pady=(50, 5))

        self.project = Entry(self.root)
        self.project.pack(pady=(20, 10), ipadx=50, ipady=100)

        frame = Frame(self.root)
        frame.pack(pady=(30, 5))

        previous = Button(frame, text="Previous", command=lambda: self.skills())
        previous.pack(side="left", ipadx=5, ipady=5)

        clear = Button(frame, text="Clear", command=lambda: self.projects())
        clear.pack(side="left", ipadx=10, ipady=5)

        save = Button(frame, text="Save", command=lambda: self.app_projects())
        save.pack(side="left", ipadx=10, ipady=5)

        self.next = Button(self.root, text="Next", bg="grey", command=lambda: self.others())
        self.next.configure(font=("Times", 12, "bold"))
        self.next.pack(pady=(5, 10), ipadx=20, ipady=4)

    def app_projects(self):
        projects = self.project.get()

        response = self.db.abt_projects(self.user_id, projects)

        if response != 0:
            messagebox.showinfo("Great", "Proceed to the next")
        else:
            messagebox.showerror("Error", "Enter valid input!")

    def others(self):
        self.clear()

        self.label1 = Label(self.root, text="Other Achievements", fg="white", bg="#6A9113")
        self.label1.configure(font=("Times", 20, "italic"))
        self.label1.pack(pady=(50, 5))

        self.label2 = Label(self.root, text="Not compulsury", fg="white", bg="#6A9113")
        self.label2.configure(font=("Times", 15, "italic"))
        self.label2.pack(pady=(10, 5))

        self.language = Button(self.root, text="Click to fillup languages", bg="grey", command=lambda: self.languages())
        self.language.configure(font=("Times", 12, "bold"))
        self.language.pack(pady=(15, 10), ipadx=20, ipady=4)

        self.award = Button(self.root, text="Click to filup Awards", bg="grey", command=lambda: self.awards())
        self.award.configure(font=("Times", 12, "bold"))
        self.award.pack(pady=(15, 10), ipadx=20, ipady=4)

        self.label3 = Label(self.root, text="Don't wanna fillup the above ?", fg="white", bg="#6A9113")
        self.label3.configure(font=("Times", 15, "italic"))
        self.label3.pack(pady=(50, 5))

        self.per_det = Button(self.root, text="Proceed to Next", bg="grey", command=lambda: self.personal_details())
        self.per_det.configure(font=("Times", 12, "bold"))
        self.per_det.pack(pady=(15, 10), ipadx=20, ipady=4)

    def languages(self):
        self.clear()

        self.label1 = Label(self.root, text="Languages you know", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 20, "italic"))
        self.label1.pack(pady=(50, 5))

        self.lng = Entry(self.root)
        self.lng.pack(pady=(20, 10), ipadx=50, ipady=100)

        frame = Frame(self.root)
        frame.pack(pady=(30, 5))

        previous = Button(frame, text="Previous", command=lambda: self.projects())
        previous.pack(side="left", ipadx=5, ipady=5)

        clear = Button(frame, text="Clear", command=lambda: self.languages())
        clear.pack(side="left", ipadx=10, ipady=5)

        save = Button(frame, text="Save", command=lambda: self.app_languages())
        save.pack(side="left", ipadx=10, ipady=5)

        self.next = Button(self.root, text="Next", bg="grey", command=lambda: self.awards())
        self.next.configure(font=("Times", 12, "bold"))
        self.next.pack(pady=(5, 10), ipadx=20, ipady=4)

    def app_languages(self):
        language = self.lng.get()

        response = self.db.abt_languages(self.user_id, language)

        if response != 0:
            messagebox.showinfo("Great", "Proceed to the next")
        else:
            messagebox.showerror("Error", "Enter valid input!")

    def awards(self):
        self.clear()

        self.label1 = Label(self.root, text="Achievements and Awards", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 20, "italic"))
        self.label1.pack(pady=(50, 5))

        self.awd = Entry(self.root)
        self.awd.pack(pady=(20, 10), ipadx=50, ipady=100)

        frame = Frame(self.root)
        frame.pack(pady=(30, 5))

        previous = Button(frame, text="Previous", command=lambda: self.languages())
        previous.pack(side="left", ipadx=5, ipady=5)

        clear = Button(frame, text="Clear", command=lambda: self.awards())
        clear.pack(side="left", ipadx=10, ipady=5)

        save = Button(frame, text="Save", command=lambda: self.app_awards())
        save.pack(side="left", ipadx=10, ipady=5)

        self.next = Button(self.root, text="Next", bg="grey", command=lambda: self.personal_details())
        self.next.configure(font=("Times", 12, "bold"))
        self.next.pack(pady=(5, 10), ipadx=20, ipady=4)

    def app_awards(self):
        awards = self.awd.get()

        response = self.db.abt_awards(self.user_id, awards)

        if response != 0:
            messagebox.showinfo("Great", "Proceed to the next")
        else:
            messagebox.showerror("Error", "Enter valid input!")

    def personal_details(self):
        self.clear()

        self.label0 = Label(self.root, text="Personal Details", fg="white", bg="#6A9113")
        self.label0.configure(font=("Times", 15, "bold"))
        self.label0.pack(pady=(5, 5))

        self.frame1 = Frame(self.root, bg="#6A9113")
        self.frame1.pack(pady=(20, 5))
        self.label1 = Label(self.frame1, text="Father's Name", fg="black", bg="#6A9113")
        self.label1.configure(font=("Times", 15, "italic"))
        self.label1.pack(side='left',ipadx=30)

        self.fname = Entry(self.frame1)
        self.fname.pack(side='left', ipadx=50, ipady=5)

        self.frame2 = Frame(self.root, bg="#6A9113")
        self.frame2.pack(pady=(20, 5))
        self.label2 = Label(self.frame2, text="Mother's Name", fg="black", bg="#6A9113")
        self.label2.configure(font=("Times", 15, "italic"))
        self.label2.pack(side='left',ipadx=28)

        self.mname = Entry(self.frame2)
        self.mname.pack(side='left', ipadx=50, ipady=5)

        self.frame3 = Frame(self.root, bg="#6A9113")
        self.frame3.pack(pady=(20, 5))
        self.label3 = Label(self.frame3, text="Address", fg="black", bg="#6A9113")
        self.label3.configure(font=("Times", 15, "italic"))
        self.label3.pack(side='left',ipadx=58)

        self.add = Entry(self.frame3)
        self.add.pack(side='left', ipadx=50, ipady=5)

        self.frame4 = Frame(self.root, bg="#6A9113")
        self.frame4.pack(pady=(20, 5))
        self.label4 = Label(self.frame4, text="DOB (yyyy-mm-dd)", fg="black", bg="#6A9113")
        self.label4.configure(font=("Times", 15, "italic"))
        self.label4.pack(side='left',ipadx=10)

        self.dtob = Entry(self.frame4)
        self.dtob.pack(side='left', ipadx=50, ipady=5)

        self.frame5 = Frame(self.root, bg="#6A9113")
        self.frame5.pack(pady=(20, 5))
        self.label5 = Label(self.frame5, text="Hobbies", fg="black", bg="#6A9113")
        self.label5.configure(font=("Times", 15, "italic"))
        self.label5.pack(side='left',ipadx=53)

        self.hobbyy = Entry(self.frame5)
        self.hobbyy.pack(side='left', ipadx=50, ipady=5)

        frame = Frame(self.root)
        frame.pack(pady=(15, 5))

        previous = Button(frame, text="Previous", command=lambda: self.awards())
        previous.pack(side="left", ipadx=5, ipady=5)

        clear = Button(frame, text="Clear", command=lambda: self.personal_details())
        clear.pack(side="left", ipadx=10, ipady=5)

        save = Button(frame, text="Save", command=lambda: self.app_personal_details())
        save.pack(side="left", ipadx=10, ipady=5)

        self.display_chk=1

        self.dsplay = Button(self.root, text="Click here to see your resume", bg="grey", command=lambda: self.display(self.db.data_fetch(self.data[0][0]),mode=self.display_chk))
        self.dsplay.configure(font=("Times", 12, "bold"))
        self.dsplay.pack(pady=(15, 10), ipadx=20, ipady=4)



    def app_personal_details(self):

        father = self.fname.get()
        mother = self.mname.get()
        address = self.add.get()
        dob = self.dtob.get()
        hobby=self.hobbyy.get()
        info = [father,mother,address,dob,hobby]

        response = self.db.abt_per_det(self.user_id, info)

        if response != 0:
            messagebox.showinfo("Great", "Proceed to the next")
        else:
            messagebox.showerror("Error", "Enter valid input!")


    def display(self,data,mode=None):

        if mode==1:

            self.root2 = Tk()

            self.root2.title("Resume App")

            self.root2.configure(background="white")

            self.root2.minsize(550,700)

            self.frame1 = Frame(self.root2, bg="white")
            self.frame1.place(x=20,y=20)

            self.label1 = Label(self.frame1, text="Name: " + data[4], fg="black", bg="white")
            self.label1.configure(font=("Times", 10, "bold"))
            self.label1.pack()

            self.frame20 = Frame(self.root2, bg="white")
            self.frame20.place(x=20, y=40)

            self.label2 = Label(self.frame20, text="Email: "+ data[5], fg="black", bg="white")
            self.label2.configure(font=("Times", 10, "bold"))
            self.label2.pack()

            self.frame21 = Frame(self.root2, bg="white")
            self.frame21.place(x=20, y=60)

            self.label3 = Label(self.frame21, text="Contact No: "+str(data[6]), fg="black", bg="white")
            self.label3.configure(font=("Times", 10, "bold"))
            self.label3.pack()

            self.frame22 = Frame(self.root2, bg="white")
            self.frame22.place(x=20, y=80)

            self.label4 = Label(self.frame22, text="GitHub Profile: "+data[7], fg="black", bg="white")
            self.label4.configure(font=("Times", 10, "bold"))
            self.label4.pack()

            self.frame23 = Frame(self.root2, bg="white")
            self.frame23.place(x=20, y=100)

            self.label5 = Label(self.frame23, text="LinkedIn Profile: "+data[8], fg="black", bg="white")
            self.label5.configure(font=("Times", 10, "bold"))
            self.label5.pack()

            self.frame2=Frame(self.root2,bg='white')
            self.frame2.place(x=20,y=130)

            self.label6 = Label(self.frame2, text="Career Objective: ", fg="red", bg="white")
            self.label6.configure(font=("Times", 10, "bold"))
            self.label6.pack()

            self.frame=Frame(self.root2,bg='white')
            self.frame.place(x=20,y=150)

            self.label7 = Label(self.frame, text=data[21], fg="black", bg="white")
            self.label7.configure(font=("Times", 10, "bold"))
            self.label7.pack()

            self.frame3 = Frame(self.root2,bg='white')
            self.frame3.place(x=20,y=180)

            self.label8 = Label(self.frame3, text="Educational Qualification", fg="red", bg="white")
            self.label8.configure(font=("Times", 10, "bold"))
            self.label8.pack()

            self.frame4=Frame(self.root2)
            self.frame4.place(x=20,y=210)

            self.label9=Label(self.frame4,text="Course",bg='red',fg='white',padx=30,pady=5)
            self.label9.configure(font=("Times", 10, "bold"))
            self.label9.grid(row=2,column=0,padx=1,pady=1,sticky='nsew')
            self.label10 = Label(self.frame4, text="Institute", bg='red', fg='white', padx=30, pady=5)
            self.label10.configure(font=("Times", 10, "bold"))
            self.label10.grid(row=2, column=1, padx=1,pady=1,sticky='nsew')
            self.label11 = Label(self.frame4, text="Score", bg='red', fg='white', padx=30, pady=5)
            self.label11.configure(font=("Times", 10, "bold"))
            self.label11.grid(row=2, column=2, padx=1,pady=1,sticky='nsew')
            self.label12 = Label(self.frame4, text="Year", bg='red', fg='white', padx=30, pady=5)
            self.label12.configure(font=("Times", 10, "bold"))
            self.label12.grid(row=2, column=3, padx=1,pady=1,sticky='nsew')

            self.frame4.grid_columnconfigure(0,weight=1)
            self.frame4.grid_columnconfigure(1, weight=1)
            self.frame4.grid_columnconfigure(2, weight=1)
            self.frame4.grid_columnconfigure(3, weight=1)

            self.frame5 = Frame(self.root2)
            self.frame5.place(x=20,y=240)

            self.label13 = Label(self.frame5, text=data[9], bg='white', fg='black', padx=30, pady=5)
            self.label13.configure(font=("Times", 10, "bold"))
            self.label13.grid(row=3, column=0, padx=1, pady=1, sticky='nsew')
            self.label14 = Label(self.frame5, text=data[10], bg='white', fg='black', padx=30, pady=5)
            self.label14.configure(font=("Times", 10, "bold"))
            self.label14.grid(row=3, column=1, padx=1, pady=1, sticky='nsew')
            self.label15 = Label(self.frame5, text=data[11], bg='white', fg='black', padx=30, pady=5)
            self.label15.configure(font=("Times", 10, "bold"))
            self.label15.grid(row=3, column=2, padx=1, pady=1, sticky='nsew')
            self.label16 = Label(self.frame5, text=data[12],bg='white', fg='black', padx=30, pady=5)
            self.label16.configure(font=("Times", 10, "bold"))
            self.label16.grid(row=3, column=3, padx=1, pady=1, sticky='nsew')

            self.frame5.grid_columnconfigure(0, weight=1)
            self.frame5.grid_columnconfigure(1, weight=1)
            self.frame5.grid_columnconfigure(2, weight=1)
            self.frame5.grid_columnconfigure(3, weight=1)

            self.frame6 = Frame(self.root2)
            self.frame6.place(x=20, y=270)

            self.label17 = Label(self.frame6, text=data[13],bg='white', fg='black', padx=30, pady=5)
            self.label17.configure(font=("Times", 10, "bold"))
            self.label17.grid(row=4, column=0, padx=1, pady=1, sticky='nsew')
            self.label18 = Label(self.frame6, text=data[14], bg='white', fg='black', padx=30, pady=5)
            self.label18.configure(font=("Times", 10, "bold"))
            self.label18.grid(row=4, column=1, padx=1, pady=1, sticky='nsew')
            self.label19 = Label(self.frame6, text=data[15],bg='white', fg='black', padx=30, pady=5)
            self.label19.configure(font=("Times", 10, "bold"))
            self.label19.grid(row=4, column=2, padx=1, pady=1, sticky='nsew')
            self.label20 = Label(self.frame6, text=data[16], bg='white', fg='black', padx=30, pady=5)
            self.label20.configure(font=("Times", 10, "bold"))
            self.label20.grid(row=4, column=3, padx=1, pady=1, sticky='nsew')

            self.frame6.grid_columnconfigure(0, weight=1)
            self.frame6.grid_columnconfigure(1, weight=1)
            self.frame6.grid_columnconfigure(2, weight=1)
            self.frame6.grid_columnconfigure(3, weight=1)

            self.frame7 = Frame(self.root2)
            self.frame7.place(x=20, y=300)

            self.label21 = Label(self.frame7, text=data[17],bg='white', fg='black', padx=30, pady=5)
            self.label21.configure(font=("Times", 10, "bold"))
            self.label21.grid(row=5, column=0, padx=1, pady=1, sticky='nsew')
            self.label22 = Label(self.frame7, text=data[18],bg='white', fg='black', padx=30, pady=5)
            self.label22.configure(font=("Times", 10, "bold"))
            self.label22.grid(row=5, column=1, padx=1, pady=1, sticky='nsew')
            self.label23 = Label(self.frame7, text=data[19],bg='white', fg='black', padx=30, pady=5)
            self.label23.configure(font=("Times", 10, "bold"))
            self.label23.grid(row=5, column=2, padx=1, pady=1, sticky='nsew')
            self.label24 = Label(self.frame7, text=data[20],bg='white', fg='black', padx=30, pady=5)
            self.label24.configure(font=("Times", 10, "bold"))
            self.label24.grid(row=5, column=3, padx=1, pady=1, sticky='nsew')

            self.frame7.grid_columnconfigure(0, weight=1)
            self.frame7.grid_columnconfigure(1, weight=1)
            self.frame7.grid_columnconfigure(2, weight=1)
            self.frame7.grid_columnconfigure(3, weight=1)

            self.frame8 = Frame(self.root2, bg='white')
            self.frame8.place(x=20, y=340)

            self.label25 = Label(self.frame8, text="Technical Skills", fg="red", bg="white")
            self.label25.configure(font=("Times", 10, "bold"))
            self.label25.pack()

            self.frame9 = Frame(self.root2, bg='white')
            self.frame9.place(x=20, y=360)

            self.label26 = Label(self.frame9, text=data[22], fg="black", bg="white")
            self.label26.configure(font=("Times", 10, "bold"))
            self.label26.pack()

            self.frame9 = Frame(self.root2, bg='white')
            self.frame9.place(x=20, y=390)

            self.label27 = Label(self.frame9, text="Projects", fg="red", bg="white")
            self.label27.configure(font=("Times", 10, "bold"))
            self.label27.pack()

            self.frame10 = Frame(self.root2, bg='white')
            self.frame10.place(x=20, y=410)

            self.label28 = Label(self.frame10, text=data[23], fg="black", bg="white")
            self.label28.configure(font=("Times", 10, "bold"))
            self.label28.pack()

            self.frame10 = Frame(self.root2, bg='white')
            self.frame10.place(x=20, y=440)

            self.label29 = Label(self.frame10, text="Languages", fg="red", bg="white")
            self.label29.configure(font=("Times", 10, "bold"))
            self.label29.pack()

            self.frame11 = Frame(self.root2, bg='white')
            self.frame11.place(x=20, y=460)

            self.label30 = Label(self.frame11, text=data[24], fg="black", bg="white")
            self.label30.configure(font=("Times", 10, "bold"))
            self.label30.pack()


            self.frame12 = Frame(self.root2, bg='white')
            self.frame12.place(x=20, y=490)

            self.label31 = Label(self.frame12, text="Achievements", fg="red", bg="white")
            self.label31.configure(font=("Times", 10, "bold"))
            self.label31.pack()

            self.frame13 = Frame(self.root2, bg='white')
            self.frame13.place(x=20, y=510)

            self.label32 = Label(self.frame13, text=data[25], fg="black", bg="white")
            self.label32.configure(font=("Times", 10, "bold"))
            self.label32.pack()

            self.frame14 = Frame(self.root2, bg='white')
            self.frame14.place(x=20, y=540)

            self.label33 = Label(self.frame14, text="Personal Details", fg="red", bg="white")
            self.label33.configure(font=("Times", 10, "bold"))
            self.label33.pack()

            self.frame15 = Frame(self.root2, bg='white')
            self.frame15.place(x=20, y=560)

            self.label34 = Label(self.frame15, text="Father's Name : "+data[26], fg="black", bg="white")
            self.label34.configure(font=("Times", 10, "bold"))
            self.label34.pack()

            self.frame16 = Frame(self.root2, bg='white')
            self.frame16.place(x=20, y=580)

            self.label35 = Label(self.frame16, text="Mother's Name : "+data[27], fg="black", bg="white")
            self.label35.configure(font=("Times", 10, "bold"))
            self.label35.pack()

            self.frame17 = Frame(self.root2, bg='white')
            self.frame17.place(x=20, y=600)

            self.label36 = Label(self.frame17, text="Address : "+data[28], fg="black", bg="white")
            self.label36.configure(font=("Times", 10, "bold"))
            self.label36.pack()

            self.frame18 = Frame(self.root2, bg='white')
            self.frame18.place(x=20, y=620)

            self.label37 = Label(self.frame18, text="Date of Birth : "+ str(data[29]), fg="black", bg="white")
            self.label37.configure(font=("Times", 10, "bold"))
            self.label37.pack()

            self.frame19 = Frame(self.root2, bg='white')
            self.frame19.place(x=20, y=640)

            self.label38 = Label(self.frame19, text="Hobbies : " + data[30], fg="black", bg="white")
            self.label38.configure(font=("Times", 10, "bold"))
            self.label38.pack()

            self.display_chk+=1

        else:
            messagebox.showerror("Oops!!", "It's already displayed!")



obj=Login()





