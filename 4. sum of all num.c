//2020/12/03

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long answer = 0;
    long i =0;
    if(a < b){
      for (i = a; i <= b; i++){
        answer+=i;
      }
    } else if (a > b){
      for (i = b; i <= a; i++){
        answer+=i;
      }
    } else answer = a;
    return answer;
}