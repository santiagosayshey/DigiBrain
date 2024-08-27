| Feature Type      | HEAP                                                                                       | STACK                                                  |
| ----------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| Memory Allocation | Dynamic memory allocations at runtime                                                      | Fixed memory allocations known at compile time         |
| Data Types        | Objects, big buffers, structs, persistence larger things                                   | Local variables, return addresses, function args       |
| Speed             | Slower, Manual<br>- Done by the programmer<br>- Malloc/calloc/realloc/free<br>- New/delete | Fast, Automatic<br>- Done by the compiler              |
| Abstraction       | N/A                                                                                        | Abstracts away any concept of allocating/de-allocating |
| Growth            | Grows upwards from the bottom                                                              | Grows downwards from the top                           |
