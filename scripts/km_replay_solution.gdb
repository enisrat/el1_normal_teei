set auto-load python-scripts on
set confirm off
add-symbol-file el1.elf

source gdb_helpers.py

b km_camp_1_startfuzz


target remote localhost:1234
cont

