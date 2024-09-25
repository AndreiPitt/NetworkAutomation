def check_out(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        device = args[1]
        if device.shell:
            text = device.shell.recv(65535).decode("utf-8")
            print("Output from the device shell:")
            print(text)
        return result

    return wrapper

