import hashlib
import sqlite3.dbapi2 as sqlite3
import os
import sys
import getpass
import time
import random

def current_time():
   return time.strftime("%d/%m/%Y %H:%M:%S")

def askcaptcha():
   captcha = hashlib.sha256(str(random.randint(0,65536)).encode()).hexdigest()[0:8]
   print(f"[PySecurity - main] Please verify you are not a robot typing the following string in the input field below: {captcha}")
   while True:
      try:
         cap = input("Type here: ")
      except KeyboardInterrupt:
         pass
      except EOFError:
         pass
      else:
         if cap == captcha:
            print("[PySecurity - main] Verification completed")
            break
         else:
            print("[PySecurity - main] Wrong captcha, verification failed")
            while True:
               try:
                  getpass.getpass("Reconnect to try again")
               except KeyboardInterrupt:
                  pass
               except EOFError:
                  pass


def askpass(password):
   attempts = 0
   print("[PySecurity - main] To complete authentication, please type your extra password below")
   while True:
      try:
         pwd = getpass.getpass()
         attempts += 1
      except KeyboardInterrupt:
         pass
      except EOFError:
         pass
      else:
         if hashlib.sha256(pwd.encode()).hexdigest() == password:
            print("[PySecurity - main] Access Granted")
            break
         else:
            print(f"[PySecurity - main] Wrong Password, remaining attempts: {3 - attempts}")
         if attempts == 3:
            while True:
               try:
                  getpass.getpass("Reconnect to try again")
               except KeyboardInterrupt:
                  pass
               except EOFError:
                  pass


def main():
   print(f"Welcome {getpass.getuser()} [{os.getuid()}] This server is protected by PySecurity\nDate & Time: {current_time()}\nAuthor: IsGiambyy aka Nocturn9x")
   query = cursor.execute("SELECT * FROM settings")
   assword, captcha = query.fetchall()[0]
   if captcha == 1:
        askcaptcha()
   askpass(password)


def setup():
   dbpath = os.path.join(os.getcwd(), "database.db")
   print("[PySecurity - setup] Welcome into the PySecurity Setup Wizard")
   try:
      getpass.getpass("Press enter to start installation")
   except KeyboardInterrupt:
      print("[PySecurity - setup] Installation aborted, exiting...")
      sys.exit(0)
   else:
      print("[PySecurity - setup] Creating and setting database")
      try:
         database = sqlite3.connect(dbpath)
         cursor = database.cursor()
      except PermissionError:
         sys.exit(f"[PySecurity - setup] ERROR: Could not create database file due to insufficient permissions. Check that the program uas the rights permissions to create files in the current directory ({os.getc$
      else:
          print("[PySecurity - setup] Database file created, creating and populating tables")
          try:
             cursor.execute("""CREATE TABLE settings(
             password TEXT NOT NULL,
             use_captcha INTEGER NOT NULL DEFAULT 0)""")
          except sqlite3.OperationalError as dberror:
            sys.exit(f"[PySecurity - setup] ERROR: Something went wrong with the database, full exception here: {dberror}")
          else:
              print("[PySecurity - setup] Database creation complete, please follow the required steps to complete installation")
              try:
                 password = getpass.getpass("Choose a strong password: ")
              except KeyboardInterrupt: 
                 print("[PySecurity - setup] Installation aborted, exiting...")
                 try:
                    os.remove(dbpath)
                 except Exception as deletionerror:
                    sys.exit(f"[PySecurity - setup] ERROR: Something went wrong during cleanup, full exception here: {deletionerror}")
                 else:
                    sys.exit(0)
              else:
                 try:
                    confirm = getpass.getpass("Please type the password again: ")
                 except KeyboardInterrupt:
                    print("[PySecurity - setup] Installation aborted, exiting...")
                    try:
                       os.remove(dbpath)
                    except Exception as deletionerror:
                      sys.exit(f"[PySecurity - setup] ERROR: Something went wrong during cleanup, full exception here: {deletionerror}")
                    else:
                       sys.exit(0)
                 else:
                    if password != confirm:
                       print("[PySecurity - setup] Passwords don't match, please run the program again and make sure to input the same password twice")
                       try:
                          os.remove(dbpath)
                       except Exception as deletionerror:
                          sys.exit(f"[PySecurity - setup] ERROR: something went wrong during cleanup, full exception here: {deletionerror}")
                       else:
                          sys.exit(0)
                    else:
                       password_hash = hashlib.sha256(password.encode()).hexdigest()
                       print("[PySecurity - setup] Do you want to enable the captcha? This can be an extra protection against automated scripts attempting to log-in")
                       try:
                          enable_captcha = input("Enable captcha? [Y/N]:")
                       except KeyboardInterrupt:
                          print("[PySecurity - setup] Installation aborted, exiting...")
                          try:
                             os.remove(dbpath)
                          except Exception as deletionerror:
                             sys.exit(f"[PySecurity - setup] ERROR: Something went wrong during cleanup, full exception here: {deletionerror}")
                          else:
                             sys.exit(0)
                       else:
                           if enable_captcha.lower().strip() in ("y","yes","yep","yeah","yup"):
                              captcha_enabled = True
                           else:
                              captcha_enabled = False
                           if captcha_enabled:
                              print("[PySecurity - setup] Captcha has been enabled")
                              captcha_enabled = 1
                           else:
                              captcha_enabled = 0
                              print("[PySecurity - setup] captcha is now disabled")
                           print("[PySecurity - setup] Finalizing installation...")
                           try:
                              cursor.execute(f"INSERT INTO settings (password, use_captcha) VALUES('{password_hash}', {captcha_enabled})")
                              database.commit()
                           except sqlite3.OperationalError as dberror:
                              print(f"[PySecurity - setup] ERROR: Something went wrong while dealing with the database, full exception here: {dberror}")
                              try:
                                 os.remove(dbpath)
                              except Exception as deletionerror:
                                 sys.exit(f"[PySecurity - setup ] ERROR: Something went wrong during cleanup, full exception here: {deletionerror}")
                              else:
                                 sys.exit(0)
                           else:
                               print("[PySecurity - setup] Database populated, finalizing install...")
                               try:
                                  with open("/etc/bash.bashrc","a") as bashrc:
                                     bashrc.write(f"python3 {os.path.join(os.getcwd(),__file__)}")
                               except Exception as final_install_error:
                                  sys.exit(f"[PySecurity - setup] Something went wrong while finalizing installation, to complete it manually edit the file /etc/bash.bashrc and put on the last line the following text without brackets: 'python3 {os.path.join(os.getcwd(),__file__)}'")
                               else:
                                  print("[PySecurity - setup] Installation complete")


if __name__ == "__main__":
    dbpath = os.getcwd() + "/PySecurity/database.db"
    if os.path.isfile(dbpath):
       database = sqlite3.connect(dbpath)
       cursor = database.cursor()
       main()
    else:
      setup()
