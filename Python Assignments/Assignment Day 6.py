from PyQt5 import QtWidgets,uic
import sys

username_main='sumanth'
password_main='passcode'

def gotoLogin():
    second.show()
    first.close()
    print("the user login is successful")
    
def gotoRegister():
    first.show()
    second.close()

def user_registration():
    global username_main,password_main
    first.rstatus.setText("Done")
    username_main=register.rusername.text()
    password_main=register.rpassword1.text()    

def user_login():
    global username_main,password_main
    username=second.lusername.text()
    password=second.lpassword.text()
    if username==username_main and password==password_main:
        second.lstatus.setText("Successfully Logged In, u will be redirected to your home page")
    else:
        second.lstatus.setText("Invalid Credentials")    

demo=QtWidgets.QApplication([])
first=uic.loadUi("/Users/ssumanth/Desktop/registration_page.ui")
second=uic.loadUi("/Users/ssumanth/Desktop/login_page.ui")

second.show()

second.lregister.clicked.connect(gotoRegister)
second.loginbutton.clicked.connect(user_login)
first.rsignup.clicked.connect(user_registration)
first.rlogin.clicked.connect(gotoLogin)
sys.exit(demo.exec())
