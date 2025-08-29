
/* #################################### BEGIN STANDARDS #################################### */
typedef long size_t;
typedef unsigned long uintptr_t;
void *memcpy(void *dst, void const *src, size_t len)
{
    unsigned char *pcDst = (unsigned char *)dst;
    unsigned char const *pcSrc = (unsigned char const *)src;

    if (len >= sizeof(long) * 2
    &&  ((uintptr_t)src & (sizeof(long) - 1)) == ((uintptr_t)dst & (sizeof(long) - 1))) {
        while (((uintptr_t)pcSrc & (sizeof(long) - 1)) != 0) {
            *pcDst++ = *pcSrc++;
            len--;
        }
        long *plDst = (long *)pcDst;
        long const *plSrc = (long const *)pcSrc;
        /* manually unroll the loop */
        while (len >= sizeof(long) * 4) {
            plDst[0] = plSrc[0];
            plDst[1] = plSrc[1];
            plDst[2] = plSrc[2];
            plDst[3] = plSrc[3];
            plSrc += 4;
            plDst += 4;
            len -= sizeof(long) * 4;
        }
        while (len >= sizeof(long)) {
            *plDst++ = *plSrc++;
            len -= sizeof(long);
        }
        pcDst = (unsigned char *)plDst;
        pcSrc = (unsigned char const *)plSrc;
    }
    while (len--) {
         *pcDst++ = *pcSrc++;
    }
    return dst;
}

void *memset(void *s, int c, unsigned int n) {
    char *p = s;
    while (n--) *p++ = c;
    return s;
}

char *strcpy(char *dest, const char *src) {
    char *d = dest;
    while (*src) *d++ = *src++;
    *d = 0;
    return dest;
}

unsigned int strlen(const char *s) {
    unsigned int len = 0;
    while (*s++) len++;
    return len;
}

int strcmp(const char *s1, const char *s2) {
    while (*s1 && *s1 == *s2) { s1++; s2++; }
    return *s1 - *s2;
}

char *strcat(char *dest, const char *src) {
    char *d = dest;
    while (*d) d++;
    while (*src) *d++ = *src++;
    *d = 0;
    return dest;
}

int strncmp(const char *s1, const char *s2, unsigned int n) {
    while (n-- && *s1 && *s1 == *s2) {
        s1++;
        s2++;
    }
    return n == -1 ? 0 : *s1 - *s2;
}
/* #################################### END STANDARDS #################################### */