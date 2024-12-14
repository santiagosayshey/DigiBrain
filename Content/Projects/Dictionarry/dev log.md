hey @everyone, I just wanted to share a small accomplishment from today as well as some metric changes. 

## Vision (almost) Realized

```bash
$ python profile_compile.py 'profiles/1080p Encode.yml' '1080p Encode (sonarr - master).json' -s
Converted profile saved to: 1080p Encode (sonarr - master).json

$ python importarr.py
Importing Quality Profiles to sonarr : Master
Updating '1080p Encode' quality profile : SUCCESS
```

These two commands are the culmination of the architecture overhaul I talked about in August: https://discord.com/channels/1202375791556431892/1246504849265266738/1272756617041154049. The Profilarr standard format _**works**_. A typical profile is now about 300 lines (down from 1000 each for radarr / sonarr), is able to be compiled from PSF to Radarr OR Sonarr (and back!). Regex patterns allow format resolution, so no more editing the same thing 5, 10... 20 times. 

I'm currently in the process of hooking up the database to the new website, and that's looking pretty cool too. I cannot even explain how good it feels to be able to edit a profile once inside Profilarr, push those changes directly from Profilarr, have those changes reflected as incoming changes for end users, and as updated information on the website all in one fell swoop. 

It's taken a huge effort the past 4 months, and I still have to actually connect it to the backend, but I'm fairly happy with how it's turned out. The changes won't be all that evident right away for you guys, but it's going to save me (and anyone who wants to contribute) hours upon hours of development time for everything that I have planned. 

## Golden Popcorn Performance Index Changes

The current GPPi algorithm is strong, but fundamentally flawed. It does not take into consideration release groups who have no data. There are terrific new groups (ZoroSenpai for example) who should be tier ~2 at least, but aren't simply because they have no data. How do we fix this? 

### Popularity

For every encode at a specific resolution for a movie / tv show that is currently popular (via PTP / BTN top 100 monthly), a release group receives +1 score to their GPPi. At the end of every month, the score is normalised / 10, and added to their permanent GPPi score. 