from demodules import register_module, BaseModule


@register_module
class Mate(BaseModule):
    name = "Mate"
    dependencies = ["mate", "mate-extra"]
    startup_cmd = "startx /usr/bin/mate-session"
    has_autostart = True
