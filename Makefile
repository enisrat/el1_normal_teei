
BUILDROOT := bin
BUILDDIR := .
VPATH = src

SOURCES := main.c printf.c smc.c
OBJECTS  := $(SOURCES:%.c=%.o)
BIN_NAME := el1.bin

CFLAGS := \
		-O0 \
		-std=gnu99 \
		-Wall \
		-static \
		-nostdlib \
		-nodefaultlibs \
		-mgeneral-regs-only \
		-fno-common \
		-fno-strict-aliasing \
		-fPIC \
		-fno-builtin


PREFIX ?= /opt/gcc-linaro-4.9.4-2017.01-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-
CC := $(PREFIX)gcc
LD := $(PREFIX)ld
OBJCOPY := $(PREFIX)objcopy

# see also db_config.py
all:    $(BIN_NAME)

clean:
	find . -name "*.o" -type f -delete
	find . -name "*.elf" -type f -delete
	find . -name "*.bin" -type f -delete

%.bin: %.elf
	$(OBJCOPY) -O binary -j .text -j .data* $< $@

.PRECIOUS: %.elf
%.elf: $(BIN_NAME).ld $(OBJECTS) init.o
	$(LD) $(LDFLAGS) -L . -T $^ -o $@

$(OBJECTS): %.o :  %.c
	$(CC) $(CFLAGS) $(USER_DEFINES)  -I. -c $^ -o $@

init.o: init.S
	$(CC) $(CFLAGS) $(USER_DEFINES) -c $< -o $@