# MT6768 Secure World Emulation

## Memmap 6768

Only DRAM (and SRAM) addresses. Hardware MMIO not included.

| Address      | Size       | Description              | used in EMU or ORIG  |
|--------------|------------|--------------------------|----- | 
| 0x00100000 | | SRAM | BOTH |
| 0x40080000   |            | kernel                   | ORIG  |
| 0x40100000   | 0x100000 | ALLOC_BASE_KMALLOC | EMU |
| 0x40200000   | 0x100000 | ALLOC_BASE_PAGE | EMU |
| 0x40300000   | 0x100000 | ISEE_SHM_BASE | EMU |
| 0x47C80000   |            | ramdisk                  |ORIG    |
| 0x4C080000   |            | mtk_bl_param_t bl31_info |BOTH|
| 0x4C11DA80   | 0x5948     | boot args ATAG           |BOTH|
| 0x4C400000   | 			| LK  | ORIG + EMU (for **lk+kernel** text)|
| 0x4CE00000   | 0c1000     | atf_arg_t tee_info       |BOTH|
| 0x4CE01000   | 0x200000   | atf                      |BOTH|
| 0x70000000   | 0x3c00000  | tee kern                 |BOTH|
| 0x7f200000   | 0x200000   | soter-shared-mem         | EMU + ORIG (Default?) |
| 0x47f800000  |            | bl33_entry (EL2 GZ)      |ORIG|

### Physical Locations

- sigma0: 0x70200000
- keymasterTA: 0x709c9000
- moe rom/arm-v8-mtk-plat.cfg : 0x70220000

## Interesting

- `MTK_SIP` `plat_smc_id_table.h` (lk)


## Breakpoints

### Koobee_mt6769_R-ota-S_isee400_K6525_P2_20220716

- 0xffffff80f001cff4 : slowtrap exception handler

### xiaomi_c3n_mt6769_SVP_U_upto_V_P2_20241115


## Exceptions

