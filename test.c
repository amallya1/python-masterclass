#include<stdio.h>
#include<string.h>
char * reverse_str(char s[]);
int main() {
   char input_str[8] = "AKshatha";
   char *out = NULL;
   int i =0;
   int str_len = strlen(input_str);
   out = reverse_str(i, input_str);
   printf("%s\n", out);


}

char * reverse_str(int i, char s[]) {
    int length = strlen(s);
    char out[length] ;
    
    printf("length = %d\n", length);
    while (length<0) {
        i = i+1;
        out[--length] = reverse_str(i, s[length-i]);
        printf("%c\n", out[length--]);
     }
     return out[7];

}
