CC = gcc
MPICC = mpicc
CFLAGS = -O2 -std=c99 -Wall -Wextra
LDFLAGS = -lm
COMMON = fft.c
HEADERS = fft.h
CLANG_FORMAT = clang-format
FORMAT_FILES = fft.c fft.h fft_serial.c fft_mpi.c

.PHONY: all serial format format-check clean
all: fft_serial fft_mpi
serial: fft_serial

fft_serial: fft_serial.c $(COMMON) $(HEADERS)
	$(CC) $(CPPFLAGS) $(CFLAGS) -o $@ fft_serial.c $(COMMON) $(LDFLAGS)

fft_mpi: fft_mpi.c $(COMMON) $(HEADERS)
	$(MPICC) $(CPPFLAGS) $(CFLAGS) -o $@ fft_mpi.c $(COMMON) $(LDFLAGS)

format:
	$(CLANG_FORMAT) -i $(FORMAT_FILES)
	
clean:
	rm -f fft_serial fft_mpi fft_serial.exe fft_mpi.exe
