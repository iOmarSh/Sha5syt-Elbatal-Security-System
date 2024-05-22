import subprocess
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Frame, Label
from PIL import Image, ImageTk
import sys
from tkinter import messagebox
import cv2

LoginFilePath = "C:\\Python Project\\S.elbatal-Encryptor\\test.txt"


class VideoPlayer(tk.Label):
    def __init__(self, parent, video_source, **kwargs):
        super().__init__(parent, **kwargs)
        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)
        self.update()

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            # Resize frame if necessary
            # frame = cv2.resize(frame, (desired_width, desired_height))

            # Convert color space from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the Image object into a TkPhoto object
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))

            # Update the image displayed
            self.config(image=self.photo)

        # Refresh the frame after 20 milliseconds
        self.after(2,self.update)

    def center_window(self, window, width, height):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position of the window
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        # Set the position of the window
        window.geometry(f"{width}x{height}+{x}+{y}")

    @staticmethod
    def skip_intro(event):
        frame1.pack_forget()
        window.overrideredirect(False)
        window.unbind("<Return>")
        log.open_login_page()
        flag = True


# def redirect():
#     new_window = tk.Tk()
#     new_window.title("New Window")
#     center_window(new_window, window_width, window_height)
#     # Add content to the new window
#     label = tk.Label(new_window, text="Redirected to new window!")
#     label.pack()
#     new_window.mainloop()

def IsUserFound(usernames, passwords, user_username, user_password):
    for i in range(len(usernames)):
        if user_username == usernames[i] and user_password == passwords[i]:
            return True
    return False


def FetchUsersandPasswords(text, usernames, passwords="none"):
    if passwords != "none":
        for i in range(0, len(text), 2):
            usernames.append(text[i][10:-1])
            passwords.append(text[i + 1][10:-1])
    else:
        for i in range(0, len(text), 2):
            usernames.append(text[i][10:-1])


def Login():
    file = open(LoginFilePath, "r+")
    text = file.readlines()
    if len(text) == 0:
        print("The file is empty no users registered yet")
    else:
        usernames = []
        passwords = []
        user_username = log.username_entry.get()
        user_password = log.password_entry.get()
        if user_username == "" or user_password == "":
            messagebox.showerror("Error", "Please Set All Feilds")
            return

        FetchUsersandPasswords(text, usernames, passwords)
        UserFound = IsUserFound(usernames, passwords, user_username, user_password)

    file.close()
    if not UserFound:
        log.username_entry.delete(0, tk.END)
        log.password_entry.delete(0, tk.END)
        messagebox.showerror("Error", "Wrong Username or Password")
    else:
        messagebox.showinfo("Success", "Login Done Successfully")
        window.destroy()
        subprocess.Popen(["python", "C:\\Python Project\\S.elbatal-Encryptor\\project.py"])

    return UserFound


def Register():
    file = open(LoginFilePath, "a+")
    username = log.reg_username_entry.get()
    if " " in username:
        messagebox.showerror("Error", "The UserName mustn't Contain Spaces")
        return

    Check_file = open(LoginFilePath, "r+")
    UsersOfFile = Check_file.readlines()
    usernames = []
    FetchUsersandPasswords(UsersOfFile, usernames)
    for i in usernames:
        if i == username:
            messagebox.showerror("Error", "User Already Exist")
            log.reg_username_entry.delete(0, tk.END)
            log.reg_password_entry.delete(0, tk.END)
            log.reg_confirm_password_entry.delete(0, tk.END)
            return
    password = log.reg_password_entry.get()
    ConfirmPassword = log.reg_confirm_password_entry.get()
    if password != ConfirmPassword:
        messagebox.showerror("Error", "Password MissMatch")
        return
    if username == "" or password == "" or ConfirmPassword == "":
        messagebox.showerror("Error", "Please Set All Feilds")
        return

    temp = f'{file.read()}username: {username}\npassword: {password}\n'
    file.write(temp)
    file.close()
    Check_file.close()
    messagebox.showinfo("Register Page", "Register Done Successfully")
    log.reg_username_entry.delete(0, tk.END)
    log.reg_password_entry.delete(0, tk.END)
    log.reg_confirm_password_entry.delete(0, tk.END)


class OpenPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('950x600')
        self.window.title('Opening Page')
        self.window.resizable(False, False)
        self.lgn_frame = Frame(self.window, bg='#000000', width=950, height=600)
        self.lgn_frame.place(x=0, y=0)
        self.show_login_page()

    def show_login_page(self):
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#000000', width=950, height=600)
        self.lgn_frame.place(x=0, y=0)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=410, y=40)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                   font=("Butcherman", 20, "bold"))
        self.sign_in_label.place(x=425, y=160)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=330, y=250)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=360, y=285, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=330, y=309)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\userIcon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=330, y=282)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=330, y=340)  # Decreased y from 380 to 340

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=360, y=376, width=244)  # Decreased y from 416 to 376

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=330, y=400)  # Decreased y from 440 to 400

        # Password icon
        self.password_icon = Image.open('images\\lockIcon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=330, y=374)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=330, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=Login)
        self.login.place(x=20, y=10)

        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=330, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405",
                                          command=self.show_register_page)
        self.signup_button_label.place(x=450, y=555, width=111, height=35)

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\viewIcon.jpg')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hideIcon.jpg')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")
        self.show_button.place(x=640, y=380)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")
        self.hide_button.place(x=640, y=380)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")
        self.show_button.place(x=640, y=380)
        self.password_entry.config(show='*')

    def show_register_page(self):
        # Clear previous content
        self.clear_frame()

        # Create registration page elements
        self.reg_frame = Frame(self.window, bg='#000000', width=950, height=600)
        self.reg_frame.place(x=0, y=0)

        # Sign Up Image
        self.reg_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.reg_image)
        self.reg_image_label = Label(self.reg_frame, image=photo, bg='#040405')
        self.reg_image_label.image = photo
        self.reg_image_label.place(x=410, y=40)

        # Sign Up Label
        self.reg_label = Label(self.reg_frame, text="Sign Up", bg="#040405", fg="white",
                               font=("Butcherman", 20, "bold"))
        self.reg_label.place(x=425, y=160)

        # Username Label and Entry
        self.reg_username_label = Label(self.reg_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.reg_username_label.place(x=330, y=220)

        self.reg_username_entry = Entry(self.reg_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                        font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.reg_username_entry.place(x=360, y=255, width=270)

        self.reg_username_line = Canvas(self.reg_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.reg_username_line.place(x=330, y=279)

        # Username Icon
        self.reg_username_icon = Image.open('images\\userIcon.png')
        photo = ImageTk.PhotoImage(self.reg_username_icon)
        self.reg_username_icon_label = Label(self.reg_frame, image=photo, bg='#040405')
        self.reg_username_icon_label.image = photo
        self.reg_username_icon_label.place(x=330, y=252)

        # Password Label and Entry
        self.reg_password_label = Label(self.reg_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.reg_password_label.place(x=330, y=300)

        self.reg_password_entry = Entry(self.reg_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                        font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.reg_password_entry.place(x=360, y=336, width=244)

        self.reg_password_line = Canvas(self.reg_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.reg_password_line.place(x=330, y=360)

        # Password Icon
        self.reg_password_icon = Image.open('images\\lockIcon.png')
        photo = ImageTk.PhotoImage(self.reg_password_icon)
        self.reg_password_icon_label = Label(self.reg_frame, image=photo, bg='#040405')
        self.reg_password_icon_label.image = photo
        self.reg_password_icon_label.place(x=330, y=334)

        # Confirm Password Label and Entry
        self.reg_confirm_password_label = Label(self.reg_frame, text="Confirm Password", bg="#040405", fg="#4f4e4d",
                                                font=("yu gothic ui", 13, "bold"))
        self.reg_confirm_password_label.place(x=330, y=380)

        self.reg_confirm_password_entry = Entry(self.reg_frame, highlightthickness=0, relief=FLAT, bg="#040405",
                                                fg="#6b6a69", font=("yu gothic ui", 12, "bold"), show="*",
                                                insertbackground='#6b6a69')
        self.reg_confirm_password_entry.place(x=360, y=416, width=244)

        self.reg_confirm_password_line = Canvas(self.reg_frame, width=300, height=2.0, bg="#bdb9b1",
                                                highlightthickness=0)
        self.reg_confirm_password_line.place(x=330, y=440)

        # Confirm Password Icon
        self.reg_confirm_password_icon = Image.open('images\\lockIcon.png')
        photo = ImageTk.PhotoImage(self.reg_confirm_password_icon)
        self.reg_confirm_password_icon_label = Label(self.reg_frame, image=photo, bg='#040405')
        self.reg_confirm_password_icon_label.image = photo
        self.reg_confirm_password_icon_label.place(x=330, y=414)

        # Register Button
        self.reg_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.reg_button)
        self.reg_button_label = Label(self.reg_frame, image=photo, bg='#040405')
        self.reg_button_label.image = photo
        self.reg_button_label.place(x=330, y=450)
        self.register = Button(self.reg_button_label, text='Register', font=("yu gothic ui", 13, "bold"), width=25,
                               bd=0, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                               command=Register)
        self.register.place(x=20, y=10)

        # Back to Login Page Button
        self.back_label = Label(self.reg_frame, text='Login?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.back_label.place(x=330, y=560)

        self.back_button_img = ImageTk.PhotoImage(file='images\\btn2.png')
        self.back_button_label = Button(self.reg_frame, image=self.back_button_img, bg='#98a65d', cursor="hand2",
                                        borderwidth=0, background="#040405", activebackground="#040405",
                                        command=self.open_login_page)
        self.back_button_label.place(x=450, y=555, width=111, height=35)

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\viewIcon.jpg')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hideIcon.jpg')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")
        self.hide_button.place(x=640, y=380)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="black"
                                  , borderwidth=0, background="black", cursor="hand2")
        self.show_button.place(x=640, y=380)
        self.password_entry.config(show='*')

    def clear_frame(self):
        # Destroy all widgets in the frame
        for widget in self.lgn_frame.winfo_children():
            widget.destroy()

    def open_register_page(self):
        self.clear_frame()
        self.show_register_page()

    def open_login_page(self):
        self.clear_frame()
        self.show_login_page()

vidflag = False
def switch():
    frame1.pack_forget()
    window.overrideredirect(False)
    window.unbind("<Return>")
    if vidflag:
        log = OpenPage(window)


if __name__ == '__main__':
    window = Tk()
    global log
    log = OpenPage(window)
    frame1 = customtkinter.CTkFrame(master=window)
    video_player = VideoPlayer(frame1, video_source="Opening.mp4")
    video_player.pack()
    video_player.center_window(window,950,600)
    frame1.pack()
    window.overrideredirect(True)
    delay_time = 4850
    frame2 = customtkinter.CTkFrame(master=window)
    window.protocol("WM_DELETE_WINDOW", window.destroy)
    window.bind("<Return>", video_player.skip_intro)
    window.after(delay_time, switch)
    window.mainloop()
