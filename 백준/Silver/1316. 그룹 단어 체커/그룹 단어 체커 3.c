#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char a[100][100];
    int n;
    int count;
    
    scanf("%d", &n);
    count = n;
    
    for(int i=0; i<n; i++) {
        scanf("%s", a[i]);
    }
    
    for(int i=0; i<n; i++) {
        int alpha[26] = {0};
        char c = ' ';
        for(int j=0; j<strlen(a[i]); j++) {
            if(alpha[a[i][j]-97] > 0 && c != a[i][j]) {
                count--;
                break;
            }
            alpha[a[i][j]-97]++;
            c = a[i][j];
        }
    }
    
    printf("%d", count);
}
