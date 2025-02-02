Hey everyone, medium-ish update today.

## Website 2.0

I've wanted to transition away from the old site / mkdocs for a while now as its quite hard to maintain and keep everything up to date, so I built a new site using Next that uses ISR to rebuild its content using the dictionarry database. Basically this just means:
- Database gets an update -> Website sees its data is stale -> Website rebuilds itself with new data -> santiago smiles in not needing to do anything

This all ties into the whole "write once" philosophy that I instilled with Profilarr and has made development much easier. 

### Profile Builder

This idea has gone through many iterations since i started Dictionarry last year.
1. A static flowchart with not nearly enough information / choice: https://github.com/santiagosayshey/website/blob/030f3631b4f6fffdb7fa9f4696e5d12defc84a46/docs/Profiles/flowchart.png
2. The "Profile Selector" (terrible name): https://selectarr.pages.dev/
3. Frankenstein's triangle: 