from demodules import register_module, BaseModule


@register_module
class Sway(BaseModule):
    name = "Sway"
    dependencies = ["sway"]
    startup_cmd = "screenshot_script.py sway"
    has_autostart = True
