from pwn import * 

print "pwn Starting ...";

# print A charactor value
print u8('A'); 

# print elf mode
elf = ELF('/bin/cat');
print hex(elf.address);
print hex(elf.symbols['write']);
print hex(elf.got['write']);
print hex(elf.plt['write']);

# enter interactive mode
sh = process('/bin/sh');
sh.send('echo Go; sleep 3; echo End');
sh.recvline(timeout=1);
sh.interactive();
sh.close();
