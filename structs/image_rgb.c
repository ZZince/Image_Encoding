#include "image_rgb.h"
#include "../DLL_export.h"
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
// gcc -m64 -shared -g -O0 -o tests/image_rgb.dll structs/image_rgb.c -I. -DIMAGE_RGB_EXPORTS -Wl,--out-implib,tests/libimage_rgb.dll.a
IMAGE_RGB_API ImageRGB image_rgb_create(int width, int height, unsigned char *pixels) {
    ImageRGB image;
    image.width = width;
    image.height = height;

    size_t size = (size_t)width * height * 3;

    if (size > 0) {
        image.pixels = (unsigned char *)malloc(size);
        if (image.pixels && pixels != NULL) {
            memcpy(image.pixels, pixels, size);
        }
    } else {
        image.pixels = NULL;
    }

    return image;
}

IMAGE_RGB_API void image_rgb_destroy(ImageRGB *image){
    if (image == NULL){
        return;
    }

    if (image->pixels != NULL){
        free(image->pixels);
        image->pixels = NULL;
    }

    image->width = 0;
    image->height = 0;

    return;
}