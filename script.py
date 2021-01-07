#!/usr/bin/env python3
from subprocess import run
import time

from demodules import *

# needed to import all de modules
from demodules import ALL_MODULES
from pacman import Pacman


def main():
    pacman = Pacman()
    packages = pacman.get_installed_packages()
    for module in ALL_MODULES:
        instance = module()
        print(f"Demoing module {instance.name}...")
        pacman.install_packages(instance.dependencies)
        # start de
        instance.start()
        # wait for the de to be ready
        time.sleep(30)  # TODO listen for a screenshot_script.sh signal
        # disconnect
        instance.stop()
        # Cleanup files
        current = pacman.get_installed_packages()
        to_uninstall = current - packages
        pacman.uninstall_packages(to_uninstall)


if __name__ == "__main__":
    main()
