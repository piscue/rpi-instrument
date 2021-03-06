# Ansible Playbooks for setting a Raspberry Pi as a Musical Instrument

The idea is to transform a Raspbian lite OS to a fully functional OS for being treated as an Instrument, that boots directly to sound by itself.

Currently, It has support for 1 MCP3008, 2 MPR121, 4 Switches (GPIO), 1 Led (GPIO), 1 Midi IN USB Core Midi interface and some external DACs based on "hifiberry" (PCM5102), IQaudIO Pi-DAC+, and Core Audio USB interfaces.

It also does some performance tuning, system setting, puredata configuration, install puredata and related libraries. It also has support to GrandOrgue install and Autostart via variable (Don't use raspbian lite, use the normal one that provides Desktop environment).

## Inital steps

1 - [Download Rasbian "Jessie" Lite image](https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2016-11-29/2016-11-25-raspbian-jessie-lite.zip) or [Download a normal Rasbian "Jessie" image with Desktop](https://downloads.raspberrypi.org/raspbian/images/raspbian-2016-11-29/2016-11-25-raspbian-jessie.zip) (tested with the following release of: 2016-06-21, 2016-11-25) - Newer releases break the way to interact with SPI for the MCP3008.

2 - [Install the Image onto an SD Card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

3 - Enable SSH: By "touching" a file called "ssh" inside the boot partition of the SD card, As described [here](https://hackernoon.com/raspberry-pi-headless-install-462ccabd75d0)

4 - Put the SD card, Plug your rPI to an Ethernet wire connected to your router, and Power the Raspberry on.

5 - Find your PI's IP Address: ( ping raspberrypi.local ) Look at your router dhcp leases or use nmap. More [details](https://www.raspberrypi.org/documentation/remote-access/ip-address.md)

6 - Update the "host" file with the IP address. Using Ansible, it allows to setup any number of network connected rPI at the same time

7 - Make you sure Ansible (Tested on 2.3.1, 2.4.3, 2.7.3 on OSX) is installed on your computer: [Getting Ansible](http://docs.ansible.com/ansible/latest/intro_installation.html)

8 - Install sshpass, or force install it if you're using [brew](https://brew.sh) on osx:

```brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb```

9 - Have your Wifi credentials and SSH key ready to paste and run this playbooks:

  Setup Hostname, Wifi and SSH Key for keyless SSH connection
  Puredata Install, Realtime Kernel (Disabled Temporary), Optimizations...

  Check the variables inside playbooks/main.yml, to setup properly

```ansible-playbook -i hosts playbooks/main.yml```

  Install a PD project and autorun it on boot, it also accepts one midi controller connected
  It comes with supersimple patch that sounds like a weird siren just to test that audio works properly

```ansible-playbook -i hosts playbooks/install-patch.yml```

The first Musical software intended to run is based Puredata, for headless running of patches.

Resources based: [Garth Vander Houwen Github's repo](https://github.com/garthvh/ansible-raspi-playbooks)
