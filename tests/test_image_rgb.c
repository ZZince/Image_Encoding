#include "../structs/image_rgb.h"
#include <stddef.h>
// gcc -m64 -g -O0 -o test_image_rgb.exe tests/test_image_rgb.c -I. -L. -l/tests/image_rgb
int main() {
    ImageRGB test1 = image_rgb_create(0, 0, NULL);
    unsigned char pixels_ptr_test2[] = {255, 255, 255, 128, 128, 128, 0, 0, 0};
    ImageRGB test2 = image_rgb_create(1,3, pixels_ptr_test2);
    image_rgb_destroy(&test1);
    image_rgb_destroy(&test2);
}