https://medium.com/innovation-labs-blog/bjontegaard-delta-rate-metric-c8c82c1bc42c

https://www.mdpi.com/2079-9292/13/5/953

> Bjontegaard Delta-Rate (BD Rate) metric can be used to compare and choose the encoder or configuration, that provides the best compression results.

This metric is aimed at identifying and ranking release groups based on their propensity to release an encode that meets a certain efficiency threshold.

## What is an Efficiency Threshold?

In it's simplest definition, it's just how big an encode is, compared to it's most likely source; typically a 1080p remux. For instance, if MovieA.encode is 10gb, and MovieB.remux is 40gb, then MovieA.encode's efficiency threshold is 25% (40/10 \*100)

## How do you determine what the best Efficiency Threshold Is?

We don't. We set a maximum limit (40%) based on data that compares 