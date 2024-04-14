import simulator
import matplotlib.pyplot as plt
import numpy as np

nl = [1,2,4,8]
sl = [1,2,8,16,32,64,128,256]

# gcc
ns = []
trI = './scheduler_outputs/val_trace_gcc-si.txt'
trO_llwp = './scheduler_outputs/val_trace_gcc-llwp-so.txt'
trO_hlat = './scheduler_outputs/val_trace_gcc-hlat-so.txt'
trO_rand = './scheduler_outputs/val_trace_gcc-rand-so.txt'
for s in sl:
    tn = []
    for n in nl:
        _,_,ipcI = simulator.main(True,s,n,trI)
        _,_,ipcO_llwp = simulator.main(True,s,n,trO_llwp)
        _,_,ipcO_hlat = simulator.main(True,s,n,trO_hlat)
        _,_,ipcO_rand = simulator.main(True,s,n,trO_rand)
        tn.append([ipcI,ipcO_llwp,ipcO_hlat,ipcO_rand])
    ns.append(tn)

for si in range(len(sl)):
    # si = 0
    plt.figure()

    bar_data = {
        'No AoT scheduling': [ns[si][e][0] for e in range(len(ns[si]))],
        'LLWP': [ns[si][e][1] for e in range(len(ns[si]))],
        'Highest Latency': [ns[si][e][2] for e in range(len(ns[si]))],
        'Random': [ns[si][e][3] for e in range(len(ns[si]))],
    }

    x = np.arange(len(nl))
    width = 0.2
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in bar_data.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        # ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel('IPC')
    ax.set_title('IPC with and without AoT scheduling: GCC (S={})'.format(sl[si]))
    ax.set_xticks(x + width, nl)
    ax.set_xlabel('N')
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, max(max(ns[si]))*1.3)
    # plt.show()
    figfnm = 'P_GCC_{}.png'.format(sl[si])
    plt.savefig(figfnm)


# perl
ns = []
trI = './scheduler_outputs/val_trace_perl-si.txt'
trO_llwp = './scheduler_outputs/val_trace_perl-llwp-so.txt'
trO_hlat = './scheduler_outputs/val_trace_perl-hlat-so.txt'
trO_rand = './scheduler_outputs/val_trace_perl-rand-so.txt'
for s in sl:
    tn = []
    for n in nl:
        _,_,ipcI = simulator.main(True,s,n,trI)
        _,_,ipcO_llwp = simulator.main(True,s,n,trO_llwp)
        _,_,ipcO_hlat = simulator.main(True,s,n,trO_hlat)
        _,_,ipcO_rand = simulator.main(True,s,n,trO_rand)
        tn.append([ipcI,ipcO_llwp,ipcO_hlat,ipcO_rand])
    ns.append(tn)

for si in range(len(sl)):
    # si = 0
    plt.figure()

    bar_data = {
        'No AoT scheduling': [ns[si][e][0] for e in range(len(ns[si]))],
        'LLWP': [ns[si][e][1] for e in range(len(ns[si]))],
        'Highest Latency': [ns[si][e][2] for e in range(len(ns[si]))],
        'Random': [ns[si][e][3] for e in range(len(ns[si]))],
    }

    x = np.arange(len(nl))
    width = 0.2
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in bar_data.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        # ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel('IPC')
    ax.set_title('IPC with and without AoT scheduling: Perl (S={})'.format(sl[si]))
    ax.set_xticks(x + width, nl)
    ax.set_xlabel('N')
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, max(max(ns[si]))*1.3)
    # plt.show()
    figfnm = 'P_PERL_{}.png'.format(sl[si])
    plt.savefig(figfnm)
