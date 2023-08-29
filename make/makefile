#this is the makefile for 3 files main.c, add.c, and hello.c
#this file must be saved by name makefile


#******** Method 1 ******************

#final_compiled:
#	gcc main.c add.c hello.c -o final_compiled


#******** Method 2 ******************
#$(CC) = gcc
#final_compiled_target:
#	$(CC) main.c add.c hello.c -o final_compiled
#
#Clean_target:
#	rm final_compiled


#******** Method 3 ******************
#$(CC) = gcc
#main_target: target1 target2 target3
#	$(CC) main.o add.o hello.o -o final_compiled
#
#target1: main.c header.h
#	$(CC) -c main.c
#
#target2: hello.c header.h
#	$(CC) -c hello.c
#
#target3: add.c header.h
#	$(CC) -c add.c
#
#Clean_target:
#	rm *.o final_compiled


#******** Method 4 ******************
$(CC) = gcc
# The CFLAGS variable sets compile flags for gcc:
#  -g        compile with debug information
#  -Wall     give verbose compiler warnings. For instance, warning related to main function returning void.
#  -O0       do not optimize generated code
#  -std=c99  use the C99 standard language definition.
CFLAGS = -g -O0 -std=c99

# The LDFLAGS variable sets flags for linker
#  -lm   says to link in libm (the math library)
LDFLAGS = -lm

# In this section, you list the files that are part of the project.
# If you add/change names of source files, here is where you
# edit the Makefile.
SOURCES = main.c hello.c add.c
OBJECTS = $(SOURCES:.c=.o)
TARGET = final_compiled


# The first target defined in the makefile is the one
# used when make is invoked with no argument. Given the definitions
# above, this Makefile file will build the one named TARGET and
# assume that it depends on all the named OBJECTS files.

$(TARGET) : $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

# Phony means not a "real" target, it doesn't build anything
# The phony target "clean" is used to remove all compiled object files.

#.PHONY: clean

clean:
	@rm -f $(TARGET) $(OBJECTS) core
