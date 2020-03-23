import sys
import os
from packages.basic.main import NetDeviceConfigurer
import getpass
from telnetlib import Telnet as telnet
# create the logs folder for logs
try:
    os.mkdir("logs")
except FileExistsError :
    pass

# get default requirements for telnet connection
target = ""
telnet_port = ""
username = ""
password = ""
local_password = ""
default_timeout = 2

# get default requirements for telnet connection
target = input("Your target ip address :")
telnet_port = input("telnet port (default = 23) :")
username = input("Your remote username :")
password = getpass.getpass("Your *remote* password :")
local_password = getpass.getpass("Your *local* password :")
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