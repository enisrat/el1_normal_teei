set auto-load python-scripts on
set confirm off
set pagination off
add-symbol-file el1.elf

source gdb_helpers.py

b km_camp_1_startfuzz
b km_camp_1_endfuzz


target remote localhost:1234
cont

