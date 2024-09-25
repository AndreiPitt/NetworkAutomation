import time

from Devices import Devices


class Router(Devices):
    """
    The Router class inherits from the Devices class and adds specific methods to configure
    the various options available in the menu for routers.

    Methods:
        configure_interface(): Configures network interfaces on the router.
        configure_staticroute(): Configures static routes on the router.
        configure_rip_v2(): Configures RIP version 2 on the router.
        configure_dhcp(): Configures DHCP settings on the router.
        configure_hsrp(): Configures HSRP (Hot Standby Router Protocol) on the router.
        test_ping(): Tests network connectivity using ping.
    """

    def __init__(self, type_device, name, ip, username, password, priv_password):
        """
        Initializes a Router object, inheriting attributes from the Devices class.
        """
        super().__init__(type_device, name, ip, username, password, priv_password)

    def configure_interface(self, connector: object) -> None:
        """
        Configures the network interface on the router.
        This method would typically interact with the router to configure the interface settings.
        """
        print(f"Configuring interface on router {self.name}...")

        interface = input("Please enter the name of the interface you want to apply security to: ")
        ip = input("Enter the IP Address: ")
        sm = input("Enter the subnet mask: ")
        connector.send_command(f"int {interface}\nip add {ip} {sm}\nno sh\nexit")
        time.sleep(2)

    def configure_staticroute(self, connector: object) -> None:
        """
        Configures static routes on the router.
        """
        print(f"Configuring static routes on router {self.name}...")
        network = input("Network1: ")
        sm = input("Subnet Mask: ")
        choise = input("Do you want to use next_hop ip address or exit interface? (next_hop / interface)")
        if choise == "next_hop":
            next_hop = input("The ip address of the next hop.")
            connector.send_command(f'ip route {network} {sm} {next_hop}')
        else:
            int_out = input("The interface: ")
            connector.send_command(f'ip route {network} {sm} {int_out}')

    def configure_rip_v2(self, connector: object) -> None:
        """
        Configures RIP version 2 (Routing Information Protocol) on the router.
        RIP v2 is a distance-vector routing protocol used in smaller networks.
        """
        print(f"Configuring RIP v2 on router {self.name}...")

        network_1 = input("Network1: ")
        network_2 = input("Network2: ")
        redistribute = input("Do you want to use redistribute? (yes / no)")
        if redistribute == "yes":
            connector.send_command(f'router rip\nversion 2\nno auto-summary\nnetwork {network_1}\n'
                                             f'network {network_2}\n')
            time.sleep(2)
        else:
            connector.send_command(f'router rip\nversion 2\nno auto-summary\nredistribute static\n'
                                             f'network {network_1}\nnetwork {network_2}\n')
            time.sleep(2)

    def configure_dhcp(self, connector: object) -> None:
        """
        Configures DHCP (Dynamic Host Configuration Protocol) on the router.
        This allows the router to dynamically assign IP addresses to devices on the network.
        """
        print(f"Configuring DHCP on router {self.name}...")
        excluded_address = input("What range of address do you want to exclude: (eg 192.168.1.1-192.168.1.20) ")
        pool = input("Name of the pool: ")
        network = input("Network: ")
        def_router = input("Default-router: ")
        dns = input("DNS: ")
        connector.send_command(f"ip dhcp excluded-address {excluded_address}\nip dhcp pool {pool}\n"
                                         f"network {network}\ndefault-router {def_router}\n"
                                         f"dns-server {dns}\nexit\n")
        time.sleep(2)

    def configure_hsrp(self, connector: object) -> None:
        """
        Configures HSRP (Hot Standby Router Protocol) on the router.
        HSRP provides high availability by enabling routers to take over if the primary fails.
        """
        print(f"Configuring HSRP on router {self.name}...")
        return super().configure_hsrp(connector)

    def test_ping(self, connector: object) -> None:
        return super().test_ping(connector)
