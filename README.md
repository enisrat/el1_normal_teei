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


## Interesting

- `MTK_SIP` `plat_smc_id_table.h` (lk)
