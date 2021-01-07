from demodules import register_module, BaseModule


@register_module
class GnomeFlashback(BaseModule):
    name = "Gnome Flashback"
    dependencies = ["gnome", "gnome-flashback"]
    startup_env = {"XDG_CURRENT_DESKTOP": "GNOME-Flashback:GNOME"}
    startup_cmd = "startx /usr/bin/gnome-session --session=gnome-flashback-metacity"
    has_autostart = True
