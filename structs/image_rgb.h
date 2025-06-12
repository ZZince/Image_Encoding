#ifndef IMAGE_H
#define IMAGE_H
#include "../DLL_export.h"

/**
 * @struct ImageRGB
 * @brief Represents a simple RGB image stored in raw pixel format.
 *
 * This structure stores image data in an uncompressed format, where each pixel
 * is represented by three consecutive bytes: red, green, and blue (RGB).
 * The pixel data is arranged in row-major order, starting from the top-left
 * corner and proceeding row by row.
 *
 * Fields:
 * - width:  The number of pixels per row (image width).
 * - height: The number of rows in the image (image height).
 * - pixels: A pointer to the raw pixel buffer (size: width * height * 3 bytes).
 */
typedef struct
{
    int width;
    int height;
    unsigned char *pixels;
} ImageRGB;


IMAGE_RGB_API ImageRGB image_rgb_create(int width, int height, unsigned char *pixels);    // Create a new ImageRGB struct
IMAGE_RGB_API void image_rgb_destroy(ImageRGB *image);

#endif