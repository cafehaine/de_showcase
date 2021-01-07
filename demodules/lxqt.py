from demodules import register_module, BaseModule


@register_module
class LXQt(BaseModule):
    name = "LXQt"
    dependencies = ["lxqt", "breeze-icons"]
    startup_cmd = "startx /usr/bin/startlxqt"
