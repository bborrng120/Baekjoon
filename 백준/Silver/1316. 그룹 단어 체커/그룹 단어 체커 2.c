#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char a[100][100];
    int n;
    int count = 0;
    
    scanf("%d", &n);
    
    for(int i=0; i<n; i++) {
        scanf("%s", a[i]);
    }
    
    for(int i=0; i<n; i++) {
        int alpha[26] = {0};
        bool check = true;
        char c = ' ';
        for(int j=0; j<strlen(a[i]); j++) {
            if(alpha[a[i][j]-97] > 0 && c != a[i][j]) {
                check = false;
                break;
            }
            alpha[a[i][j]-97]++;
            c = a[i][j];
        }
        
        if(check) {
            count++;
        }
    }
    
    printf("%d", count);
}
