import socket


def is_online():
    try:
        # connect to the host -- tells us if the host is actually zvailable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

print("net test imported")
