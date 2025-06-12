# === Variables ===
CC = gcc
CFLAGS = -g -O0 -m64 -I. -DIMAGE_RGB_EXPORTS
LDFLAGS = -shared -Wl,--out-implib,tests/libimage_rgb.dll.a
TARGET_DLL = tests/image_rgb.dll
TARGET_EXE = tests/test_image_rgb.exe
SRC_DLL = structs/image_rgb.c
SRC_TEST = tests/test_image_rgb.c

all: test_struct_rgb

# === Compilation et test avec Dr. Memory ===
test_struct_rgb: $(TARGET_DLL) $(TARGET_EXE)
	@echo "==> Running Dr. Memory..."
	drmemory ./$(TARGET_EXE)

$(TARGET_DLL): $(SRC_DLL)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

$(TARGET_EXE): $(SRC_TEST)
	$(CC) -g -O0 -m64 -o $@ $< -I. -Ltests -limage_rgb

# === Nettoyage ===
clean:
	@echo "==> Cleaning..."
	@del /Q /S *.dll *.dll.a *.exe *.lib 2>nul || true
	@echo "Clean complete."
