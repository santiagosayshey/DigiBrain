> [!idea]+ Understanding Endianness in Memory
>
> Endianness refers to the order in which bytes are stored in memory for representing larger data types, such as multi-byte integers or floating-point numbers. There are two common endianness formats: 
>
> 1. **Little Endian**: In this format, the least significant byte (LSB) is stored at the lowest memory address, and the most significant byte (MSB) is stored at the highest memory address. Intel x86 processors use this format.
>
> 2. **Big Endian**: In this format, the most significant byte (MSB) is stored at the lowest memory address, and the least significant byte (LSB) is stored at the highest memory address.
> 
> For example, consider the 32-bit integer value `0x01234567` (decimal: 19,088,743):
>
> - In little-endian format, it would be stored in memory as: `0x67 0x45 0x23 0x01`
> - In big-endian format, it would be stored in memory as: `0x01 0x23 0x45 0x67`
>



