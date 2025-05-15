#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define SIZE 1000  // matrix size

void matrixMult(double* A, double* B, double* C, int size) {
  for (int i = 0; i < size; i++)
    for (int j = 0; j < size; j++) {
      double sum = 0.0;
      for (int k = 0; k < size; k++)
        sum += A[i * size + k] * B[k * size + j];
      C[i * size + j] = sum;
    }
}

int main() {
  double* A = malloc(SIZE * SIZE * sizeof(double));
  double* B = malloc(SIZE * SIZE * sizeof(double));
  double* C = malloc(SIZE * SIZE * sizeof(double));

  // Initialize matrices with dummy values
  for (int i = 0; i < SIZE * SIZE; i++) {
    A[i] = 1.0;
    B[i] = 2.0;
  }
  // Call in an infinite loop, stop within Python UI
  while (1) {
    matrixMult(A, B, C, SIZE);
}

  // Free up allocated memory
  free(A);
  free(B);
  free(C);

  return 0;
}

