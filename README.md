# Ansible Playbooks for setting a Raspberry Pi as a Musical Instrument

The idea is to transform a Raspbian lite OS to a fully functional OS for being treated as an Instrument, that boots directly to sound by itself.

The base of this code (the handlers, tasks, and new-default.yml), is obtained from this other [Garth Vander Houwen Github's repo](https://github.com/garthvh/ansible-raspi-playbooks). This allows to pre-setup the Raspberry locales, Wifi Network, Update it and more things.

## Inital steps

1 - [Download Rasbian Lite image](https://downloads.raspberrypi.org/raspbian_lite_latest) (tested with the following releases of: 2016-06-21, 2017-07-05)

2 - [Install the Image onto an SD Card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

3 - Enable SSH: By "touching" a file called "ssh" inside the boot partition of the SD card, As described [here](https://hackernoon.com/raspberry-pi-headless-install-462ccabd75d0)

4 - Put the SD card, Plug your rPI to an Ethernet wire connected to your router, and Power the Raspberry on.

5 - Find your PI's IP Address: Look at your router dhcp leases or use nmap. More [details](https://www.raspberrypi.org/documentation/remote-access/ip-address.md)

6 - Update the "host" file with the IP address. Using Ansible, it allows to setup any number of network connected rPI at the same time

7 - Make you sure Ansible is installed on your computer: [Getting Ansible](http://docs.ansible.com/ansible/latest/intro_installation.html)

8 - Install sshpass, or force install it if you're using [brew](https://brew.sh) on osx:

```brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb```

9 - Install raspi_ro_root role from Ansible Galaxy

```ansible-galaxy install DinoTools.raspi_ro_root```

10 - Have your Wifi credentials and SSH key ready to paste and run this playbooks:

  Setup Hostname, Wifi and SSH Key for keyless SSH connection

```ansible-playbook -i hosts playbooks/new-default.yml```

  Puredata Install, Realtime Kernel (Disabled Temporary), Optimizations...

```ansible-playbook -i hosts playbooks/main.yml```

  Install a PD project and autorun it on boot, it also accepts one midi controller connected

```ansible-playbook -i hosts playbooks/install-patch.yml```

This is the firsts commits to start the project, ****this development is not yet in alpha****.

The first Musical software intended to run is based Puredata, for headless running of patches.
