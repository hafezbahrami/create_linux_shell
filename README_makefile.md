ctrl+shit+v for compiled .md file
Reference: https://www.youtube.com/watch?v=Dq8l1_-QgAc&ab_channel=LowLevelLearning

Also a good source for Virtualization course:
https://web.stanford.edu/class/archive/cs/cs107/cs107.1174/guide_make.html


# Summary
Here we want to create our own shell. We will explore a couple of important system-calls, such as fork(), wait(), execv().
We will explore, when we write "ls -l -a" in command line, how does it get run. We will figure it out that "ls" is actually a c progmra
located in "/bin/ls" and we basically run this c-program.

Note: Makefile is super sensitive to the white spaces and tab spaces. Below is a good read, on how to use vim to spot the spaces:
https://itslinuxfoss.com/fix-makefile-missing-separator/#:~:text=To%20fix%20the%20error%20Makefile,mistake%20can%20cause%20this%20error.


# makefile

## make folder

I have created some dummy *.c files and one dummy header.h. Now, I can build all 3-4 files into one gcc command:

```
    gcc ./make/main.c ./make/add.c ./make/hello.c ./make/header.h -o final_compiled
    ./final_compiled
```

Now, what if we have 100 files to be compiled. Naming them all in one gcc command will be tedious.

For the rest of this, let's move the root directory to the make folder.

### makefile method 1
The simplest way is the target is noted as final_compiled.

```
final_compiled:
	gcc main.c add.c hello.c -o final_compiled
```

now in the command line, we just need to run the following to create the final_compiled binaries. We could mention the target name
after the make in the command line.
```
make
```

We then can simply:
```
./final_compiled
```

### makefile method 2
We here define two targets: (1) final_compiled, nd (2) Clean.
We first define a variable by: $(CC) = gcc, then we use this variable wherever we want.

The "Clean" target, wants to remove: (1) all *.o files, and (2) our executable final_compiled

```
$(CC) = gcc
final_compiled_target:
	$(CC) main.c add.c hello.c -o final_compiled

Clean_target:
	rm *.o final_compiled
```

Now, let's run this make file, which includes two Targets. If we run 1st target, it will do all the builds and 
compiling command, but not the second target which is for cleaning:
```
make final_compiled_target
```

To clean it
```
make Clean_target
```

### makefile method 3: Multiple Targets
Now make a main target that depends some other targets to get build. Therefore, first the child targets will get build, and finall the 
main target.

```
$(CC) = gcc
main_target: target1 target2 target3
	$(CC) main.o add.o hello.o -o final_compiled

target1: main.c header.h
	$(CC) -c main.c

target2: hello.c header.h
	$(CC) -c hello.c

target3: add.c header.h
	$(CC) -c add.c

Clean_target:
	rm *.o final_compiled
```

The main build happens by:
```
make main_target
```

Then, to clean all the *.o files:
```
make Clean_target
```

### makefile method 4: Multiple Targets
Here we follow the standard explained by the Virtualization course, and more macros.

To run the make file (this will not run the clean target part):

```
make
```

And, to clean:
```
make clean
```