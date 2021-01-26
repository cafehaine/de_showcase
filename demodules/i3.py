from demodules import register_module, BaseModule


@register_module
class I3(BaseModule):
    name = "i3"
    dependencies = ["i3", "ttf-dejavu"]
    startup_cmd = "/usr/bin/i3"
    has_autostart = False
