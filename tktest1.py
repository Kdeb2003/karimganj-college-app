import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.properties import StringProperty

Window.size = (320, 580)

class MainApp(MDApp):
    otp = ""
    otp_timer = None
    time_left = StringProperty("02:00")

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Builder.load_file("forgetpassword.kv"))
        self.sm.add_widget(Builder.load_file("update password.kv"))
        return self.sm

    def send_otp(self, email):
        self.otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.send_email(email, self.otp)
        #self.show_popup("OTP sent", f"An OTP has\nbeen sent to {email}")
        self.show_otp_dialog()

    def send_email(self, to_email, otp):
        from_email = "test123deb@gmail.com"
        from_password = "vntyvnwxunxzsobx"

        subject = "Your OTP Code"
        body = f"Your OTP code is {otp}"

        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, message.as_string())
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(300, 200))
        popup.open()

    def show_otp_dialog(self):
        self.otp_field = MDTextField(
            hint_text="Enter OTP",
            size_hint=(0.8, None),
            height="40dp"
        )
        self.timer_label = Label(
            text=self.time_left,
            size_hint=(0.8, None),
            height="40dp",
            halign="center"
        )
        content = self.otp_field
        self.otp_dialog = MDDialog(
            title="OTP Verification",
            type="custom",
            content_cls=self.otp_field,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=self.close_otp_dialog
                ),
                MDRaisedButton(
                    text="VERIFY",
                    on_release=self.verify_otp
                ),
            ],
        )
        self.otp_dialog.content_cls.add_widget(self.timer_label)
        self.otp_dialog.open()
        self.start_otp_timer()

    def start_otp_timer(self):
        self.time_left = "02:00"
        self.otp_timer = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        minutes, seconds = map(int, self.time_left.split(":"))
        seconds -= 1
        if seconds < 0:
            seconds = 59
            minutes -= 1

        self.time_left = f"{minutes:02}:{seconds:02}"
        self.timer_label.text = self.time_left

        if self.time_left == "02:00":
            self.otp_timeout(0)

    def otp_timeout(self, dt):
        self.close_otp_dialog()
        self.show_popup("Error", "OTP expired. Please try again.")

    def close_otp_dialog(self, *args):
        if self.otp_timer:
            self.otp_timer.cancel()
        self.otp_dialog.dismiss()

    def verify_otp(self, *args):
        entered_otp = self.otp_field.text
        if entered_otp == self.otp:
            self.close_otp_dialog()
            self.sm.current = "updatepassword"
        else:
            self.show_popup("Error", "Invalid OTP. Please try again.")

if __name__ == '__main__':
    MainApp().run()
