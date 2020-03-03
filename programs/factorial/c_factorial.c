#include<stdio.h>
#include<stdlib.h>
#include<time.h>

long double factorial(long double n){
    if(n==0){
             return(1);
    }
    return(n * factorial(n-1));
}

clock_t start, end;
double cpu_time_used;

int main(){
    long double n;
    printf("Given your number\n");
    scanf("%Lf", &n);
    start = clock();
    printf("The factorial of this number is: %Lf\n", factorial(n));
    end = clock();
    cpu_time_used = ((double) (end - start))/CLOCKS_PER_SEC;
    printf("Total time %f\n", cpu_time_used);
    return(0);
}
