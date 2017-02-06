import Adafruit_PCA9685, time, threading

pwm = Adafruit_PCA9685.PCA9685()

##servo_min = 244
##servo_max = 488
frequency = 60
maximum_ticks = 4069
maximum_pulse_width = 2000
minimum_pulse_width = 1100

pwm.set_pwm_freq(60)

def ticks(pulse_width):
    cycle = 1/frequency
    time_per_tick = cycle/maximum_ticks *1000000
    return pulse_width/time_per_tick

def make_interpolater(from_min, from_max, to_min, to_max, inverted = False):
    from_min_prime = from_min if not inverted else from_max
    from_max_prime = from_max if not inverted else from_min
    
    from_span = from_max_prime - from_min_prime
    to_span = to_max - to_min

    scaler = float(to_span)/float(from_span)

    def interpolator(value):
        return int(to_min + (value - from_min_prime) * scaler)

    return interpolator
    
class Weever(object):
    def __init__(self):
        self.servo_min = ticks(minimum_pulse_width)
        self.servo_max = ticks(maximum_pulse_width)
        self.servo_center = int(ticks((maximum_pulse_width-minimum_pulse_width)/2 + minimum_pulse_width))
        self.degrees_interpolator = make_interpolater(-90, 90, self.servo_min, self.servo_max)
        self.percentage_interpolator = make_interpolater(-100, 100, self.servo_min, self.servo_max, True)
        self.turn(0)
        self.drive(0)
        
    # degrees value between -90 and 90
    def turn(self, degrees):
        self.steering_angle = degrees
        ticks = self.degrees_interpolator(degrees)
        print('turn degrees {} = {} ticks'.format(degrees, ticks))
        pwm.set_pwm(0, 0, ticks)

    # percentage between -100 and 100
    # duration in ms, null = infinate
    def drive(self, percentage, duration = None):
        if('timer' in locals()):
            self.timer.cancel()
        
        self.thrust = percentage
        ticks = self.percentage_interpolator(percentage)
        print('drive percentage {} = {} ticks'.format(percentage, ticks))
        pwm.set_pwm(1, 0, ticks)
        if (duration):
            self.timer = threading.Timer(duration * 0.001, self.brake)
            self.timer.start()

    def brake(self, duration = 2000):
        print ('brake duration {}'.format(duration))
        if (self.thrust > 0):
            self.drive(-50, duration)
        else:
            self.drive(0)
        
    # x and y degrees between -90 and 90
    def look(self, x, y):
        print('look')
        
    # lights bool. true enables false disables
    def lights(self, lights):
        print('lights')
        
