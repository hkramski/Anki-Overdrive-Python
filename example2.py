from overdrive import Overdrive

def locationChangeCallback(addr, location, piece, speed, clockwise):
    # Print out addr, piece ID, location ID of the vehicle, this print everytime when location changed
    print("\033[F\033[KLocation from " + addr + " : " + "Piece=" + str(piece) + " Location=" + str(location) + " Clockwise=" + str(clockwise) + " Speed=" + str(speed))

# car = Overdrive("FA:E8:5E:4D:46:E9") # Ground Shock C
car = Overdrive("E0:31:C9:C4:F0:62") # Ground Shock A

car.setLocationChangeCallback(locationChangeCallback) # Set location change callback to function above

# start driving
car.changeSpeed(500, 1000, 1) # Set car speed with speed = 500, acceleration = 1000, respect road piece speed limit = yes


cmd = input()
while cmd != "q":
    if cmd == "l":
        car.changeLaneLeft(1000, 1000) 
    elif cmd == "r":
        car.changeLaneRight(1000, 1000) 
    else: 
        car.changeSpeed(max(0, int(cmd)), 1000, 0) 
    cmd = input()
    
car.changeSpeed(0, 1000, 1) 
car.disconnect()

