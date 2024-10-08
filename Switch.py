import time

from Devices import Devices


class Switch(Devices):
    """
    The Switch class inherits from the Devices class and adds specific methods to configure
    the various options available in the menu for switches.

    Methods:
        configure_vlan(): Configures VLAN (Virtual Local Area Network) settings on the switch.
        configure_security(): Configures security features on the switch to enhance network security.
        configure_stp(): Configures Spanning Tree Protocol (STP) to prevent loops in the network.
        configure_rstp(): Configures Rapid Spanning Tree Protocol (RSTP) for faster convergence.
        configure_hsrp(): Configures HSRP (Hot Standby Router Protocol) for high availability.
    """

    def __init__(self, type_device, name, ip, username, password, priv_password):
        """
        Initializes a Switch object, inheriting attributes from the Devices class.
        """
        super().__init__(type_device, name, ip, username, password, priv_password)

    def configure_vlan(self, connector: object) -> None:
        """
        Configures VLAN (Virtual Local Area Network) settings on the switch.
        This method would typically interact with the switch to configure VLANs.
        """
        print(f"Configuring VLAN on switch {self.name}...")
        vlan = input("Please enter the name of the VLAN you want to be allowed to pass: ")
        ip = input("Enter the ip address: ")
        sm = input("Please enter the subnet mask: ")
        connector.send_command(f"int vlan {vlan}\nip add {ip} {sm}\nno sh\n")
        time.sleep(2)

    def configure_security(self, connector: object) -> None:
        """
        Configures security features on the switch to enhance network security.
        This may include port security, DHCP snooping, and other features.
        """
        print(f"Configuring security on switch {self.name}...")

        interface = input("Please enter the name of the interface you want to apply security to: ")
        vlan = input("Please enter the name of the VLAN you want to be allowed to pass: ")
        mac = input("How many MAC addresses do you want to have on the port?")
        violation_type = input("What should the device do if the security is breached?")
        connector.send_command(f'int {interface}\nswitchport mode access'
                               f'\nswitchport access vlan {vlan}'
                               f'\nswitchport port-security\nswitchport port-security maximum {mac}'
                               f'\nswitchport port-security violation {violation_type}'
                               f'\nspanning-tree bpduguard disable\n')
        time.sleep(2)

    def configure_stp(self, connector: object) -> None:
        """
        Configures Spanning Tree Protocol (STP) on the switch.
        STP is used to prevent loops in the network by creating a loop-free logical topology.
        """
        print(f"Configuring Spanning Tree Protocol (STP) on switch {self.name}...")
        interfaces = input("Please enter the name of the interfaces you want to trunk: ")
        vlans = input("Please enter the name of the VLAN you want to be allowed to pass: ")
        root_bridge = input("Do you want to configure root bridge on this device? (yes/no) ")
        if root_bridge == "yes":
            vlan_prim = input("Enter the range of the VLANs you want to be root primmary. ")
            vlan_sec = input("Enter the range of the VLANs you want to be root secondary. ")

            connector.send_command(f'interface range {interfaces}\nenc dot'
                                   f'\nsw mo tr\nsw tr all vlan {vlans}'
                                   f'\nexit\nspanning-tree vlan {vlan_sec} root sec'
                                   f'\nspanning-tree vlan {vlan_prim} root prim'
                                   f'\nspanning-tree portfast\n')
            time.sleep(2)
        else:
            connector.send_command(f'interface range {interfaces}\nenc dot'
                                   f'\nsw mo tr\nsw tr all vlan {vlans}\n')

    def configure_rstp(self, connector: object) -> None:
        """
        Configures Rapid Spanning Tree Protocol (RSTP) for faster convergence compared to STP.
        This method helps in quickly recovering from network changes.
        """
        print(f"Configuring Rapid Spanning Tree Protocol (RSTP) on switch {self.name}...")
        connector.send_command(f'span mode rap\n')
        time.sleep(2)

    def configure_hsrp(self, connector: object) -> None:
        """
        Configures HSRP (Hot Standby Router Protocol) on the switch.
        HSRP provides high availability by allowing routers to take over if the primary fails.
        """
        print(f"Configuring HSRP on switch {self.name}...")
        return super().configure_hsrp(connector)

    def test_ping(self, connector: object) -> None:
        return super().test_ping(connector)

    def save_config(self, connector: object) -> None:
        super().save_config(connector)
