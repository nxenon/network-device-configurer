import sys
from telnetlib import Telnet as telnet
import socket
sys.path.append(".../")
from packages.telnet.basic.main import NetDeviceConfigurer

class Interface(NetDeviceConfigurer):
    def __init__(self ,target ,telnet_port ,username ,password ,localpassword ,default_timeout):
        self.target = target
        self.username = username
        self.password = password
        self.localpassword = localpassword
        self.telnet_port = telnet_port
        self.default_timeout = default_timeout

    def show_interfaces_status(self):
        try :
            tc = telnet(self.target ,self.telnet_port ,self.default_timeout)
        except socket.timeout :
            print("Connection failed !")
        else :
            try :
                tc.read_until(b"Username:" ,1)
                tc.write(self.username.encode("ascii") + b"\n")
                if self.password:
                    tc.read_until(b"Password:" ,1)
                    tc.write(self.password.encode("ascii") + b"\n")
            except socket.timeout :
                print("Connection failed !")
            else:
                tc.write(b"show ip interface brief\n")
                tc.write(b"exit\n")
                result = tc.read_all().decode("ascii")
                start_interface_text = result.find("Interface")
                last_interface_text = result.rfind(">")
                print("")
                print(result[start_interface_text:last_interface_text])
                with open("logs/log.txt", "a") as txt_file:
                    import datetime
                    txt_file.write("----------------------\n")
                    command_execution_time = datetime.datetime.now()
                    txt_file.write(str(command_execution_time) + "\n")
                    txt_file.write("show_interfaces_status command executed ... ")
                    txt_file.write(result)
                    txt_file.write("----------------------\n")
                show_result = input("Do you want to open log file ? (y) :")
                if show_result == "y" or show_result == "yes":
                    import os
                    os.system("start logs/log.txt")

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
                if self.password:
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
                with open("logs/log.txt", "a") as txt_file:
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
                    os.system("start logs/log.txt")

    def interface_turn_off(self):
        '''set a new ip address for an interface'''
        local_pass = self.localpassword
        interface = input("Interface :")
        try:
            tc = telnet(self.target, self.telnet_port, self.default_timeout)
        except socket.timeout:
            print("Connection failed !")
        else:
            try:
                tc.read_until(b"Username:", 1)
                tc.write(self.username.encode("ascii") + b"\n")
                if self.password:
                    tc.read_until(b"Password:", 1)
                    tc.write(self.password.encode("ascii") + b"\n")
            except socket.timeout:
                print("Connection failed !")
            else:
                tc.write(b"enable\n")
                tc.read_until(b"Password:", 1)
                tc.write(local_pass.encode("ascii") + b"\n")
                tc.write(b"configure terminal\n")
                tc.write(b"interface " + interface.encode("ascii") + b"\n")
                tc.write(b"shutdown\n")
                tc.write(b"exit\n")
                tc.write(b"exit\n")
                tc.write(b"exit\n")
                result = tc.read_all().decode("ascii")
                with open("logs/log.txt", "a") as txt_file:
                    import datetime
                    txt_file.write("----------------------\n")
                    command_execution_time = datetime.datetime.now()
                    txt_file.write(str(command_execution_time) + "\n")
                    txt_file.write("interface_turn_off command executed ... ")
                    txt_file.write(result)
                    txt_file.write("----------------------\n")
                show_result = input("Do you want to open log file ? (y) :")
                if show_result == "y" or show_result == "yes":
                    import os
                    os.system("start logs/log.txt")

    def interface_turn_on(self):
        '''set a new ip address for an interface'''
        local_pass = self.localpassword
        interface = input("Interface :")
        try:
            tc = telnet(self.target, self.telnet_port, self.default_timeout)
        except socket.timeout:
            print("Connection failed !")
        else:
            try:
                tc.read_until(b"Username:", 1)
                tc.write(self.username.encode("ascii") + b"\n")
                if self.password:
                    tc.read_until(b"Password:", 1)
                    tc.write(self.password.encode("ascii") + b"\n")
            except socket.timeout:
                print("Connection failed !")
            else:
                tc.write(b"enable\n")
                tc.read_until(b"Password:", 1)
                tc.write(local_pass.encode("ascii") + b"\n")
                tc.write(b"configure terminal\n")
                tc.write(b"interface " + interface.encode("ascii") + b"\n")
                tc.write(b"no shutdown\n")
                tc.write(b"exit\n")
                tc.write(b"exit\n")
                tc.write(b"exit\n")
                result = tc.read_all().decode("ascii")
                with open("logs/log.txt", "a") as txt_file:
                    import datetime
                    txt_file.write("----------------------\n")
                    command_execution_time = datetime.datetime.now()
                    txt_file.write(str(command_execution_time) + "\n")
                    txt_file.write("interface_turn_on command executed ... ")
                    txt_file.write(result)
                    txt_file.write("----------------------\n")
                show_result = input("Do you want to open log file ? (y) :")
                if show_result == "y" or show_result == "yes":
                    import os
                    os.system("start logs/log.txt")
