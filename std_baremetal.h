#ifndef STD_BAREMETAL_H
#define STD_BAREMETAL_H

void *memcpy(void *dest, const void *src, unsigned int n);
void *memset(void *s, int c, unsigned int n);
char *strcpy(char *dest, const char *src);
unsigned int strlen(const char *s);
int strcmp(const char *s1, const char *s2);
char *strcat(char *dest, const char *src);

int strncmp(const char *s1, const char *s2, unsigned int n);
#endif