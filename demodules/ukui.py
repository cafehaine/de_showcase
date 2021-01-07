from demodules import register_module, BaseModule


@register_module
class UKUI(BaseModule):
    name = "UKUI"
    dependencies = ["ukui"]
    startup_cmd = "startx /usr/bin/ukui-session"
    has_autostart = True
