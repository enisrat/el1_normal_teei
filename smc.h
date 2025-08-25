#include <sys/types.h>

size_t smc(size_t function_id,
			 size_t arg0, size_t arg1, size_t arg2,
			 size_t arg3, size_t *r1, size_t *r2, size_t *r3);