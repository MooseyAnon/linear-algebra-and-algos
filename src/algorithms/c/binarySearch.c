#include <assert.h>
#include <stdio.h>

int binary_search(int arr[], int first, int last, int item) {
    /* A recursive binary search */

    int middle = (last + first) / 2;
    if (last >= first) {

        if (arr[middle] == item) {
            return middle;
        }

        if (item > arr[middle]){
            return binary_search(arr, middle + 1, last, item);
        } else {
            return binary_search(arr, first, middle - 1, item);
        }
  
    } else {
        return -1;
    }
}

int main(void) {
    printf("Hello World\n");

    int myarr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // --------- tests -------
    assert(binary_search(myarr, 0, 10, 5) == 4);
    assert(binary_search(myarr, 0, 10, 1) == 0);
    assert(binary_search(myarr, 0, 10, 10) == 9);
    assert(binary_search(myarr, 0, 10, 0) == -1);
    assert(binary_search(myarr, 0, 10, -2) == -1);
    return 0;
}
