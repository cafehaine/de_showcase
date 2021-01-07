from demodules import register_module, BaseModule


@register_module
class LXDE(BaseModule):
    name = "LXDE"
    dependencies = ["lxde-gtk3"]
    startup_cmd = "startx /usr/bin/startlxde"
    has_autostart = True
