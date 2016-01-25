from threading import Timer


pitft = PiTFT_GPIO()
sleep = False


def shadow():
  pitft.Backlight(False)
  global sleep
  sleep = True




while True:
    global sleep 
    if sleep == False:
	t = Timer(120.0, shadow)
	t.start()
  
    if pitft.pressed:
        pitft.Backlight(True)
        global sleep
        sleep = False
	
    if pitft.Button3:
        print "Button 3 pressed"
    if pitft.Button4:
        print "Button 4 pressed"