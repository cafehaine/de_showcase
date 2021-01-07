from demodules import register_module, BaseModule


@register_module
class Enlightenment(BaseModule):
    name = "Enlightenment"
    dependencies = ["enlightenment"]
    startup_cmd = "startx /usr/bin/enlightenment_start"
