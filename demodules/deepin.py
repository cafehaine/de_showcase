from demodules import register_module, BaseModule


@register_module
class Deepin(BaseModule):
    name = "Deepin"
    dependencies = ["deepin", "deepin-extra"]
    startup_cmd = "startx /usr/bin/startdde"
    has_autostart = True
