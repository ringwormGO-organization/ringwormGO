CC = gcc
CFLAGS = -Wall -Wextra -pedantic -g -lm

OBJDIR = objects
OBJS = $(addprefix $(OBJDIR)/, $(patsubst %.c, %.o, $(wildcard *.c)))

BIN = tau

all : $(OBJDIR) $(BIN)

$(OBJDIR):
	mkdir $(OBJDIR)

$(BIN) : $(OBJS)
	$(CC) $(OBJS) -o $(BIN) $(CFLAGS)

$(OBJDIR)/%.o : %.c
	$(CC) $(CFLAGS) -c $< -o $@

run:
	./$(BIN)

clean:
	rm -rf $(wildcard *.o) objects

full_clean:
	rm -rf $(BIN) $(wildcard *.o) objects
