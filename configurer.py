#!/usr/bin/env python3

'''
Cisco Device Configurer Script
'''

import sys
import os
from packages.telnet.basic.main import NetDeviceConfigurer
from packages.telnet.routing_options.main_routing import Routing
from packages.telnet.interface_options.main_interface import Interface

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

update_again = True
def update_connection_data():
    while True :
        global target,telnet_port,username,password,local_password,default_timeout,connection,connection_routing,connection_interface
        # get default requirements for telnet connection
        target = input("Your target ip address :").strip()
        telnet_port = input("telnet port (default = 23) :").strip()
        username = input("Your remote username :").strip()
        password = getpass.getpass("Your *remote* password :").strip()
        local_password = getpass.getpass("Your *local* password :").strip()
        default_timeout = 2
        if not telnet_port:
            telnet_port = 23

        connection = NetDeviceConfigurer(target, telnet_port, username, password, local_password, default_timeout)
        # set a connection to Routing class
        connection_routing = Routing(target, telnet_port, username, password, local_password, default_timeout)
        # set a connection for Interface class
        connection_interface = Interface(target, telnet_port, username, password, local_password, default_timeout)

        correct_or_not_up = input("Correct ? (y) :").lower()
        if correct_or_not_up == "y" or correct_or_not_up == "yes" :
            break
        else :
            print("")

connection = NetDeviceConfigurer(target, telnet_port, username, password, local_password, default_timeout)
# set a connection to Routing class
connection_routing = Routing(target, telnet_port, username, password, local_password, default_timeout)
# set a connection for Interface class
connection_interface = Interface(target, telnet_port, username, password, local_password, default_timeout)

update_connection_data()

config_again = True
config_again_routing = True
config_again_interface = True
while config_again :
    print("Options :")
    print("\n\t1) Interface options")
    print("\n\t2) Create a new user")
    print("\n\t3) Enable SSH")
    print("\n\t4) Routing options")
    print("\nUpdate the connection information (ip,pass and ..) ? type => (update)")
    print("\nquit => (exit)")

    option_chosen = input("\nOption number :").lower()
    if option_chosen == "1" or option_chosen == "interface options":

        while config_again_interface:
            print("--")
            print("")
            print("Interface options :")
            print("\n\t1) Show interfaces status")
            print("\n\t2) Set ip address")
            print("\n\t3) Turn a interface off")
            print("\n\t4) Turn a interface on")
            print("\n Go to previous menu => (Back)")
            option_chosen_interface = input("\nOption number :").lower()

            if option_chosen_interface == "1" or option_chosen_interface == "show interfaces status":
                connection_interface.show_interfaces_status()
            elif option_chosen_interface == "2" or option_chosen_interface == "set ip address":
                connection_interface.set_ip()
            elif option_chosen_interface == "3" or option_chosen_interface == "turn a interface off":
                connection_interface.interface_turn_off()
            elif option_chosen_interface == "4" or option_chosen_interface == "turn a interface on":
                connection_interface.interface_turn_on()
            elif option_chosen_interface == "back" or option_chosen_interface == "go to previous menu" :
                break
            else:
                print("Invalid option")
                again_or_not = input("again ? (y) :").lower()
                if again_or_not == "y" or again_or_not == "yes":
                    config_again_routing = True
                else:
                    break

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

    elif option_chosen == "4" or option_chosen == "show routing options" :

        while config_again_routing:
            print("--")
            print("")
            print("Routing options :")
            print("\n\t1) Show routing table")
            print("\n\t2) Set static route")
            print("\n Go to previous menu => (Back)")
            option_chosen_routing = input("\nOption number :").lower()
            if option_chosen_routing == "1" or option_chosen_routing == "show routing table":
                connection_routing.show_routing_table()
            elif option_chosen_routing == "2" or option_chosen_routing == "set static route":
                connection_routing.set_static_route()
            elif option_chosen_routing == "back" or option_chosen_routing == "go to previous menu" :
                break
            else:
                print("Invalid option")
                again_or_not = input("again ? (y) :").lower()
                if again_or_not == "y" or again_or_not == "yes":
                    config_again_routing = True
                else:
                    break

    elif option_chosen == "quit" or option_chosen == "exit":
        config_again = False
    else:
        print("Invalid option")
        again_or_not = input("again ? (y) :").lower()
        if again_or_not == "y" or again_or_not == "yes":
            config_again = True
        else:
            config_again = False

print("Exit ...")
exit()
