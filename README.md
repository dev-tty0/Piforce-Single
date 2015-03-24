# Piforce-Single

Piforce-Single is a raspberry pi image which loads a single game to a Triforce, Naomi, or Chihiro arcade system. The advantages of this system are:

- fast boot times (< 12 seconds on raspberry pi2!)
- no soldering required
- just the netdimm, a crossover cable, raspberry pi and a SD card required
- supports raspberry pi 1 & 2
- no need to use a partition manager to re-size the card
- simple installation and useage


Piforce-Single uses debugmode's triforce tools to load a NetDIMM board with binaries for a Triforce, Naomi, or Chihiro arcade system. A single game is loaded every time, which means that no soldering or additional components other than the raspberry pi and a SD card are required to netboot a game.

loading times are fast (around 12 seconds for raspberry pi2, and 22 for raspberry pi1)

# Download

The image can be downloaded here:
http://www.mediafire.com/download/tfpbeupbpd602cx/Piforce-Single_v1.0.zip

# Requirements

You will need the following items to use Piforce-Single:

- A Raspberry Pi - http://www.raspberrypi.org/
- An SD Card (4GB or greater, but any additional space wont be used)
- A Naomi, Triforce, or Chihiro arcade system.
- A Netdimm with a zero-key security PIC installed. 
- A crossover cable

The netdimm will need to be configured in static mode with an IP address of 192.168.1.2, netmask of 255.255.255.0, and gateway of 192.168.1.1.


# Installation

All that is needed is to write the image, and hook everything up. Installing the SD card image is the same as for any other raspberry pi install, so if you are familiar with that, then you are good to go, of not, there are a bunch of guides for whatever OS you are running here:
http://www.raspberrypi.org/documentation/installation/installing-images/

Once done, the card can be used in Windows/Linux/OSx, and there is a /rom directory where the game you own should be copied. 

# Usage

On powerup, the raspberry pi will automatically send the game to the naomi.

I provide this script and image without warranty etc. 


# Shouts

Thanks to travistyoj, and debugmode's triforce tools script. As travistyoj says: debugmode's done the heavy lifting this is just an interface for his work. 
