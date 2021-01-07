from demodules import register_module, BaseModule


@register_module
class Budgie(BaseModule):
    name = "Budgie"
    dependencies = ["gnome", "budgie-desktop"]
    startup_env = {"XDG_CURRENT_DESKTOP": "Budgie:GNOME"}
    startup_cmd = "startx /usr/bin/budgie-desktop"
    has_autostart = True
