import tkinter as tk
from tkinter import messagebox

class ITASApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ITAS - IT Assistance for Seniors")

        # Create and configure widgets
        self.label = tk.Label(root, text="IT Assistance for Seniors")
        self.label.pack(pady=10)

        self.register_button = tk.Button(root, text="Register User", command=self.show_registration_form)
        self.register_button.pack()

        self.login_button = tk.Button(root, text="Login", command=self.show_login_form)
        self.login_button.pack()

        self.help_button = tk.Button(root, text="Help", command=self.show_help)
        self.help_button.pack()

    def show_registration_form(self):
        registration_root = tk.Toplevel(self.root)
        RegistrationForm(registration_root)

    def show_login_form(self):
        login_root = tk.Toplevel(self.root)
        LoginForm(login_root)

    def show_help(self):
        help_text = "Welcome to IT Assistance for Seniors!\n\n" \
                    "This program is designed to provide personalized IT assistance for seniors.\n\n" \
                    "For assistance or to register, please contact:\n" \
                    "Phone: 87075253180\n" \
                    "Email: support@itas.com\n\n" \
                    "Instructions:\n" \
                    "1. Register by clicking 'Register User'.\n" \
                    "2. Log in using your username and password.\n" \
                    "3. Explore the features and get IT assistance tailored for seniors.\n"

        messagebox.showinfo("Help", help_text)

class RegistrationForm:
    def __init__(self, root):
        self.root = root

        self.label = tk.Label(root, text="User Registration")
        self.label.pack(pady=10)

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(root, text="Register", command=self.register_user)
        self.register_button.pack()

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            # Perform registration logic here (you can add your logic or call a function)
            messagebox.showinfo("Registration Result", "Registration successful.")
            self.root.destroy()

class LoginForm:
    def __init__(self, root):
        self.root = root

        self.label = tk.Label(root, text="User Login")
        self.label.pack(pady=10)

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.authenticate_user)
        self.login_button.pack()

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            # Perform authentication logic here (you can add your logic or call a function)
            messagebox.showinfo("Login Result", "Login successful.")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ITASApp(root)
    root.mainloop()
