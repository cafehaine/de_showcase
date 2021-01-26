from demodules import register_module, BaseModule


@register_module
class Sugar(BaseModule):
    name = "Sugar"
    dependencies = ["sugar", "sugar-fructose", "sugar-runner"] # TODO sugar-runner no longer needed?
    startup_cmd = "/usr/bin/sugar"
    has_autostart = False
