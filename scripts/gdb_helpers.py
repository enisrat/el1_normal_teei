import gdb
import varint

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


loadi()