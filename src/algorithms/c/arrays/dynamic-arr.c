#include <stdio.h>
#include <stdlib.h>


struct dynamArray {
    int *arr;
    // maximum number of items in array will be capacity - 1
    int capacity ;
    int numberOfItems;
};


void
printArr(struct dynamArray *t_arr, size_t size) {
    for(size_t i = 0; i < size; i++) {
        if (i >= t_arr->capacity) {
            printf("out of array bounds\n");
            exit(1);
        }
        printf("%d\n", t_arr->arr[i]);
    }
}


int *
initNewArr(int size) {
    int *new_arr = malloc(size * sizeof(int));
    if (new_arr) {
        return new_arr;
    }
    return NULL;
}


static int
isFull(struct dynamArray *t_arr) {
    return t_arr->numberOfItems == t_arr->capacity;
}


static int
isSparse(struct dynamArray *t_arr) {
    return (float)t_arr->numberOfItems / (float)t_arr->capacity <= 0.25;
}


static int *
resizeArr(struct dynamArray *t_arr, int newSize) {
    int *newArr = initNewArr(newSize);

    if (!newArr) {
        printf("newArr did not resize properly, exiting\n");
        exit(1);
    }
    // move values to newArr:
    // arr size will always be larger than numberOfItems so we can use this
    // as the iterator test when moving over items
    // note: numberOfItems is the last index of the array + 1
    for(int i = 0; i < t_arr->numberOfItems; i++) {
        newArr[i] = t_arr->arr[i];
    }
    // change capacity to newSize
    t_arr->capacity = newSize;

    // free old array
    free(t_arr->arr);
    return newArr;
}


void
append(struct dynamArray *t_arr, int val) {
    if (isFull(t_arr)) {
        t_arr->arr = resizeArr(t_arr, t_arr->capacity * 2);
    }
    t_arr->arr[t_arr->numberOfItems] = val;
    t_arr->numberOfItems += 1;
}


int
pop(struct dynamArray *t_arr) {
    if (t_arr->numberOfItems == 0) {
        printf("empty array ");
        return -1;
    }
    if (isSparse(t_arr)) {
        t_arr->arr = resizeArr(t_arr, t_arr->capacity / 2);
    }
    // the number of items is 1 more than the indexs because
    // we are 0 indexing. So we need to decrement first, then
    // get the value.
    t_arr->numberOfItems -= 1;
    int lastItem = t_arr->arr[t_arr->numberOfItems];

    return lastItem;
}


int main() {
    printf("Hello, world!\n");

    struct dynamArray test;
    test.capacity = 2;
    test.numberOfItems = 0;
    test.arr = initNewArr(test.capacity);
    printf("memeory addr of outside arr = %p\n", test.arr);

    for(int i = 1; i <= 40; i++){
      append(&test, i);
    }
    printf("total capacity of array is %d\n", test.capacity);
    printf("last item of items is %d\n", test.numberOfItems);
    printf("------------------------------\n");

    // print array safely
    printArr(&test, test.capacity);
    for(int i = 40; i >= 0; i--){
      int x = pop(&test);
      printf("last popped item was %d\n", x);
    }
    return 0;
}
