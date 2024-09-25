from Connection import Connection
from Menu import Menu


def run_main() -> None:
    """
    This function manages the configuration of a network device (router or switch) based on the user's input.

    The function:
    - Displays a menu with configuration options specific to the type of device (router or switch).
    - Based on the user's selection, it triggers specific configuration commands on the connected device.
    - After each configuration step, it asks the user if they want to configure something else on the device.
    - If the user chooses not to continue, the connection to the device is closed.
    """
    while True:
        menu.display_menu(item=device)
        myoption = Menu.pick_option()
        if device.type_device == "router":
            if myoption == 1:
                print("Configure interface")
                device.configure_interface(connector)
            elif myoption == 2:
                print("Configure static route")
                device.configure_staticroute(connector)
            elif myoption == 3:
                print("Configure RIP v2")
                device.configure_rip_v2(connector)
            elif myoption == 4:
                print("Configure DHCP")
                device.configure_dhcp(connector)
            elif myoption == 5:
                print("Configure HSRP")
                device.configure_hsrp(connector)
            elif myoption == 6:
                print("Test ping")
                device.test_ping(connector)
            elif myoption == 7:
                device.save_config(connector)
            else:
                print("This command does not exist!")
        elif device.type_device == "switch":
            if myoption == 1:
                print("Configure VLAN")
                device.configure_vlan(connector)
            elif myoption == 2:
                print("Configure Security")
                device.configure_security(connector)
            elif myoption == 3:
                print("Configure STP")
                device.configure_stp(connector)
            elif myoption == 4:
                print("Configure RSTP")
                device.configure_rstp(connector)
            elif myoption == 5:
                print("Configure HSRP")
                device.configure_hsrp(connector)
            elif myoption == 6:
                print("Test ping")
                device.test_ping(connector)
            elif myoption == 7:
                device.save_config(connector)
            else:
                print("This command does not exist!")

        connector.view_output()

        # Întreabă utilizatorul dacă vrea să configureze altceva
        continue_config = input("Do you want to configure something else on this device? (yes/no): ").strip().lower()
        if continue_config != 'yes':
            break

    connector.close()


if __name__ == "__main__":
    menu = Menu()
    name = input("What is the name of the device you want to connect? ")
    device = Menu.pick_object(device_name=name)
    connector = Connection(device)
    connector.connect()
    print("The connection was successful!")
    run_main()
