
 
import sys
import time
from gpio import * 
from ledpins import *

def lightExit (gpio):
	gpioSetVal(gpio, val="0")
	gpioUnexport(gpio)
	return 
	
def lightInit (gpio):
	gpioExport(gpio)
	gpioSetDir(gpio, flag="out")
 	gpioSetVal(gpio, val="0")
 	return
 	
def lightOn (gpio):
	gpioSetVal(gpio, val="1")
	return 
	
def lightOff (gpio):
	gpioSetVal(gpio, val="0")
	return 
	
	
def trafficInitAll():
	lightInit(str(NORTH_GREEN))
	lightInit(str(NORTH_YELLOW))
	lightInit(str(NORTH_RED))
	lightInit(str(EAST_GREEN))
	lightInit(str(EAST_YELLOW))
	lightInit(str(EAST_RED))
	lightInit(str(SOUTH_GREEN))
	lightInit(str(SOUTH_YELLOW))
	lightInit(str(SOUTH_RED))
	lightInit(str(WEST_GREEN))
	lightInit(str(WEST_YELLOW))
	lightInit(str(WEST_RED))
	return	

def trafficExitAll():
	lightExit(str(NORTH_GREEN))
	lightExit(str(NORTH_YELLOW))
	lightExit(str(NORTH_RED))
	lightExit(str(EAST_GREEN))
	lightExit(str(EAST_YELLOW))
	lightExit(str(EAST_RED))
	lightExit(str(SOUTH_GREEN))
	lightExit(str(SOUTH_YELLOW))
	lightExit(str(SOUTH_RED))
	lightExit(str(WEST_GREEN))
	lightExit(str(WEST_YELLOW))
	lightExit(str(WEST_RED))
	return	

def northOn():
	lightOff(str(EAST_YELLOW))
	lightOff(str(WEST_YELLOW))
	lightOff(str(NORTH_RED))
	

	lightOn(str(EAST_RED))
	lightOn(str(WEST_RED))
	lightOn(str(SOUTH_RED))

	lightOn(str(NORTH_GREEN))
	

	time.sleep(10)

	lightOff(str(NORTH_GREEN))
	
	lightOn(str(NORTH_YELLOW))
	
	time.sleep(1)
	return

def WestOn():
	lightOff(str(NORTH_YELLOW))
	lightOff(str(EAST_YELLOW))
	lightOff(str(SOUTH_YELLOW))
	
	lightOff(str(WEST_RED))

	lightOn(str(NORTH_RED))
	lightOn(str(SOUTH_RED))
	lightOn(str(EAST_RED))

	
	lightOn(str(WEST_GREEN))

	time.sleep(10)

	
	lightOff(str(WEST_GREEN))

	
	lightOn(str(WEST_YELLOW))
	time.sleep(1)
	return


def SouthOn():
	lightOff(str(EAST_YELLOW))
	lightOff(str(NORTH_YELLOW))
	lightOff(str(WEST_YELLOW))
	
	lightOff(str(SOUTH_RED))

	lightOn(str(EAST_RED))
	lightOn(str(WEST_RED))
	lightOn(str(NORTH_RED))

	
	lightOn(str(SOUTH_GREEN))

	time.sleep(10)

	
	lightOff(str(SOUTH_GREEN))

	
	lightOn(str(SOUTH_YELLOW))
	time.sleep(1)
	return


def eastOn():
	lightOff(str(NORTH_YELLOW))
	lightOff(str(SOUTH_YELLOW))
	lightOff(str(EAST_RED))
	

	lightOn(str(NORTH_RED))
	lightOn(str(SOUTH_RED))
	lightOn(str(WEST_RED))

	lightOn(str(EAST_GREEN))
	

	time.sleep(10)

	lightOff(str(EAST_GREEN))
	

	lightOn(str(EAST_YELLOW))
	
	time.sleep(1)
	return



	
	
try:		
	print "\nTraffic Signal Light Simulation using Python"
	print "-----------------------------------------------"
	trafficExitAll()
	trafficInitAll()
	for x in range(0, 10):
		print "\nNORTH	--> [GO]"
		print "EAST-WEST-SOUTH 	--> [STOP]\n"
		northOn()
		time.sleep(1)
		print "\nWEST	--> [GO]"
		print "NORTH-SOUTH -EAST	--> [STOP]\n"
		WestOn()
		time.sleep(1)
		print "\nSOUTH	--> [GO]"
		print "EAST-WEST-NORTH 	--> [STOP]\n"
		SouthOn()
		time.sleep(1)
		print "\nEAST	--> [GO]"
		print "NORTH-SOUTH -WEST	--> [STOP]\n"
		eastOn()
		time.sleep(1)
		
	trafficExitAll()	
	print "done"
	exit()
except KeyboardInterrupt:
	trafficExitAll()	
	print "Program Exit due to CTRL-C"
	exit()
    	sys.exit(0)

