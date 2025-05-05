#include <stdio.h>
#include <math.h>

int main() {
  // Using volatile data type to prevent compiler optimization
  volatile double x = 0.0001;

  while (1) {
    for (int i = 0; i < 1000000; ++i) {
      x = sin(x) * cos(x) * tan(x);
    }
  }

  return 0;
}
