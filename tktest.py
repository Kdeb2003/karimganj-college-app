import smtplib
import random
from email.message import EmailMessage
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.properties import StringProperty

Window.size = (320, 580)


class MainApp(MDApp):
    global sm
    sm = ScreenManager()

    def build(self):
        self.timer = 300
        sm.add_widget(Builder.load_file("forgetpassword.kv"))
        sm.add_widget(Builder.load_file("update password.kv"))
        return sm

    def send_email(self, email, password, recipient, subject, message):
        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = subject
        msg["From"] = email
        msg["To"] = recipient

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
        server.quit()

    def send_otp1(self, *args):
        det = sm.get_screen('forgetpassword')
        recipient = det.ids.email_id.text

        self.email = "test123deb@gmail.com"  # Predefined sender email
        self.password = "vntyvnwxunxzsobx"  # Predefined sender password

        self.otp = str(random.randint(100000, 999999))

        self.send_email(
            self.email,
            self.password,
            recipient,
            "OTP Verification",
            f"Your OTP is: {self.otp}",
        )

        self.show_otp_dialog1()

    def show_otp_dialog1(self):
        self.dialog1 = MDDialog(
            title="Verify OTP",
            type="custom",
            content_cls=BoxLayout(
                orientation="vertical",
                spacing="10dp",
                size_hint=(None, None),
                width="280dp",
                height="240dp"
            ),
            buttons=[
                MDRectangleFlatButton(text="Cancel", on_release=self.close_dialog2),
                MDRectangleFlatButton(text="Verify", on_release=self.verify_otp1),
            ],
        )

        content = self.dialog1.content_cls

        # OTP verification label
        label = MDLabel(
            text="OTP Verification",
            pos_hint={"center_x": 0.668}
        )
        content.add_widget(label)

        # Text field for OTP input
        self.otp_text1 = MDTextField(
            hint_text="Enter OTP",
            size_hint=(None, None),
            size=(200, 48),
            mode="rectangle"
        )
        content.add_widget(self.otp_text1)

        # Timer countdown label
        self.timer_label1 = MDLabel(
            text=f"Time Left: {self.timer} seconds",
            font_size="10sp",
            halign="center",
            theme_text_color="Secondary",
        )
        content.add_widget(self.timer_label1)

        self.dialog1.open()

        Clock.schedule_interval(self.update_timer1, 1)

    def on_otp_input1(self, instance, value):
        self.otp_input1 = value

    def close_dialog2(self, *args):
        self.dialog1.dismiss()

    def verify_otp1(self, *args):
        if self.otp_text1.text == self.otp:
            self.dialog1.dismiss()
            self.verification_status = "OTP Verified!"
            self.show_success_dialog1()
            if self.verification_status == "OTP Verified!":
                sm.current = "updatepassword"
        else:
            self.dialog1.dismiss()
            self.show_failure_dialog1()

    def show_success_dialog1(self):
        self.success_dialog1 = MDDialog(
            title="Success",
            text="OTP Verified!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_success_dialog1)],
        )
        self.success_dialog1.open()

    def close_success_dialog1(self, *args):
        self.success_dialog1.dismiss()

    def show_failure_dialog1(self):
        self.failure_dialog1 = MDDialog(
            title="Failure",
            text="Invalid OTP!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_failure_dialog1)],
        )
        self.failure_dialog1.open()

    def close_failure_dialog1(self, *args):
        self.failure_dialog1.dismiss()

    def update_timer1(self, dt):
        self.timer -= 1
        if self.timer == 0:
            Clock.unschedule(self.update_timer1)
            self.show_otp_expired_dialog1()
        else:
            self.timer_label1.text = f"Time Left: {self.timer} seconds"

    def show_otp_expired_dialog1(self):
        self.otp_expired_dialog1 = MDDialog(
            title="OTP Expired",
            text="The OTP has expired.",
            buttons=[
                MDRectangleFlatButton(
                    text="Resend OTP", on_release=self.resend_otp_dialog1
                ),
                MDRectangleFlatButton(text="Cancel", on_release=self.close_otp_expired_dialog1),
            ],
        )
        self.otp_expired_dialog1.open()

    def close_otp_expired_dialog1(self, *args):
        self.otp_expired_dialog1.dismiss()

    def resend_otp_dialog1(self, *args):
        self.dialog1.dismiss()
        self.send_otp1()

    def on_stop1(self):
        Clock.unschedule(self.update_timer1)

    def update_password(self,newpassword,confpassword):
        det = sm.get_screen("forgetpassword")
        email = det.ids.text




if __name__ == '__main__':
    MainApp().run()
