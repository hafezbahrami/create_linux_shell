press ctrl + shoft + V
We should look at the buggy.c

Reference: https://www.youtube.com/watch?v=Dq8l1_-QgAc&ab_channel=LowLevelLearning

# 0 Basic VIM

```
vim buggy.c

press "esc"         ==> puts it in normal (just display) mode
pres i              ==> puts it in insert and modifying mode

: then q!           ==> quitting w/o saving
  then x!           ==> save and then quit 

in normal/only-display mode,
: set number        ==> after hitting "enter", it shows the line-numbers
:6                  ==>  //     //      //   , it goes to line 6

```

# 1 Compile the code in c: 
### 1-1 With no debug inforrmation
To compile our c file (-s stands for stripped):
```
gcc -o buggy_comp_out buggy.c -s
```

With this the lef file (linux exe file) [buggy_comp_out] will be created. We can see the header of this elf file bybelow. We can read the machin [X86] this was build for, or the memmory entry point for this elf file.
```
readelf -h ./buggy_comp_out

readelf -s ./buggy_comp_out
```

We also can see the whole diassembled code for this, by following command (and put the output in a *.lst file for reading it through vim):
```
objdump --disassemble-all ./buggy_comp_out  >  XX.lst
objdump -D ./buggy_comp_out  >  XX.lst
```

vim the XX.lst, and then search for main by "/main".
```
/main         ==> [or more precisely   /<main>]    will look for the word "mina", main function, in the disassembled file

:sp buggy.c   ==> will also open the buggy.c file in the vim edditor, simulatenously
:set nu       ==> will set the line numbers in the buggy.c in the vim edditor
```

To see the complied file, in linux:
```
file buggy_comp_out
```

To get the size of this compile file (we will see it is only 6-7 k-bite) [-c ==> count, -l ==> # of lines]:
```
wc -c buggy_comp_out
```

Now, we can not run the gdb on the compiled_file (buggy_comp_out) as is, since we did not compile it with debug information:
```
gdb ./buggy_comp_out    
```
===> and then (lay means layout here) []write "quit" or "q" to exit the debug mode]
```
(gdb) list            ==> list the whole actual c-code for us
lay next              ==> lays out the assemble code for us
```

### 1-2 With debug inforrmation
To get the debug infromation into the comiled file, we need to add additional tag into it, and that is instead of -s, we should use tag 
```
gcc -o buggy_comp_out buggy.c -g
```

Now, if we look at the compiled file, and run the followig, if we read the output carefully we see the "with debug info".
```
file buggy_comp_out
```

With debug information, our compiled file is little bigger than without debug-infomration (section 1 above):
```
wc -c buggy_comp_out
```

# 2 gdb: debugging
Now that we put the debug information, we can not run the gdb on it as is, and see the source code on it:
```
gdb ./buggy_comp_out    
```
===> and then (lay means layout here)
```
lay next
```

After few enter, we can see the code, followed by the assembly code for this program afterwards. Now we can step through our code.

### 2-1 Few useful gdb commands:
1) Breakpoint:
Suppose we want to add a breakpoint at the line starts with main:
```
(gdb) b main            [==> or (gdb) break main]
(gdb) b main.c:4        [ put a bbreak at line=4 of main.c]

(gdb) r                 [==> (gdb) run]
(gdb) c                 [==> (gdb) continue]

(gdb) n                 [==> next line in the c-code, which might mean several lines code in assembly]
(gdb) ni                [==> (gdb) nexti    means next line in the assembly code]

(gdb) si                [==> (gdb) stepi    means step into]
(gdb) si 3              [==> do 3 line of instructions at the same time]

```


### 2-2 Reading debug info:
After hitting "(gdb) next" a couple of time, we finlaly get into the scanf line, where the problem is. If we enter a numer, say 5, then
we get a bunch of debug information inthe command line:

```
(gdb) info registers        [==> regiters infos]
(gdb) info registers rsp rip rbp      [==> only registers info for these few registers]
(gdb) info locals           [==> local variables infos]
(gdb) info args


(gdb) p  XXVarname      ==> to brint a variable
(gdb) p  XXVarname=1    ==> setting this variable (=1) while in debugging mode

(gdb) bt   (or bt full) ==> shows the backtrace or the call stack that we have in VScode UI 

(gdb) x/5i $pc          ==> $pc is allias for $rip  [(gdb) x/5i $rip ], the pointer/register for instruction  ==> so, basically we extract (x) next 5 instructions (i) 
(gdb) x/32x $rsp        ==> show 32 memory-location, right after wherever rsp register address is in the memory.  ==> the "x" after 32, means show the memory address in hexa-decimal
(gdb) x/32  $rsp        ==> [identical to x/32i  $rsp]  ==> show 32 next instructions and the memory address


(gdb) disasseble        ==> gives all the assebly code/instruction within this code. Part of which (just 5 lines) will be obvious by "(gdb) x/5i $pc"
                        ==> This is exactly what we got in previous section by "objdunp -D ...."

(gdb) quit              ==> or simply "q"
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


