Hey everyone, medium-ish update today.

## Website 2.0

I've wanted to transition away from the old site / mkdocs for a while now as its quite hard to maintain and keep everything up to date, so I built a new site using Next.js that uses ISR to rebuild its content using the dictionarry database. Basically this just means:
- Database gets an update -> Website sees its data is stale -> Website rebuilds itself with new data -> Santiago smiles in not needing to do anything

This all ties into the whole "write once" philosophy that I instilled with Profilarr and has made development much easier. 

### Profile Selector?

This idea has gone through many iterations since i started Dictionarry last year.
1. A static flowchart with not nearly enough information / choice: https://github.com/santiagosayshey/website/blob/030f3631b4f6fffdb7fa9f4696e5d12defc84a46/docs/Profiles/flowchart.png
2. The "Profile Selector" (terrible name): https://selectarr.pages.dev/
3. Frankenstein's triangle: [Discord Link](https://discord.com/channels/1202375791556431892/1246504849265266738/1246536424925171925)

Frankenstein's triangle was supposed to be what i shipped with the new website (and I actually finished it too!). It worked by calculating the area of the efficiency/quality/compatibility triangle using some formula named after some guy i forget, to guesstimate user choice based on their previous selection. It did this by normalizing the "score" of each profile on each of it's axes and finding the best fitting triangle that used the axis that was changed. 

Results were pretty good but I felt that it abstracted *too much* of what made any user choice meaningful so I decided to scrap it. 

### Profile Builder!

In it's place is the "Profile Builder" (maybe also a terrible name). It still attempts to abstract audio/video down into more quantifiable groupings, but limits itself to explanations of certain things where more abstraction isn't worthwhile. It's pretty self explanatory once you use it, but basically you choose through increasingly niche groupings -> resolution -> compression -> encode type -> codec -> HDR. At each step, a list of recommended profiles will be shown. I think this new system helps to fix the "trying to get the profile I want" issue as it starts pretty broad and gets increasingly more specific the more things you choose. It's up now, give it a playwith; let me know if its good / bad / needs changes. 

#### Modules

