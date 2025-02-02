Hey everyone, medium-ish update today.

## Website 2.0

I've wanted to transition away from the old site / mkdocs for a while now as its quite hard to maintain and keep everything up to date, so I built a new site using Next that uses ISR to rebuild its content using the dictionarry database. Basically this just means:
- Database gets an update -> Website sees its data is stale -> Website rebuilds itself with new data -> santiago smiles in not needing to do anything

This all ties into the whole "write once" philosophy that I instilled with Profilarr and has made development much easier. 

### Profile Builder

This idea has gone through many iterations since i started Dictionarry last year.
1. A static flowchart with not nearly enough information / choice: https://github.com/santiagosayshey/website/blob/030f3631b4f6fffdb7fa9f4696e5d12defc84a46/docs/Profiles/flowchart.png
2. The "Profile Selector" (terrible name): https://selectarr.pages.dev/
3. Frankenstein's triangle: [Discord Link](https://discord.com/channels/1202375791556431892/1246504849265266738/1246536424925171925)

Frankenstein's triangle was supposed to be what i shipped with the new website (and I actually finished it too!), but I decided to scrap it at the last minute. Basically it worked by calculating the area of the triangle using some formula named after some guy i forget to guesstimate user choice based on their previous selection. It did this by normalising the "score" of each profile on each of it's axes and finding the best fitting profile based on triangle area that used the axis that was changed. It was decent, but results were a bit of a black box and eve