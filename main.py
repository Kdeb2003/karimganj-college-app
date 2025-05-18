import datetime
import os
import traceback
from datetime import date
from io import BytesIO

from PIL import Image
from kivy.app import App
from kivy.atlas import CoreImage
from kivy.clock import Clock
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.modalview import ModalView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import TwoLineListItem, ThreeLineListItem, OneLineListItem, ThreeLineAvatarIconListItem, \
    IconRightWidget
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton, MDRaisedButton, MDIconButton
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
import mysql.connector
import re
import smtplib
from email.message import EmailMessage
import random
from threading import Thread
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivymd.uix.card import MDCard
Window.size = (310, 580)



class Karimganj_College(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
        )
        # self.file_manager1 = MDFileManager(
        #     exit_manager=self.exit_file_manager1,
        #     select_path=self.select_path1,
        # )
        self.file_manager2 = MDFileManager(
            exit_manager=self.exit_file_manager2,
            select_path=self.select_path2,
        )
        self.file_manager3 = MDFileManager(
            exit_manager=self.exit_file_manager3,
            select_path=self.select_path3,
        )
        self.file_manager5 = MDFileManager(
            exit_manager=self.exit_manager5,
            select_path=self.select_path5,
            ext=[".pdf"]
        )
        self.file_manager6 = MDFileManager(
            exit_manager=self.exit_manager6,
            select_path=self.select_path6,
            ext=[".pdf"]
        )
        self.file_manager7 = MDFileManager(
            exit_manager=self.exit_manager7,
            select_path=self.select_path7,
            ext=[".pdf"]
        )
    dialog = None
    database = mysql.connector.Connect(host="localhost", user="root", password="Kushal@2003",
                                        database="karimganjcollege",)
    #database = mysql.connector.connect(user="sql12643515",host="sql12.freesqldatabase.com",password="gSpCSP2vBZ",database="sql12643515")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    cursor = database.cursor()
    cursor.execute("select * from signupstudent")
    for i in cursor.fetchall():
        print(i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7])
    #cursor.execute("select * from signupadmin")
    #for i in cursor.fetchall():
    #    print(i[0], i[1], i[2], i[3],i[4],i[5])
    #cursor.execute("select * from company_details")
    #for i in cursor.fetchall():
    #    print(i[0], i[1], i[2], i[3],i[4],i[5])
    #cursor.execute("select * from placementofficer")
    #for i in cursor.fetchall():
    #    print(i[0], i[1], i[2], i[3],i[4],i[5],i[6])
    #cursor.execute("select * from job_details")
    #for i in cursor.fetchall():
    #    print(i[0], i[1], i[2], i[3],i[4],i[5],i[6],i[7])
    #cursor.execute("select * from applied_jobs")
    #for i in cursor.fetchall():
    #    print(i[0], i[1], i[2], i[3],i[4],i[5],i[6])
    KV_FILES = {
        os.path.join(os.getcwd(),"home.kv"),
        os.path.join(os.getcwd(), "tinni2.kv"),
        os.path.join(os.getcwd(), "tinni3.kv"),
        os.path.join(os.getcwd(), "job.kv")
    }
