press ctrl + shoft + V
We should look at the debug_test.c

Reference: https://www.youtube.com/watch?v=V95FNRJGHyM&t=601s&ab_channel=NPTEL-NOCIITM

# 1 Initial preparation:

```
gcc -o test debug_test.c -g                     ==> Compiling with debug info (-g), and  the  elf/executable will be created

readelf -h ./test                                ==> looking at the header (-h) of the elf file
                                                    Take a look at "Entry point memory address for this elf file:               0x560"
readelf -s ./test

objdump --disassemble-all ./test  > test.lst    ==> create a disassembled file and then write it into a *.lst file (> *.lst). 
                                                    We can vim the *.lst file: (a) search for <main> by:    /<main>      in vim, in normal mode
                                                    we can simultaneously open the corresponding test.c file in this vim session ==> :sp debug_test.c
                                                                                    and then set the line numbers                ==> :set nu
objdump -D ./test  > test.lst


```

By taking a look at the disassembled_obj_file (vim test.lst), and then search for "<main>:" in vim (by /<main>:), we can see:

![disassembled_obj_file](./img/disassembled_obj_file.png)


# 2 debug
We will use GNU debugger, gdb, to look at registers, and debug informations. We can run the "gdb test", and then:

```
(gdb) list
(gdb) b main            [==> or (gdb) break main]
(gdb) b main.c:4        [ put a bbreak at line=4 of main.c]

(gdb) r                 [==> (gdb) run]
(gdb) c                 [==> (gdb) continue]

(gdb) n                 [==> next line in the c-code, which might mean several lines code in assembly]
(gdb) ni                [==> (gdb) nexti    means next line in the assembly code]

(gdb) si                [==> (gdb) stepi    means step into]
(gdb) si 3              [==> do 3 line of instructions at the same time]


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