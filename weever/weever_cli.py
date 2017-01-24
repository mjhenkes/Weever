import time
import cmd, argparse
import weever

bot = weever.Weever()

class WeeverCLI(cmd.Cmd):
    def do_turn(self, line):
        parser = argparse.ArgumentParser()
        parser.add_argument('degrees', type=int)
        args = parser.parse_args(line.split())
        bot.turn(args.degrees)

    def do_drive(self, line):
        parser = argparse.ArgumentParser()
        parser.add_argument('percentage', type=int)
        parser.add_argument('-d','--duration', type=int)
        args = parser.parse_args(line.split())
        bot.drive(args.percentage, args.duration)

if __name__ == '__main__':
    WeeverCLI().cmdloop()
