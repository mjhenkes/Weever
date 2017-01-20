import zerorpc
import piconzero as pz, time
import cmd

pz.init()
pz.setOutputConfig(0, 2)

class HelloRPC(object):
    def steer(self, degrees):
        pz.setOutput(0, degrees)
        return "%d" % degrees

class CommandLine(cmd.Cmd):
    def steer(self, line):
        print(line)

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
