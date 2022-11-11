

echo "====> COMPILING THE BOOTLOADER <===="
nasm -f bin bootl.S -o bootl.bin

echo "====> COMPILING THE KERNEL     <===="
nasm -f bin kernl.s -o system.bin

echo "====> CREATING THE DISK IMAGE <===="
dd if=/dev/zero of=disk.img bs=512 count=2880
mkfs.fat -F 12 -n "REFACTORING" disk.img
dd if=bootl.bin of=disk.img conv=notrunc
mcopy -i disk.img system.bin "::system.bin"
