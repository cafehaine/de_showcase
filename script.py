#!/usr/bin/env python3
from shutil import rmtree
import socket
import time

from demodules import *

# needed to import all de modules
from demodules import ALL_MODULES, BaseModule
from pacman import Pacman

SOCK_PORT = 1042
SOCK_MESSAGE = b"OK\n"
SOCK_TIMEOUT = 30


class InvalidMessage(ValueError):
    pass


def wait_socket(sock: socket.socket) -> None:
    sock.settimeout(30)
    conn, addr = sock.accept()
    msg = conn.recv(len(SOCK_MESSAGE))
    if msg != SOCK_MESSAGE:
        raise InvalidMessage("Received invalid message.")
    conn.close()


def handle_module(pacman: Pacman, instance: BaseModule, sock: socket.socket) -> None:
    packages = pacman.get_installed_packages()
    print(f"Demoing module {instance.name}...")
    pacman.install_packages(instance.dependencies)
    # start de
    instance.start()
    # wait for the de to be ready
    try:
        wait_socket(sock)
        print("Screenshot taken")
    except socket.timeout:
        print("Timed out waiting for the screenshot script.")
    except InvalidMessage:
        print("Received an invalid message from the screenshot script.")
    except Exception as exc:
        print("Unknown exception:")
        print(exc)
    # disconnect
    instance.stop()
    # Cleanup files
    current = pacman.get_installed_packages()
    to_uninstall = current - packages
    pacman.uninstall_packages(to_uninstall)
    rmtree("/home/vagrant/.local", ignore_errors=True)
    rmtree("/home/vagrant/.config", ignore_errors=True)
    rmtree("/home/vagrant/Desktop", ignore_errors=True)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("", SOCK_PORT))
        sock.listen(1)
        pacman = Pacman()
        for Module in ALL_MODULES:
            handle_module(pacman, Module(), sock)


if __name__ == "__main__":
    main()
