from demodules import register_module, BaseModule


@register_module
class LXQt(BaseModule):
    name = "LXQt"
    dependencies = ["lxqt", "breeze-icons", "ttf-dejavu"]
    startup_cmd = "startx /usr/bin/startlxqt"
    has_autostart = True
