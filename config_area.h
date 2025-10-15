// Fixed config RAM area (VM`s physical memory) to pass config from host

#include <stdint.h>

#define CONFIG_AREA_BASE 0x300000

static volatile uint32_t *CFG = (volatile uint32_t *)CONFIG_AREA_BASE;