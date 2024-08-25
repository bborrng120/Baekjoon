#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char a[101];
    int n;
    int count;
    
    scanf("%d", &n);
    count = n;
    
    for(int i=0; i<n; i++) {
        int alpha[26] = {0};
        char c = ' ';
        scanf("%s", a);
        for(int j=0; a[j]!='\0'; j++) {
            if(alpha[a[j]-97] > 0 && c != a[j]) {
                count--;
                break;
            }
            alpha[a[j]-97]++;
            c = a[j];
        }
    }
    
    printf("%d", count);
}