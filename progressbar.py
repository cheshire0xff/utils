import sys
import subprocess
import time

class Bar:
    def __init__(self, title, maxvalue, unit = ''):
        self.progress = 0
        self.title = title
        self.size  = 100
        self.maxval = maxvalue
        self.unit = unit
        self.barstartpos = 0
    def __enter__(self):
        self.draw()
        self.starttime = time.time()
        return self
    def __exit__(self, *args):
        elapsedtime = time.time() - self.starttime
        if elapsedtime:
            freq = self.maxval / elapsedtime
        else:
            freq = 0
        maxvallength = len(str(self.maxval))
        offset = 10 - 1 + maxvallength
        print(self.title + '\t' + f'%{offset}.1f' % freq + self.unit + '/s [' + '#' * self.size + '] 100%')

    def update(self, value): 
        percentage = value / self.maxval
        filledcount = int(self.size * percentage)
        print(self.title + '\t' +'%10d/%d' % (value, self.maxval) + self.unit +  ' [' + '#'*filledcount +\
                '.'*(self.size- filledcount) + '] %3d' % (percentage * 100) + '%',\
                end='\r')
    def getterminalwidth(self):
        try:
            output = subprocess.getoutput('stty size')
            width = int(output.split()[1])
            width = width - 50
            if width < 2:
                width = 2
            return width
        except:
            pass
    def draw(self):
        self.size = self.getterminalwidth()
        self.update(0)
