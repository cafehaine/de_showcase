from subprocess import run
from typing import Collection

from pyalpm import Handle


class Pacman:
    """A class to simplify interactions with the pyalpm library."""

    def __init__(self, root: str = "/", dbpath: str = "/var/lib/pacman"):
        # TODO initialize pyalpm
        # handle = Handle(".", "/var/lib/pacman")
        # self._db = handle.get_localdb()
        pass

    def get_installed_packages(self) -> set[str]:
        """Return a set of currently installed packages."""
        # TODO use pyalpm
        # return set(pkg.name for pkg in self._db.search('.*'))
        pacman = run(["pacman", "-Qq"], capture_output=True, check=True)
        return set(pacman.stdout.decode("utf-8").split("\n"))

    def install_packages(self, packages: Collection[str]) -> None:
        """Install the given packages."""
        # TODO use pyalpm
        run(["pacman", "-S", "--noconfirm"] + list(packages), check=True)

    def uninstall_packages(self, packages: Collection[str]) -> None:
        """Uninstall the given packages."""
        # TODO use pyalpm
        run(["pacman", "-R", "--noconfirm"] + list(packages), check=True)
