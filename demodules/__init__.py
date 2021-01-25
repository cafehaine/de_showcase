from abc import ABC
import os
from subprocess import run
from typing import Collection, Dict, Optional

__all__ = [
    "gnome",
    "sway",
    "plasma",
    "enlightenment",
    "xfce4",
    "deepin",
    "sugar",
    "gnome_flashback",
    "budgie",
    "lxqt",
    "lxde",
    "cinnamon",
    "mate",
    "ukui",
    "i3",
]  # TODO generate automatically

ALL_MODULES: set["BaseModule"] = set()


class BaseModule(ABC):
    name: str = "BASE MODULE"
    dependencies: Collection[str] = []
    startup_env: Dict[str, str] = {}
    startup_cmd: str = "exit 1"
    has_autostart: bool = False

    def start(self):
        with open("/home/vagrant/gui", "w") as output:
            output.write("#!/bin/bash\n")
            for key, value in self.startup_env.items():
                output.write(f"export {key}={value}\n")
            output.write(f"export DE_NAME='{self.name}'\n")
            if not self.has_autostart:
                # relatively safe delay, should be fine on most computers
                output.write(f"sleep 10 && screenshot_script.py&\n")
            output.write(f"{self.startup_cmd}\n")

        os.chmod("/home/vagrant/gui", 0o755)

        run(["systemctl", "start", "getty@tty1.service"], check=True)

    def stop(self):
        run(["systemctl", "stop", "getty@tty1.service"], check=True)


def register_module(module):
    if not issubclass(module, BaseModule):
        raise ValueError("Tried to register module that doesn't inherit BaseModule.")
    ALL_MODULES.add(module)
