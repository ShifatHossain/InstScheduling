import simulator
import matplotlib.pyplot as plt

nl = [1,2,4,8]
sl = [8,16,32,64,128,256]

# gcc
ns = []
trname = './traces/val_trace_gcc.txt'
for n in nl:
    tn = []
    for s in sl:
        _,_,ipc = simulator.main(True,s,n,trname)
        tn.append(ipc)
    ns.append(tn)

plt.figure()
for ni in range(len(nl)):
    plt.plot(sl,ns[ni],label='N = {}'.format(nl[ni]))

plt.legend()
plt.title('IPC-Scheduling Queue Size graph - GCC')
plt.xlabel('Scheduling Queue Size (S)')
plt.ylabel('IPC')
plt.show()


# perl
ns = []
trname = './traces/val_trace_perl.txt'
for n in nl:
    tn = []
    for s in sl:
        _,_,ipc = simulator.main(True,s,n,trname)
        tn.append(ipc)
    ns.append(tn)

plt.figure()
for ni in range(len(nl)):
    plt.plot(sl,ns[ni],label='N = {}'.format(nl[ni]))

plt.legend()
plt.title('IPC-Scheduling Queue Size graph - PERL')
plt.xlabel('Scheduling Queue Size (S)')
plt.ylabel('IPC')
plt.show()
