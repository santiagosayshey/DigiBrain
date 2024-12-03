hey @everyone, I've been hard at work on the next Profilarr version over the past few weeks and have a new feature to show off!

## Profile Tweaks
The profiles we make are meant to be (really good) starting points, not a strict standard on what you *should* be grabbing. Up until now, profiles existed as singular entities that don't respect custom changes. Merge conflict resolution was a big step in the right direction for this (read more in the last dev log), but it's a bit more hands on, and not something I expect most people to engage with. 

Enter 'Profile Tweaks'. These are simple check boxes you can enable / disable and are unique to each profile. They will ALWAYS be respected, regardless of what updates we make to the base profile. For now, these tweaks include:

- Prefer Freeleech
- Allow Prereleases (CAMS, Screeners, etc)
- Language Strictness
- Allow Lossless audio
- Allow Dolby Vision without Fallback
- Allow bleeding edge codecs (AV-1, H266)

If anyone has any tweak ideas (even super specific ones), please let me know and I'll work on getting it integrated! Here's an image of the Tweaks Tab:
![[Pasted image 20241203190613.png]]

I'd also like to get some feedback on which Tweaks should be enabled by default. Vote below!

## Profilarr Progress
- Progress is steady, I've been working on it every day since my semester ended. It's taken way, way longer than I've expected (sorry!) but I'm happy with how it's starting to look. 
- Git integration is com