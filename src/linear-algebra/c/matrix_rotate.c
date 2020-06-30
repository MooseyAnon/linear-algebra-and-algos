/* Rotate a matrix 90°
A = {
    {1, 2, 3, 4, 5},
    {6, 7, 8, 9, 10},
    {11, 12, 13, 14, 15},
    {16, 17, 18, 19, 20},
    {21, 22, 23, 24, 25},
};

R = {
    {21, 16, 11, 6, 1},
    {22, 17, 12, 7, 2},
    {23, 18, 13, 8, 3},
    {24, 19, 14, 9, 4},
    {25, 20, 15, 10, 5},
}

idea, corners move first:
    - (0, 0) -> (0, 4),
    - (0, 4) -> (4, 4),
    - (4, 4) => (4, 0),
    - (4, 0) -> (0, 0),

then one item in (and up):
    - (0, 1) -> (1, 4),
    - (1, 4) -> (4, 3),
    - (4, 3) -> (3, 0),
    - (3, 0) -> (0, 1),

then same again for all items k in floor(matrix columns / 2):
    - (0, 2) -> (2, 4),
    - (2, 4) -> (4, 2),
    - (4, 2) -> (2, 0),
    - (2, 0) -> (0, 2)
*/

#include <stdio.h>

void print_matrix(int *matrix, int cols) {
    /* Print a given matrix */
    for (int i = 0; i < cols; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", *matrix++);
        }
        printf("\n");
    }
}


int rotate(int *matrix, int rows, int cols){
    /* Rotate a matrix 90° clockwise. */

    if (rows != cols){
        return -1;
    }

    int i = 0;
    int depth = (cols - 1) / 2;

    while (i <= depth) {
        int right = i;
        int left = (cols - 1) - i;

        for (int k = 0; k < left - i; k++) {
            // here we can use k to either take us left to right or
            // up and down.

            int top_right = matrix[(right * rows) + (k + i)];
            // k * rows -> takes us down
            // i * rows -> starts us at the right depth each iteration
            // left - i -> moves us in each iteration to the right depth
            int top_left = matrix[
                (k * rows + right) + (i * rows) + (left - i)];
            int bottom_right = matrix[(left * rows) + (left - k)];
            int bottom_left = matrix[(left * rows + right) - (k * rows)];

            // swap items
            matrix[(right * rows) + (k + i)] = bottom_left;
            matrix[(k * rows + right) + (i * rows) + (left - i)] = top_right;
            matrix[(left * rows) + (left - k)] = top_left;
            matrix[(left * rows + right) - (k * rows)] = bottom_right;
        }
        i += 1;
    }
    return 0;
}


int main(void) {
    A = {
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 10},
        {11, 12, 13, 14, 15},
        {16, 17, 18, 19, 20},
        {21, 22, 23, 24, 25},
    };
    print_matrix(*A, 5);
    printf("\n");

    if (rotate(*A, 5, 5) != -1){
        print_matrix(*A, 5);
    }
    return 0;
}
