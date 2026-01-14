#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct w{
    char word[51];
};

typedef struct w w;

int compare(const void *a, const void *b){
    w *p1 = (w*)a;
    w *p2 = (w*)b;

    int len1 = strlen(p1->word);
    int len2 = strlen(p2->word);

    if (len1 != len2){
        return (len1 - len2);
    }
    else{
        for (int i = 0; i < len1; i++){
            if ((int)(p1->word[i]) < (int)(p2->word[i])){
                return -1;
            }
            else if ((int)(p1->word[i]) > (int)(p2->word[i])){
                return 1;
            }
        }
        return 0;
    }
}

int main(){
    int N;
    scanf("%d", &N);
    w* list = (w*) malloc(sizeof(w) * N);
    for (int i = 0; i < N; i++){
        scanf("%s", list[i].word);
    }

    qsort(list, N, sizeof(w), compare);

    int issame = 0;

    
    for (int i = 0; i < N; i++){
        issame = 0;
        if (i > 0 && (strlen(list[i].word) == strlen(list[i-1].word))){
            issame = 1;
            for (int j = 0; list[i].word[j] != '\0'; j++){
                if (list[i].word[j] != list[i-1].word[j]){
                    issame = 0;
                    break;
                }
            }
        }
        if (issame == 0){
            printf("%s\n", list[i].word);
        }
    }
    free(list);

    return 0;
}