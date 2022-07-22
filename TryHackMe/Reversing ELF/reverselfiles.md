# Reversing ELF
## Room for beginner Reverse Engineering CTF players

Common commands:
#### Note: replace `<crackme>` with the actual name of the `crackme` file. Don't include the `<` or `>`.

`file <crackme>`: for researching file
`strings <crackme>`: for printing out human readable strings in `<crackme>`
`chmod +x <crackme>`: to set the execute bit
`.\crackme`: to run the crackme

### Radare2 
#### Sometime we need to "dig deeper" so use. 
Description:  Advanced commandline hexadecimal editor, disassembler and debugger

`r2 -d <crackme>`
Once you have started radare2, enter these commands to investigate.
`aaa`:
`afl`
`pdf @main`
`pdf @sym.imp.printf`
`pdf @sym.compare_pwd`
When debugging:
1. `ood 'argument'`: provide argument to program; can be random.
2. `db <address>`: set breakpoint at address; include `0x` as well.
	1. Use `db -<address>` to remove breakpoint.
3. `dc`: execute program, which will hit the breakpoint.

`vV`: enter graph mode
You can use `:` to enter the same commands as in text mode.
