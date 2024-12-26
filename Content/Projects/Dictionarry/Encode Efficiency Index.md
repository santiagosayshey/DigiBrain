This metric is aimed at identifying and ranking release groups based on their propensity to release encodes that meet efficiency thresholds, with particular focus on HEVC releases where optimal efficiency occurs in specific bitrate ranges. By ranking these groups, we effectively prioritize releases that maximize HEVC's compression capabilities while maintaining quality at minimal file sizes.

## What is an Efficiency Threshold?

In its simplest form, it's the size of an encode compared to its likely source (typically a 1080p remux). For example, if MovieA.encode is 10GB and MovieA.remux is 40GB, then MovieA.encode's efficiency threshold is 25% (10GB/40GB × 100).

## Why Is This Important?

Understanding efficiency thresholds helps balance two competing needs: maintaining high video quality while minimizing file size. Modern codecs like HEVC have a "sweet spot" where they deliver excellent quality with significant size savings. Finding this optimal point is crucial because:
- Storage and bandwidth are always limited resources
- Going beyond certain bitrates provides diminishing quality returns
- Different codecs have different efficiency curves
- Release groups need clear standards for quality vs. size trade-offs

## What Threshold is Best?

There's no one-size-fits-all answer when it comes to choosing the perfect efficiency threshold. The "best" threshold depends entirely on the end user's priorities and constraints:
- Space-conscious users might prefer smaller files around 5-10% of source size, accepting some quality trade-offs
- Quality-focused users might push towards 30-40% of source size for more transparent results
- Most users find a sweet spot in the middle, balancing quality and size
However, there's a clear technical limit where going larger becomes pointless - this is where we get to our maximum threshold of 40%.

## Why Set a Maximum Threshold of 40%?

The 40% ceiling exists because we can roughly measure  where HEVC stops being more efficient than older codecs. We do this using three key video quality measurements:

VMAF, developed by Netflix, analyzes how humans perceive video quality and scores it from 0-100. SSIM looks at how similar two images are on a scale of 0-1, focusing on what we actually see rather than just comparing pixels. BD-Rate tells us how much smaller one encode is compared to another while maintaining the same quality level.

Using these tools together shows us that:
- HEVC achieves 20-40% smaller files in the mid-bitrate range (~2-10 Mbps for 1080p)
- These space savings are consistent across different quality levels
- Beyond this point, both old and new codecs reach nearly perfect quality, making HEVC's advantages disappear
- Within these optimal bitrates, HEVC consistently scores above 90 on VMAF (excellent quality) while keeping files well under 40% of the source size

Would you like me to clarify any part of this explanation?

https://medium.com/innovation-labs-blog/bjontegaard-delta-rate-metric-c8c82c1bc42c

https://www.mdpi.com/2079-9292/13/5/953