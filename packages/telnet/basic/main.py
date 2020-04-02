import time
import sys
sys.path.append(".../")
import socket
from telnetlib import Telnet as telnet

print("You had to configure the device to enable Telnet at first !")
print("")

class NetDeviceConfigurer() :
    '''configuring network device with telnet'''
    def __init__(self ,target ,telnet_port ,username ,password ,localpassword ,default_timeout):
        self.target = target
        self.username = username
        self.password = password
        self.localpassword = localpassword
        self.telnet_port = telnet_port
        self.default_timeout = default_timeout

    def create_user(self):
        '''create a new user'''
        create_user = input("Username that you wanna create :")
        create_pass = input("Password that you wanna create :")
        local_pass = self.localpassword
        try:
            tc = telnet(self.target ,self.telnet_port ,self.default_timeout)
        except socket.timeout :
            print("Connection failed !")
        else:
            try :
                tc.read_until(b"Username:" ,1)
                tc.write(self.username.encode("ascii") + b"\n")
                if self.password:
                    tc.read_until(b"Password:" ,1)
                    tc.write(self.password.encode("ascii") + b"\n")
            except socket.timeout :
                print("Connection failed !")
            else :
                tc.write(b"enable\n")
                tc.read_until(b"Password:" ,1)
                tc.write(local_pass.encode("ascii") + b"\n")
                tc.write(b"conf t\n")
                tc.write(b"username " + create_user.encode("ascii") + b" password " + create_pass.encode("ascii") + b"\n")
                tc.write(b"exit\n")
                tc.write(b"exit\n")
                result = tc.read_all().decode("ascii")
                with open("logs/log.txt", "a") as txt_file:
                    import datetime
                    txt_file.write("----------------------\n")
                    command_execution_time = datetime.datetime.now()
                    txt_file.write(str(command_execution_time) + "\n")
                    txt_file.write("create_user command executed ... ")
                    txt_file.write(result)
                    txt_file.write("----------------------\n")
                show_result = input("Do you want to open log file ? (y) :")
                if show_result == "y" or show_result == "yes":
                    import os
                    os.system("start logs/log.txt")

    def enable_ssh(self):
        '''enable ssh on network device'''
        host_name = input("write a host name :")
        local_pass = self.localpassword
        encryption_bits = input("RSA encryption bits [(default = 512) , [from 360 to 4096]] :")
        if not encryption_bits :
            encryption_bits = "512"

        try :
            tc = telnet(self.target, self.telnet_port, self.default_timeout)
        except socket.timeout :
            print("Connection failed !")
        else:
            try :
                tc.read_until(b"Username:" ,1)
                tc.write(self.username.encode("ascii") + b"\n")
                if self.password:
                    tc.read_until(b"Password:" ,1)
                    tc.write(self.password.encode("ascii") + b"\n")
            except socket.timeout :
                print("Connection failed !")
            else:
                tc.write(b"enable\n")
                tc.read_until(b"Password:" ,1)
                tc.write(local_pass.encode("ascii") + b"\n")
                tc.write(b"conf t\n")
                tc.write(b"ip domain-name " + host_name.encode("ascii") + b"\n")
                tc.write(b"crypto key generate rsa\n")
                # check if a rsa key exists
                try:
                    tc.read_until(b"How many bits in the modulus [512]:" ,1.5)
                except socket.timeout :
                        print("Connection failed !")
                else:
                    tc.write(b"yes\n")
                    tc.write(encryption_bits.encode("ascii") + b"\n")
                    tc.write(b"line vty 0 4\n")
                    tc.write(b"transport input ssh telnet\n")
                    tc.write(b"exit\n")
                    tc.write(b"exit\n")
                    tc.write(b"exit\n")
                    result = tc.read_all().decode("ascii")
                    with open("logs/log.txt", "a") as txt_file:
                        import datetime
                        txt_file.write("----------------------\n")
                        command_execution_time = datetime.datetime.now()
                        txt_file.write(str(command_execution_time) + "\n")
                        txt_file.write("enable_ssh command executed ... ")
                        txt_file.write(result)
                        txt_file.write("----------------------\n")
                    show_result = input("Do you want to open log file ? (y) :")
                    if show_result == "y" or show_result == "yes":
                        import os
                        os.system("start logs/log.txt")
