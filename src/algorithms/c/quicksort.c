#include <stdio.h>


int quicksort_inner(int *arr, int first, int last);

void print_array(int *arr, int length) {
    /* Pretty print an array */
    for (int i = 0; i <= length; i++) {
        printf("%d, ", arr[i]);
    }
    printf("\n");
}


int * in_place_quicksort(int *arr, int first, int last) {
    /* A recursive in-place quicksort 

    NOTE: THIS DOES NOT WORK FOR ARRAYS WITH MORE THAN 2 DUPLICATES, FIX AND
    TEST.
    */
    if (first < last) {
        int piv = quicksort_inner(arr, first, last);

        // recurse
        in_place_quicksort(arr, first, piv - 1);
        in_place_quicksort(arr, piv + 1, last);
    }
    return arr;
}


void swap_indexes(int *arr, int item_1, int item_2) {
    /* Swap the values of two indexes in an array. */
    int tmp = arr[item_1];
    arr[item_1] = arr[item_2];
    arr[item_2] = tmp;
}


int quicksort_inner(int *arr, int first, int last) {
    /* Sort some subsection of an array. */
    int pivot = (first + last) / 2;
    int counter = 0;
    int last_swap = 0;

    //  swap pivot with last index
    swap_indexes(arr, pivot, last);

    while (counter <= last) {

        if (arr[counter] < arr[last]) {
            swap_indexes(arr, counter, last_swap);
            last_swap++; 
        }

        counter++;
    }
    // swap pivot with last swap
    swap_indexes(arr, last, last_swap);

    return last_swap;
}

int main(void) {
    printf("Hello World\n");

    int y[11] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    int *arr = in_place_quicksort(y, 0, 10);

    if (arr) {
        print_array(arr, 10);
    }
    return 0;
}
