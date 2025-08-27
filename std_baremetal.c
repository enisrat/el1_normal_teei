
/* #################################### BEGIN STANDARDS #################################### */
void *memcpy(void *dest, const void *src, unsigned int n) {
    char *d = dest;
    const char *s = src;
    while (n--) *d++ = *s++;
    return dest;
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