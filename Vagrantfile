Vagrant.configure("2") do |config|
  config.vm.box = "archlinux/archlinux"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = true # Only for debug
    vb.memory = "2048"
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    # disable mkinitcpio alpm hooks
    mkdir -p /etc/pacman.d/hooks
    ln -s /dev/null /etc/pacman.d/hooks/60-mkinitcpio-remove.hook
    ln -s /dev/null /etc/pacman.d/hooks/90-mkinitcpio-install.hook

    # Stop getty for tty1
    systemctl stop getty@tty1.service
    systemctl disable getty@tty1.service

    # Add a user that will auto login, and setup a bashrc
    cp /vagrant/bashrc /home/vagrant/.bashrc

    # Enable autologin for tty1 for vagrant
    mkdir -p /etc/systemd/system/getty@tty1.service.d
    cp /vagrant/getty_override.conf /etc/systemd/system/getty@tty1.service.d/override.conf

    # install common requirements
    pacman -Syu --noconfirm python python-psutil pyalpm xorg-server xorg-xinit wayland grim scrot --ignore linux,linux-firmware

    # install the screenshot script
    cp /vagrant/screenshot_script.py /usr/bin/screenshot_script.py
    chmod 755 /usr/bin/screenshot_script.py
    mkdir -p /etc/xdg/autostart
    cp /vagrant/screenshot.desktop /etc/xdg/autostart/screenshot.desktop
    chmod 644 /etc/xdg/autostart/screenshot.desktop
    mkdir -p /vagrant/screenshots

    python /vagrant/script.py
    poweroff
  SHELL
end
