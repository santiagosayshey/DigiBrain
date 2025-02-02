Hey everyone, medium-ish update today.

## Website 2.0

I've wanted to transition away from the old site / mkdocs for a while now as its quite hard to maintain and keep everything up to date, so I built a new site using Next that uses ISR to rebuild its content using the dictionarry database. Basically this just means:
- Database gets an update -> Website sees its data is stale -> Website rebuilds itself with new data -> santiago smiles in not needing to do anything

This all ties into the whole "write once" philosophy that I instilled with Profilarr and has made development much easier. 

### Profile Builder

Going back to the very first dev log i wrote in June last year, I wrote about "profile selector v3" and this very abstract triangular 