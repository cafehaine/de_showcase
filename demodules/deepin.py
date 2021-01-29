import os

from demodules import register_module, BaseModule


@register_module
class Deepin(BaseModule):
    name = "Deepin"
    dependencies = ["deepin", "deepin-extra"]
    startup_cmd = "/usr/bin/startdde"
    has_autostart = False

    def start(self):
        os.makedirs("/home/vagrant/.config/deepin/deepin-wm-switcher")
        with open(
            "/home/vagrant/.config/deepin/deepin-wm-switcher/config.json", "w"
        ) as config_file:
            config_file.write(
                """
            {
                "allow_switch": true,
                "last_wm": "deepin-metacity"
            }
            """
            )
        super().start()
