So, how does Dictionarry *actually simplify media automation?*

Well, first we need to understand that we're trying to automate the subjective analysis of how "good" a release is. To do that, we need to first define what "good" even means. To some people, it could mean how well something looks on their screen, or sounds through speakers; we define this as quality. To others, it means how many releases they can download while still maintaining some kind of quality standard; we define this as efficiency. 

So, new question - how do we measure quality and efficiency? You might think we'd want to parse releases and find their technical properties; resolution, bitrate, video / audio codecs, hdr, etc. 

```
Release 1 (25.2 GiB): Blockbuster Movie A 2022 Hybrid 1080p WEBRip DDPA5.1 x264-group A

Release 2 (27.3 GiB): Blockbuster Movie A.1080p.WEBRip.DD+7.1.x264-group B
```

Looking at these two releases, you'll notice that they both have the EXACT same technical specification and would rank equally. But they're different sizes... so which is better? Using technical properties to measure quality / efficiency can be effective, but is largely limited by the information that they convey. You can't adequately answer which is better just by looking at these releases in isolation. So how do we not look at these releases in isolation? Or rather, how do we extrapolate information that isn't already there? 

Our answer lies in the little bit of information at the end of every release - it's group tag. Dictionarry tracks historic release group data in order to rank groups based on their propensity to reach quantifiable levels of quality and efficiency. We do this using two metrics:

1. Golden Popcorn Performance Index (GPPi): How many golden popcorns a release group has, as a ratio of their total number of releases
2. Encode Efficiency Index (EEi): The average size of a release group's encode compared to it's likely source. 

These metrics are evidence based, data driven and objective. They DO NOT rely on reputation or word of mouth or any other subjective means of measurement. 

TL;DR: Dictionarry simplifies media automation by prioritizing release groups that achieve quantifiable levels of quality and efficiency through objective measurement. These release group rankings are built and maintained as custom formats to be scored in their respective quality profiles. You can review these group rankings below. 

