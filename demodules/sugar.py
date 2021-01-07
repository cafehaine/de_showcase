from demodules import register_module, BaseModule


@register_module
class Sugar(BaseModule):
    name = "Sugar"
    dependencies = ["sugar", "sugar-fructose", "sugar-runner"]
    startup_cmd = "sugar-runner"
