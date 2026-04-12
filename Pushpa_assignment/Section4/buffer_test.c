#include<stdio.h>
#include<string.h>
int main(){
char buffer[16];
printf("Enter input: ");
gets(buffer);
printf("Your entered: %s\n",buffer);
return 0;
}
