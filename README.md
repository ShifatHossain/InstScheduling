# Instruction Scheduling project for CDA5106-Advanced Computer Architecture (UCF)


## To run the simulator

python ./simulator.py \<\s> <\n> <\trace_file>

Simulator outputs are stored in "./outputs" directory

## To run the AoT scheduler

python ./scheduler/scheduler_py -a/-b/-c <\trace_file>

1. -a : LLWP heuristic
2. -b : Highest Latency heuristic
3. -c : Random heuristic

Scheduler outputs are stored in "./scheduler_outputs" directory

For each input file, the scheduler generates a un-scheduled "-si" and post scheduled "-so" file in the output directory. Each "-so" file is generated with a postfix of the heuristic function ('-llwp', '-hlat', and '-rand').

The AoT scheduler is designed based on ILOC local forward list instruction scheduler project (https://github.com/pilliq/scheduler/tree/master)