```
Set INVALID INSN at "RsaSignOperation::SignDigested start" in keymaster TA
(gdb) set {int*}0x70993950 = 0xffffffff

km4     | Exception: State:
km4     |  r0=00000003  r1=80007b4c  r2=00000000  r3=00000004
km4     |  r4=80007b4c  r5=000073f8  r6=80007b40  r7=000065f0
km4     |  r8=00000000  r9=80007bc0 r10=6b3ddd8d r11=80007b4c
km4     | r12=01036acc  sp=80007a90  lr=010120b8  pc=01036954
km4     | psr=20000010 err=00100000 pfa=fffffff8
km4     | Codes around PC[0x1036934,0x1036974]:
km4     | 0x01036934 : 0xeafffffb    
km4     | 0x01036938 : 0xeafffffc    
km4     | 0x0103693c : 0xe92d4070    
km4     | 0x01036940 : 0xe1a05000    
km4     | 0x01036944 : 0xe24dd018    
km4     | 0x01036948 : 0xe3a00003    
km4     | 0x0103694c : 0xe1a04001    
km4     | 0x01036950 : 0xffffffff    
km4     | 0x01036954 : 0x00000000    <-PC
km4     | 0x01036958 : 0xeb04fc92    
km4     | 0x0103695c : 0xe5950098    
km4     | 0x01036960 : 0xe28d2014    
km4     | 0x01036964 : 0xe3a01000    
km4     | 0x01036968 : 0xeb00ca84    
km4     | 0x0103696c : 0xe3500001    
km4     | 0x01036970 : 0xe1a06000    
km4     | stack dump (hex, 1 page most):
km4     | stack 0x80007a90 - 0x80007fff
km4     | 80007a80: -------- -------- -------- -------- 80007b4c e880007b 6ae88000 036ae880
km4     | 80007aa0: 000065f0 00000000 80007b88 000073f8 80007b40 010120b8 80007b60 80007b4c
km4     | 80007ac0: 6b3ddd8d 32e419e2 00000000 0101ee18 0000740c 00007434 011a9158 80007bc0
km4     | 80007ae0: 00006a64 80007b3c 011a9158 00000000 011b0088 80007b98 80007b3c 011b0cf8
km4     | 80007b00: 0121bfa8 00006a40 011ae6e8 011ae710 011b0088 00000653 00000020 0100317c
km4     | 80007b20: 6f4e2065 7272456e 6553726f 6c616972 01011f8c 00000000 0000000a 00006a60
km4     | 80007b40: 011ae6e8 00000003 00000000 011b0cf8 00000000 00000000 00000000 00000000
km4     | 80007b60: 011b0088 00000000 00000000 80007b64 80007b68 00000000 00000000 00000000
km4     | 80007b80: 00000000 00000000 011ae710 00000003 6b3ddd8d 32e419e2 011b0cf8 00000000
km4     | 80007ba0: 00000000 00000000 00000000 011b0cf8 00000000 00000000 00000000 00000000
km4     | 80007bc0: 011b0088 00000000 00000000 80007bc4 80007bc8 00000000 00000000 00000000
km4     | 80007be0: 00000000 00000000 00000000 00006a40 0121bfa8 80007da0 0000000c 80007d9c
km4     | 80007c00: 00000024 01004eb8 80007d9c 80007da0 00000000 000000c8 011a9720 80007d78
km4     | 80007c20: 00000024 00000653 00000000 0119a71c 010000d0 fffffffe 01011f8c 00000000
km4     | 80007c40: 80007cb5 80007ca0 80007ca0 80007d68 00000000 00000000 011a9198 00000000
km4     | 80007c60: 0111639c 00000001 00000000 00000000 00000000 00000001 00000000 00000000
km4     | 80007c80: 00000002 00000002 01175be8 011b5660 80007ca0 80007cb5 73726576 80007d78
km4     | 80007ca0: 61206d6b 73656363 6f6e2073 6573206e 65727563 646e000a 000a633a 00000000
km4     | 80007cc0: 00000000 00000000 00000011 011a9138 00000000 00000000 80007cd0 80007cd4
km4     | 80007ce0: 00000000 00000000 00000000 00000000 00000000 0121bdd0 011ae758 00000003
km4     | 80007d00: 6b3ddd8d 00001000 00000000 0121bdd0 00411000 01170398 011702cc 00001000
km4     | 80007d20: 80007d48 01171fa0 01236c68 0000004b 01236c5c 011983f8 80007d68 80007d44
km4     | 80007d40: 80007d58 0042b000 011702cc 0121bdd0 00000000 00000000 011702cc 80007e18
km4     | 80007d60: 00000020 00006a40 00411048 00011800 00000024 00000653 00000000 010018b0
km4     | 80007d80: 00000000 00000000 00000000 2d525f39 00000000 80007e18 80007ea4 00000000
km4     | 80007da0: 00000000 fffff800 0027f448 0042b000 00411000 00000000 00000000 00000000
km4     | 80007dc0: 00000000 00000000 80007e18 80007e38 00000653 00411000 80007e18 0000000c
km4     | 80007de0: 0121bdd0 011172c0 0000aa50 00004b78 000000b0 000000e4 0000006e 000000da
5[tz_driver][INFO]: smc_type: DONE
5[tz_driver][INFO]: Handling SCHED_IRQ
5[tz_driver][INFO]: ut_smc_handler returning with value: 1
km4     | 80007e00: 00000061 00000055 0000006c 0000003a 011702cc 0121bdd0 00000001 00000000
km4     | 80007e20: 00411028 00000020 00411048 00011800 00000000 00000000 01218000 00000023
km4     | 80007e40: 00000000 80007e97 80007eac 00000000 b3000200 0111639c 01218088 00000023
km4     | 80007e60: 00000000 011166b4 fffff800 00000000 80007eac 011eb16c 011eb070 01116500
km4     | 80007e80: 011702cc 0121bdd0 00000000 00001000 00000000 011eb070 0000e000 80007eac
km4     | 80007ea0: 00000000 00006810 012190e0 00000008 b3000200 b3000200 00000020 00000000
km4     | 80007ec0: 00000000 b3000200 b3000200 00000000 01170200 0041b000 00002000 00000000
km4     | 80007ee0: 0118ea48 00000023 012371e0 80007fa4 00000001 0119af00 00000000 00000000
km4     | 80007f00: 00000000 00000000 00000000 00000000 00000003 01000034 00000000 00000000
km4     | 80007f20: 00000005 00000006 00000006 00001000 00000000 00000000 00000000 00000000
km4     | 80007f40: 00000000 00000000 00000000 00000000 0000000b 00000000 0000000c 00000000
km4     | 80007f60: 0000000d 00000000 0000000e 00000000 00000000 b0019258 00000001 00000000
km4     | 80007f80: 00000000 00000000 00000000 00000000 00000000 00000000 011a8f48 00000000
km4     | 80007fa0: 80007fa4 b1007f87 00000000 00000000 00000005 00000006 00000003 01000034
km4     | 80007fc0: 0000000e 00000000 0000000d 00000000 0000000c 00000000 0000000b 00000000
km4     | 80007fe0: 00000006 00001000 000000f0 b1007f70 000000f1 b1007df0 00000000Doing SIGSEGV
km4     | [main.cc:281/ta_panic]<err>************* TA Crash ***************** 
km4     | 
uTbtaLdr| [bta_control.h:487/InvokeCommand]<err>keep alive ta crash,enable to reboot
uTbtaLdr| 
```

