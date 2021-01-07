from demodules import register_module, BaseModule


@register_module
class Gnome(BaseModule):
    name = "Gnome"
    dependencies = ["gnome"]
    startup_env = {"XDG_SESSION_TYPE": "x11", "GDK_BACKEND": "x11"}
    startup_cmd = "startx /usr/bin/gnome-session"
    has_autostart = True
