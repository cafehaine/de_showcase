# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# If running trom tty1 and WAYLAND_DISPLAY isn't set, start GUI
if [ $(tty) == "/dev/tty1" ]; then
	source ~/gui
	exit 0
fi
