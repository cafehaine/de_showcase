from demodules import register_module, BaseModule


@register_module
class Cinnamon(BaseModule):
    name = "Cinnamon"
    dependencies = ["cinnamon"]
    startup_cmd = "startx /usr/bin/cinnamon-session"
    has_autostart = True
