
#include "common.h"
#include "smc_id_bl.h"


void kernel_main() {
	size_t ret;
	printf("HELLO from Kernel!\r\n");

	ret = smc(MTK_SIP_LK_RPMB_INIT, 0, 0, 0, 0, 0, 0, 0);
	printf("SMC ret: %llx\r\n", ret);

	teei_client_init();
	soter_driver_init();
	init_teei_framework();

	kmtest_optee();

	while(1){
	};
}



