#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct max_vector {
    unsigned int col_index;
    unsigned int row_index;
    int index_value;
} max_vector;


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


max_vector find_col_peak(int *arr, int rows, int col){
    /* Find the peak of a column.
    
    This function treats a 2D array like a 1D array and
    traverses using some basic pointer arithmetic.

    next item = *((i * row + arr) + j)
    where:
        - i == current row number (the y axis in matrix i.e. up and down)
        - j == column number in column space (the x axis i.e left to right)
        - row == the number of items in each row
        - *arr == the first item in the array
    */

    // we want a vector to save the max number and its index
    max_vector vector;
    
    // set max to the first item of the column
    vector.col_index = 0;
    vector.index_value = *(col + arr);

    // loop through the rest of the column
    for (int i=1; i < rows; i++){
        int next_number = arr[i * rows + col];
        if (next_number > vector.index_value){
            vector.col_index = i;
            vector.index_value = next_number;
        }
    }
    printf("the max value is %d and it is at index %d\n",
        vector.index_value, vector.col_index);
    return vector;
}


max_vector peak_finder(int *matrix, int rows, int first, int last){
    /* Find a local 2D peak.

    NOTE: Expects a matrix of size row x col

    A peak is defined as:
    (i, j) >= (i, j + 1), (i, j - 1), (i + 1, j) (i - 1, j)
    */

    max_vector vector;
    
    int middle = last / 2;
    vector = find_col_peak(matrix, rows, middle);

    if (middle == first || middle == last){
        vector.row_index = middle;
        return vector;
    }

    if (last > first) {
        int current = matrix[vector.col_index * rows + middle];
        int one_less = matrix[vector.col_index * rows + middle - 1];
        int one_more = matrix[vector.col_index * rows + middle + 1];

        if (one_less <= current >= one_more) {
            vector.row_index = middle;
            return vector;
        }

        // if current is not a peak we can free the vector
        if (one_less > current){
            return peak_finder(matrix, rows, first, middle - 1);
        } else {
            return peak_finder(matrix, rows, middle + 1, last);
        } 
    }
    vector.row_index = middle;
    return vector;
}


int main(void) {
    printf("Hello World\n");

    int myarr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // --------- binary search tests -------
    assert(binary_search(myarr, 0, 10, 5) == 4);
    assert(binary_search(myarr, 0, 10, 1) == 0);
    assert(binary_search(myarr, 0, 10, 10) == 9);
    assert(binary_search(myarr, 0, 10, 0) == -1);
    assert(binary_search(myarr, 0, 10, -2) == -1);

    // ------------ 2D peak ----------

    int arr [5][5] = {
        {10, 8, 11, 10, 16},
        {14, 13, 12, 11, 24},
        {15, 9, 11, 21, 6},
        {16, 21, 19, 20, 12},
        {100, 6, 13, 19, 9},
    };

    max_vector ptr = peak_finder(*arr, 5, 0, 5);
    printf("the local peak is at %d, %d", ptr.row_index, ptr.col_index);
    return 0;
}
