import math

class MyROB:
    def __init__(self):
        self.state = 0
        self.src_state1 = 0
        self.src_state2 = 0
        self.oprand_state = 0
        self.tag = 0
        self.list_dispatch = 0
        self.list_issue = 0
        self.list_execute = 0
        self.valid = 0
        self.fu_type = 0
        self.src1 = 0
        self.src2 = 0
        self.dst = 0
        self.if_cycle = 0
        self.if_dur = 0
        self.id_cycle = 0
        self.id_dur = 0
        self.is_cycle = 0
        self.is_dur = 0
        self.ex_cycle = 0
        self.ex_dur = 0
        self.wb_cycle = 0
        self.wb_dur = 0
        self.i = 0
        self.cycle = 0
        self.count_ex = 0
        self.entry = 0
        self.depend_entry1 = 0
        self.depend_entry2 = 0
        self.nextrob = None
        self.lastrob = None

class RegisterFile:
    def __init__(self):
        self.tag = 0
        self.valid = 0

def main():
    rob = [MyROB() for _ in range(1024)]
    rf = [RegisterFile() for _ in range(100)]

    cycle_final = 0
    str_v = ''

    head = rob[0]
    tail = head
    tag=0
    N=0

    rob[1023].nextrob = rob[0]
    rob[0].lastrob = rob[1023]

    printednum = 0

    for i in range(1023):
        rob[i+1].lastrob = rob[i]
        rob[i].nextrob = rob[i+1]

    for i in range(1024):
        rob[i].valid = 1
        rob[i].list_dispatch = 0
        rob[i].list_issue = 0
        rob[i].list_execute = 0
        rob[i].entry = i
        rob[i].oprand_state = 1

    for j in range(100):
        rf[j].valid = 1

    clk_cycle = 0
    count_rob = 0
    count_rob_id = 0

    in_s = 256
    in_n = 8

    pipestate = 0

    tracename = "./traces/val_trace_gcc.txt"
    tracefile = open(tracename, "r")
    if tracefile is None:
        print("cannot open tracefile")
        return

    outputname = "myoutput_{}_{}_gcc.txt".format(in_s,in_n)
    out = open(outputname, "w")
    if out is None:
        print("cannot open this out file")
        return

    count_issue = in_s
    count_FU = in_n + 1
    count_rob = in_n
    count_rob_id = in_n * 2
    temprob2 = head
    head.lastrob = None
    issue_rate = 0

    while printednum < 10000:
        issue_rate = in_n + 1
        if clk_cycle == 196:
            pass  # Handle input

        print(f"CYCLE={clk_cycle}, TAG={tag}, PRINTEDNUM={printednum}")

        if printednum == 9777:
            print('This is it')

        # FakeRetire(); WB-> OUT
        temprob = head
        while temprob != tail:
            if head.state == 6:
                head = head.nextrob
            temprob = temprob.nextrob

        temprob = head
        while temprob != tail:
            if temprob.state == 5:
                i += 1
                temprob.state = 6
                temprob.valid = 0
                temprob.wb_dur = 1
                if temprob2.state == 6 and temprob2.tag == printednum and printednum < 10000:
                    # pass  # Print to output file
                    if temprob2.tag == 10053:
                        str_v = input()
                        print('STOP\n')
                    
                    out.write("{0} fu{{{1}}} src{{{2},{3}}} dst{{{4}}} IF{{{5},{6}}} ID{{{7},{8}}} IS{{{9},{10}}} EX{{{11},{12}}} WB{{{13},{14}}}\n".format(
                        temprob2.tag, temprob2.fu_type, temprob2.src1, temprob2.src2, temprob2.dst,
                        temprob2.if_cycle, temprob2.if_dur, temprob2.id_cycle, temprob2.id_dur,
                        temprob2.is_cycle, temprob2.is_dur, temprob2.ex_cycle, temprob2.ex_dur,
                        temprob2.wb_cycle, temprob2.wb_dur))

                    if tag>9990:
                        print("{0} fu{{{1}}} src{{{2},{3}}} dst{{{4}}} IF{{{5},{6}}} ID{{{7},{8}}} IS{{{9},{10}}} EX{{{11},{12}}} WB{{{13},{14}}}".format(
                            temprob2.tag, temprob2.fu_type, temprob2.src1, temprob2.src2, temprob2.dst,
                            temprob2.if_cycle, temprob2.if_dur, temprob2.id_cycle, temprob2.id_dur,
                            temprob2.is_cycle, temprob2.is_dur, temprob2.ex_cycle, temprob2.ex_dur,
                            temprob2.wb_cycle, temprob2.wb_dur))

                    if cycle_final<temprob2.wb_cycle+temprob2.wb_dur:
                        cycle_final = temprob2.wb_cycle+temprob2.wb_dur

                    print('printed: {0} temprob2-tag: {1}\n'.format(printednum,temprob2.tag))
                    printednum += 1
                    temprob2 = temprob2.nextrob
            temprob = temprob.nextrob

        # Execute(); EX-> WB
        # for temprob in rob:
        temprob = head
        while temprob != tail:
            if not temprob.count_ex and temprob.state == 4:
                temprob.list_execute = 0
                temprob.state = 5
                count_FU += 1
                if temprob.dst != -1:
                    if temprob.entry == rf[temprob.dst].tag:
                        rf[temprob.dst].valid = 1
                temprob.oprand_state = 1
                temprob.wb_cycle = clk_cycle
                temprob.ex_dur = temprob.wb_cycle - temprob.ex_cycle
            elif temprob.state == 4:
                temprob.count_ex -= 1

            temprob = temprob.nextrob

        # Issue(); IS-> EX
        # for temprob in rob:
        temprob = head
        while temprob != tail:
            if (pipestate == 1 and count_FU and temprob.state == 3) or (pipestate == 0 and temprob.state == 3 and issue_rate):
                if (rob[temprob.depend_entry1].oprand_state or temprob.src_state1) and (rob[temprob.depend_entry2].oprand_state or temprob.src_state2):
                    issue_rate -= 1
                    count_FU -= 1
                    temprob.count_ex -= 1
                    temprob.list_issue = 0
                    temprob.list_execute = 1
                    temprob.state = 4
                    count_issue += 1
                    temprob.ex_cycle = clk_cycle
                    temprob.is_dur = temprob.ex_cycle - temprob.is_cycle
            temprob = temprob.nextrob

        # Dispatch(); ID->IS
        # for temprob in rob:
        temprob = head
        while temprob != tail:
            if count_issue and temprob.state == 2:
                count_issue -= 1
                count_rob_id += 1
                temprob.list_dispatch = 0
                temprob.list_issue = 1
                temprob.state = 3
                temprob.is_cycle = clk_cycle
                temprob.id_dur = temprob.is_cycle - temprob.id_cycle
            temprob = temprob.nextrob


        # Fetch(); IF->ID
        # for temprob in rob:
        temprob = head
        while temprob != tail:
            if count_rob_id and temprob.state == 1:
                temprob.list_dispatch = 1
                count_rob += 1
                temprob.state = 2
            temprob = temprob.nextrob

        # IN -> IF
        while count_rob and count_rob_id:
            count_rob -= 1
            count_rob_id -= 1
            rltrf = tracefile.readline().split()
            print(rltrf)

            if len(rltrf) == 0:
                break

            seq_no = rltrf[0]
            op, dst, src1, src2 = map(int, rltrf[1:])
            tail.fu_type = op
            if tail.fu_type == 0:
                tail.count_ex = 1
            elif tail.fu_type == 1:
                tail.count_ex = 2
            elif tail.fu_type == 2:
                tail.count_ex = 5
            tail.tag = tag
            tail.src1 = src1
            tail.src2 = src2
            tail.dst = dst
            tail.if_cycle = clk_cycle
            tail.id_cycle = clk_cycle + 1
            tail.if_dur = 1
            tail.state = 1
            tail.oprand_state = 0

            if (not rf[tail.src1].valid) and tail.src1 != -1:
                tail.depend_entry1 = rf[tail.src1].tag
                tail.src_state1 = 0
            elif rf[tail.src1].valid or tail.src1 == -1:
                tail.src_state1 = 1
                tail.depend_entry1 = tail.entry

            if (not rf[tail.src2].valid) and tail.src2 != -1:
                tail.depend_entry2 = rf[tail.src2].tag
                tail.src_state2 = 0
            elif rf[tail.src2].valid or tail.src2 == -1:
                tail.src_state2 = 1
                tail.depend_entry2 = tail.entry

            rf[tail.dst].tag = tail.entry
            rf[tail.dst].valid = 0
            tag += 1
            tail = tail.nextrob

        clk_cycle += 1

    IPC = printednum / cycle_final
    print(f"number of instructions = {printednum}")
    print(f"number of cycles = {cycle_final}")
    print("IPC = {:1.5f}".format(IPC))
    out.write(f"number of instructions = {printednum}\n")
    out.write(f"number of cycles = {cycle_final}\n")
    out.write("IPC = {:1.5f}\n".format(IPC))

    out.close()
    tracefile.close()

if __name__ == "__main__":
    main()

