import time
import sys
import socket
from telnetlib import Telnet as telnet

# get default requirements for telnet connection
target = ""
telnet_port = ""
username = ""
password = ""
local_password = ""
default_timeout = 2
if not telnet_port :
    telnet_port = 23

print("You had to configure the device to enable Telnet at first !")

class NetDeviceConfigurer() :
    '''configuring network device with telnet'''
    def __init__(self ,target ,telnet_port ,username ,password ,localpassword ,default_timeout):
        self.target = target
        self.username = username
        self.password = password
        self.localpassword = localpassword
        self.telnet_port = telnet_port
        self.default_timeout = default_timeout

    def set_ip(self):
        '''set a new ip address for an interface'''
        interface = input("Interface :")
        ip_address = input("IP address :")
        subnet_mask = input("Subnet mask :")
        local_pass = self.localpassword

        try :
            tc = telnet(self.target ,self.telnet_port ,self.default_timeout)
        except socket.timeout :
            print("Connection failed !")
        else :
            try :
                tc.read_until(b"Username:" ,1)
                tc.write(self.username.encode("ascii") + b"\n")
                if password:
                    tc.read_until(b"Password:" ,1)
                    tc.write(self.password.encode("ascii") + b"\n")
            except socket.timeout :
                print("Connection failed !")
            else:
                tc.write(b"enable\n")
                tc.read_until(b"Password:" ,1)
                tc.write(local_pass.encode("ascii") + b"\n")
                tc.write(b"configure terminal\n")
                tc.write(b"interface " + interface.encode("ascii") + b"\n")
                tc.write(b"ip address " + ip_address.encode("ascii") + b" " + subnet_mask.encode("ascii") + b"\n")
                tc.write(b"no shutdown\n")
                tc.write(b"exit\n")
                tc.write(b"exit\n")
                tc.write(b"exit\n")
                result = tc.read_all().decode("ascii")
                with open("log.txt", "a") as txt_file:
                    import datetime
                    txt_file.write("----------------------\n")
                    command_execution_time = datetime.datetime.now()
                    txt_file.write(str(command_execution_time) + "\n")
                    txt_file.write("set_ip command executed ... ")
                    txt_file.write(result)
                    txt_file.write("----------------------\n")
                show_result = input("Do you want to open log file ? (y) :")
                if show_result == "y" or show_result == "yes":
                    import os
                    os.system("start log.txt")

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
                if password:
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
                with open("log.txt", "a") as txt_file:
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
                    os.system("start log.txt")

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
                if password:
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
                    with open("log.txt", "a") as txt_file:
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
                        os.system("start log.txt")


# get default requirements for telnet connection
target = input("Your target ip address :")
telnet_port = input("telnet port (default = 23) :")
username = input("Your remote username :")
password = input("Your *remote* password :")
local_password = input("Your *local* password :")
default_timeout = 2
if not telnet_port:
    telnet_port = 23



connection = NetDeviceConfigurer(target, telnet_port, username, password, local_password, default_timeout)

update_again = True
def update_connection_data():

    while True :
        # get default requirements for telnet connection
        target = input("Your target ip address :")
        telnet_port = input("telnet port (default = 23) :")
        username = input("Your remote username :")
        password = input("Your *remote* password :")
        local_password = input("Your *local* password :")
        default_timeout = 2
        if not telnet_port:
            telnet_port = 23
        again_or_not_up = input("Correct ? (y) :").lower()
        connection = NetDeviceConfigurer(target, telnet_port, username, password, local_password, default_timeout)
        if again_or_not_up == "y" or again_or_not_up == "yes" :
            break
        else :
            print("")


config_again = True
while config_again :
    print("Options :")
    print("\n\t1) set an IP address")
    print("\n\t2) Create a new user")
    print("\n\t3) Enable SSH")
    print("\nUpdate the connection information (ip,pass and ..) ? type => (update)")

    connection = NetDeviceConfigurer(target, telnet_port, username, password, local_password, default_timeout)

    option_chosen = input("\nOption number :").lower()
    if option_chosen == "1" or option_chosen == "set an ip address":
        connection.set_ip()
        again_or_not = input("again ? (y) :").lower()
        if again_or_not == "y" or again_or_not == "yes" :
            config_again = True
        else:
            config_again = False

    elif option_chosen == "2" or option_chosen == "create a new user" :
        connection.create_user()
        again_or_not = input("again ? (y) :").lower()
        if again_or_not == "y" or again_or_not == "yes":
            config_again = True
        else:
            config_again = False

    elif option_chosen == "3" or option_chosen == "enable ssh" :
        connection.enable_ssh()
        again_or_not = input("again ? (y) :").lower()
        if again_or_not == "y" or again_or_not == "yes":
            config_again = True
        else:
            config_again = False

    elif option_chosen == "u" or option_chosen == "update" :
        update_connection_data()

    else:
        print("Invalid option")
        again_or_not = input("again ? (y) :").lower()
        if again_or_not == "y" or again_or_not == "yes":
            config_again = True
        else:
            config_again = False
            print("Exit ...")

print("Exit ...")
exit()