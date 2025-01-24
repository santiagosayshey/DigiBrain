So, how does Dictionarry *actually simplify media automation?*

Well, first we need to understand that we're trying to automate the subjective analysis of how "good" a release is. To do that, we need to first define what "good" even means. To some people, it could mean how well something looks on their screen, or sounds through speakers; we define this as quality. To others, it means how many releases they can download while still maintaining some kind of quality standard; we define this as efficiency. 

So, new question - how do we measure quality and efficiency? You might think we'd want to parse releases and find their technical properties; resolution, bitrate, video / audio codecs, hdr, etc. 

```
Release 1: Blockbuster Movie A 2022 Hybrid 1080p WEBRip DDPA5.1 x264-group A

Release 2: Blockbuster Movie A.1080p.WEBRip.DD+7.1.x264-group B
```

Looking at these two releases, you'll notice that they both have the EXACT same technical specification and would rank equally! So using technical properties to measure quality / efficiency can be effective, but is largely limited by the information that they convey. 

- rank release groups
- release groups are the most consistent and simple way to measure how "good" something is. 
	- if group A has a proven track record of achieving metric A, then it should be prioritsed
	- if group B has a proven track record of achieving metric B, then IT should be prioritised
- ok, well what "track records" are we measuring? 
- well, the two most important properties of media is its 
	- quality - how good it looks / sounds
	- efficiency - how well it utilises its file size
- so, we rank release groups based on how consistently they achieve certain levels of quality and or efficiency.
- ok, but how we quantify this?
	- data driven analysis through two key metrics

