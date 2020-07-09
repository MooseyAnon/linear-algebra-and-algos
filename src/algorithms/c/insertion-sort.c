/* Insertion sort */


void print_array(int *arr, int length) {
    for (int i = 0; i <= length; i++) {
        printf("%d, ", arr[i]);
    }
    printf("\n");
}


int * insertion_sort(int *arr, int last){
    /* Insertion sort

    A stable in-place implementation of the insertion sort algorithm.
    */

    int current = 1;
    while (current <= last) {

        // we want to start the comparision with the item before current
        int j = current - 1;
        while (j >= 0){
            if (arr[current] >= arr[j]){
                break;
            }

            int tmp = arr[current];
            arr[current] = arr[j];
            arr[j] = tmp;

            // current has moved to the place j was previously so we need to
            // update the pointer to current
            current = j;
            j--;
        }

        current++;
    }

    return arr;
}


int main(void) {
    printf("Hello World\n");

    int y[11] = {100, 2, 5, 7, 3, 2, 2, 2, 10, 11, 0};
    int *arr = insertion_sort(y, 10);

    if (arr) {
        print_array(arr, 10);
    }
    return 0;
}
