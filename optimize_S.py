import simulator
import matplotlib.pyplot as plt

nl = [1,2,4,8]
sl = [8,16,32,64,128,256]

# gcc
print('######################\nGCC')
trname = './traces/val_trace_gcc.txt'
for n in nl:
    tn = []
    s = 256
    _,_,ipc_b = simulator.main(True,s,n,trname)
    ipc_min = ipc_b - ipc_b*0.05

    ipc_new = ipc_b
    
    s = 256
    while ipc_new > ipc_min:
        ipc_old = ipc_new
        s -= 1
        _,_,ipc_new = simulator.main(True,s,n,trname)
    
    print('N={},S={},Opt IPC={},Base IPC={},Min IPC={}'.format(n,s+1,ipc_old,ipc_b,ipc_min))


# perl
print('######################\nPERL')
trname = './traces/val_trace_perl.txt'
for n in nl:
    tn = []
    s = 256
    _,_,ipc_b = simulator.main(True,s,n,trname)
    ipc_min = ipc_b - ipc_b*0.05

    ipc_new = ipc_b
    s = 256
    while ipc_new > ipc_min:
        ipc_old = ipc_new
        s -= 1
        _,_,ipc_new = simulator.main(True,s,n,trname)
    
    print('N={},S={},Opt IPC={},Base IPC={},Min IPC={}'.format(n,s+1,ipc_old,ipc_b,ipc_min))