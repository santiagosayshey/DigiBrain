Hello, I'd like to share the passion project I've been working on for the past 2 years of my life. I often see that many posts here on linkedin are self congratulatory and indulge in celebrating each other's careers, goals and achievements. This is a good thing, this platform is meant to be a place in which we can show ourselves off and convince our future employers - hire me! 

I feel like its the expected culture at this point:

```
im <emotional adjective> to share that i'm <verb>ing as a <superfluous title> at <prestigious company>.

here's what i learned
- something about teamwork
- something about overcoming challenges
- something about the importance of learning
```

There's nothing wrong with this these posts, but they fail to capture our full experiences. They fail to show that real achievement and growth is hard, doesn't usually happen, and requires more than just hard work. In this post, I want to share my genuine experience in working on something that actually meant something to me. Not so that I can wallow in my misery, or get engagement by being different, but so that I can help encourage people to keep doing what they're doing, and not feel intimidated or scared or less than, for not following the status quo. 

I worked on Dictionarry and Profilarr for 2 years. I used every bit of knowledge I've learned so far in my 3 years of computer science. I built a website. Then I built a better website. Then I built a full stack development platform with git integration, authentication and a custom compiler!

At no point, did I *ever* feel like I knew what i was doing. I constantly felt like an impostor; that what i was building was impossible, nobody would appreciate and would ultimately be forgotten. People would see through my unoptimized, non factory pattern singleton functional code and not recognize me as a developer, but as a fraud. Somebody who is somehow deceiving us for monetary gain and clout. I remember going to bed one night so anxious about the merge conflict module that I actually dreamed about someone wanting to fight me over it because it sucked that bad. 

My brain still convinces me that these are facts sometimes. Even after I look at the 3000+ commits on GitHub, the community I've built on Discord and even the optional donations I've received. I still see the few harsh comments from entitled users / disgruntled competitors and convince myself that it's on me to change their mind. It's on me to write better code. It's on me to *do better*. 

I'll see a LinkedIn / Facebook / Instagram post and think to myself - "Wow! This person really has their stuff together, I need to be more like them." That this person has ended up in this terrific new situation of growth and money and all these great things we want, simply because they are a better person than I am. 

But what I'm starting to understand, is that none of those things really matter. It's not actually on me to convince every single person on the planet that my project is good. What somebody else is doing with their life shouldn't influence how I go about living mine. None of those things matter, because I'm already doing the best I can, and that is enough. That's what I want people to take away from this post - if you're doing the best you can, then nothing else matters. 

Pat yourself on the back. Pat others on the back too. 

With that being said, I introduce Dictionarry. It's a self hosting companion ecosystem that aims to abstract complex audio / video concepts into quantifiable needs through objective, data driven configurations. 

- The database is the core of the project and contains all the user configurations and wiki articles
	- Rather than using any traditional sql / nosql database, I opted for plain yml so that we could version control the configurations and let end users make custom changes that could be persisted. 
	- https://github.com/Dictionarry-Hub/database
- The website acts as documentation for this database and allows users to interact with it to find their desired configurations.
	- Using Next.js, we build a fully static website that can be rebuilt using incremental static regeneration whenever the database receives an update.  
	- https://dictionarry.dev/
- Profilarr is a companion tool that allows end users to:
	- Easily connect our configurations with their existing setups
	- Directly interface with the database and submit improvements / new features
	- React powers the frontend, Flask in the backend. 
	- https://github.com/Dictionarry-Hub/profilarr (currently sitting at 272 stars, go check it out!!)

Dictionarry is the culmination of two years of very hard work. I poured my heart and my soul into this project because I wanted to help people. I have spent 2000+ hours coding, researching and designing. I have 4000+ commits in the past year alone on my personal GitHub. I make no money working on this, it drives me insane and I sometimes think about deleting it all and disappearing to a cabin in the woods. I'm not writing code that solves world hunger. I'm not building a startup worth a billion dollars. I'm building a very niche solution to a very niche problem that matters to me. And that's okay. 

But I keep going. Not because I need to prove anything to anyone, but because this is what doing my best looks like. And that's worth celebrating just as much as any polished LinkedIn success story.