from demodules import register_module, BaseModule


@register_module
class Enlightenment(BaseModule):
    name = "Enlightenment"
    dependencies = ["enlightenment"]
    startup_cmd = "/usr/bin/enlightenment_start"
    has_autostart = False
