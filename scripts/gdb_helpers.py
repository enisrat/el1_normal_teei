import gdb
import varint
import parse_meta
import json
import os

ex = gdb.execute
pe = gdb.parse_and_eval

class loadi(gdb.Command):
    def __init__(self):
        super(loadi, self).__init__("loadi", gdb.COMMAND_USER)

    def invoke(self, argument, fromtty):
        argv = gdb.string_to_argv(argument)
        if len(argv) > 0:
            with open(argv[0], 'rb') as f:
                func = varint.decode_stream(f)
                sz = varint.decode_stream(f)
                buf = f.read(sz)
                zero_buf = b'\x00' * 0x11800
                gdb.selected_inferior().write_memory(pe("KM_CAMP1_INPUT"), zero_buf, 0x11800)
                gdb.selected_inferior().write_memory(pe("KM_CAMP1_FUNC"), func.to_bytes(4, byteorder='little'), 4)
                gdb.selected_inferior().write_memory(pe("KM_CAMP1_INPUT"), buf, len(buf))
                ex(f"set *KM_CAMP1_SIZE = {len(buf)}")
        else:
            print("No arguments supplied")

class replay_solution(gdb.Command):
    def __init__(self):
        super(replay_solution, self).__init__("replay_solution", gdb.COMMAND_USER)

    def invoke(self, argument, fromtty):
        argv = gdb.string_to_argv(argument)
        if len(argv) > 0:
            inputs = parse_meta.load_solution(argv[0])
            for i, (func, buf) in enumerate(inputs):
                zero_buf = b'\x00' * 0x11800
                gdb.selected_inferior().write_memory(pe("KM_CAMP1_INPUT"), zero_buf, 0x11800)
                gdb.selected_inferior().write_memory(pe("KM_CAMP1_FUNC"), func.to_bytes(4, byteorder='little'), 4)
                gdb.selected_inferior().write_memory(pe("KM_CAMP1_INPUT"), buf, len(buf))
                ex(f"set *KM_CAMP1_SIZE = {len(buf)}")
                print(f"Input {i}")
                print("")
                ex("continue")
        else:
            print("No arguments supplied")
  


loadi()
replay_solution()