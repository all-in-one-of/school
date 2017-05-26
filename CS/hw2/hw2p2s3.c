#include <stdio.h>

/* count digits, white space, others */
/* to run, try:    gcc THIS_FILE.c ; cat ANY_FILE | ./a.out */
/*SOLUTION 3*/
int main() {
    char x1[100] = "The 25 quick brown foxes jumped over the 27 lazy dogs 15 times."; 
    char *x1ptr = x1;
    int i, nwhite, nother;
    int ndigit[10];
    nwhite = nother = 0;
    for (i = 0; i < 10; i++) {
        ndigit[i] = 0;	
    }
    while(*x1ptr != '\0') {
	if (*x1ptr >= '0' && *x1ptr <= '9')
	   ++ndigit[*x1ptr-'0'];
	
        else if (*x1ptr == ' ' || *x1ptr == '\n' || *x1ptr == '\t')
            ++nwhite;
        else
            ++nother;
       	x1ptr++;
    }
    printf("digits =");
    for (i = 0; i < 10; ++i) {
        printf(" %d", ndigit[i]);
    }
    printf(", white space = %d, other = %d\n",
        nwhite, nother);
    return 0;
}
