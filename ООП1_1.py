class Little_child:
    noise=0
    def print_noise(self):
        print('noise = ' + str(self.noise))
    def __init__(self,noise):
        self.noise=noise

Baby_one=Little_child(input())
Baby_one.print_noise()
