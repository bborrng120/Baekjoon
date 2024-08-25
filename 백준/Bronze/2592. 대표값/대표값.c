#include <stdio.h>

int main(void)
{
    int a[101] = {0};
    int i, n, k;
    int sums = 0;
    int maxs = 0;
    
    for(i=0; i<10; i++) {
        scanf("%d", &n);
        a[n/10]++;
        sums += n;
    }
    
    for(i=0; i<101; i++) {
        if(maxs < a[i]) {
            maxs = a[i];
            k = i;
        }
    }

    printf("%d\n", sums / 10);
    printf("%d\n", k*10);

    return 0;
}