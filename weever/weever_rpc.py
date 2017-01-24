import zerorpc
import weever

bot = weever.Weever()
##import piconzero as pz, time
##
##pz.init()
##pz.setOutputConfig(0, 2)

class HelloRPC(object):
    def turn(self, degrees):
        bot.turn(degrees)
        return "%d" % degrees

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
