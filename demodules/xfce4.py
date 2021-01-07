from demodules import register_module, BaseModule


@register_module
class Xfce4(BaseModule):
    name = "Xfce4"
    dependencies = ["xfce4", "xfce4-goodies"]
    startup_cmd = "startxfce4"
    has_autostart = True
