Reference: https://www.youtube.com/watch?v=Dq8l1_-QgAc&ab_channel=LowLevelLearning

# Compile the code in c, with no debug inforrmation
To compile our c file:
```
gcc -o c_debugging c_debugging.c -s
```
Here, we better to use the following, if our root directory is CUDA fo;der:
```
gcc -o c_debugging ./02_cuda-intro-main/c_debugging.c -s
```

To see the complied file, in linux:
```
file c_debugging
```

To get the size of this compile file (we will see it is only 6-7 k-bite):
```
wc -c c_debugging
```

Now, we can not run the gdb on it as is, and see the source code on it:
```
gdb ./c_debugging    
```
===> and then (lay means layout here)
```
lay next
```

# Compile the code in c, with debug inforrmation
To get the debug infromation into the comiled file, we need to add additional tag into it, and that is instead of -s, we should use tag 
```
gcc -o c_debugging c_debugging.c -g
```

Now, if we look at the compiled file, and run the followig, if we read the output carefully we see the "with debug info".
```
file c_debugging
```

With debug information, our compiled file is little bigger than without debug-infomration (section 1 above):
```
wc -c c_debugging
```

## debugging:
Now that we put the debug information, we can not run the gdb on it as is, and see the source code on it:
```
gdb ./c_debugging    
```
===> and then (lay means layout here)
```
lay next
```

After few enter, we can see the code, followed by the assembly code for this program afterwards. Now we can step through our code.

## few useful gdb commands:
1) Breakpoint:
Suppose we want to add a breakpoint at the line starts with main:
```
(gdb) break main
```

2) We can now run the program, and it will stop at the breakpoint in the assemby code. One line of c original code, implies multiple lines
of assembly code. We can walk through the assembly code or through the original c code:
```
(gdb) run
```

3) Go to next line: This one goes to the next line in the c original code. It means in the assembly code, i nthe (gdb) we see several lines of
assembly code is being jumped over.
```
(gdb) next
```

if we used nexti, it would have gone to the next line in the assembly:
```
(gdb) nexti
```

3) Step into
```
(gdb) step
```

## Reading debug info:
After hitting "(gdb) next" a couple of time, we finlaly get into the scanf line, where the problem is. If we enter a numer, say 5, then
we get a bunch of debug information inthe command line:

```
(gdb) next
5

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff7a51872 in _IO_vfscanf_internal (s=<optimized out>, format=<optimized out>,
    argptr=argptr@entry=0x7fffffffd670, errp=errp@entry=0x0) at vfscanf.c:1898
```

Here, it shows it goes into the "_IO_vfscanf_internal", and something went wrong there.

Question: In the assembly code, what instruction in "our scanf" made it problematic?

x/  ==> means "examine right view memory"
x/i ==> means "examin the instruction"
x/i $pc

```
(gdb) x/i $pc
```
This will produce the following in the command line:
```
=> 0x7ffff7a51872 <_IO_vfscanf_internal+18050>: mov    %eax,(%rdx)
```

This will be read" "it is trying to move into "eax", the thing pointed to by "rdx"". This is the Itel instruction that
says dereference "rdx" and put it into "eax". Then we can do:

```
(gdb) info registers
```
This is to figure out what is the register state of the program that is causing this to happen during this instruction.
From the outputted text in the command line, we see that "rax is 5", and "rdx is 2". However, from "(gdb) x/i $pc", we know
that it tried to de-reference rdx and put it into eax. So, the number 2 in rdx is not a valid instruction. This is because
scanf takes a pointer, nit a number.


