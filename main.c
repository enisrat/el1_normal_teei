
#include "common.h"
#include "smc_id_bl.h"

extern void entry_kernel();

void set_rot() {
	uint32_t h[] = {1, 2, 3, 4};
	for (int i = 0; i < 6; i++)
		smc(MTK_SIP_LK_ROOT_OF_TRUST_AARCH32, h[0], h[1], h[2], h[3], 0, 0, 0);
}

void lk_main(char *param) {
	size_t ret;
	printf("HELLO from Bootloader!\r\n");

	ret = smc(MTK_SIP_LK_RPMB_INIT, 0, 0, 0, 0, 0, 0, 0);
	printf("SMC ret: %llx\r\n", ret);

	smc(MTK_SIP_KERNEL_BOOT, &entry_kernel, 0, 0, 0, 0, 0, 0);
}

void kernel_main() {
	size_t ret;
	printf("HELLO from Kernel!\r\n");

	ret = smc(MTK_SIP_LK_RPMB_INIT, 0, 0, 0, 0, 0, 0, 0);
	printf("SMC ret: %llx\r\n", ret);

	while(1){
	};
}