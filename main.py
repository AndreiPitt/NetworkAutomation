from Connection import Connection
from Menu import Menu


if __name__ == "__main__":
    menu = Menu()
    name = input("What is the name of the device you want to connect? ")
    device = Menu.pick_object(device_name=name)
    print(f"This device exist! He belongs to the {type(device)}")
    connector = Connection(device)
    connector.connect()
    menu.display_menu(item=device)
    myoption = Menu.pick_option()
    if device.type_device == "router":
        if myoption == 1:
            print("Configure interface")
        elif myoption == 2:
            print("Configure intervlan")
        elif myoption == 3:
            print("Configure RIP v2")
        elif myoption == 4:
            print("Configure DHCP")
        elif myoption == 5:
            print("Configure HSRP")
        elif myoption == 6:
            print("Test ping")
            device.test_ping(connector)
        else:
            print("This command does not exist!")
    elif device.type_device == "switch":
        if myoption == 1:
            print("Configure VLAN")
        elif myoption == 2:
            print("Configure Security")
        elif myoption == 3:
            print("Configure STP")
        elif myoption == 4:
            print("Configure RSTP")
        elif myoption == 5:
            print("Configure HSRP")
        elif myoption == 6:
            print("Test ping")
            device.test_ping(connector)
            connector.view_output()
            connector.close()
        else:
            print("This command does not exist!")
