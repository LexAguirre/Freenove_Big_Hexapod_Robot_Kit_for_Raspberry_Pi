import time

def test_Led():
    from led import Led
    led = Led()
    try:
        #Red wipe
        print ("\nRed wipe")
        led.color_wipe([255, 0, 0]) 
        time.sleep(1)

        #Green wipe
        print ("\nGreen wipe")
        led.color_wipe([0, 255, 0]) 
        time.sleep(1)
    
        #Blue wipe
        print ("\nBlue wipe")
        led.color_wipe([0, 0, 255]) 
        time.sleep(1)

        #White wipe
        print ("\nWhite wipe")
        led.color_wipe([255, 255, 255]) 
        time.sleep(1)
    
        led.color_wipe([0, 0, 0])   #turn off the light
        print ("\nEnd of program")
    except KeyboardInterrupt:
        led.color_wipe([0, 0, 0])   #turn off the light
        print ("\nEnd of program")

def test_Ultrasonic():
    from ultrasonic import Ultrasonic
    ultrasonic=Ultrasonic()
    try:
        while True:
            data=ultrasonic.get_distance()   #Get the value
            print ("Obstacle distance is "+str(data)+"CM")
            time.sleep(0.01)
    except KeyboardInterrupt:
        print ("\nEnd of program")

def test_Servo():
    from servo import Servo
    servo = Servo()
    try:
        for i in range(50):
            servo.set_servo_angle(15,90+i)
            servo.set_servo_angle(12,90+i)
            servo.set_servo_angle(9,90+i)
            servo.set_servo_angle(16,90+i)
            servo.set_servo_angle(19,90+i)
            servo.set_servo_angle(22,90+i)
            time.sleep(0.005)
        for i in range(60):
            servo.set_servo_angle(14,90+i)
            servo.set_servo_angle(11,90+i)
            servo.set_servo_angle(8,90+i)
            servo.set_servo_angle(17,90-i)
            servo.set_servo_angle(20,90-i)
            servo.set_servo_angle(23,90-i)
            time.sleep(0.005)
        for i in range(120):
            servo.set_servo_angle(13,i)
            servo.set_servo_angle(10,i)
            servo.set_servo_angle(31,i)
            servo.set_servo_angle(18,180-i)
            servo.set_servo_angle(21,180-i)
            servo.set_servo_angle(27,180-i)
            time.sleep(0.005)
        print ("\nEnd of program")      
        servo.relax()
    except KeyboardInterrupt:
        servo.relax()
        print ("\nEnd of program")

def test_Servo_Channel(channel, min_angle=60, max_angle=120, hold=1.0):
    from servo import Servo
    servo = Servo()
    try:
        if channel < 0 or channel > 31:
            print ("Channel must be between 0 and 31")
            return

        print ("Testing servo channel: " + str(channel))
        print ("Move to " + str(min_angle))
        servo.set_servo_angle(channel, min_angle)
        time.sleep(hold)

        print ("Move to " + str(max_angle))
        servo.set_servo_angle(channel, max_angle)
        time.sleep(hold)

        print ("Move to 90 (center)")
        servo.set_servo_angle(channel, 90)
        time.sleep(hold)

        print ("\nEnd of program")
        servo.relax()
    except KeyboardInterrupt:
        servo.relax()
        print ("\nEnd of program")

def set_servo_neutral(channel):
    from servo import Servo
    servo = Servo()
    if channel < 0 or channel > 31:
        print ("Channel must be between 0 and 31")
        return
    servo.set_servo_angle(channel, 90)
    print ("Servo " + str(channel) + " set to neutral angle 90")
    servo.relax()


def test_Adc():
    from adc import ADC
    adc = ADC()
    try:
        while True:
            Power=adc.read_battery_voltage()
            print ("The battery voltage is "+str(Power)+'\n')
            time.sleep(1)
    except KeyboardInterrupt:
        print ("\nEnd of program")

def test_Buzzer():
    from buzzer import Buzzer
    buzzer = Buzzer()
    try:
        buzzer.set_state(True)
        time.sleep(1)
        print ("1S")
        time.sleep(1)
        print ("2S")
        time.sleep(1)
        print ("3S")
        buzzer.set_state(False)
        print ("End of program")
    except KeyboardInterrupt:
        buzzer.set_state(False)
        print ("End of program")

def test_Buzzer_Song():
    from buzzer import Buzzer
    buzzer = Buzzer()
    # Imperial March-inspired rhythm for an active buzzer (single tone).
    song_pattern = [
        # DA DA DA - DAAAH
        (0.16, 0.08), (0.16, 0.08), (0.16, 0.08), (0.48, 0.20),
        # DA DA DA - DAAAH
        (0.16, 0.08), (0.16, 0.08), (0.16, 0.08), (0.48, 0.20),
        # DA DA DA DA DAAAH
        (0.16, 0.08), (0.16, 0.08), (0.16, 0.08), (0.16, 0.08), (0.48, 0.20),
        # Transition
        (0.14, 0.07), (0.14, 0.07), (0.14, 0.07), (0.32, 0.18),
    ]
    try:
        print ("\nPlaying buzzer song...")
        for on_time, off_time in song_pattern:
            buzzer.set_state(True)
            time.sleep(on_time)
            buzzer.set_state(False)
            time.sleep(off_time)
        print ("Song finished")
    except KeyboardInterrupt:
        print ("\nSong interrupted")
    finally:
        buzzer.set_state(False)
        

if __name__ == '__main__':
    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the device")
        print ("Usage: sudo python3 test.py [Led|Ultrasonic|Servo|ADC|Buzzer|BuzzerSong] [channel]")
        exit() 
    if sys.argv[1] == 'Led':
        test_Led()
    elif sys.argv[1] == 'Ultrasonic':
        test_Ultrasonic()
    elif sys.argv[1] == 'Servo': 
        if len(sys.argv) >= 3:
            try:
                channel = int(sys.argv[2])
                test_Servo_Channel(channel)
            except ValueError:
                print ("Channel must be an integer")
        else:
            test_Servo()               
    elif sys.argv[1] == 'ADC':   
        test_Adc()  
    elif sys.argv[1] == 'Buzzer':   
        test_Buzzer()
    elif sys.argv[1] == 'BuzzerSong':
        test_Buzzer_Song()
    elif sys.argv[1] == 'Serv_nut':
        print("Setting servo to neutral position")
        print("Channel:", int(sys.argv[2]))
        set_servo_neutral(int(sys.argv[2]))
    elif sys.argv[1] == 'Serv_max':
        print("Setting servo to maximum position")
        print("Channel:", int(sys.argv[2]))
        test_Servo_Channel(int(sys.argv[2]))
