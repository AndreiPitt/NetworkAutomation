import sys

from Devices import Devices
from Router import Router
from Switch import Switch


class Menu:
    """
    The Menu class provides a Singleton interface for displaying and selecting network device configurations.

     Methods:
        pick_object(device_name): Finds and returns a device object from the list based on its name.
        pick_option(): Prompts the user to select a menu option.
        display_menu(item): Displays configuration options based on the device type (router or switch).
    """
    _instance = None

    def __new__(cls):
        """ This method implements the Singleton pattern, ensuring only one instance of the class is created. It
        initializes cls._instance with device data, calling Devices.update_devices() to update the device list. The
        instance will contain item (the device list).
        """
        if cls._instance is None:
            cls._instance = super(Menu, cls).__new__(cls)
            Devices.update_devices()
            cls._instance.items = Devices.devices_list if Devices.devices_list else []
        return cls._instance

    @classmethod
    def pick_object(cls, device_name: str) -> object:
        """ This function searches for and returns an object from the device list based on the provided device_name.
        If the device is not found, it raises an exception with an error message.
        """
        object_searched = None
        for item in cls._instance.items:
            if item.name == device_name:
                if item.type_device == "router":
                    return Router(type_device=item.type_device, name=item.name, ip=item.ip,
                                  username=item.username, password=item.password, priv_password=item.priv_password)
                elif item.type_device == "switch":
                    return Switch(type_device=item.type_device, name=item.name, ip=item.ip,
                                  username=item.username, password=item.password, priv_password=item.priv_password)
        if object_searched is None:
            raise Exception(f"ERROR: This device does not exist. You entered {device_name}")

    @classmethod
    def pick_option(cls) -> int:
        """
        Prompts the user for an input (1 to 6) and converts it to an integer. If the input is invalid, it displays an
        error or informs the user that the command does not exist.
        """
        try:
            var = input("What do you want to do? (Pass q for exit) ")
            if var == "q":
                sys.exit()
            var = int(var)
            return var

        except Exception as e:
            print("ERROR: ", e)

    @classmethod
    def display_menu(cls, item: object) -> None:
        """
        Displays a set of options based on the type of the device (router or switch). Each device type has its own
        configuration options listed in the menu.
        """
        print(f"Options for {item.name} ({item.type_device}):")
        if item.type_device == 'router':
            print("    1. Configure interface")
            print("    2. Configure intervlan")
            print("    3. Configure RIP v2")
            print("    4. Configure DHCP")
            print("    5. Configure HSRP")
            print("    6. Test ping")

        elif item.type_device == 'switch':
            print("    1. Configure VLAN")
            print("    2. Configure Security")
            print("    3. Configure STP")
            print("    4. Configure RSTP")
            print("    5. Configure HSRP")
            print("    6. Test ping")
