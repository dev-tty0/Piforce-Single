import os, collections, signal, sys, subprocess, socket
import triforcetools
#from systemd import daemon
from time import sleep

#logfile = open('/tmp/log.txt', 'w')             # open input file
rom_dir = '/boot/rom/'

#foundromfiles = os.popen('ls '+rom_dir).readlines( )
foundromfiles = [romf[:-1] for romf in os.popen('ls '+rom_dir)]

rom = romf.rstrip()
#print "rom = "+rom

while True:

                try:
                    triforcetools.connect('192.168.1.2', 10703)
                except:
                    #logfile.write("Error:\nConnect Failed")
                    continue

                #logfile.write("Sending...")

                triforcetools.HOST_SetMode(0, 1)
                triforcetools.SECURITY_SetKeycode("\x00" * 8)
				#argv[0] not games(selection)
                triforcetools.DIMM_UploadFile(rom_dir+rom)
                triforcetools.HOST_Restart()
                triforcetools.TIME_SetLimit(10*60*1000)
                triforcetools.disconnect()

                #logfile.write("Transfer\nComplete!")
                sleep(5)
		exit()
				