## Problems with QEMU

### icount

- when using _icount_ with a DEBUG build
  - `-icount,shift=auto,align=off,sleep=off'
  - I got the below error (which I did not get for OPTIMIZED build or without icount...)
  - QEMU virt clock seems to be too _SLOW_ in this case...

```
uTInit  | begin to start sst.
REEagent| [main.cc:54/start_core_service]<err>failed to l4_ipc_wait (err=-2003)
REEagent| [main.cc:181/main]<err>failed to start core service(1)(err=-2)
```


## GDB

### campaing 1 - km single input

- Debug an input with QEMU

```
PYTHONPATH=$PYTHONPATH:$(pwd) gdb-multiarch -x scripts/test_input_km_single.gdb
```

- When stopping at `km_camp_1_startfuzz`, use `loadi <filepath>` in gdb to load an input
- In QEMU monitor you can enable `logfile /tmp/trace` `log exec,nochain` to get a trace
  - or you can use gdb, IDA, etc to debug
- Then `continue`


## Command IDs km

| Command ID | Function/Operation                        |
| ---------- | ----------------------------------------- |
| 0x00       | GenerateKey                               |
| 0x04       | beginOperation                            |
| 0x08       | updateOperation                           |
| 0x0c       | finishOperation                           |
| 0x10       | AbortOperation                            |
| 0x14       | ImportKey                                 |
| 0x18       | ExportKey                                 |
| 0x20       | AddRngEntropy                             |
| 0x3c       | GetKeyCharacteristics                     |
| 0x40       | AttestKey                                 |
| 0x44       | UpgradeKey                                |
| 0x48       | Configure                                 |
| 0x50       | ComputeSharedHMAC                         |
| 0x54       | VerifyAuthorization                       |
| 100 (0x64) | ImportWrappedKey                          |
| 0x68       | deviceLocked                              |
|            |                                           |
| 0x3e9      | km HMAC key                               |
| 0x3ea      | km ENC_PW                                 |
| 0x3eb      | km ENC_AUTHTOKEN                          |
| 0x3ec      | KM_COMMAND_CREATE_KEYPAIR_AND_ATTENTATION |