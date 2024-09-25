import time

import paramiko


class Connection:
    """
        The Connection class manages an SSH connection to a network device using Paramiko.

        Methods:
            connect(): Establishes the SSH connection to the device.
            send_command(command): Sends a command to the device and returns the command output and error.
            close(): Closes the SSH connection if it's open.
        """
    process_list = []

    def __init__(self, device: object):
        """
        Initializes the Connection class with device information.
        """
        self.type_device = device.type_device
        self.name = device.name
        self.ip = device.ip
        self.username = device.username
        self.password = device.password
        self.priv_password = device.priv_password
        self.client = None
        self.shell = None

    def connect(self) -> None:
        """
        Establishes an SSH connection to the device using Paramiko.

        Raises:
            paramiko.AuthenticationException: If the authentication fails.
            paramiko.SSHException: If there's an error with the SSH connection.
        """
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(self.ip, username=self.username, password=self.password)
            self.shell = self.client.invoke_shell()
            self.shell.send(f'ena\n{self.priv_password}\nconf t\n')
            time.sleep(2)
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials.")
        except paramiko.SSHException as e:
            print(f"Unable to establish SSH connection: {e}")

    def send_command(self, command: str) -> None:
        """
        Sends a command to the connected device and returns the output.
        """
        self.shell.send(command)

    def view_output(self):
        """
        This function is used to watch the output of the console.
        """
        text = self.shell.recv(65535).decode("utf-8")
        print(text)

    def close(self) -> None:
        """
        Closes the SSH connection if it's open.
        """
        if self.client:
            self.client.close()
