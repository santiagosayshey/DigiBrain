#### Header Guards
```cpp
#ifndef CLASS_H
#define CLASS_H
...
#endif
```

#### Class Declaration
##### Header
```cpp
class Name {
  public:
    Name();
    ~Name();
    int function1();
    bool function2(int var1, float var3);
  private:
    int var1;
    std::string var2;
    bool var3;
};
```

##### CPP
```cpp
#include "Name.h"

Name::Name() {...}
Name::~Name() {...}
int Name::function1() {...}
bool Name::function2(int var1, float var3) {...}
```

#### Templates

- Before every function / member type:
- Where A is the variable to be substituted
```cpp
template <typename A>
```

##### Template function in a class
```cpp
template <typename T>
class A {
  T function1();
};

T A<T>::function1() {...}
```

#### SOLID
1.  SRP: Split classes into separate classes that handle only one responsibility.
2.  OCP: Use inheritance and polymorphism to extend the behavior of a class without modifying its code.
3.  LSP: Make sure subclasses can replace their parent classes without affecting the correctness of the program.
4.  ISP: Create smaller interfaces so that classes only need to implement the methods they require.
5.  DIP: Depend on abstractions (interfaces) rather than concrete implementations to make it easier to change components.

#### ADTs
