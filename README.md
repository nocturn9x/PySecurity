# PySecurity
This simple python script asks for an extra password and, optionally, a captcha after SSH login.

## Why should I use PySecurity?

PySecurity is a very simple software. However, it greatly increases your server security and keeps attackers away from your Unix-like server.

## Requirements

  * Python 3.6 or higher
  * A Unix-Like server (VPS or Dedicated) like Debian, Ubuntu, CentOS...
  * 60 seconds of your time for installation
  * That's all! No extra dependencies, no external packages, just pure Python

## Installing PySecurity

The installation is very easy: once run the setup wizard will guide you step by step trough (very fast) the installation procedure and handle all the hassle for you, but before you start installing you need to make everything is set up accordingly. 

### STEP 1 -  PySecurity's Folder

For security purposes, PySecurity **must** be installed inside a folder named "PySecurity" (without apexes). The absolute path is not important, as long as the last folder name is "PySecurity" (e.g. /home/user/PySecurity/main.py is fine, but also /etc/PySecurity/main.py is)

### STEP 2 - The actual install

After setting up the right path,just unzip the archive downloaded from the repository, you can run the main.py file with the following command, without apexes: "python3 main.py" .

The setup wizard will guide you in the installation process automatically.

### DISCLAIMER

As stated by the license, joined with the executable, the software is provided "as is", with no warranty of any kind and it might have bugs and/or issues that the developer still didn't, or couldn't, fix. The installer needs read/write permissions to its own directory and to the **/etc/bash.bashrc** file in order to work properl
It is recommended that this software is installed as root user to avoid any permission related issues, though if there are non-root users on the server they won't be able to access the installation directory and the protection will be useless, so the best way of installing PySecurity is on a user-accessible directory


