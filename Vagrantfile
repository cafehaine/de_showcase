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

    # Add a user that will auto login, and setup a bashrc
    useradd -m deshowcase
    cp /vagrant/bashrc /home/deshowcase/.bashrc

    # Enable autologin for tty1 for deshowcase
    mkdir -p /etc/systemd/system/getty@tty1.service.d
    cp /vagrant/getty_override.conf /etc/systemd/system/getty@tty1.service.d/override.conf

    # install common requirements
    pacman -Syu --noconfirm python pyalpm xorg-server xorg-xinit wayland grim scrot --ignore linux,linux-firmware

    # install the screenshot script
    cp /vagrant/screenshot_script.sh /usr/bin/screenshot_script.sh
    chmod +x /usr/bin/screenshot_script.sh
    cp /vagrant/screenshot.desktop /etc/xdg/autostart/screenshot.desktop

    python /vagrant/script.py
    poweroff
  SHELL
end
