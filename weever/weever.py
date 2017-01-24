import Adafruit_PCA9685, time, threading

##pwm = Adafruit_PCA9685.PCA9685()

##servo_min = 244
##servo_max = 488
frequency = 60
maximum_ticks = 4069
maximum_pulse_width = 2000
minimum_pulse_width = 1000

##pwm.set_pwm_freq(60)

def ticks(pulse_width):
    cycle = 1/frequency
    time_per_tick = cycle/maximum_ticks *1000000
    return pulse_width/time_per_tick

##def pulse_end(percentage):
##    return (percentage * (servo_max - servo_min))/100 + servo_min

def make_interpolater(from_min, from_max, to_min, to_max):
    from_span = from_max - from_min
    to_span = to_max - to_min

    scaler = float(to_span)/float(from_span)

    def interpolator(value):
        return to_min + (value - from_min) * scaler

    return interpolator
    
class Weever(object):
    def __init__(self):
        self.servo_min = ticks(1000)
        self.servo_max = ticks(2000)
        self.servo_center = ticks(2000-1000)
        self.degrees_interpolator = make_interpolater(-90, 90, self.servo_min, self.servo_max)
        self.percentage_interpolator = make_interpolater(-100, 100, self.servo_min, self.servo_max)
        
    # degrees value between -90 and 90
    def turn(self, degrees):
        ticks = self.degrees_interpolator(degrees)
        print('turn degrees {} = {} ticks'.format(degrees, ticks))
##        pwm.set_pwm(0, 0, ticks)

    # percentage between -100 and 100
    # duration in ms, null = infinate
    def drive(self, percentage, duration = None):
        ticks = self.percentage_interpolator(percentage)
        print('drive percentage {} = {} ticks'.format(percentage, ticks))
##        pwm.set_pwm(0, 0, ticks)
        if (duration):
            t=threading.Timer(duration * 0.001, self.reset_drive)
            t.start()

    def reset_drive(self):
        print ('drive reset')
##        pwm.set_pwm(0, 0, self.servo_center)
        
    # x and y degrees between -90 and 90
    def look(self, x, y):
        print('look')
        
    # lights bool. true enables false disables
    def lights(self, lights):
        print('lights')
        
