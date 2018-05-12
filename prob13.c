/*********************************************************
 * Title: Euler Project Problem 13
 * Author: Osami Yamamoto
 * Date: Sat May 12 20:54:53 JST 2018
 *********************************************************/
#include <stdio.h>
#include <stdlib.h>

void work(){
  enum {BUFLEN = 51 * 120};
  char *fname = "prob13.txt";
  FILE *fp = fopen(fname, "r");
  char buff[BUFLEN];
  int num[50];
  int i, j, count;

  fread(&buff[0], BUFLEN, 1, fp);
  fclose(fp);
  
  for (i = 49; i >= 0; i--){
    num[i] = 0;
    for (j = 0; j < 100; j++){
      num[i] += buff[j * 51 + (49 - i)] - '0';
    }
  }
  for (i = 0; i < 49; i++){
    int c = num[i];
    num[i] = c % 10;
    num[i + 1] += c / 10;
  }
  count = 0;
  for (i = 49; i >= 0; i--){
    int v = num[i];
    printf("%d", v);
    if (v >= 1000) count += 4;
    else if (v >= 100) count += 3;
    else if (v >= 10) count += 2;
    else count += 1;
    if (count >= 10) break;
  }
  putchar('\n');
}

int main(){
  work();
  return 0;
}


