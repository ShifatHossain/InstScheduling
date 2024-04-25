# Instruction Scheduling project for CDA5106-Advanced Computer Architecture (UCF)

Authors: M Shifat Hossain, Tasbiraha Athaya, Rony Chowdhury Ripan, M Iffat Hossain, Maruf Chowdhury, Fahimul Aleem

Report file: Ahead_of_Time__AOT__Instruction_Scheduling.pdf


## Basic Tomasulo's simulator

### To run the simulator

python ./simulator.py \<\s> <\n> <\trace_file>

Simulator outputs are stored in "./outputs" directory

### To plot the figures of Q1 in project instructions (Fig.3 in paper)

python ./run_simulator.py

### To get the optimized scheduling quque size (S) (Q2 in project instruction, Table I in paper)

python ./optimize_S.py


## AoT Scheduler

### To run the AoT scheduler on traces

python ./scheduler/scheduler_py -a/-b/-c <\trace_file>

1. -a : LLWP heuristic
2. -b : Highest Latency heuristic
3. -c : Random heuristic

Scheduler outputs are stored in "./scheduler_outputs" directory

For each input file, the scheduler generates a un-scheduled "-si" and post scheduled "-so" file in the output directory. Each "-so" file is generated with a postfix of the heuristic function ('-llwp', '-hlat', and '-rand').

The AoT scheduler is designed based on ILOC local forward list instruction scheduler project (https://github.com/pilliq/scheduler/tree/master)

### To run the simulator for the AoT scheduled traces

After you have scheduled both the GCC and PERL traces using the AoT scheduler for all three heuristics (LLWP, HLat, and Random), you can run the following command to generate the bar charts (Fig.5 in paper):

python ./run_simulator_scheduled.py
