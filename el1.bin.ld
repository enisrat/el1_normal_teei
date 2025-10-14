

SECTIONS
{
    .text 0x4c400000 :
    {
        KEEP(*(.entry))
        *(.text)
        *(.text*)
        *(*.text)
        *(.data)
        *(.rodata*)
        *(.bss)
        *(.got*)
    }

    /DISCARD/ :
    {
        *(.pdr)
        *(.gnu.attributes)
        *(.reginfo)
        *(.note)
        *(.comment)
        *(__ex_table)
        *(.interp)
    }
}
