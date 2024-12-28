This metric is aimed at identifying and ranking release groups based on their propensity to release encodes that meet certain compression ratios, with particular focus on HEVC releases where optimal efficiency occurs in specific bitrate ranges. By ranking these groups, we effectively prioritize releases that maximize HEVC's compression capabilities while maintaining quality at minimal file sizes.

## What is a Compression Ratio?

A compression ratio is a special metric we created specifically for evaluating encodes against their sources. We express this as the encoded file size as a percentage of its source size (typically a 1080p remux).

For example:

| Movie   | Source (Remux) | Encode | Compression Ratio |
| ------- | -------------- | ------ | ----------------- |
| Movie A | 40 GB          | 10 GB  | 25%               |
| Movie B | 30 GB          | 6 GB   | 20%               |
| Movie C | 50 GB          | 15 GB  | 30%               |

## Why Is This Important?

Understanding compression ratios helps balance two competing needs: maintaining high video quality while minimizing file size. Modern codecs like HEVC have a "sweet spot" where they deliver excellent quality with significant size savings. Finding this optimal point is crucial because:
- Storage and bandwidth are always limited resources
- Going beyond certain bitrates provides diminishing quality returns
- Different codecs have different efficiency curves
- Release groups need clear standards for quality vs. size trade-offs

## What Ratio is Best?

There's no one-size-fits-all answer when it comes to choosing the perfect compression ratio. The "best" ratio depends entirely on the end user's priorities and constraints:
- Space-conscious users might prefer smaller files around 5-10% of source size, accepting some quality trade-offs
- Quality-focused users might push towards 30-40% of source size for more transparent results
- Most users find a sweet spot in the middle, balancing quality and size
However, there's a clear technical limit where going larger becomes pointless - this is where we get to our maximum ratio of 40%.

## Why Set a Maximum Ratio of 40%?

The 40% ceiling exists because we can roughly measure where HEVC stops being more efficient than older codecs. We do this using two key video quality metrics:
- **VMAF,** developed by Netflix, analyzes how humans perceive video quality and scores it from 0-100. 
- **BD-Rate** tells us how much smaller one encode is compared to another while maintaining the same quality level.

Using these tools together shows us that:
- HEVC achieves 20-40% smaller files in the mid-bitrate range (~2-10 Mbps for 1080p)
- These space savings are consistent across different quality levels
- Beyond this point, both old and new codecs saturate at near transparent quality, making HEVC's advantages disappear

Give these articles a read to better understand how VMAF and BD-Rate tell us how efficient a codec is.

https://medium.com/innovation-labs-blog/bjontegaard-delta-rate-metric-c8c82c1bc42c
https://www.mdpi.com/2079-9292/13/5/953

## How Do We Apply This Index?

