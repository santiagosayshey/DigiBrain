- A release is packaging up code and pushing it to whatever version of production you have

## Semantic Versioning

- its just a number schema that tracks changes for code
- Once a version is released, it cannot be changed
- Any new changes needs to be a new released

```
MAJOR.MINOR.PATCH
```

- Patch is incremented for bug fixes & trivial updates
- Minor is incremented for backwards compatible functionality changes (user doesnt need to worry about upgrading)
- Major is incremented for breaking functionality changes (user might need to start over completely, apis need to be used differently, etc)


## Git Tags

- it's just a way to apply a marker to a commit