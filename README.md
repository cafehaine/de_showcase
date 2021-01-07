# Desktop Environment Showcase
## What is DE Showcase?

Desktop Environment Showcase is a small project meant to create screenshot of
'stock' configurations of most Linux desktop environments.

It is based on an Arch Linux Vagrant box, and some python scripts to automate
the setup and startup of each desktop environment.

I've built this since those UIs tend to change regularly, but I'm too lazy to
create VMs to try those out regularly, so creating screenshots of the desktop
is a good compromise in my opinion.

## What DE am I planning to support?

All the DEs that are listed as 'Officially supported' on the ArchWiki, but also
some window managers (i3, sway…):

- Desktop Environments:
  - [x] Budgie
  - [x] Cinnamon
  - [ ] **WIP** Deepin (need to proceed through setup wizard)
  - [ ] **WIP** Enlightenment (need to proceed through setup wizard)
  - [x] GNOME
  - [x] GNOME Flashback
  - [ ] **WIP** KDE Plasma (no longer starts)
  - [x] LXDE (gtk3 version)
  - [ ] **WIP** LXQt (completely unreadable, needs debugging)
  - [x] MATE
  - [ ] **WIP** Sugar (need to proceed through setup wizard)
  - [x] UKUI
  - [x] Xfce
- Window managers
  - [x] i3
  - [x] sway

I'm open to adding more environments to this list, if it's not too hard to setup
on Arch Linux.