#    KV_FILES1 = {
#        os.path.join(os.getcwd(),"profile.kv"),
#        os.path.join(os.getcwd(), "tinni6.kv")
#    }

    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'
        self.timer = 300
        global img
        global screen_manager

        screen_manager = ScreenManager()


        screen_manager.add_widget(Builder.load_file("spl.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signupadmin.kv"))
        # screen_manager.add_widget(Builder.load_file("signupstudent.kv"))
        screen_manager.add_widget(Builder.load_file("bekkar2.kv"))
        screen_manager.add_widget(Builder.load_file("signupfacalty.kv"))
        screen_manager.add_widget(Builder.load_file("signupteacher.kv"))
        screen_manager.add_widget(Builder.load_file("signupothers.kv"))
        screen_manager.add_widget(Builder.load_file("selection.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("search.kv"))
        screen_manager.add_widget(Builder.load_file("firstselection.kv"))
        screen_manager.add_widget(Builder.load_file("notification.kv"))
        screen_manager.add_widget(Builder.load_file("inbox.kv"))
        screen_manager.add_widget(Builder.load_file("addjob.kv"))
        #screen_manager.add_widget(Builder.load_file("profile.kv"))
        #screen_manager.add_widget(Builder.load_file("testprofile.kv"))
        screen_manager.add_widget(Builder.load_file("adminhome.kv"))
        screen_manager.add_widget(Builder.load_file("adminprofile.kv"))
        screen_manager.add_widget(Builder.load_file("companyhome.kv"))
        #screen_manager.add_widget(Builder.load_file("companyprofile.kv"))
        screen_manager.add_widget(Builder.load_file("po_home.kv"))
        screen_manager.add_widget(Builder.load_file("poprofile.kv"))
        screen_manager.add_widget(Builder.load_file("job.kv"))
        screen_manager.add_widget(Builder.load_file("jobview.kv"))
        screen_manager.add_widget(Builder.load_file("applyjob.kv"))
        screen_manager.add_widget(Builder.load_file("companynotification.kv"))
        screen_manager.add_widget(Builder.load_file("company_sees_student_application.kv"))
        screen_manager.add_widget(Builder.load_file("update_profile.kv"))
        screen_manager.add_widget(Builder.load_file("studentdetailswhoappliedjobs.kv"))
        screen_manager.add_widget(Builder.load_file("addnotice.kv"))
        screen_manager.add_widget(Builder.load_file("jobdetailsshowtocompany.kv"))
        screen_manager.add_widget(Builder.load_file("viewjob.kv"))
        screen_manager.add_widget(Builder.load_file("studentdetailsshowtopo.kv"))
        screen_manager.add_widget(Builder.load_file("viewstudentbypo.kv"))
        screen_manager.add_widget(Builder.load_file("companydetailsviewtopo.kv"))
        screen_manager.add_widget(Builder.load_file("viewcompanybypo.kv"))
        screen_manager.add_widget(Builder.load_file("joblistviewtopo.kv"))
        screen_manager.add_widget(Builder.load_file("viewjobbypo.kv"))
        screen_manager.add_widget(Builder.load_file("show_applied_jobs_topo.kv"))
        screen_manager.add_widget(Builder.load_file("viewappliedjobtopo.kv"))
        screen_manager.add_widget(Builder.load_file("studentappliedjobs.kv"))
        screen_manager.add_widget(Builder.load_file("placementofficerviewtoadmin.kv"))
        screen_manager.add_widget(Builder.load_file("updatejobdetails.kv"))
        screen_manager.add_widget(Builder.load_file("shortlistedstudents.kv"))
        screen_manager.add_widget(Builder.load_file("showshortlistedatudentstopo.kv"))
        screen_manager.add_widget(Builder.load_file("viewnoticetopo.kv"))
        screen_manager.add_widget(Builder.load_file("adminnotification.kv"))
        screen_manager.add_widget(Builder.load_file("forgetpassword.kv"))
        screen_manager.add_widget(Builder.load_file("changepassword.kv"))
        screen_manager.add_widget(Builder.load_file("studentprofile.kv"))
        screen_manager.add_widget(Builder.load_file("noticedetailstostu.kv"))
        screen_manager.add_widget(Builder.load_file("noticedetailstocom.kv"))
        screen_manager.add_widget(Builder.load_file("comoanyprofilenew.kv"))
        screen_manager.add_widget(Builder.load_file("updatecompanyprofile.kv"))
        screen_manager.add_widget(Builder.load_file("reviewstudentsjobapplication.kv"))
        screen_manager.add_widget(Builder.load_file("detailsofstudentswhoseapplicationisbeingreviewd.kv"))
        return screen_manager


    def change_screen(self, screen_name):
        screen_manager.current = screen_name

    def chkbox(self):
        checkbox = Builder.load_file("selection.kv")
        return checkbox

    def on_start(self):
        Clock.schedule_once(self.login, 8)

    def login(*args):
        screen_manager.current = "login"
    def show_snackbar(self, text):
        Snackbar(text=text).open()

    def on_click_shownoticelisttopo(self):
        screen_manager.current = "viewnotice"
        self.cursor.execute("select noticeid,noticedate,notice from notice")
        row = self.cursor.fetchall()
        notice_list = self.root.get_screen('viewnotice').ids.viewnoticelist
        notice_list.clear_widgets()
        for i in row:
            item_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100)
            item100 = ThreeLineListItem(text = i[0], secondary_text = str(i[1]),tertiary_text = str(i[2]))
            icon_button = MDIconButton(icon='trash-can-outline', size_hint=(None, None))
            icon_button.bind(on_release=lambda btn, notice_id=i[0]: self.delete_notice(notice_id))
            item_layout.add_widget(item100)
            item_layout.add_widget(icon_button)
            notice_list.add_widget(item_layout)

    def delete_notice(self, notice_id):
        # Delete the notice from the database based on the provided notice_id
        query = "DELETE FROM notice WHERE noticeid = %s"
        self.cursor.execute(query, (notice_id,))
        self.database.commit()
        self.show_snackbar("Notice deleted successfully")
        self.on_click_shownoticelisttopo()
    def removepo(self, notice_id):
        try:
            dts_scr = screen_manager.get_screen("poviewtoadmin")
            poid = dts_scr.ids.id.text
            self.cursor.execute(
                "DELETE FROM placementofficer WHERE po_id = %s",
                (poid,)
            )
            self.database.commit()
            self.database.close()
            self.show_snackbar("PO removed successfully.")
            screen_manager.current= "adminhome"
        except Exception as e:
            self.database.rollback()  # Rollback the transaction if an error occurs
            print("Error:", e)
            self.show_snackbar("Failed, Try Again")
    def on_click_shownoticelisttostudent(self):
        self.cursor.execute("select notice from notice")
        row = self.cursor.fetchall()
        notice_list = self.root.get_screen('notification').ids.noticefrompotostu
        notice_list.clear_widgets()
        for i in row:
            item100 = OneLineListItem(text = i[0])
            notice_list.add_widget(item100)
    def on_click_shownoticelisttoadmin(self):
        self.cursor.execute("select notice from notice")
        row = self.cursor.fetchall()
        notice_list = self.root.get_screen('adminnotification').ids.noticefrompotoadmin
        notice_list.clear_widgets()
        for i in row:
            item100 = OneLineListItem(text = i[0])
            notice_list.add_widget(item100)
    def check_email_exists(self, email):
        try:
            tables = ['signupstudent', 'company_details', 'placementofficer', 'signupadmin']
            for table in tables:
                query = f"SELECT email_id FROM {table} WHERE email_id = %s"
                self.cursor.execute(query, (email,))
                result = self.cursor.fetchone()
                if result is not None:
                    return True  # Email exists in at least one table
            return False  # Email doesn't exist in any table
        except Exception as e:
            print("Error:", e)
            return False

    def send_data(self, user_id, full_name, email_id, phone_no, address, department, password, dob, yearofjoining):
        try:
            if re.fullmatch(self.regex, email_id.text):
                if not self.check_email_exists(email_id.text):
                    self.cursor.execute(
                        f"INSERT INTO signupstudent VALUES ('{user_id.text}', '{full_name.text}', '{email_id.text}',"
                        f"'{phone_no.text}', '{address.text}', '{department.text}', '{password.text}', '{dob.text}','{yearofjoining.text}')"
                    )
                    self.database.commit()
                    email_id.text = " "
                    password.text = " "
                    self.show_snackbar("Registration Successful")
                else:
                    self.show_snackbar("Email already exists in one of the tables")
        except Exception as e:
            self.database.rollback()  # Rollback the transaction if an error occurs
            print("Error:", e)
            self.show_snackbar("An error occurred during registration.")

    # Replace self.show_snackbar with the appropriate method you're using to display snackbars in your application.

    def send_data1(self, user_id, full_name, email_id, phone_no, address, password):
        try:
            if re.fullmatch(self.regex, email_id.text):
                if not self.check_email_exists(email_id.text):
                    self.cursor.execute(
                        f"INSERT INTO signupadmin VALUES ('{user_id.text}', '{full_name.text}', '{email_id.text}',"
                        f"'{phone_no.text}', '{address.text}', '{password.text}')"
                    )
                    self.database.commit()
                    email_id.text = " "
                    password.text = " "
                    self.show_snackbar("Registration Successful")
                else:
                    self.show_snackbar("Email already exists in one of the tables")
        except Exception as e:
            self.database.rollback()  # Rollback the transaction if an error occurs
            print("Error:", e)
            self.show_snackbar("An error occurred during registration.")

    # Replace self.show_snackbar with the appropriate method you're using to display snackbars in your application.

    def send_data2(self, company_id, company_name, email_id, phone_no, address,password):

        if re.fullmatch(self.regex, email_id.text):
            if not self.check_email_exists(email_id.text):
                try:
                    self.cursor.execute(
                        f"insert into company_details values('{company_id.text}', '{company_name.text}', '{email_id.text}','{phone_no.text}','{address.text}','{password.text}' )")
                    self.database.commit()
                    email_id.text = " "
                    password.text = " "
                    self.show_snackbar("Registration Successful")
                except Exception as e:
                    print("Error:", e)
            else:
                self.show_snackbar("Email already exists in one of the tables")

    def send_data3(self, po_id, po_name, email_id, phone_no, department,address,password):

        if re.fullmatch(self.regex, email_id.text):
            if not self.check_email_exists(email_id.text):
                try:
                    self.cursor.execute(
                        f"insert into placementofficer values('{po_id.text}', '{po_name.text}', '{email_id.text}','{phone_no.text}','{department.text}','{address.text}','{password.text}' )")
                    self.database.commit()
                    email_id.text = " "
                    password.text = " "
                    self.show_snackbar("Registration Successful")
                except Exception as e:
                    print("Error:", e)
            else:
                self.show_snackbar("Email already exists in one of the tables")

    # Replace self.show_snackbar with the appropriate method you're using to display snackbars in your application.

    # def send_data4(self, job_code, job_title, student_name, email_id, phone_no, why_applying, why_hire, com_name):
    #     try:
    #         self.cursor.execute(
    #             f"INSERT INTO applied_jobs VALUES ('{job_code.text}', '{job_title.text}', '{student_name.text}', "
    #             f"'{email_id.text}', '{phone_no.text}', '{why_applying.text}', '{why_hire.text}', '{com_name.text}')"
    #         )
    #         self.database.commit()
    #
    #         self.dialog = MDDialog(
    #             title="Submitted Successfully",
    #             buttons=[
    #                 MDFillRoundFlatButton(text="OK", on_release=self.close_dialog)
    #             ]
    #         )
    #         self.dialog.open()
    #         det = screen_manager.get_screen("applyjob")
    #         det.ids.job_code.text  = ""
    #         det.ids.job_title.text  = ""
    #         det.ids.com_name.text  = ""
    #         det.ids.student_name.text  = ""
    #         det.ids.email_id.text  = ""
    #         det.ids.phone_no.text  = ""
    #         det.ids.why_applying.text  = ""
    #         det.ids.why_hire.text  = ""
    #
    #     except Exception as e:
    #         self.database.rollback()  # Rollback the transaction if an error occurs
    #         print("Error:", e)
    #         self.show_snackbar("An error occurred while submitting the application.")

    # Replace self.show_snackbar with the appropriate method you're using to display snackbars in your application.
    def send_data4(self, job_code, job_title, student_name, email_id, phone_no, why_applying, why_hire):
        try:
            # Check if the job has already been applied for by this user
            self.cursor.execute(
                "SELECT COUNT(*) FROM applied_jobs WHERE job_id = %s AND email_id = %s",
                (job_code.text, email_id.text)
            )
            count = self.cursor.fetchone()[0]

            if count > 0:
                # Job has already been applied for
                self.dialog = MDDialog(
                    title="Already Applied",
                    text="You have already applied for this job.",
                    buttons=[
                        MDFillRoundFlatButton(text="OK", on_release=self.close_dialog125)
                    ]
                )
                self.dialog.open()
            else:
                # Job has not been applied for, proceed with insertion
                det = screen_manager.get_screen("jobview")
                com_name = det.ids.companynameview.text
                self.cursor.execute(
                    "INSERT INTO applied_jobs (job_id, job_title, student_name, email_id, phone_no, why_applying, why_hire, company_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (job_code.text, job_title.text, student_name.text, email_id.text, phone_no.text, why_applying.text,
                     why_hire.text, com_name)
                )
                self.database.commit()

                self.dialog = MDDialog(
                    title="Submitted Successfully",
                    buttons=[
                        MDFillRoundFlatButton(text="OK", on_release=self.close_dialog125)
                    ]
                )
                self.dialog.open()
                det = screen_manager.get_screen("applyjob")
                det.ids.job_code.text = ""
                det.ids.job_title.text = ""
                det.ids.com_name.text = ""
                det.ids.student_name.text = ""
                det.ids.email_id.text = ""
                det.ids.phone_no.text = ""
                det.ids.why_applying.text = ""
                det.ids.why_hire.text = ""

        except Exception as e:
            self.database.rollback()  # Rollback the transaction if an error occurs
            print("Error:", e)
            self.show_snackbar("An error occurred while submitting the application.")

    def close_dialog125(self, *args):
        self.dialog.dismiss(force=True)

    def send_data5(self, jobcodeprovideid, jobtitleprovideid, companyidprovide, companynameprovideid,
                   jobdescriptionprovide, salaryprovideid, dateofprovidingjob, lastdateofapplying):
        try:
            self.cursor.execute(
                f"INSERT INTO job_details VALUES ('{jobcodeprovideid.text}', '{jobtitleprovideid.text}', "
                f"'{jobdescriptionprovide.text}', '{companynameprovideid.text}', '{companyidprovide.text}', "
                f"'{dateofprovidingjob.text}', '{lastdateofapplying.text}', '{salaryprovideid.text}')"
            )
            self.database.commit()
            det = screen_manager.get_screen("addjob")
            det.ids.jobcodeprovideid.text = ""
            det.ids.jobtitleprovideid.text = ""
            det.ids.companyidprovide.text = ""
            det.ids.companynameprovideid.text = ""
            det.ids.jobdescriptionprovide.text = ""
            det.ids.salaryprovideid.text = ""
            det.ids.dateofprovidingjob.text = ""
            det.ids.lastdateofapplying.text = ""
            self.dialog = MDDialog(
                title="Submitted Successfully",
                text="Job details have been submitted successfully.",
                buttons=[
                    MDFillRoundFlatButton(text="OK", on_release=self.close_dialog)
                ]
            )
            self.dialog.open()
        except Exception as e:
            self.database.rollback()  # Rollback the transaction if an error occurs
            print("Error:", e)
            self.dialog = MDDialog(
                title="Error",
                text="An error occurred while submitting job details.",
                buttons=[
                    MDFillRoundFlatButton(text="OK", on_release=self.close_dialog)
                ]
            )
            self.dialog.open()

    # Replace self.show_snackbar with the appropriate method you're using to display snackbars in your application.

    import datetime
    import traceback

    def shortlist(self):
        try:
            det = screen_manager.get_screen('studentdetailsthathaveappliedjobs')
            userid = det.ids.user_id.text
            full_name = det.ids.full_name.text
            dept = det.ids.department.text
            det1 = screen_manager.get_screen('companyseesstudentapplication')
            jobcode = det1.ids.jobidviewtocompany.text
            jobtitle = det1.ids.jobtitleviewtocompany.text
            comemail = det1.ids.companyname.text
            today = datetime.date.today()
            a = "shortlisted"

            # Check the 'shortlisted_ornot' status
            shortlisted_query = f"SELECT shortlisted_ornot FROM shortlisted_students WHERE user_id = '{userid}' AND job_id = '{jobcode}'"
            self.cursor.execute(shortlisted_query)
            shortlisted_record = self.cursor.fetchone()

            if shortlisted_record and shortlisted_record[0] == "rejected":
                # Update the 'shortlisted_ornot' status to 'shortlisted'
                self.cursor.execute(
                    "UPDATE shortlisted_students SET shortlisted_ornot = %s, date_of_replying = %s WHERE user_id = %s AND job_id = %s",
                    (a, today, userid, jobcode)
                )
                self.database.commit()
                self.show_snackbar("Student status updated successfully.")
                screen_manager.current = "companyhome"
            else:
                # Insert into shortlisted_students table
                self.cursor.execute(
                    "INSERT INTO shortlisted_students (user_id, full_name, department, job_id, job_title, shortlisted_ornot, date_of_replying, company_name) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (userid, full_name, dept, jobcode, jobtitle, a, today, comemail)
                )
                self.database.commit()
                self.show_snackbar("Student status updated successfully.")
                screen_manager.current = "companyhome"

            self.cursor.execute("SELECT email_id FROM signupstudent WHERE user_id = %s", (userid,))
            student_email_tuple = self.cursor.fetchone()
            student_email = student_email_tuple[0]  # Extract the email from the tuple
            print(student_email)

            self.cursor.execute("SELECT * FROM applied_jobs WHERE email_id = %s", (student_email,))
            rows = self.cursor.fetchall()

            for row in rows:
                job_code = row[0]
                job_title = row[1]
                student_name = row[2]
                email_id = row[3]
                phone_no = row[4]
                why_applying = row[5]
                why_hire = row[6]
                com_name = row[7]

                self.cursor.execute(
                    "INSERT INTO prev_applied_jobs (job_id, job_title, student_name, email_id, phone_no, why_applying, why_hire, company_name) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (job_code, job_title, student_name, email_id, phone_no, why_applying, why_hire, com_name)
                )

            delete_query = "DELETE FROM applied_jobs WHERE email_id = %s"
            self.cursor.execute(delete_query, (student_email,))
            self.database.commit()
            self.show_snackbar("Student shortlisted successfully.")
            screen_manager.current = "companyhome"

        except Exception as e:
            # Print the stack trace for debugging
            print(traceback.format_exc())

            # Show an error message to the user
            self.show_snackbar("An error occurred. Please try again later.")

    def reject(self):
        det = screen_manager.get_screen('studentdetailsthathaveappliedjobs')
        userid = det.ids.user_id.text
        full_name = det.ids.full_name.text
        dept = det.ids.department.text
        det1 = screen_manager.get_screen('companyseesstudentapplication')
        jobcode = det1.ids.jobidviewtocompany.text
        jobtitle = det1.ids.jobtitleviewtocompany.text
        comemail = det1.ids.companyname.text
        today = datetime.date.today()
        a = "rejected"

        try:
            # Check if the student is already shortlisted
            shortlisted_query = f"SELECT shortlisted_ornot FROM shortlisted_students WHERE user_id = '{userid}' AND job_id = '{jobcode}'"
            self.cursor.execute(shortlisted_query)
            shortlisted_record = self.cursor.fetchone()

            if shortlisted_record and shortlisted_record[0] == "shortlisted":
                # Student is already shortlisted, so update the 'shortlisted_ornot' column
                self.cursor.execute(
                    "UPDATE shortlisted_students SET shortlisted_ornot = %s, date_of_replying = %s WHERE user_id = %s AND job_id = %s",
                    (a, today, userid, jobcode)
                )
                self.database.commit()
                self.show_snackbar("Student status updated successfully.")
            else:
                # Student is not shortlisted, so insert a new record
                self.cursor.execute(
                    "INSERT INTO shortlisted_students (user_id, full_name, department, job_id, job_title, shortlisted_ornot, date_of_replying, company_name) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (userid, full_name, dept, jobcode, jobtitle, a, today, comemail)
                )
                self.database.commit()
                self.cursor.execute("SELECT email_id FROM signupstudent WHERE user_id = %s", (userid,))
                student_email = self.cursor.fetchone()[0]  # Extract the email string from the tuple
                print(student_email)
                self.cursor.execute("SELECT * FROM applied_jobs WHERE email_id = %s", (student_email,))
                rows = self.cursor.fetchall()

                for row in rows:
                    job_code = row[0]
                    job_title = row[1]
                    student_name = row[2]
                    email_id = row[3]
                    phone_no = row[4]
                    why_applying = row[5]
                    why_hire = row[6]
                    com_name = row[7]

                    self.cursor.execute(
                        "INSERT INTO prev_applied_jobs (job_id, job_title, student_name, email_id, phone_no, why_applying, why_hire, company_name) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (job_code, job_title, student_name, email_id, phone_no, why_applying, why_hire, com_name)
                    )
                delete_query = f"DELETE FROM applied_jobs WHERE email_id = %s"
                self.cursor.execute(delete_query, (student_email,))
                self.database.commit()
                self.show_snackbar("Student rejected successfully.")

        except Exception as e:
            self.database.rollback()
            self.show_snackbar(f"An error occurred: {str(e)}")

    def receive_data(self, email_id, password):
        self.cursor.execute("select * from signupstudent")
        email_list1 = []
        for i in self.cursor.fetchall():
            email_list1.append(i[2])
        self.cursor.execute("select * from signupadmin")
        email_list2 = []
        for i in self.cursor.fetchall():
            email_list2.append(i[2])
        self.cursor.execute("select * from company_details")
        email_list3 = []
        for i in self.cursor.fetchall():
            email_list3.append(i[2])
        self.cursor.execute("select * from placementofficer")
        email_list4 = []
        for i in self.cursor.fetchall():
            email_list4.append(i[2])
        if email_id.text in email_list1 and email_id.text != " ":
            self.cursor.execute(f"select password from signupstudent where email_id= '{email_id.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    screen_manager.current='home'
                    #app.on_click_shownoticelisttostudent()
                    self.dialog = MDDialog(
                        title="You have successfully logged in",
                        buttons=[
                            MDFillRoundFlatButton(text="OK", on_release=self.close_dialog),
                            #MDRectangleFlatButton(text="more", text_color=self.theme_cls.primary_color),
                        ],
                    )
                    self.dialog.open()
                    #print("You have successfully loggedin")
                else:
                    self.dialog = MDDialog(
                        title="Invalid Password",
                        buttons=[
                            MDFillRoundFlatButton(text="close", on_release=  self.close_dialog),
                            MDRectangleFlatButton(text="more", text_color=self.theme_cls.primary_color),
                        ],
                    )
                    self.dialog.open()
                    print("Invalid password")
        elif email_id.text in email_list2 and email_id.text != " ":
            self.cursor.execute(f"select password from signupadmin where email_id= '{email_id.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    screen_manager.current = 'adminhome'
                    self.dialog = MDDialog(
                        title="You have successfully logged in",
                        buttons=[
                            MDFillRoundFlatButton(text="OK", on_release=self.close_dialog),
                            #MDRectangleFlatButton(text="more", text_color=self.theme_cls.primary_color),
                        ],
                    )
                    self.dialog.open()
                    #print("You have successfully loggedin")
                else:
                    self.dialog = MDDialog(
                        title="Invalid Password",
                        buttons=[
                            MDFillRoundFlatButton(text="close", on_release=  self.close_dialog),
                            MDRectangleFlatButton(text="more", text_color=self.theme_cls.primary_color),
                        ],
                    )
                    self.dialog.open()
                    print("Invalid password")
        elif email_id.text in email_list3 and email_id.text != " ":
            self.cursor.execute(f"select password from company_details where company_emailid= '{email_id.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    screen_manager.current = 'companyhome'
                    self.on_click_shownoticelist()
                    self.dialog = MDDialog(
                        title="You have successfully logged in",
                        buttons=[
                            MDFillRoundFlatButton(text="OK", on_release=self.close_dialog),
                            #MDRectangleFlatButton(text="more", text_color=self.theme_cls.primary_color),
                        ],
                    )
                    self.dialog.open()

                    #print("You have successfully loggedin")
                else:
                    self.dialog = MDDialog(
                        title="Invalid Password",
                        buttons=[
                            MDFillRoundFlatButton(text="close", on_release=  self.close_dialog),
                            MDRectangleFlatButton(text="more", text_color=self.theme_cls.primary_color),
                        ],
                    )
                    self.dialog.open()
                    print("Invalid password")
        elif email_id.text in email_list4 and email_id.text != " ":
            self.cursor.execute(f"select password from placementofficer where email_id= '{email_id.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    screen_manager.current = 'pohome'
                    self.dialog = MDDialog(
                        title="You have successfully logged in",
                        buttons=[
                            MDFillRoundFlatButton(text="OK", on_release=self.close_dialog),
                            #MDRectangleFlatButton(text="more", text_color=self.theme_cls.primary_color),
                        ],
                    )
                    self.dialog.open()
                    #print("You have successfully loggedin")
                else:
                    self.dialog = MDDialog(
                        title="Invalid Password",
                        buttons=[
                            MDFillRoundFlatButton(text="close", on_release=  self.close_dialog),
                            MDRectangleFlatButton(text="more", text_color=self.theme_cls.primary_color),
                        ],
                    )
                    self.dialog.open()
                    print("Invalid password")
        else:
            self.dialog = MDDialog(

                title="Invalid Email ID",
                text = "Please re-enter the email id",
                buttons=[
                    MDFillRoundFlatButton(text="cancel", on_release=self.close_dialog),
                    MDRectangleFlatButton(text="more", text_color=self.theme_cls.primary_color),
                ],
            )
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
    def display_data(self,):
       # self.cursor.execute(f"select full_name from signupstudent where email_id = '{email_id.text}'")
        #email_list = []
        #for i in self.cursor.fetchone():
            #email_list.append(i[2])
       # if email_id.text in email_list:
            #self.root.ids.my_label.text= email_id
        screen_manager.current='profile'
        det = screen_manager.get_screen('login')
        email=det.ids.email_id.text
        det2 = screen_manager.get_screen('profile')
        det2.ids.my_label.text=email

        self.cursor.execute("select * from signupstudent where email_id = %s",(email,))
        row = self.cursor.fetchone()
        det2.ids.name.text = str(row[1])
        det2.ids.phone.text = str(row[3])
        det2.ids.dept.text = str(row[5])
        det2.ids.addr.text = str(row[4])
    def display_data1(self,):
       # self.cursor.execute(f"select full_name from signupstudent where email_id = '{email_id.text}'")
        #email_list = []
        #for i in self.cursor.fetchone():
            #email_list.append(i[2])
       # if email_id.text in email_list:
            #self.root.ids.my_label.text= email_id
        screen_manager.current='adminprofile'
        det = screen_manager.get_screen('login')
        email1=det.ids.email_id.text
        det2 = screen_manager.get_screen('adminprofile')
        #det2.ids.admin_label.text=email1

        self.cursor.execute("select * from signupadmin where email_id = %s",(email1,))
        row = self.cursor.fetchone()
        det2.ids.name.text = str(row[1])
        det2.ids.my_label.text = str(row[2])
        det2.ids.phone.text = str(row[3])
        det2.ids.addr.text = str(row[4])
        det2.ids.id.text = str(row[0])
        #det2.ids.dept.text = str(row[5])
    def display_data2(self,):
        screen_manager.current='companyprofile'
        det = screen_manager.get_screen('login')
        email2=det.ids.email_id.text
        det2 = screen_manager.get_screen('companyprofile')
        det2.ids.my_label.text=email2

        self.cursor.execute("select * from company_details where company_emailid = %s",(email2,))
        row = self.cursor.fetchone()
        det2.ids.name.text = str(row[1])
        det2.ids.phone.text = str(row[3])
        det2.ids.addr.text = str(row[4])
        det2.ids.co_id.text = str(row[0])
    def display_company_name(self,):
        screen_manager.current='companyhome'
        det = screen_manager.get_screen('login')
        email2=det.ids.email_id.text
        det2 = screen_manager.get_screen('companyhome')
        #det2.ids.company_label.text=email2

        self.cursor.execute("select company_name from company_details where company_emailid = %s",(email2,))
        row = self.cursor.fetchone()[0]
        det2.ids.comp_name.text = str(row)
        #det2.ids.phone.text = str(row[3])
        #det2.ids.dept.text = str(row[5])
    def display_data3(self,):
       # self.cursor.execute(f"select full_name from signupstudent where email_id = '{email_id.text}'")
        #email_list = []
        #for i in self.cursor.fetchone():
            #email_list.append(i[2])
       # if email_id.text in email_list:
            #self.root.ids.my_label.text= email_id
        screen_manager.current='poprofile'
        det = screen_manager.get_screen('login')
        email3=det.ids.email_id.text
        det2 = screen_manager.get_screen('poprofile')
        #det2.ids.company_label.text=email3

        self.cursor.execute("select * from placementofficer where email_id = %s",(email3,))
        row = self.cursor.fetchone()
        det2.ids.name.text = str(row[1])
        det2.ids.my_label.text = str(row[2])
        det2.ids.phone.text = str(row[3])
        det2.ids.addr.text = str(row[5])
        det2.ids.department.text = str(row[4])
        det2.ids.po_id.text = str(row[0])
    def display_data4(self,):
        screen_manager.current='adminprofile'
        det = screen_manager.get_screen('login')
        email3=det.ids.email_id.text
        det2 = screen_manager.get_screen('adminprofile')
        #det2.ids.company_label.text=email3

        self.cursor.execute("select * from signupadmin where email_id = %s",(email3,))
        row = self.cursor.fetchone()
        det2.ids.name.text = str(row[1])
        det2.ids.my_label.text = str(row[2])
        det2.ids.phone.text = str(row[3])
        det2.ids.addr.text = str(row[4])
        det2.ids.id.text = str(row[0])
    def display_potadmin(self,):
        screen_manager.current = "poviewtoadmin"
        det = screen_manager.get_screen('poviewtoadmin')
        self.cursor.execute("select * from placementofficer")
        row = self.cursor.fetchone()
        det.ids.name.text = str(row[1])
        det.ids.my_label.text = str(row[2])
        det.ids.phone.text = str(row[3])
        det.ids.addr.text = str(row[5])
        det.ids.id.text = str(row[0])
        det.ids.dept.text = str(row[4])


    def on_click_showlist(self):
        self.cursor.execute("select job_code,job_title,company_name from job_details")
        row = self.cursor.fetchall()
        job_list = self.root.get_screen('job').ids.lula_list
        job_list.clear_widgets()
        for i in row:
            item = ThreeLineListItem(text = i[1], secondary_text = str(i[0]),tertiary_text = str(i[2]))
            item.bind(on_release= self.show_details_ofjob)
            job_list.add_widget(item)


    def show_details_ofjob(self,item):
        self.cursor.execute("select * from job_details where job_code = %s",(item.secondary_text,))
        row = self.cursor.fetchone()
        screen_manager.current = "jobview"
        job_details_screen = screen_manager.get_screen("jobview")
        if job_details_screen:
            job_details_screen.ids.companynameview.text=str(row[3])
            job_details_screen.ids.jobtitleview.text=str(row[1])
            job_details_screen.ids.jobdescriptionview.text=str(row[2])
            job_details_screen.ids.jobcodeview.text = str(row[0])
            job_details_screen.ids.lastapplyingdate.text = str(row[6])



    def on_click_showcompanylist(self):
        screen_manager.current = "Company_Notification"
        screen_manager.transition.direction = "right"
        det = screen_manager.get_screen('login')
        emailco = det.ids.email_id.text
        self.cursor.execute("select company_name from company_details where company_emailid = %s",(emailco,))
        det1 = self.cursor.fetchone()[0]
        print(emailco)
        print(det1)
        self.cursor.execute("select job_id,student_name,email_id from applied_jobs where company_name = %s",(det1,))
        row = self.cursor.fetchall()
        job_list = self.root.get_screen('Company_Notification').ids.company_notification_list
        job_list.clear_widgets()
        for i in row:
            item1 = ThreeLineListItem(text = i[1], secondary_text = str(i[0]), tertiary_text = str(i[2]))
            item1.bind(on_release= self.show_company_notification)
            item1.bind(on_release= self.shw)
            item1.bind(on_release= self.on_click_showstudentpdf)
            job_list.add_widget(item1)

    def on_click_showstudentpdf(self,item1):
        screen_manager.current = "Company_Notification"
        # det = screen_manager.get_screen('Company_Notification')
        # emailco = det.ids.studentemailidviewtocompany.text
        self.cursor.execute("select uid,name from stu_resume where uid = %s",(item1.tertiary_text,))
        # det1 = self.cursor.fetchone()[0]
        # print(emailco)
        # print(det1)
        # self.cursor.execute("select job_id,student_name,email_id from applied_jobs where company_name = %s",(det1,))
        row = self.cursor.fetchall()
        print(row)
        job_list = self.root.get_screen('companyseesstudentapplication').ids.studentpdf
        job_list.clear_widgets()
        for i in row:
            item_layout1 = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
            item2 = TwoLineListItem(text = "Student Resume",secondary_text = i[0] )
            icon_button = MDIconButton(icon='download', size_hint=(None, None))
            icon_button.bind(on_release=lambda btn, student_email=i[0]: self.show_save_dialog(btn,student_email))
            item_layout1.add_widget(item2)
            item_layout1.add_widget(icon_button)
            job_list.add_widget(item_layout1)
    def show_save_dialog(self, btn, student_email):
        connection = mysql.connector.connect(
            host='localhost',
            database='karimganjcollege',
            user='root',
            password='Kushal@2003'
        )
        cursor = connection.cursor()

        try:
            # Fetch file data from the database
            query = f"SELECT name,pdf_data FROM stu_resume WHERE uid = %s"
            para = (student_email,)
            cursor.execute(query, para)
            result = cursor.fetchone()

            if result:
                # Create and open the SaveDialog
                save_dialog = SaveDialog(callback=self.download_pdf)
                save_dialog.open()

            else:
                print(f"PDF file for {student_email} not found")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        except Exception as e:
            # Handle other exceptions
            print(f"Unexpected error: {e}")

        finally:
            # Close the database connection
            cursor.close()
            connection.close()
    def download_pdf(self,chosen_directory):
        a = screen_manager.get_screen("companyseesstudentapplication")
        stuemail = a.ids.studentemailidviewtocompany.text
        # self.cursor.execute("SELECT pdf_data FROM stu_resume WHERE uid = %s", (stuemail,))
        # pdf_row = self.cursor.fetchone()
        # if pdf_row:
        #     pdf_data = pdf_row[0]
        #     # Save the PDF data to a file
        #     with open("downloaded_pdf.pdf", "wb") as pdf_file:
        #         pdf_file.write(pdf_data)
        #     self.show_snackbar("PDF Downloaded")
        connection = mysql.connector.connect(
            host='localhost',
            database='karimganjcollege',
            user='root',
            password='Kushal@2003'
        )
        cursor = connection.cursor()

        try:
            # Fetch file data from the database
            query = f"SELECT name, pdf_data FROM stu_resume WHERE uid = %s"
            para = (stuemail,)
            cursor.execute(query,para)
            result = cursor.fetchone()

            if result:
                name, pdf_data = result

                # Write the PDF file to the chosen directory
                pdf_path = f"{chosen_directory}/{name}.pdf"
                with open(pdf_path, 'wb') as pdf_file:
                    pdf_file.write(pdf_data)

                print(f"PDF file '{name}' downloaded successfully as '{pdf_path}'")

            else:
                print(f"PDF file not found")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        except Exception as e:
            # Catch and ignore the specific file access permission error
            if 'The process cannot access the file' in str(e):
                print("Ignoring file access permission error.")
            else:
                print(f"Unexpected error: {e}")

        finally:
            # Close the database connection
            cursor.close()
            connection.close()
    def show_company_notification(self,item1):
        #print(item1.secondary_text)
        self.cursor.execute("select * from applied_jobs where job_id = %s",(item1.secondary_text,))

        row = self.cursor.fetchone()
        print(row)
        screen_manager.current = "companyseesstudentapplication"
        job_details_screen = screen_manager.get_screen("companyseesstudentapplication")
        if job_details_screen:
            job_details_screen.ids.jobtitleviewtocompany.text=str(row[1])
            job_details_screen.ids.jobidviewtocompany.text=str(row[0])
            job_details_screen.ids.stunametocompany.text=str(row[2])
            job_details_screen.ids.studentemailidviewtocompany.text = str(row[3])
            job_details_screen.ids.companyname.text = str(row[7])
            job_details_screen.ids.whyapplyingviewtocompany.text = str(row[5])
            job_details_screen.ids.whyhireviewtocompany.text = str(row[6])

    def showdetails_student(self,):
        screen_manager.current='updateprofile'
        det = screen_manager.get_screen('login')
        emailstu=det.ids.email_id.text
        self.cursor.execute("select * from signupstudent where email_id = %s ",(emailstu,))
        row=self.cursor.fetchone()
        screen_manager.current = "updateprofile"
        dts_scr = screen_manager.get_screen("updateprofile")
        if dts_scr:
            dts_scr.ids.user_id.text = str(row[0])
            dts_scr.ids.user_id.disabled = True
            dts_scr.ids.full_name.text = str(row[1])
            dts_scr.ids.email_id.text = str(row[2])
            dts_scr.ids.email_id.disabled = True
            dts_scr.ids.phone_no.text = str(row[3])
            dts_scr.ids.address.text = str(row[4])
            dts_scr.ids.department.text = str(row[5])
            dts_scr.ids.password.text = str(row[6])
            dts_scr.ids.dob.text = str(row[7])
        self.database.commit()

        #self.database.close()

    def updateprofile(self,user_id,full_name,email_id,phone_no,address,department,dob, password):
        try:
            self.cursor.execute(
                "UPDATE signupstudent SET user_id = %s, full_name = %s, email_id = %s, phone_no = %s, address = %s, department = %s, password = %s, dob = %s WHERE email_id = %s",
                (user_id,full_name,email_id,phone_no,address,department, password, dob, email_id)
            )
            self.cursor.execute("select * from signupstudent where email_id = %s", (email_id,))
            row = self.cursor.fetchone()
            if row:
                dts_scr = screen_manager.get_screen("updateprofile")
                dts_scr.ids.user_id.text = str(row[0])
                dts_scr.ids.full_name.text = str(row[1])
                dts_scr.ids.email_id.text = str(row[2])
                dts_scr.ids.phone_no.text = str(row[3])
                dts_scr.ids.address.text = str(row[4])
                dts_scr.ids.department.text = str(row[5])
                dts_scr.ids.password.text = str(row[6])
                dts_scr.ids.dob.text = str(row[7])
            self.show_snackbar("Updated Successfully")
        except Exception as e:
            self.database.rollback()
            self.show_snackbar(f"Error; try again: {str(e)}")

    def showjobdetailstoupdatepage(self):
        try:
            det = screen_manager.get_screen('login')
            email = det.ids.email_id.text
            self.cursor.execute("SELECT company_id FROM company_details WHERE company_emailid =%s",(email,))
            x = self.cursor.fetchone()[0]
            print(x)
            self.cursor.execute("SELECT * FROM job_details WHERE companyidprovide = %s", (x,))
            row = self.cursor.fetchone()
            print(row)
            dts_scr = screen_manager.get_screen("updatejobdetails")
            if dts_scr:
                dts_scr.ids.jobcodeprovideid.text = str(row[0])
                dts_scr.ids.jobcodeprovideid.disabled = True
                dts_scr.ids.jobtitleprovideid.text = str(row[1])
                dts_scr.ids.companyidprovide.text = str(row[4])
                dts_scr.ids.companyidprovide.disabled = True
                dts_scr.ids.companynameprovideid.text = str(row[3])
                dts_scr.ids.companynameprovideid.disabled = True
                dts_scr.ids.jobdescriptionprovide.text = str(row[2])
                dts_scr.ids.salaryprovideid.text = str(row[7])
                dts_scr.ids.dateofprovidingjob.text = str(row[5])
                dts_scr.ids.lastdateofapplying.text = str(row[6])
        except Exception as e:
            print("Error:", e)
            self.show_snackbar("An error occurred while fetching job details.")
        #
        # screen_manager.current = "updatejobdetails"
        # self.database.commit()

    def updatejobdetails(self, jobcodeprovideid, jobtitleprovideid, companyidprovide, companynameprovideid,
                         jobdescriptionprovide, salaryprovideid, dateofprovidingjob, lastdateofapplying):
        try:
            # Handle any unread results before executing the new query
            if self.cursor.with_rows:
                self.cursor.fetchall()

            self.cursor.execute(
                "UPDATE job_details SET job_code = %s, job_title = %s, jobdescriptionprovide = %s, "
                "company_name = %s, companyidprovide = %s, dateofprovidingjob = %s, Last_Applying_Date = %s, "
                "salaryprovideid = %s WHERE job_code = %s",
                (jobcodeprovideid, jobtitleprovideid, jobdescriptionprovide, companynameprovideid, companyidprovide,
                 dateofprovidingjob, lastdateofapplying, salaryprovideid, jobcodeprovideid)
            )

            # Clear any results from the UPDATE query
            if self.cursor.with_rows:
                self.cursor.fetchall()

            self.database.commit()

            # Ensure any unread results from previous queries are handled
            if self.cursor.with_rows:
                self.cursor.fetchall()

            self.cursor.execute("SELECT * FROM job_details WHERE companyidprovide = %s", (companyidprovide,))
            row = self.cursor.fetchone()
            if row:
                dts_scr = screen_manager.get_screen("updatejobdetails")
                dts_scr.ids.jobcodeprovideid.text = str(row[0])
                dts_scr.ids.jobtitleprovideid.text = str(row[1])
                dts_scr.ids.companyidprovide.text = str(row[4])
                dts_scr.ids.companynameprovideid.text = str(row[3])
                dts_scr.ids.jobdescriptionprovide.text = str(row[2])
                dts_scr.ids.salaryprovideid.text = str(row[7])
                dts_scr.ids.dateofprovidingjob.text = str(row[5])
                dts_scr.ids.lastdateofapplying.text = str(row[6])
            self.show_snackbar("Job details updated successfully.")
        except Exception as e:
            self.database.rollback()  # Rollback the transaction if an error occurs
            print("Error:", e)
            self.show_snackbar("An error occurred while updating job details.")

    def removejob(self):
        try:
            dts_scr = screen_manager.get_screen("viewjob")
            jobcode = dts_scr.ids.job_id.text
            self.cursor.execute(
                "DELETE FROM job_details WHERE job_code = %s",
                (jobcode,)
            )
            self.database.commit()
            self.show_snackbar("Job removed successfully.")
            screen_manager.current= "companyhome"
        except Exception as e:
            self.database.rollback()  # Rollback the transaction if an error occurs
            print("Error:", e)
            self.show_snackbar("Failed, Try Again")

    def show_det(self,):
        #screen_manager.current = 'studentdetailsthathaveappliedjobs'
        det = screen_manager.get_screen('companyseesstudentapplication')
        eml = det.ids.studentemailidviewtocompany.text
        print("eml",eml)
        det2 = screen_manager.get_screen('studentdetailsthathaveappliedjobs')
        self.cursor.execute("SELECT * FROM signupstudent WHERE user_id = %s ",(eml,))
        #self.cursor.fetchall()  # Consume previous query results
        row = self.cursor.fetchone()
        print(row)
        #det2.ids.user_id.text = str(row[0])
    def shw(self,item1):
        self.cursor.execute("select * from signupstudent where email_id = %s",(item1.tertiary_text,))

        row = self.cursor.fetchone()
        print(row)
        screen_manager.current = "studentdetailsthathaveappliedjobs"
        job_details_screen = screen_manager.get_screen("studentdetailsthathaveappliedjobs")
        if job_details_screen:
            job_details_screen.ids.user_id.text=str(row[0])
            job_details_screen.ids.full_name.text=str(row[1])
            job_details_screen.ids.email_id.text=str(row[2])
            job_details_screen.ids.phone_no.text = str(row[3])
            job_details_screen.ids.address.text = str(row[4])
            job_details_screen.ids.department.text = str(row[5])
    def jobdetails_show(self,):
        det = screen_manager.get_screen('login')
        email3=det.ids.email_id.text
        det2 = screen_manager.get_screen('jobdetailsshowtocompany')
        #det2.ids.company_label.text=email3

        self.cursor.execute("select company_id from company_details where company_emailid = %s",(email3,))

        row = self.cursor.fetchone()[0]
        self.cursor.execute("select * from job_details where company_id = %s", (row,))
        bro = self.cursor.fetchone()
        det2.ids.job_id.text = str(bro[0])
        det2.ids.job_title.text = str(bro[1])
        det2.ids.Last_Applying_Date.text = str(bro[6])
        det2.ids.Providing_Date.text = str(bro[5])

    def on_click_showjoblist(self):
        try:
            screen_manager.current = "jobdetailsshowtocompany"
            det = screen_manager.get_screen('login')
            emailco = det.ids.email_id.text

            # Ensure any unread results are handled before executing the new query
            if self.cursor.with_rows:
                self.cursor.fetchall()

            self.cursor.execute("SELECT company_name FROM company_details WHERE company_emailid = %s", (emailco,))
            det1 = self.cursor.fetchone()[0]

            # Ensure any unread results are handled before executing the new query
            if self.cursor.with_rows:
                self.cursor.fetchall()

            self.cursor.execute(
                "SELECT job_code, job_title, Last_Applying_Date FROM job_details WHERE company_name = %s", (det1,))
            row = self.cursor.fetchall()

            job_list = self.root.get_screen('jobdetailsshowtocompany').ids.job_viewtocompany_list
            job_list.clear_widgets()

            for i in row:
                item2 = ThreeLineListItem(text=i[1], secondary_text=str(i[0]), tertiary_text=str(i[2]))
                item2.bind(on_release=self.show_jobdetails_tocompany)
                job_list.add_widget(item2)

            #self.show_snackbar("Job list displayed successfully.")
        except Exception as e:
            print("Error:", e)
            self.show_snackbar("Error Occurred")

    def show_jobdetails_tocompany(self, item2):
        try:
            # Ensure any unread results are handled before executing the new query
            if self.cursor.with_rows:
                self.cursor.fetchall()

            self.cursor.execute("SELECT * FROM job_details WHERE job_code = %s", (item2.secondary_text,))
            row = self.cursor.fetchone()

            if row:
                screen_manager.current = "viewjob"
                job_details_screen = screen_manager.get_screen("viewjob")
                if job_details_screen:
                    job_details_screen.ids.job_id.text = str(row[0])
                    job_details_screen.ids.job_title.text = str(row[1])
                    job_details_screen.ids.company_id.text = str(row[4])
                    job_details_screen.ids.Providing_Date.text = str(row[5])
                    job_details_screen.ids.Last_date.text = str(row[6])
                    job_details_screen.ids.Salary.text = str(row[7])

            #self.show_snackbar("Job details displayed successfully.")
        except Exception as e:
            print("Error:", e)
            self.show_snackbar("Error Occurred")

    # def on_click_showshoortlistedstudentlist(self):
    #     screen_manager.current = "shortlistedstudents"
    #     det = screen_manager.get_screen('login')
    #     emailco = det.ids.email_id.text
    #     self.cursor.execute("select company_name from company_details where company_emailid = %s",(emailco,))
    #     det1 = self.cursor.fetchone()[0]
    #     #print(emailco)
    #     #print(det1)
    #     self.cursor.execute("select full_name,job_title,shortlisted_ornot from shortlisted_students where company_name = %s",(det1,))
    #     row = self.cursor.fetchall()
    #     job_list = self.root.get_screen('shortlistedstudents').ids.shortlistedstudent_list
    #     job_list.clear_widgets()
    #     for i in row:
    #         item2 = ThreeLineListItem(text = i[1], secondary_text = str(i[0]), tertiary_text = str(i[2]))
    #         #item2.bind(on_release= self.show_jobdetails_tocompany)
    #         #item1.bind(on_release= self.shw)
    #         job_list.add_widget(item2)

    def on_click_showshoortlistedstudentlisttopo(self):
        screen_manager.current = "shortlistedstudentstopo"
        # det = screen_manager.get_screen('login')
        # emailco = det.ids.email_id.text
        # self.cursor.execute("select company_name from company_details where company_emailid = %s",(emailco,))
        # det1 = self.cursor.fetchone()[0]
        # #print(emailco)
        # #print(det1)
        self.cursor.execute("select full_name,job_title,shortlisted_ornot from shortlisted_students")
        row = self.cursor.fetchall()
        job_list = self.root.get_screen('shortlistedstudentstopo').ids.shortlistedstudent_viewtopo_list
        job_list.clear_widgets()
        for i in row:
            item2 = ThreeLineListItem(text = i[1], secondary_text = str(i[0]), tertiary_text = str(i[2]))
            #item2.bind(on_release= self.show_jobdetails_tocompany)
            #item1.bind(on_release= self.shw)
            job_list.add_widget(item2)


    def on_click_showstudetailstopo(self):
        screen_manager.current = "stuviewpo"
        #det = screen_manager.get_screen('login')
        #emailco = det.ids.email_id.text
        #self.cursor.execute("select company_name from company_details where company_emailid = %s",(emailco,))
        #det1 = self.cursor.fetchone()[0]
        #print(emailco)
        #print(det1)
        self.cursor.execute("select user_id,full_name,department from signupstudent")
        row = self.cursor.fetchall()
        job_list = self.root.get_screen('stuviewpo').ids.student_viewtopo_list
        job_list.clear_widgets()
        for i in row:
            item4 = ThreeLineListItem(text = i[1], secondary_text = str(i[0]), tertiary_text = str(i[2]))
            item4.bind(on_release= self.show_studentdetails_topo)
            #item1.bind(on_release= self.shw)
            job_list.add_widget(item4)


    def show_studentdetails_topo(self,item4):
        #print(item1.secondary_text)
        self.cursor.execute("select * from signupstudent where user_id = %s",(item4.secondary_text,))

        row = self.cursor.fetchone()
        #print(row)
        screen_manager.current = "viewstudent"
        job_details_screen = screen_manager.get_screen("viewstudent")
        if job_details_screen:
            job_details_screen.ids.user_id.text=str(row[0])
            job_details_screen.ids.full_name.text=str(row[1])
            job_details_screen.ids.email_id.text=str(row[2])
            job_details_screen.ids.phone.text = str(row[3])
            job_details_screen.ids.addr.text = str(row[4])
            job_details_screen.ids.dept.text = str(row[5])
            job_details_screen.ids.dob.text = str(row[7])
            job_details_screen.ids.yearofjoining.text = str(row[8])

    def on_click_showcompany_list_topo(self):
        screen_manager.current = "companyiewpo"
        self.cursor.execute("select company_id,company_name from company_details")
        row = self.cursor.fetchall()
        job_list = self.root.get_screen('companyiewpo').ids.company_viewtopo_list
        job_list.clear_widgets()
        for i in row:
            item5 = TwoLineListItem(text = i[1], secondary_text = str(i[0]))
            item5.bind(on_release= self.show_companydetails_topo)
            #item1.bind(on_release= self.shw)
            job_list.add_widget(item5)


    def show_companydetails_topo(self,item5):
        #print(item1.secondary_text)
        self.cursor.execute("select * from company_details where company_id = %s",(item5.secondary_text,))

        row = self.cursor.fetchone()
        #print(row)
        screen_manager.current = "viewcompany"
        job_details_screen = screen_manager.get_screen("viewcompany")
        if job_details_screen:

            job_details_screen.ids.com_name.text=str(row[1])
            job_details_screen.ids.comid.text=str(row[0])
            job_details_screen.ids.email_id.text=str(row[2])
            job_details_screen.ids.phone.text = str(row[3])
            job_details_screen.ids.addr.text = str(row[4])


    def on_click_showjoblisttopo(self):
        screen_manager.current = "jobviewpo"
        self.cursor.execute("select job_code,job_title from job_details")
        row = self.cursor.fetchall()
        job_list = self.root.get_screen('jobviewpo').ids.job_viewtopo_list
        job_list.clear_widgets()
        for i in row:
            item8 = TwoLineListItem(text = i[1], secondary_text = str(i[0]))
            item8.bind(on_release= self.show_jobdetails_topo)
            #item1.bind(on_release= self.shw)
            job_list.add_widget(item8)


    def show_jobdetails_topo(self,item8):
        #print(item1.secondary_text)
        self.cursor.execute("select * from job_details where job_code = %s",(item8.secondary_text,))

        row = self.cursor.fetchone()
        #print(row)
        screen_manager.current = "viewjobtopo"
        job_details_screen = screen_manager.get_screen("viewjobtopo")
        if job_details_screen:
            job_details_screen.ids.job_id.text=str(row[0])
            job_details_screen.ids.job_title.text=str(row[1])
            job_details_screen.ids.company_id.text=str(row[4])
            job_details_screen.ids.company_name.text=str(row[3])
            job_details_screen.ids.Providing_Date.text = str(row[5])
            job_details_screen.ids.Last_date.text = str(row[6])
            job_details_screen.ids.Salary.text = str(row[7])


    def on_click_showappliedjoblisttopo(self):
        screen_manager.current = "showappliedjobstopo"
        #det = screen_manager.get_screen('login')
        #emailco = det.ids.email_id.text
        #self.cursor.execute("select company_name from company_details where company_emailid = %s",(emailco,))
        #det1 = self.cursor.fetchone()[0]
        #print(emailco)
        #print(det1)
        self.cursor.execute("select job_id,job_title,student_name from applied_jobs")
        row = self.cursor.fetchall()
        job_list = self.root.get_screen('showappliedjobstopo').ids.appliedjob_viewtopo_list
        job_list.clear_widgets()
        for i in row:
            item9 = ThreeLineListItem(text = i[1], secondary_text = str(i[0]),tertiary_text = str(2))
            item9.bind(on_release= self.show_appliedjobdetails_topo)
            #item1.bind(on_release= self.shw)
            job_list.add_widget(item9)


    def show_appliedjobdetails_topo(self,item9):
        #print(item1.secondary_text)
        self.cursor.execute("select * from applied_jobs where job_id = %s",(item9.secondary_text,))

        row = self.cursor.fetchone()
        #print(row)
        screen_manager.current = "viewappliedjobtopo"
        job_details_screen = screen_manager.get_screen("viewappliedjobtopo")
        if job_details_screen:
            job_details_screen.ids.job_id.text=str(row[0])
            job_details_screen.ids.job_title.text=str(row[1])
            job_details_screen.ids.company_id.text=str(row[2])
            job_details_screen.ids.Providing_Date.text = str(row[3])
            job_details_screen.ids.Last_date.text = str(row[4])
            job_details_screen.ids.Salary.text = str(row[7])
    def on_click_showstudentappliedjoblist(self):
        det = screen_manager.get_screen('login')
        eml = det.ids.email_id.text
        self.cursor.execute("select job_id, job_title, company_name from applied_jobs where email_id =%s",(eml,))
        #self.cursor.execute("select applied_jobs.job_title,applied_jobs.company_name,shortlisted_students.shortlisted_ornot FROM applied_jobs JOIN shortlisted_students ON applied_jobs.job_id = shortlisted_students.job_id")
        row = self.cursor.fetchall()
        job_list = self.root.get_screen('studentappliedjobs').ids.appliedjob_viewtostudent_list
        job_list.clear_widgets()
        for i in row:
            item = ThreeLineListItem(text = i[2], secondary_text = str(i[0]),tertiary_text = str(i[1]))
            #item.bind(on_release= self.show_applieddetails_ofjobtostudent)
            job_list.add_widget(item)
        screen_manager.current = "studentappliedjobs"
        screen_manager.transition.direction = "left"

    def open_file_manager(self):
        self.file_manager.show('/')  # Show the file manager starting from the root directory

    def show_dialog99(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                ),
            ],
        )
        dialog.open()

    def select_path(self, path):
        _, file_extension = os.path.splitext(path)
        valid_extensions = ['.jpg', '.jpeg', '.png']

        if file_extension.lower() not in valid_extensions:
            self.show_dialog99("Invalid file type", "The file selected is not of form jpg, jpeg, or png format. Please upload a file of that format.")
            return

        det = screen_manager.get_screen('login')
        eml = det.ids.email_id.text
        self.cursor.execute("SELECT user_id FROM signupstudent WHERE email_id = %s", (eml,))
        row = self.cursor.fetchone()
        if row is not None:
            row = row[0]
            print(row)
            with open(path, 'rb') as image_file:
                img = image_file.read()

            # Check if an image already exists for the user
            self.cursor.execute("SELECT COUNT(*) FROM student_image WHERE user_id = %s", (row,))
            count = self.cursor.fetchone()[0]

            if count > 0:
                # If image exists, update it
                self.cursor.execute("UPDATE student_image SET stu_image = %s WHERE user_id = %s", (img, row))
                self.show_snackbar("Profile updated successfully")
            else:
                # If no image exists, insert it
                self.cursor.execute("INSERT INTO student_image (user_id, stu_image) VALUES (%s, %s)", (row, img))
                self.show_snackbar("Profile uploaded successfully")

            self.database.commit()
            self.file_manager.close()
            print("Selected File:", path)
            det = screen_manager.get_screen('profile')
            det.ids.stu_image.source = path
        else:
            print("No user found with the specific email")

    def is_image_uploaded(self):
        det = screen_manager.get_screen('login')
        eml = det.ids.email_id.text
        self.cursor.execute("SELECT user_id FROM signupstudent WHERE email_id = %s", (eml,))
        row = self.cursor.fetchone()
        if row is not None:
            row = row[0]
            self.cursor.execute("SELECT stu_image FROM student_image WHERE user_id = %s", (row,))
            image_data = self.cursor.fetchone()
            return image_data is not None and image_data[0] is not None
        return False
    def check_and_update_button_state(self):
        det = screen_manager.get_screen('profile')
        button = det.ids.upload_button
        if self.is_image_uploaded():
            button.disabled = True
        else:
            button.disabled = False
    def exit_file_manager(self, *args):
        self.file_manager.close()
    def exit_file_manager1(self, *args):
        self.file_manager1.close()
    def exit_file_manager2(self, *args):
        self.file_manager2.close()
    def exit_file_manager3(self, *args):
        self.file_manager3.close()
    def shw_image(self):
        det = screen_manager.get_screen('login')
        eml = det.ids.email_id.text
        self.cursor.execute("SELECT user_id FROM signupstudent WHERE email_id=%s", (eml,))
        row = self.cursor.fetchone()

        if row is not None:
            user_id = row[0]
            print(user_id)
            self.cursor.execute("SELECT stu_image FROM student_image WHERE user_id = %s", (user_id,))
            row = self.cursor.fetchone()
            if row:
                image_data = row[0]
                image = Image.open(BytesIO(image_data))

                # Convert image to RGB if it's in RGBA mode
                if image.mode == 'RGBA':
                    image = image.convert('RGB')

                image.save("temp_image.jpg")
                screen_manager.current = 'profile'
                det = screen_manager.get_screen('profile')
                det.ids.stu_image.source = 'temp_image.jpg'
            else:
                print("No image found for the specified user")
        else:
            print("No user found with the specified email")

    def file_manager_open_comp(self):
        self.file_manager1 = MDFileManager(
            exit_manager=self.exit_manager2,
            select_path=self.select_path1,
            preview=True,
        )
        self.file_manager1.show('/')

    def select_path1(self, path):
        self.upload_comp_logo(path)
        self.set_comp_profile_image()
        # self.show_popup1("Success", "Profile photo uploaded successfully.")
        self.exit_manager2()

    def exit_manager2(self, *args):
        self.file_manager1.close()

    def show_popup3(self, title, message):
        Snackbar(text=f"{title}: {message}").open()

    def upload_comp_logo(self, image_path):
        try:
            _, file_extension = os.path.splitext(image_path)
            valid_extensions = ['.jpg', '.jpeg', '.png']

            if file_extension.lower() not in valid_extensions:
                self.show_dialog99("Invalid file type",
                                   "The file selected is not of form jpg, jpeg, or png format. Please upload a file of that format.")
                return
            #Convert image to binary data
            with open(image_path, 'rb') as file:
                binary_data = file.read()

            det = screen_manager.get_screen("login")
            email = det.ids.email_id.text
            self.cursor.execute("select company_id from company_details where company_emailid=%s", (email,))
            row = self.cursor.fetchone()
            if row:
                comid = row[0]

                # Check if the student profile already exists
                self.cursor.execute("SELECT comp_image FROM company_logo WHERE company_id = %s", (comid,))
                existing_profile = self.cursor.fetchone()
                if existing_profile:
                    print("Updating existing profile")  # Debugging print
                    # Update existing record
                    self.cursor.execute("UPDATE company_logo SET comp_image = %s WHERE company_id = %s",
                                   (binary_data, comid))
                    self.database.commit()
                    self.show_popup3("Success", "Profile photo updated successfully.")
                else:
                    print("Inserting new profile")  # Debugging print
                    # Insert new record
                    self.cursor.execute("INSERT INTO company_logo (company_id, comp_image) VALUES (%s, %s)",
                                   (comid, binary_data))
                    self.database.commit()
                    self.show_popup3("Success", "Profile photo uploaded successfully.")
            else:
                print("User not found")  # Debugging print
                self.show_popup3("Error", "User not found.")
        except Exception as e:
            print(f"An error occurred: {e}")  # Debugging print
            self.show_popup3("Error", f"An error occurred: {e}")

    def set_comp_profile_image(self):
        try:
            det = screen_manager.get_screen("login")
            email = det.ids.email_id.text
            self.cursor.execute("select company_id from company_details where company_emailid=%s", (email,))
            row1 = self.cursor.fetchone()
            if row1:
                comp_id = row1[0]
                self.cursor.execute("SELECT comp_image FROM company_logo WHERE company_id = %s", (comp_id,))
                row = self.cursor.fetchone()  # Use fetchone() to get a single record
                if row:
                    image_data = row[0]
                    profile_screen = screen_manager.get_screen("companyprofile")
                    profile_screen.ids.comp_image.texture = self.image_from_binary(image_data)
        except Exception as e:
            self.show_popup3("Error", f"An error occurred while setting the profile image: {e}")

    def image_from_binary(self, binary_data):
        try:
            data = BytesIO(binary_data)
            img = CoreImage(data, ext="png").texture
            return img
        except Exception as e:
            self.show_popup3("Error", f"An error occurred while converting binary data to image: {e}")
            return None

    # def open_file_manager1(self):
    #     self.file_manager1.show('/')  # Show the file manager starting from the root directory
    # def select_path1(self, path):
    #     _, file_extension = os.path.splitext(path)
    #     valid_extensions = ['.jpg', '.jpeg', '.png']
    #
    #     if file_extension.lower() not in valid_extensions:
    #         self.show_dialog99("Invalid file type", "The file selected is not of form jpg, jpeg, or png format. Please upload a file of that format.")
    #         return
    #
    #     det = screen_manager.get_screen('login')
    #     eml = det.ids.email_id.text
    #     self.cursor.execute("select company_id from company_details where company_emailid=%s", (eml,))
    #     row = self.cursor.fetchone()
    #     if row is not None:
    #         row = row[0]
    #         print(row)
    #         with open(path, 'rb') as image_file:
    #             img = image_file.read()
    #
    #         # Check if an image already exists for the user
    #         self.cursor.execute("SELECT COUNT(*) FROM student_image WHERE user_id = %s", (row,))
    #         count = self.cursor.fetchone()[0]
    #
    #         if count > 0:
    #             # If image exists, update it
    #             self.cursor.execute("UPDATE company_logo SET comp_image = %s WHERE company_id = %s", (img, row))
    #             self.show_snackbar("Profile updated successfully")
    #         else:
    #             # If no image exists, insert it
    #             self.cursor.execute("INSERT INTO company_logo (company_id, comp_image) VALUES (%s, %s)", (row, img))
    #             self.show_snackbar("Profile uploaded successfully")
    #
    #         self.database.commit()
    #         self.file_manager1.close()
    #         print("Selected File:", path)
    #         det = screen_manager.get_screen('companyprofile')
    #         det.ids.comp_image.source = path
    #     else:
    #         print("No user found with the specific email")
    # def is_image_uploaded1(self):
    #     det = screen_manager.get_screen('login')
    #     eml = det.ids.email_id.text
    #     self.cursor.execute("SELECT company_id FROM company_details WHERE company_emailid = %s", (eml,))
    #     row = self.cursor.fetchone()
    #     if row is not None:
    #         row = row[0]
    #         self.cursor.execute("SELECT comp_image FROM company_logo WHERE company_id = %s", (row,))
    #         image_data = self.cursor.fetchone()
    #         return image_data is not None and image_data[0] is not None
    #     return False
    # def check_and_update_button_state1(self):
    #     det = screen_manager.get_screen('companyprofile')
    #     button = det.ids.upload_button1
    #     if self.is_image_uploaded1():
    #         button.disabled = True
    #     else:
    #         button.disabled = False
    # def shw_image1(self):
    #     det = screen_manager.get_screen('companyprofile')
    #     eml = det.ids.my_label.text
    #     self.cursor.execute("select company_id from company_details where company_emailid=%s",(eml,))
    #     row = self.cursor.fetchone()[0]
    #
    #     if row is not None:
    #         print(row)
    #         self.cursor.execute("SELECT comp_image FROM company_logo WHERE company_id = %s",(row,))
    #         result = self.cursor.fetchone()
    #         print(result)
    #
    #         if result is not None:
    #             image_data = result[0]
    #             image = Image.open(BytesIO(image_data))
    #             image.save("companylogo.jpg")
    #             screen_manager.current = 'companyprofile'
    #             det = screen_manager.get_screen('companyprofile')
    #             det.ids.comp_image.source = 'companylogo.jpg'
    #         else:
    #             print("No image found")
    #     else:
    #         print("No Company")
    def open_file_manager2(self):
        self.file_manager2.show('/')  # Show the file manager starting from the root directory

    def select_path2(self, path):
        det = screen_manager.get_screen('login')
        bml = det.ids.email_id.text
        print(bml)
        self.cursor.execute("select PO_ID from placementofficer where email_id=%s",(bml,))
        row = self.cursor.fetchone()
        print(row)
        try:
            if row is not None:
                row = row[0]
                print(row)
                bu = None
                self.cursor.execute("INSERT INTO placementofficer_image (PO_ID, po_image) VALUES (%s, %s)", (row, bu))

                #self.cursor = self.database.cursor()
                # Handle the selected image file path here
                self.file_manager2.close()
                print("Selected File:", path)
                det = screen_manager.get_screen('poprofile')
                det.ids.po_image_preview.source = path
                with open(path, 'rb') as image_file:
                    img1 = image_file.read()

                    #sql = "UPDATE  student_image SET student_image = %s WHERE id = %s"
                self.cursor.execute("UPDATE  placementofficer_image SET po_image = %s WHERE PO_ID = %s",(img1,row,))
                self.database.commit()

        except Exception as e:
            print(e)
    def shw_image_po(self):
        det = screen_manager.get_screen('login')
        eml = det.ids.email_id.text
        self.cursor.execute("select PO_ID from placementofficer where email_id=%s",(eml,))
        row = self.cursor.fetchone()[0]
        print(row)
        if row is not None:
            print(row)
            self.cursor.execute("SELECT po_image FROM placementofficer_image WHERE PO_ID = %s",(row,))
            result = self.cursor.fetchone()
            print(result)

            if result is not None:
                image_data = result[0]
                image = Image.open(BytesIO(image_data))
                image.save("placementimage.jpg")
                screen_manager.current = 'poprofile'
                det = screen_manager.get_screen('poprofile')
                det.ids.po_image.source = 'placementimage.jpg'
            else:
                print("No image found")
        else:
            print("No Company")
    def open_file_manager3(self):
        self.file_manager3.show('/')  # Show the file manager starting from the root directory

    def select_path3(self, path):
        det = screen_manager.get_screen('login')
        bml = det.ids.email_id.text
        print(bml)
        self.cursor.execute("select user_id from signupadmin where email_id=%s",(bml,))
        row = self.cursor.fetchone()
        print(row)
        try:
            if row is not None:
                row = row[0]
                print(row)
                bu = None
                self.cursor.execute("INSERT INTO admin_image (user_id, admin_image) VALUES (%s, %s)", (row, bu))

                #self.cursor = self.database.cursor()
                # Handle the selected image file path here
                self.file_manager3.close()
                print("Selected File:", path)
                det = screen_manager.get_screen('adminprofile')
                det.ids.admin_image_preview.source = path
                with open(path, 'rb') as image_file:
                    img1 = image_file.read()

                    #sql = "UPDATE  student_image SET student_image = %s WHERE id = %s"
                self.cursor.execute("UPDATE  admin_image SET admin_image = %s WHERE user_id = %s",(img1,row,))
                self.database.commit()

        except Exception as e:
            print(e)

    def shw_image3(self):
        det = screen_manager.get_screen('login')
        eml = det.ids.email_id.text
        self.cursor.execute("select user_id from signupadmin where email_id=%s",(eml,))
        row = self.cursor.fetchone()[0]
        print(row)
        if row is not None:
            print(row)
            self.cursor.execute("SELECT admin_image FROM admin_image WHERE user_id = %s",(row,))
            result = self.cursor.fetchone()
            print(result)

            if result is not None:
                image_data = result[0]
                image = Image.open(BytesIO(image_data))
                image.save("adminimage.jpg")
                screen_manager.current = 'adminprofile'
                det = screen_manager.get_screen('adminprofile')
                det.ids.admin_image.source = 'adminimage.jpg'
            else:
                print("No image found")
        else:
            print("No Company")


    def shw_image2(self):
        det = screen_manager.get_screen('companyseesstudentapplication')
        eml = det.ids.studentemailidviewtocompany.text
        self.cursor.execute("SELECT user_id FROM signupstudent WHERE email_id=%s", (eml,))
        row = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT stu_image FROM student_image WHERE user_id = %s", (row,))
        row = self.cursor.fetchone()
        if row:
            image_data = row[0]
            image = Image.open(BytesIO(image_data))
            image.save("studentimage.jpg")
            screen_manager.current = 'studentdetailsthathaveappliedjobs'
            det = screen_manager.get_screen('studentdetailsthathaveappliedjobs')
            det.ids.showstudentimagetocompany.source = 'studentimage.jpg'
    def showdetailsofcompanytojobproviding(self,):
        screen_manager.current='addjob'
        screen_manager.transition.direction = "right"
        det = screen_manager.get_screen('login')
        email = det.ids.email_id.text
        self.cursor.execute("select * from company_details where company_emailid = %s ",(email,))
        row=self.cursor.fetchone()
        screen_manager.current = "addjob"
        dts_scr = screen_manager.get_screen("addjob")
        if dts_scr:
            dts_scr.ids.companyidprovide.text = str(row[0])
            dts_scr.ids.companyidprovide.disabled = True
            dts_scr.ids.companynameprovideid.text = str(row[1])
            dts_scr.ids.companynameprovideid.disabled = True
        self.database.commit()

    def selectdirectvalues(self):
        screen_manager.current = 'applyjob'
        det = screen_manager.get_screen('jobview')
        jobcode = det.ids.jobcodeview.text
        jobtitle = det.ids.jobtitleview.text
        compname = det.ids.companynameview.text
        det1 = screen_manager.get_screen("login")
        email = det1.ids.email_id.text

        self.cursor.execute("select * from signupstudent where email_id = %s", (email,))
        row = self.cursor.fetchone()

        if row is None:
            print("No matching student found for email:", email)
            return

        print("Query result:", row)  # Debug print to check the structure of `row`

        screen_manager.current = "applyjob"
        dts_scr = screen_manager.get_screen("applyjob")
        if dts_scr:
            dts_scr.ids.job_code.text = jobcode
            dts_scr.ids.job_code.disabled = True
            dts_scr.ids.job_title.text = jobtitle
            dts_scr.ids.job_title.disabled = True
            dts_scr.ids.com_name.text = compname
            dts_scr.ids.com_name.disabled = True

            if len(row) >= 4:
                dts_scr.ids.student_name.text = str(row[1])
                dts_scr.ids.email_id.text = str(row[2])
                dts_scr.ids.email_id.disabled = True
                dts_scr.ids.phone_no.text = str(row[3])
            else:
                print("Row does not have enough columns:", row)  # Debug print to check the row structure

        self.database.commit()

    class ProfileCard(FakeRectangularElevationBehavior, MDFloatLayout):
        pass
    class ProfileCard1(FakeRectangularElevationBehavior, MDFloatLayout):
        pass
    class ProfileCard2(FakeRectangularElevationBehavior, MDFloatLayout):
        pass
    class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
        pass
    class SearchBar(FakeRectangularElevationBehavior, MDFloatLayout):
        pass
    class CircularProgressBar(AnchorLayout):
        bar_color = ListProperty([1,0,100/255])
        bar_width = NumericProperty(10)

    def dizabule(self,):
        dts_scr = screen_manager.get_screen("bekkar2")
        dts_scr.ids.phone_no.disabled = True
        dts_scr.ids.address.disabled = True
        dts_scr.ids.department.disabled = True
        dts_scr.ids.dob.disabled = True
        dts_scr.ids.password.disabled = True
    def dizabule1(self,):
        dts_scr = screen_manager.get_screen("signupadmin")
        dts_scr.ids.phone_no.disabled = True
        dts_scr.ids.address.disabled = True
        dts_scr.ids.password.disabled = True
    def dizabule2(self,):
        dts_scr = screen_manager.get_screen("signupother")
        dts_scr.ids.phone_no.disabled = True
        dts_scr.ids.address.disabled = True
        dts_scr.ids.department.disabled = True
        dts_scr.ids.password.disabled = True
    def dizabule3(self,):
        dts_scr = screen_manager.get_screen("signupfacalty")
        dts_scr.ids.phone_no.disabled = True
        dts_scr.ids.address.disabled = True
        dts_scr.ids.password.disabled = True

    def send_email(self, email, password, recipient, subject, message):
        try:
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

        except Exception as e:
            print(e)

    def send_otp(self, *args):
        try:
            det = screen_manager.get_screen('bekkar2')
            recipient = det.ids.email_id.text

            self.email = "test123deb@gmail.com"  # Predefined sender email
            self.password = "vntyvnwxunxzsobx"  # Predefined sender password

            self.otp = str(random.randint(100000, 999999))
            #print("OTP:", self.otp)

            self.send_email(
                self.email,
                self.password,
                recipient,
                "OTP Verification",
                f"Your OTP is: {self.otp}",
            )

            self.show_otp_dialog()

        except Exception as e:
            print(e)

    def show_otp_dialog(self):
        self.dialog = MDDialog(
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
                MDRectangleFlatButton(text="Cancel", on_release=self.close_dialog),
                MDRectangleFlatButton(text="Verify", on_release=self.verify_otp),
            ],
        )

        content = self.dialog.content_cls

        # OTP verification label
        label = MDLabel(text="OTP Verification",font_name = "MPoppins",pos_hint = {"center_x":0.668})
        content.add_widget(label)

        # Text field for OTP input
        self.otp_text = MDTextField(hint_text="Enter OTP",
                                    size_hint = (None,None),
                                    size=(200, 48),
                                    mode = "rectangle")
        content.add_widget(self.otp_text)

        # Timer countdown label
        self.timer_label = MDLabel(
            text=f"Time Left: {self.timer} seconds",
            font_size = "10sp",
            halign="center",
            theme_text_color="Secondary",
        )
        content.add_widget(self.timer_label)

        self.dialog.open()

        Clock.schedule_interval(self.update_timer, 1)
    def on_otp_input(self, instance, value):
        self.otp_input = value

    def close_dialog1(self, *args):
        self.dialog.dismiss()

    def verify_otp(self, *args):
        if self.otp_text.text == self.otp:
            self.dialog.dismiss()
            self.verification_status = "OTP Verified!"
            self.show_success_dialog()
            if self.verification_status == "OTP Verified!":
                dts_scr = screen_manager.get_screen("bekkar2")
                dts_scr.ids.phone_no.disabled = False
                dts_scr.ids.address.disabled =False
                dts_scr.ids.department.disabled = False
                dts_scr.ids.dob.disabled = False
                dts_scr.ids.password.disabled =False

        else:
            self.dialog.dismiss()
            self.show_failure_dialog()

    def show_success_dialog(self):
        self.success_dialog = MDDialog(
            title="Success",
            text="OTP Verified!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_success_dialog)],
        )
        self.success_dialog.open()

    def close_success_dialog(self, *args):
        self.success_dialog.dismiss()

    def show_failure_dialog(self):
        self.failure_dialog = MDDialog(
            title="Failure",
            text="Invalid OTP!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_failure_dialog)],
        )
        self.failure_dialog.open()

    def close_failure_dialog(self, *args):
        self.failure_dialog.dismiss()

    def update_timer(self, dt):
        self.timer -= 1
        if self.timer == 0:
            Clock.unschedule(self.update_timer)
            self.show_otp_expired_dialog()
        else:
            self.timer_label.text = f"Time Left: {self.timer} seconds"

    def show_otp_expired_dialog(self):
        self.otp_expired_dialog = MDDialog(
            title="OTP Expired",
            text="The OTP has expired.",
            buttons=[
                MDRectangleFlatButton(
                    text="Resend OTP", on_release=self.resend_otp_dialog
                ),
                MDRectangleFlatButton(text="Cancel", on_release=self.close_otp_expired_dialog),
            ],
        )
        self.otp_expired_dialog.open()

    def close_otp_expired_dialog(self, *args):
        self.otp_expired_dialog.dismiss()

    def resend_otp_dialog(self, *args):
        self.dialog.dismiss()

        self.send_otp()

    def on_stop(self):
        Clock.unschedule(self.update_timer)

    def send_otp1(self, *args):
        try:
            det = screen_manager.get_screen('signupadmin')
            recipient = det.ids.email_id.text

            self.email = "test123deb@gmail.com"  # Predefined sender email
            self.password = "vntyvnwxunxzsobx"  # Predefined sender password

            self.otp = str(random.randint(100000, 999999))
            #print("OTP:", self.otp)

            self.send_email(
                self.email,
                self.password,
                recipient,
                "OTP Verification",
                f"Your OTP is: {self.otp}",
            )

            self.show_otp_dialog1()

        except Exception as e:
            print(e)

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
        label = MDLabel(text="OTP Verification",font_name = "MPoppins",pos_hint = {"center_x":0.668})
        content.add_widget(label)

        # Text field for OTP input
        self.otp_text1 = MDTextField(hint_text="Enter OTP",
                                    size_hint = (None,None),
                                    size=(200, 48),
                                    mode = "rectangle")
        content.add_widget(self.otp_text1)

        # Timer countdown label
        self.timer_label1 = MDLabel(
            text=f"Time Left: {self.timer} seconds",
            font_size = "10sp",
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
                dts_scr = screen_manager.get_screen("signupadmin")
                dts_scr.ids.phone_no.disabled = False
                dts_scr.ids.address.disabled =False
                dts_scr.ids.password.disabled =False

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

    def send_otp2(self, *args):
        try:
            det = screen_manager.get_screen('signupother')
            recipient = det.ids.email_id.text

            self.email = "test123deb@gmail.com"  # Predefined sender email
            self.password = "vntyvnwxunxzsobx"  # Predefined sender password

            self.otp = str(random.randint(100000, 999999))
            #print("OTP:", self.otp)

            self.send_email(
                self.email,
                self.password,
                recipient,
                "OTP Verification",
                f"Your OTP is: {self.otp}",
            )

            self.show_otp_dialog2()

        except Exception as e:
            print(e)

    def show_otp_dialog2(self):
        self.dialog2 = MDDialog(
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
                MDRectangleFlatButton(text="Cancel", on_release=self.close_dialog3),
                MDRectangleFlatButton(text="Verify", on_release=self.verify_otp2),
            ],
        )

        content = self.dialog2.content_cls

        # OTP verification label
        label = MDLabel(text="OTP Verification",font_name = "MPoppins",pos_hint = {"center_x":0.668})
        content.add_widget(label)

        # Text field for OTP input
        self.otp_text2 = MDTextField(hint_text="Enter OTP",
                                    size_hint = (None,None),
                                    size=(200, 48),
                                    mode = "rectangle")
        content.add_widget(self.otp_text2)

        # Timer countdown label
        self.timer_label2 = MDLabel(
            text=f"Time Left: {self.timer} seconds",
            font_size = "10sp",
            halign="center",
            theme_text_color="Secondary",
        )
        content.add_widget(self.timer_label2)

        self.dialog2.open()

        Clock.schedule_interval(self.update_timer2, 1)
    def on_otp_input2(self, instance, value):
        self.otp_input2 = value

    def close_dialog3(self, *args):
        self.dialog2.dismiss()

    def verify_otp2(self, *args):
        if self.otp_text2.text == self.otp:
            self.dialog2.dismiss()
            self.verification_status = "OTP Verified!"
            self.show_success_dialog2()
            if self.verification_status == "OTP Verified!":
                dts_scr = screen_manager.get_screen("signupother")
                dts_scr.ids.phone_no.disabled = False
                dts_scr.ids.department.disabled = False
                dts_scr.ids.address.disabled =False
                dts_scr.ids.password.disabled =False

        else:
            self.dialog2.dismiss()
            self.show_failure_dialog2()

    def show_success_dialog2(self):
        self.success_dialog2= MDDialog(
            title="Success",
            text="OTP Verified!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_success_dialog2)],
        )
        self.success_dialog2.open()

    def close_success_dialog2(self, *args):
        self.success_dialog2.dismiss()

    def show_failure_dialog2(self):
        self.failure_dialog2 = MDDialog(
            title="Failure",
            text="Invalid OTP!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_failure_dialog2)],
        )
        self.failure_dialog2.open()

    def close_failure_dialog2(self, *args):
        self.failure_dialog2.dismiss()

    def update_timer2(self, dt):
        self.timer -= 1
        if self.timer == 0:
            Clock.unschedule(self.update_timer1)
            self.show_otp_expired_dialog2()
        else:
            self.timer_label2.text = f"Time Left: {self.timer} seconds"

    def show_otp_expired_dialog2(self):
        self.otp_expired_dialog2 = MDDialog(
            title="OTP Expired",
            text="The OTP has expired.",
            buttons=[
                MDRectangleFlatButton(
                    text="Resend OTP", on_release=self.resend_otp_dialog1
                ),
                MDRectangleFlatButton(text="Cancel", on_release=self.close_otp_expired_dialog2),
            ],
        )
        self.otp_expired_dialog2.open()

    def close_otp_expired_dialog2(self, *args):
        self.otp_expired_dialog2.dismiss()

    def resend_otp_dialog2(self, *args):
        self.dialog2.dismiss()

        self.send_otp2()

    def on_stop2(self):
        Clock.unschedule(self.update_timer2)

    def send_otp3(self, *args):
        try:
            det = screen_manager.get_screen('signupfacalty')
            recipient = det.ids.email_id.text

            self.email = "test123deb@gmail.com"  # Predefined sender email
            self.password = "vntyvnwxunxzsobx"  # Predefined sender password

            self.otp = str(random.randint(100000, 999999))
            #print("OTP:", self.otp)

            self.send_email(
                self.email,
                self.password,
                recipient,
                "OTP Verification",
                f"Your OTP is: {self.otp}",
            )

            self.show_otp_dialog3()

        except Exception as e:
            print(e)

    def show_otp_dialog3(self):
        self.dialog3 = MDDialog(
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
                MDRectangleFlatButton(text="Cancel", on_release=self.close_dialog4),
                MDRectangleFlatButton(text="Verify", on_release=self.verify_otp3),
            ],
        )

        content = self.dialog3.content_cls

        # OTP verification label
        label = MDLabel(text="OTP Verification",font_name = "MPoppins",pos_hint = {"center_x":0.668})
        content.add_widget(label)

        # Text field for OTP input
        self.otp_text3 = MDTextField(hint_text="Enter OTP",
                                    size_hint = (None,None),
                                    size=(200, 48),
                                    mode = "rectangle")
        content.add_widget(self.otp_text3)

        # Timer countdown label
        self.timer_label3 = MDLabel(
            text=f"Time Left: {self.timer} seconds",
            font_size = "10sp",
            halign="center",
            theme_text_color="Secondary",
        )
        content.add_widget(self.timer_label3)

        self.dialog3.open()

        Clock.schedule_interval(self.update_timer3, 1)
    def on_otp_input3(self, instance, value):
        self.otp_input3 = value

    def close_dialog4(self, *args):
        self.dialog3.dismiss()

    def verify_otp3(self, *args):
        if self.otp_text3.text == self.otp:
            self.dialog3.dismiss()
            self.verification_status = "OTP Verified!"
            self.show_success_dialog3()
            if self.verification_status == "OTP Verified!":
                dts_scr = screen_manager.get_screen("signupfacalty")
                dts_scr.ids.phone_no.disabled = False
                dts_scr.ids.address.disabled =False
                dts_scr.ids.password.disabled =False

        else:
            self.dialog3.dismiss()
            self.show_failure_dialog3()

    def show_success_dialog3(self):
        self.success_dialog3 = MDDialog(
            title="Success",
            text="OTP Verified!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_success_dialog3)],
        )
        self.success_dialog3.open()

    def close_success_dialog3(self, *args):
        self.success_dialog3.dismiss()

    def show_failure_dialog3(self):
        self.failure_dialog3 = MDDialog(
            title="Failure",
            text="Invalid OTP!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_failure_dialog3)],
        )
        self.failure_dialog3.open()

    def close_failure_dialog3(self, *args):
        self.failure_dialog3.dismiss()

    def update_timer3(self, dt):
        self.timer -= 1
        if self.timer == 0:
            Clock.unschedule(self.update_timer3)
            self.show_otp_expired_dialog3()
        else:
            self.timer_label3.text = f"Time Left: {self.timer} seconds"

    def show_otp_expired_dialog3(self):
        self.otp_expired_dialog3 = MDDialog(
            title="OTP Expired",
            text="The OTP has expired.",
            buttons=[
                MDRectangleFlatButton(
                    text="Resend OTP", on_release=self.resend_otp_dialog3
                ),
                MDRectangleFlatButton(text="Cancel", on_release=self.close_otp_expired_dialog3),
            ],
        )
        self.otp_expired_dialog3.open()

    def close_otp_expired_dialog3(self, *args):
        self.otp_expired_dialog3.dismiss()

    def resend_otp_dialog3(self, *args):
        self.dialog3.dismiss()

        self.send_otp3()

    def on_stop3(self):
        Clock.unschedule(self.update_timer3)

    def file_manager_open(self):
        self.file_manager5.show('/')  # No argument required

    def exit_manager5(self, *args):
        self.file_manager5.close()

    def select_path5(self, path):
        self.file_path = path
        self.exit_manager5()
        self.upload_pdf()

    def upload_pdf(self):
        det = screen_manager.get_screen('profile')
        email = det.ids.my_label.text
        self.cursor.execute("select full_name, email_id from signupstudent where email_id = %s", (email,))
        row = self.cursor.fetchone()
        uid = row[1]
        name = row[0]
        name = row[0]
        print(uid, name)

        if not self.file_path:
            self.show_snackbar("No file selected")
            return

        _, file_extension = os.path.splitext(self.file_path)
        if file_extension.lower() != '.pdf':
            self.show_dialog99("Invalid file type", "The file selected is not of PDF format. Please upload a file of that format.")
            return

        max_size = 10 * 1024 * 1024  # Maximum file size in bytes (10MB)
        file_size = os.path.getsize(self.file_path)
        if file_size > max_size:
            self.show_snackbar("File size exceeds the limit")
            return

        # Read the PDF file content
        with open(self.file_path, "rb") as file:
            pdf_data = file.read()

        try:
            database = mysql.connector.connect(user="root", host="localhost",
                                               password="Kushal@2003", database="karimganjcollege")
            cursor = database.cursor()

            # Check if the resume already exists for the user
            cursor.execute("SELECT COUNT(*) FROM stu_resume WHERE uid = %s", (uid,))
            count = cursor.fetchone()[0]

            if count > 0:
                # Update the existing resume
                cursor.execute("UPDATE stu_resume SET pdf_data = %s WHERE uid = %s",
                               (pdf_data, uid))
                self.show_snackbar("PDF updated successfully")
            else:
                # Insert a new resume
                cursor.execute("INSERT INTO stu_resume (uid, name, pdf_data) VALUES (%s, %s, %s)",
                               (uid, name, pdf_data))
                self.show_snackbar("PDF uploaded successfully")

            database.commit()
            cursor.close()
            database.close()

            # self.refresh_pdf_list()  # Refresh the PDF list
        except mysql.connector.Error as error:
            self.show_snackbar(f"Error uploading PDF: {error}")
            print(f"{error}")

    def removestu(self):
        det = screen_manager.get_screen('viewstudent')
        email = det.ids.email_id.text

        try:
            self.cursor.execute("DELETE FROM signupstudent WHERE email_id=%s", (email,))
            self.database.commit()
            self.show_snackbar("Student removed successfully")
            screen_manager.current = "pohome"

        except mysql.connector.Error as err:
            # Handle the exception and show an error snackbar
            error_message = f"Error: {err}"
            self.show_snackbar("Something went wrong")
    def removecompany(self):
        det = screen_manager.get_screen('viewcompany')
        email = det.ids.email_id.text

        try:
            self.cursor.execute("DELETE FROM company_details WHERE company_emailid=%s", (email,))
            self.database.commit()
            self.show_snackbar("Company removed successfully")
            screen_manager.current = "pohome"

        except mysql.connector.Error as err:
            # Handle the exception and show an error snackbar
            error_message = f"Error: {err}"
            self.show_snackbar("Something went wrong")

    def removejobbypo(self):
        det = screen_manager.get_screen('viewjobtopo')
        jobcode = det.ids.job_id.text

        try:
            self.cursor.execute("DELETE FROM job_details WHERE job_code=%s", (jobcode,))
            self.database.commit()
            self.show_snackbar("Job removed successfully")
            screen_manager.current = "pohome"

        except mysql.connector.Error as err:
            # Handle the exception and show an error snackbar
            error_message = f"Error: {err}"
            self.show_snackbar("Something went wrong")

    # def addnotice(self,noticeid,noticedate,notice):
    #     try:
    #         self.cursor.execute(
    #             f"INSERT INTO notice (noticeid, noticedate, notice) VALUES ('{noticeid.text}', '{noticedate.text}', '{notice.text}')"
    #         )
    #         self.database.commit()
    #         self.show_snackbar("Notice added successfully")
    #         det = screen_manager.get_screen("addnotice")
    #         det.ids.noticeid.text = ""
    #         det.ids.noticedate.text = ""
    #         det.ids.notice.text = ""
    #     except Exception as e:
    #         self.database.rollback()  # Rollback the transaction if an error occurs
    #         self.show_snackbar("Error: " + str(e))
    #         print("Error: " + str(e))
        # self.cursor.execute(
        #     f"INSERT INTO notice (notice_id, notice_date, notice_content) VALUES ('{noticeid.text}', '{noticedate.text}', '{notice.text}'"
        #              )
        # self.database.commit()
        # self.show_snackbar("Successfull")
    # def display_notice(self,):
    #     #screen_manager.current='companyhome'
    #     self.cursor.execute("select notice from notice where noticeid = 'n2'")
    #     row = self.cursor.fetchone()[0]
    #     det = screen_manager.get_screen("companyhome")
    #     det.ids.noticefrompo.text = str(row)
    #     screen_manager.current = 'companyhome'

        #screen_manager.current = 'companyhome'
    def send_otpforforgetpassword(self, *args):
        try:
            det = screen_manager.get_screen('forgetpassword')
            recipient = det.ids.email_id.text

            self.email = "test123deb@gmail.com"  # Predefined sender email
            self.password = "vntyvnwxunxzsobx"  # Predefined sender password

            self.otp = str(random.randint(100000, 999999))
            #print("OTP:", self.otp)

            self.send_email(
                self.email,
                self.password,
                recipient,
                "OTP Verification",
                f"Your OTP is: {self.otp}",
            )

            self.show_otp_dialog7()

        except Exception as e:
            print(e)

    def show_otp_dialog7(self):
        self.dialog7 = MDDialog(
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
                MDRectangleFlatButton(text="Cancel", on_release=self.close_dialog7),
                MDRectangleFlatButton(text="Verify", on_release=self.verify_otp7),
            ],
        )

        content = self.dialog7.content_cls

        # OTP verification label
        label = MDLabel(text="OTP Verification",font_name = "MPoppins",pos_hint = {"center_x":0.668})
        content.add_widget(label)

        # Text field for OTP input
        self.otp_text7 = MDTextField(hint_text="Enter OTP",
                                    size_hint = (None,None),
                                    size=(200, 48),
                                    mode = "rectangle")
        content.add_widget(self.otp_text7)

        # Timer countdown label
        self.timer_label7 = MDLabel(
            text=f"Time Left: {self.timer} seconds",
            font_size = "10sp",
            halign="center",
            theme_text_color="Secondary",
        )
        content.add_widget(self.timer_label7)

        self.dialog7.open()

        Clock.schedule_interval(self.update_timer7, 1)
    def on_otp_input7(self, instance, value):
        self.otp_input7 = value

    def close_dialog7(self, *args):
        self.dialog7.dismiss()

    def verify_otp7(self, *args):
        if self.otp_text7.text == self.otp:
            self.dialog7.dismiss()
            self.verification_status = "OTP Verified!"
            self.show_success_dialog7()
            if self.verification_status == "OTP Verified!":
                screen_manager.current = "updatepassword"

        else:
            self.dialog7.dismiss()
            self.show_failure_dialog7()

    def show_success_dialog7(self):
        self.success_dialog7 = MDDialog(
            title="Success",
            text="OTP Verified!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_success_dialog7)],
        )
        self.success_dialog7.open()

    def close_success_dialog7(self, *args):
        self.success_dialog7.dismiss()

    def show_failure_dialog7(self):
        self.failure_dialog7 = MDDialog(
            title="Failure",
            text="Invalid OTP!",
            buttons=[MDRectangleFlatButton(text="OK", on_release=self.close_failure_dialog7)],
        )
        self.failure_dialog7.open()

    def close_failure_dialog7(self, *args):
        self.failure_dialog7.dismiss()

    def update_timer7(self, dt):
        self.timer -= 1
        if self.timer == 0:
            Clock.unschedule(self.update_timer7)
            self.show_otp_expired_dialog7()
        else:
            self.timer_label7.text = f"Time Left: {self.timer} seconds"

    def show_otp_expired_dialog7(self):
        self.otp_expired_dialog7 = MDDialog(
            title="OTP Expired",
            text="The OTP has expired.",
            buttons=[
                MDRectangleFlatButton(
                    text="Resend OTP", on_release=self.resend_otp_dialog7
                ),
                MDRectangleFlatButton(text="Cancel", on_release=self.close_otp_expired_dialog7),
            ],
        )
        self.otp_expired_dialog7.open()

    def close_otp_expired_dialog7(self, *args):
        self.otp_expired_dialog7.dismiss()

    def resend_otp_dialog7(self, *args):
        self.dialog7.dismiss()

        self.send_otpforforgetpassword()

    def on_stop7(self):
        Clock.unschedule(self.update_timer7)

    def updatepassword(self):
        self.show_snackbar("Password Changed")
        screen_manager.current =  "login"

    def change_screen1(self):
        screen_manager.current = "updateprofile"

    def handle_touch(self):
        self.showdetails_student()
        self.change_screen1()

    def logout(self):
        screen_manager.current = "login"
        det = screen_manager.get_screen("login")
        det.ids.email_id.text = ""
        det.ids.password.text = ""

    def file_manager_open1(self):
        self.file_manager6.show('/')  # No argument required

    def exit_manager6(self, *args):
        self.file_manager6.close()

    def select_path6(self, path):
        self.file_path = path
        self.exit_manager6()
        if self.file_path.lower().endswith('.pdf'):
            screen_manager.get_screen("addnotice").ids.notice_pdf_name.text = f"Selected PDF: {os.path.basename(self.file_path)}"
        else:
            screen_manager.get_screen("addnotice").ids.notice_pdf_name.text = "No PDF selected"

    def update_date_of_add_notice(self):
        screen_manager.current = "addnotice"
        screen_manager.transition.direction = "left"
        today = datetime.date.today()
        print(today)
        det = screen_manager.get_screen("addnotice")
        det.ids.noticedate.text = today.strftime('%Y-%m-%d')

    def addnotice(self, noticeid, noticedate, notice):
        try:
            if not self.file_path.lower().endswith('.pdf'):
                self.show_dialog99("Invalid Format", "File type is not of form PDF, please upload a PDF file")
                return

            with open(self.file_path, 'rb') as file:
                pdf_data = file.read()

            self.cursor.execute(
                "INSERT INTO notice (noticeid, noticedate, notice, notice_pdf) VALUES (%s, %s, %s, %s)",
                (noticeid.text, noticedate.text, notice.text, pdf_data)
            )
            self.database.commit()
            self.show_snackbar("Notice added successfully")
            det = screen_manager.get_screen("addnotice")
            det.ids.noticeid.text = ""
            det.ids.noticedate.text = ""
            det.ids.notice.text = ""
            det.ids.notice_pdf_name.text= ""
            self.file_path = None  # Clear the file path after successful insertion
        except Exception as e:
            self.database.rollback()  # Rollback the transaction if an error occurs
            self.show_snackbar("Error: " + str(e))
            print("Error: " + str(e))

    def on_click_showstudentsnotification(self):
        screen_manager.current = "notification"
        self.cursor.execute("select * from notice")
        row = self.cursor.fetchall()
        notice_list = self.root.get_screen('notification').ids.stu_notification_list
        notice_list.clear_widgets()

        for i in row:
            # Create a FloatLayout to hold the TwoLineListItem and the MDIconButton
            item_layout = MDFloatLayout(size_hint_y=None, height=100)

            # Create the TwoLineListItem
            item50 = ThreeLineListItem(text=str(i[0]), secondary_text=str(i[1]), tertiary_text = str(i[2]))
            item50.size_hint = (0.85, None)
            item50.pos_hint = {"center_y": 0.5, "x": 0}

            # Create the download icon button
            download_button = MDIconButton(icon='download', size_hint=(None, None), size=(40, 40))
            download_button.pos_hint = {"center_y": 0.5, "right": 1}

            # Bind the button to the download function
            #download_button.bind(on_release=lambda btn, notice_id=i[0]: self.download_notice(notice_id))

            # Add the TwoLineListItem and the MDIconButton to the FloatLayout
            item_layout.add_widget(item50)
            item_layout.add_widget(download_button)
            item50.bind(on_release= self.show_notice_to_students)
            # Add the FloatLayout to the notice list
            notice_list.add_widget(item_layout)



    def show_notice_to_students(self,item50):
        #print(item1.secondary_text)
        self.cursor.execute("select * from notice where noticeid = %s",(item50.text,))

        row = self.cursor.fetchone()
        screen_manager.current = "noticedetailstostu"
        notice_details_screen = screen_manager.get_screen("noticedetailstostu")
        if notice_details_screen:
            notice_details_screen.ids.dateofnotice.text=str(row[1])
            notice_details_screen.ids.notice.text=str(row[2])

    # def on_click_shownoticelist(self):
    #     self.cursor.execute("select noticeid, noticedate, notice from notice")
    #     row = self.cursor.fetchall()
    #     notice_list = self.root.get_screen('companyhome').ids.noticefrompo
    #     notice_list.clear_widgets()
    #     for i in row:
    #         item100 = ThreeLineListItem(text = i[0], secondary_text = i[1], tertiary_text = i[2])
    #         notice_list.add_widget(item100)
    def on_click_shownoticelist(self):
        self.cursor.execute("SELECT noticeid, noticedate, notice FROM notice")
        rows = self.cursor.fetchall()
        notice_list = self.root.get_screen('companyhome').ids.noticefrompo
        notice_list.clear_widgets()
        for i in rows:
            item100 = CustomThreeLineListItem(text=str(i[2]), secondary_text=str(i[1]), tertiary_text=str(i[0]))
            item100.bind(on_release=self.show_notice_to_company)
            notice_list.add_widget(item100)

    def show_notice_to_company(self,item100):
        #print(item1.secondary_text)
        self.cursor.execute("select * from notice where noticeid = %s",(item100.tertiary_text,))

        row = self.cursor.fetchone()
        screen_manager.current = "noticedetailstocompany"
        notice_details_screen = screen_manager.get_screen("noticedetailstocompany")
        if notice_details_screen:
            notice_details_screen.ids.dateofnotice.text=str(row[1])
            notice_details_screen.ids.notice.text=str(row[2])

    def file_manager_open2(self):
        self.file_manager7.show('/')  # No argument required

    def exit_manager7(self, *args):
        self.file_manager7.close()

    def select_path7(self, path):
        self.file_path = path
        self.exit_manager7()
        self.upload_pdf1()

    def upload_pdf1(self):
        det = screen_manager.get_screen('companyprofile')
        email = det.ids.my_label.text
        self.cursor.execute("select company_name, company_emailid from company_details where company_emailid = %s", (email,))
        row = self.cursor.fetchone()
        emailid = row[1]
        name = row[0]
        print(emailid, name)

        if not self.file_path:
            self.show_snackbar("No file selected")
            return

        _, file_extension = os.path.splitext(self.file_path)
        if file_extension.lower() != '.pdf':
            self.show_dialog99("Invalid file type", "The file selected is not of PDF format. Please upload a file of that format.")
            return

        max_size = 10 * 1024 * 1024  # Maximum file size in bytes (10MB)
        file_size = os.path.getsize(self.file_path)
        if file_size > max_size:
            self.show_snackbar("File size exceeds the limit")
            return

        # Read the PDF file content
        with open(self.file_path, "rb") as file:
            pdf_data = file.read()

        try:
            database = mysql.connector.connect(user="root", host="localhost",
                                               password="Kushal@2003", database="karimganjcollege")
            cursor = database.cursor()

            # Check if the resume already exists for the user
            cursor.execute("SELECT COUNT(*) FROM company_gst_registration_pdf WHERE email_id = %s", (emailid,))
            count = cursor.fetchone()[0]

            if count > 0:
                # Update the existing resume
                cursor.execute("UPDATE company_gst_registration_pdf SET gst_pdf = %s WHERE email_id = %s",
                               (pdf_data, emailid))
                self.show_snackbar("PDF updated successfully")
            else:
                # Insert a new resume
                cursor.execute("INSERT INTO company_gst_registration_pdf (email_id, comp_name, gst_pdf) VALUES (%s, %s, %s)",
                               (emailid, name, pdf_data))
                self.show_snackbar("PDF uploaded successfully")

            database.commit()
            cursor.close()
            database.close()

            # self.refresh_pdf_list()  # Refresh the PDF list
        except mysql.connector.Error as error:
            self.show_snackbar(f"Error uploading PDF: {error}")
            print(f"{error}")
    def showdetails_company(self,):
        screen_manager.current='updatecompanyprofile'
        det = screen_manager.get_screen('login')
        emailcomp=det.ids.email_id.text
        self.cursor.execute("select * from company_details where company_emailid = %s ",(emailcomp,))
        row=self.cursor.fetchone()
        screen_manager.current = "updatecompanyprofile"
        dts_scr = screen_manager.get_screen("updatecompanyprofile")
        if dts_scr:
            dts_scr.ids.comp_id.text = str(row[0])
            dts_scr.ids.comp_id.disabled = True
            dts_scr.ids.comp_name.text = str(row[1])
            dts_scr.ids.email_id.text = str(row[2])
            dts_scr.ids.email_id.disabled = True
            dts_scr.ids.phone_no.text = str(row[3])
            dts_scr.ids.address.text = str(row[4])
            dts_scr.ids.password.text = str(row[5])
        self.database.commit()

        #self.database.close()

    def updatecompanyprofile(self,comp_id,comp_name,email_id,phone_no,address,password):
        try:
            self.cursor.execute(
                "UPDATE company_details SET company_id = %s, company_name = %s, company_emailid = %s, phone_no = %s, address = %s, password = %s WHERE company_emailid = %s",
                (comp_id,comp_name,email_id,phone_no,address,password, email_id)
            )
            self.cursor.execute("select * from company_details where company_emailid = %s", (email_id,))
            row = self.cursor.fetchone()
            if row:
                dts_scr = screen_manager.get_screen("updatecompanyprofile")
                dts_scr.ids.comp_id.text = str(row[0])
                dts_scr.ids.comp_name.text = str(row[1])
                dts_scr.ids.email_id.text = str(row[2])
                dts_scr.ids.phone_no.text = str(row[3])
                dts_scr.ids.address.text = str(row[4])
                dts_scr.ids.password.text = str(row[5])
            self.show_snackbar("Updated Successfully")
        except Exception as e:
            self.database.rollback()
            self.show_snackbar(f"Error; try again: {str(e)}")

    def show_jobdetails_tocompanyagain(self):
        try:
            det = screen_manager.get_screen("updatejobdetails")
            companyidprovide = det.ids.companyidprovide.text

            # Ensure any unread results are handled before executing the new query
            if self.cursor.with_rows:
                self.cursor.fetchall()

            self.cursor.execute("SELECT * FROM job_details WHERE companyidprovide = %s", (companyidprovide,))
            row = self.cursor.fetchone()

            screen_manager.current = "viewjob"
            job_details_screen = screen_manager.get_screen("viewjob")
            if job_details_screen and row:
                job_details_screen.ids.job_id.text = str(row[0])
                job_details_screen.ids.job_title.text = str(row[1])
                job_details_screen.ids.company_id.text = str(row[4])
                job_details_screen.ids.Providing_Date.text = str(row[5])
                job_details_screen.ids.Last_date.text = str(row[6])
                job_details_screen.ids.Salary.text = str(row[7])

            #self.show_snackbar("Job details displayed successfully.")
        except Exception as e:
            print("Error:", e)
            self.show_snackbar("Error Occurred")

    def on_click_showshoortlistedstudentlist(self):
        try:
            screen_manager.current = "shortlistedstudents"
            det = screen_manager.get_screen('login')
            emailco = det.ids.email_id.text
            self.cursor.execute("SELECT company_name FROM company_details WHERE company_emailid = %s", (emailco,))
            det1 = self.cursor.fetchone()[0]
            self.cursor.execute(
                "SELECT full_name, user_id, job_id, shortlisted_ornot FROM shortlisted_students WHERE company_name = %s",
                (det1,))
            row = self.cursor.fetchall()
            job_list = self.root.get_screen('shortlistedstudents').ids.shortlistedstudent_list
            job_list.clear_widgets()
            for i in row:
                item155 = ThreeLineAvatarIconListItem(text=i[0], secondary_text=str(i[2]), tertiary_text=str(i[1]))
                if i[3] == 'shortlisted':
                    icon = IconRightWidget(icon="check", theme_text_color="Custom",
                                           text_color=(129 / 255, 232 / 255, 0, 1))
                    icon.bind(
                        on_release=lambda x: self.show_dialognew("Shortlisted", "Student is shortlisted for interview"))
                else:
                    icon = IconRightWidget(icon="close", theme_text_color="Custom", text_color=(232 / 255, 0, 0, 1))
                    icon.bind(
                        on_release=lambda x: self.show_dialognew("Rejected", "Student is excluded from the interview"))
                item155.add_widget(icon)
                item155.bind(on_release=self.review_students_job_application)
                item155.bind(on_release=self.on_click_showstudent_resume_to_comp_again)
                item155.bind(on_release=self.shw_reviewed_students_details_to_comp)
                job_list.add_widget(item155)
        except Exception as e:
            print(f"Error in on_click_showshoortlistedstudentlist: {e}")
    def show_dialognew(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            size_hint=(0.8, 1),
            elevation = 0,
            buttons=[
                MDIconButton(
                    icon="check",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def review_students_job_application(self, item155):
        try:
            self.cursor.execute("SELECT email_id FROM signupstudent WHERE user_id = %s", (item155.tertiary_text,))
            row1 = self.cursor.fetchall()
            if row1:
                stueml = row1[0][0]  # Extract the email ID from the tuple
                self.cursor.execute("SELECT * FROM prev_applied_jobs WHERE email_id = %s", (stueml,))
                row = self.cursor.fetchone()
                if row:
                    screen_manager.current = "reviewstudentsjobapplication"
                    job_details_screen = screen_manager.get_screen("reviewstudentsjobapplication")
                    if job_details_screen:
                        job_details_screen.ids.jobtitleviewtocompany.text = str(row[1])
                        job_details_screen.ids.jobidviewtocompany.text = str(row[0])
                        job_details_screen.ids.stunametocompany.text = str(row[2])
                        job_details_screen.ids.studentemailidviewtocompany.text = str(row[3])
                        job_details_screen.ids.companyname.text = str(row[7])
                        job_details_screen.ids.whyapplyingviewtocompany.text = str(row[5])
                        job_details_screen.ids.whyhireviewtocompany.text = str(row[6])
                else:
                    print("No job application found for the provided email ID.")
            else:
                print("No student found with the provided user ID.")
        except Exception as e:
            print(f"Error in review_students_job_application: {e}")

    def on_click_showstudent_resume_to_comp_again(self, item155):
        try:
            print(item155.tertiary_text)
            self.cursor.execute("SELECT email_id FROM signupstudent WHERE user_id= %s", (item155.tertiary_text,))
            em = self.cursor.fetchone()
            if em:
                stueml = em[0]
            self.cursor.execute("SELECT uid, name FROM stu_resume WHERE uid = %s", (stueml,))
            row = self.cursor.fetchall()
            #print("Hello" + str(row))
            job_list = self.root.get_screen('reviewstudentsjobapplication').ids.studentpdf
            job_list.clear_widgets()
            for i in row:
                item_layout1 = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
                item2 = TwoLineListItem(text="Student Resume", secondary_text=i[0])
                icon_button = MDIconButton(icon='download', size_hint=(None, None))
                icon_button.bind(on_release=lambda btn, student_email=i[0]: self.show_save_dialog1(btn, student_email))
                item_layout1.add_widget(item2)
                item_layout1.add_widget(icon_button)
                job_list.add_widget(item_layout1)
        except Exception as e:
            print(f"Error in on_click_showstudent_resume_to_comp_again: {e}")
    def show_save_dialog1(self, btn, student_email):
        connection = mysql.connector.connect(
            host='localhost',
            database='karimganjcollege',
            user='root',
            password='Kushal@2003'
        )
        cursor = connection.cursor()

        try:
            # Fetch file data from the database
            query = f"SELECT name,pdf_data FROM stu_resume WHERE uid = %s"
            para = (student_email,)
            cursor.execute(query, para)
            result = cursor.fetchone()

            if result:
                # Create and open the SaveDialog
                save_dialog = SaveDialog(callback=self.download_pdf1)
                save_dialog.open()

            else:
                print(f"PDF file for {student_email} not found")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        except Exception as e:
            # Handle other exceptions
            print(f"Unexpected error: {e}")

        finally:
            # Close the database connection
            cursor.close()
            connection.close()

    def download_pdf1(self,chosen_directory):
        a = screen_manager.get_screen("reviewstudentsjobapplication")
        stuemail = a.ids.studentemailidviewtocompany.text
        connection = mysql.connector.connect(
            host='localhost',
            database='karimganjcollege',
            user='root',
            password='Kushal@2003'
        )
        cursor = connection.cursor()

        try:
            # Fetch file data from the database
            query = f"SELECT name, pdf_data FROM stu_resume WHERE uid = %s"
            para = (stuemail,)
            cursor.execute(query,para)
            result = cursor.fetchone()

            if result:
                name, pdf_data = result

                # Write the PDF file to the chosen directory
                pdf_path = f"{chosen_directory}/{name}.pdf"
                with open(pdf_path, 'wb') as pdf_file:
                    pdf_file.write(pdf_data)

                print(f"PDF file '{name}' downloaded successfully as '{pdf_path}'")

            else:
                print(f"PDF file not found")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        except Exception as e:
            # Catch and ignore the specific file access permission error
            if 'The process cannot access the file' in str(e):
                print("Ignoring file access permission error.")
            else:
                print(f"Unexpected error: {e}")

        finally:
            # Close the database connection
            cursor.close()
            connection.close()

    def shw_reviewed_students_details_to_comp(self, item155):
        try:
            self.cursor.execute("SELECT * FROM signupstudent WHERE user_id = %s", (item155.tertiary_text,))
            row = self.cursor.fetchone()

            if row is None:
                print("No student found with the given email ID.")
                return

            print(row)
            screen_manager.current = "detailsofstudentswhoseapplicationisbeingreviewed"
            job_details_screen = screen_manager.get_screen("detailsofstudentswhoseapplicationisbeingreviewed")

            if job_details_screen:
                job_details_screen.ids.user_id.text = str(row[0])
                job_details_screen.ids.full_name.text = str(row[1])
                job_details_screen.ids.email_id.text = str(row[2])
                job_details_screen.ids.phone_no.text = str(row[3])
                job_details_screen.ids.address.text = str(row[4])
                job_details_screen.ids.department.text = str(row[5])
        except Exception as e:
            print(f"Error in shw_reviewed_students_details_to_comp: {e}")
    def shw_image_of_stu_to_comp(self):
        try:
            if self.cursor.with_rows:
                self.cursor.fetchall()

            det = screen_manager.get_screen('reviewstudentsjobapplication')
            eml = det.ids.studentemailidviewtocompany.text
            print("Gu " + eml)

            self.cursor.execute("SELECT user_id FROM signupstudent WHERE email_id= %s",(eml,))
            row1 = self.cursor.fetchone()

            if row1:
                user_id = row1[0]
                self.cursor.execute("SELECT stu_image FROM student_image WHERE user_id = %s", (user_id,))
                row = self.cursor.fetchone()

                if row:
                    image_data = row[0]
                    image = Image.open(BytesIO(image_data))
                    image.save("studentimage.jpg")

                    screen_manager.current = 'detailsofstudentswhoseapplicationisbeingreviewed'
                    det = screen_manager.get_screen('detailsofstudentswhoseapplicationisbeingreviewed')
                    det.ids.showstudentimagetocompany.source = 'studentimage.jpg'
        except Exception as e:
            print("Error in shw_image_of_stu_to_comp")
            
    def toggle_password(self, textfield, icon):
        # Toggle the password visibility
        if textfield.password:
            textfield.password = False
            icon.icon = "checkbox-marked"
        else:
            textfield.password = True
            icon.icon = "checkbox-blank-outline"

    def on_text(self, instance, value):
        # Enable or disable the eye button based on the text field value
        det = screen_manager.get_screen("login")
        eye_button = det.ids.toggle_icon
        if value:
            eye_button.disabled = False
        else:
            eye_button.disabled = True
class CustomThreeLineListItem(ThreeLineListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids._lbl_primary.font_style = 'Caption'
        self.ids._lbl_primary.font_size = '14sp'
        self.ids._lbl_secondary.font_style = 'Caption'
        self.ids._lbl_secondary.font_size = '12sp'
        self.ids._lbl_tertiary.font_style = 'Caption'
        self.ids._lbl_tertiary.font_size = '8sp'
        self.height = '70dp'  # Set the height of the list item
        self.padding = '8dp'

class SaveDialog(ModalView):
    def __init__(self, callback, **kwargs):
        super(SaveDialog, self).__init__(**kwargs)
        self.callback = callback

        layout = BoxLayout(orientation='vertical', spacing=10)

        self.file_chooser = FileChooserListView()
        layout.add_widget(self.file_chooser)

        save_button = Button(text="Save", on_press=self.save)
        layout.add_widget(save_button)

        self.add_widget(layout)

    def save(self, instance):
        chosen_directory = self.file_chooser.path or './'
        self.callback(chosen_directory)
        self.dismiss()

if __name__ == "__main__":
    LabelBase.register(name='MPoppins', fn_regular=("Poppins Medium 500.ttf"))
    LabelBase.register(name='BPoppins', fn_regular=("Poppins Light 300.ttf"))
    LabelBase.register(name='CPoppins', fn_regular=("Poppins ExtraBold Italic 800.ttf"))
    LabelBase.register(name='DPoppins', fn_regular=("Poppins SemiBold 600.ttf"))
    app = Karimganj_College()
    app.run()

