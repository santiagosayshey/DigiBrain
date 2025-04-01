hey @everyone, long awaited announcement :)

## Profilarr is in Beta 🚀

Many people are already aware, but I thought I should formally announce here on discord that Profilarr is out in beta! I've been working on it since around July last year and put in a massive effort over the Christmas break to get it working. Even though it's not nearly as stable as I would like it to be, it implements the core architecture I first talked about [here](https://dictionarry.dev/devlog/architecture_overhaul). There is still so (x10) much to be done in terms of bugs & polish & new features, but I'm happy sharing it as is. Hopefully you can all find some benefit in using it too :)

### Databases

Along with Profilarr, the Dictionarry database has also got an overhaul. We introduced the new encode efficiency index, 2160p Quality and Balanced profiles as well as other small improvements like editions, repacks and freeleech. Here are some scattered thoughts that you might also be interested in: 
- @seraphys has been working on a scoring refactor that introduces 720p fallback, fixes streaming service names, and groups similar releases together better. It's a huge change that I haven't been able to fully test myself, but I've merged it into a separate branch because I know people are pretty antsy to start testing themselves :) Anyone is free to give it a try, you just have to switch to the `scoring-refactor` branch in Profilarr. Please direct any issues / improvements to the database's [Issue Tracker](https://github.com/Dictionarry-Hub/database).
- I'm personally not too happy with the state of the current database - poorly named files and renames/imports weren't taken into enough consideration and it's causing way too many download loops. I'm still trying to figure out exactly how I want to tackle these problems but I just want people to know that it is on my mind and it will be improved in future. 

### Tweaks

I talked about tweaks in detail [here](https://dictionarry.dev/devlog/profile_tweaks) and had actually implemented some of them into Profilarr, but decided to remove them at the last minute. On paper, it's an interesting system. In practice, it's confusing and really hard to program for. It's meant to be a database agnostic feature, but was hardcoded into profilarr's profile system. I'm going to keep this feature on the roadmap as maybe for now, but I'm gonna have to completely rethink how to implement it from the ground up. 
## Housekeeping

