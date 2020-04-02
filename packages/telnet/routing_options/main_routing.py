import sys
from telnetlib import Telnet as telnet
import socket
sys.path.append(".../")
from packages.telnet.basic.main import NetDeviceConfigurer

class Routing(NetDeviceConfigurer):
    def __init__(self ,target ,telnet_port ,username ,password ,localpassword ,default_timeout):
        self.target = target
        self.username = username
        self.password = password
        self.localpassword = localpassword
        self.telnet_port = telnet_port
        self.default_timeout = default_timeout

    def show_routing_table(self):
        try :
            tc = telnet(self.target ,self.telnet_port ,self.default_timeout)
        except socket.timeout :
            print("Connection failed !")
        else :
            try:
                tc.read_until(b"Username:", 1)
                tc.write(self.username.encode("ascii") + b"\n")
                if self.password:
                    tc.read_until(b"Password:", 1)
                    tc.write(self.password.encode("ascii") + b"\n")
            except socket.timeout:
                print("Connection failed !")
            else:
                tc.write(b"show ip route\n")
                tc.write(b"exit\n")
                result = tc.read_all().decode("ascii")
                start_routing_text = result.find("Gateway of last resort is not set")
                last_routing_text = result.rfind(">")
                print(result[start_routing_text:last_routing_text])
                with open("logs/log.txt", "a") as txt_file:
                    import datetime
                    txt_file.write("----------------------\n")
                    command_execution_time = datetime.datetime.now()
                    txt_file.write(str(command_execution_time) + "\n")
                    txt_file.write("show_routing_table command executed ... ")
                    txt_file.write(result)
                    txt_file.write("----------------------\n")
                show_result = input("Do you want to open log file ? (y) :")
                if show_result == "y" or show_result == "yes":
                    import os
                    os.system("start logs/log.txt")

    def set_static_route(self):
        print("")
        network = input("Network :")
        subnet_mask = input("Subnet mask :")
        destination = input("Destination ip or router interface :")
        local_pass = self.localpassword

        try :
            tc = telnet(self.target ,self.telnet_port ,self.default_timeout)
        except socket.timeout :
            print("Connection failed !")
        else :
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
                tc.write(b"ip route " + network.encode("ascii") + b" " + subnet_mask.encode("ascii") + b" " + destination.encode("ascii") + b"\n")
                print("")
                Routing.show_routing_table(self)
                print("")
                is_correct = input("Correct (y) :")
                if is_correct == "y" or is_correct == "yse" :
                    pass
                else:
                    tc.write(b"no ip route " + network.encode("ascii") + b" " + subnet_mask.encode("ascii") + b" " + destination.encode("ascii") + b"\n")
                tc.write(b"exit\n")
                tc.write(b"exit\n")
                result = tc.read_all().decode("ascii")
                with open("logs/log.txt", "a") as txt_file:
                    import datetime
                    txt_file.write("----------------------\n")
                    command_execution_time = datetime.datetime.now()
                    txt_file.write(str(command_execution_time) + "\n")
                    txt_file.write("set_static_route command executed ... ")
                    txt_file.write(result)
                    txt_file.write("----------------------\n")
                show_result = input("Do you want to open log file ? (y) :")
                if show_result == "y" or show_result == "yes":
                    import os
                    os.system("start logs/log.txt")
