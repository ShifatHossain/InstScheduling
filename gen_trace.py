import random
import os

init_addr = random.randint(0x2b6420,0x300000)

traceOut = []

cnt = 0
c_addr = init_addr
while cnt < 10000:
    o = random.randint(0,2)
    d = random.randint(-1,127)
    s1 = random.randint(-1,127)
    s2 = random.randint(-1,127)

    ttrace = hex(c_addr).split('x')[1] + ' ' + str(o) + ' ' + str(d) + ' ' + str(s1) + ' ' + str(s2) + '\n'
    traceOut.append(ttrace)
    c_addr += 4
    cnt += 1


fc = 0
while os.path.exists('./traces/val_trace_rnd{}.txt'.format(fc)):
    fc += 1    
trFile = './traces/val_trace_rnd{}.txt'.format(fc)

with open(trFile,'w') as f:
    f.writelines(traceOut)