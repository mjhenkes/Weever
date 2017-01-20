import piconzero as pz,
import time
import cmd, argparse
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

servo_min = 244
servo_max = 488

pwm.set_pwm_freq(60)
##pz.init()
##pz.setOutputConfig(0, 2)
##pz.setOutputConfig(1, 2)
##pz.setOutput(0, 120)
##pz.setOutput(1, 120)

def pulse_end(percentage)
    return (percentage * (servo_max - servo_min))/100 + servo_min

class WeeverCLI(cmd.Cmd):
    def do_turn(self, line):
##        pz.setOutput(0, 80)
##        pz.setOutput(1, 80)
        parser = argparse.ArgumentParser()
        parser.add_argument('degrees', type=int)
        args = parser.parse_args(line.split())
        print(args.degrees)
        print(line)
        pwm.set_pwm(0, 0, pulse_end(args.degrees))
##        pz.setOutput(0, 30)
##        pz.setOutput(0, args.degrees)
##        pz.setOutput(1, args.degrees)

if __name__ == '__main__':
    WeeverCLI().cmdloop()
