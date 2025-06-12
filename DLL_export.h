#ifdef _WIN32
    #ifdef IMAGE_RGB_EXPORTS
        #define IMAGE_RGB_API __declspec(dllexport)
    #else
        #define IMAGE_RGB_API __declspec(dllimport)
    #endif

#else
    #define IMAGE_RGB_API
#endif