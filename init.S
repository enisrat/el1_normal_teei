.section .entry


.extern lk_main
.extern kernel_main

entry_lk:
	LDR X20, =(0x4C400000-16)
	MOV SP, X20
    B lk_main

.global entry_kernel
entry_kernel:
	LDR X20, =(0x4C400000-16)
	MOV SP, X20
    B kernel_main