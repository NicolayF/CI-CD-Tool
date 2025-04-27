CC = g++
CFLAGS = -std=c++1 -Wall
BIN_DIR = bin

all: build test

build:
		mkdir -p $(BIN_DIR)
		$(CC) $(CFLAGS) src/main.cpp src/utils.cpp -o $(BIN_DIR)/app

test:
		$(CC) $(CFLAGS) tests/test_utils.cpp src/utils.cpp -o $(BIN_DIR)/test
		./$(BIN_DIR)/test

clean:
		rm -rf $(BIN_DIR)

.PHONY: all build test clean