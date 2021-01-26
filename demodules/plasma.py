from demodules import register_module, BaseModule


@register_module
class Plasma(BaseModule):
    name = "Plasma"
    dependencies = ["plasma"]
    startup_env = {"DESKTOP_SESSION": "plasma"}
    startup_cmd = "startplasma-x11"
    has_autostart = False
