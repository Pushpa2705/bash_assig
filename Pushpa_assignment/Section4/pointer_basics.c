#include <stdio.h>
int main(){
int port=80;
int *ptr= &port;
printf("Value using variable: %d\n",port);
printf("Value using pointer: %d\n", *ptr);
*ptr=443;
printf("Nem value using pointer: %d\n",port);
return 0;
}
