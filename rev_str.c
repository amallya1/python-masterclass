#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char** argv) {

    int str_length, i = 0;

    char *reversed_str, *input_str = NULL;
    
    input_str = (char*) malloc(strlen(argv[1]));
    reversed_str = (char*) malloc(strlen(argv[1]));

    str_length = strlen(argv[1]);

    strcpy(input_str, argv[1]);
   
    printf("%s\t %d\n", input_str, str_length);
  
    str_length--;
    while(str_length >= 0) {
      printf("%d\t %d\n", str_length, i);
       reversed_str[i] =  input_str[str_length];
       str_length--;
       i++; 
    }
    printf("%s\n", reversed_str);

}

