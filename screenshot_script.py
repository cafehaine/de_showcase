#!/usr/bin/env python3
from os import getenv
import socket
from subprocess import run, Popen, CalledProcessError
import sys
from time import sleep

import psutil


def main():
    if len(sys.argv) > 1:
        print("Starting DE in background...")
        Popen(sys.argv[1:])
        sleep(5)

    print("Waiting for DE to be ready.")

    # Wait for the DE to be ready
    sleep(5)
    while psutil.cpu_percent(interval=1) >= 10:
        sleep(1)
    print("DE should be ready.")

    # Take the screenshot
    de_name = getenv("DE_NAME", None)
    if de_name is None:
        raise ValueError("The environment variable DE_NAME isn't set.")
    path = f"/vagrant/screenshots/{de_name}.png"

    commands = [
        ["scrot", path, "--overwrite"],  # X11
        ["grim", path],  # Wayland
    ]

    for command in commands:
        result = run(command)
        if result.returncode == 0:
            break
    else:
        raise RuntimeError("No command could take a screenshot.")

    print(f"Screenshot written to {path!r}")

    # Send confirmation to the listener
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", 1042))
        sock.sendall(b"OK\n")

    print("Done.")


if __name__ == "__main__":
    main()
