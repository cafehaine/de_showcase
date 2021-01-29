from demodules import register_module, BaseModule


@register_module
class Sugar(BaseModule):
    name = "Sugar"
    dependencies = ["sugar", "sugar-fructose"]
    startup_cmd = "/usr/bin/sugar"
    has_autostart = False
