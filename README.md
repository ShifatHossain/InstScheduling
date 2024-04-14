# Instruction Scheduling project for CDA5106-Advanced Computer Architecture (UCF)


## To run the simulator

python ./simulator.py <s> <n> <trace_file>

Simulator outputs are stored in "./outputs" directory

## To run the scheduler

python ./scheduler/scheduler_py -a/-b/-c <trace_file>

-a : LLWP heuristic
-b : Highest Latency heuristic
-c : Random heuristic

Scheduler outputs are stored in "./scheduler_outputs" directory

For each input file, the scheduler generates a prescheduled "_si" and post scheduled "_so" file in the output directory.
