from Connection import Connection
from Menu import Menu


if __name__ == "__main__":
    menu = Menu()
    name = input("What is the name of the device you want to connect? ")
    device = Menu.pick_object(device_name=name)
    connector = Connection(device)
    connector.connect()
    print("The connection was  successfull!")
    menu.display_menu(item=device)
    myoption = Menu.pick_option()
    if device.type_device == "router":
        if myoption == 1:
            print("Configure interface")
            device.configure_interface(connector)
            connector.view_output()
            connector.close()
        elif myoption == 2:
            print("Configure intervlan")
            device.configure_intervlan(connector)
            connector.view_output()
            connector.close()
        elif myoption == 3:
            print("Configure RIP v2")
            device.configure_rip_v2(connector)
            connector.view_output()
            connector.close()
        elif myoption == 4:
            print("Configure DHCP")
            device.configure_dhcp(connector)
            connector.view_output()
            connector.close()
        elif myoption == 5:
            print("Configure HSRP")
            device.configure_hsrp(connector)
            connector.view_output()
            connector.close()
        elif myoption == 6:
            print("Test ping")
            device.test_ping(connector)
        else:
            print("This command does not exist!")
    elif device.type_device == "switch":
        if myoption == 1:
            print("Configure VLAN")
            device.configure_vlan(connector)
            connector.view_output()
            connector.close()
        elif myoption == 2:
            print("Configure Security")
            device.configure_security(connector)
            connector.view_output()
            connector.close()
        elif myoption == 3:
            print("Configure STP")
            device.configure_stp(connector)
            connector.view_output()
            connector.close()
        elif myoption == 4:
            print("Configure RSTP")
            device.configure_rstp(connector)
            connector.view_output()
            connector.close()
        elif myoption == 5:
            print("Configure HSRP")
            device.configure_hsrp(connector)
            connector.view_output()
            connector.close()
        elif myoption == 6:
            print("Test ping")
            device.test_ping(connector)
            connector.view_output()
            connector.close()
        else:
            print("This command does not exist!")
