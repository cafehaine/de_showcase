from demodules import register_module, BaseModule


@register_module
class Plasma(BaseModule):
    name = "Plasma"
    dependencies = ["plasma"]
    # TODO switch back to x11
    startup_env = {"XDG_SESSION_TYPE": "wayland"}
    startup_cmd = "dbus-run-session startplasma-wayland"
    has_autostart = True
