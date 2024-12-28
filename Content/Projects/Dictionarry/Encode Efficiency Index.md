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

I'll help improve that section with more detail and concrete examples. Here's a clearer explanation:

## How Do We Apply This Index?

The ranking system works by calculating how close each Release Group / Streaming Service comes to achieving a user's desired compression ratio. This is done through a few key steps:

1. **Delta Calculation**: We calculate the absolute difference (delta) between a group's average compression ratio and the target ratio. For example, if a group averages 25% compression and our target is 20%, their delta would be |25 - 20| = 5 percentage points.

2. **K-means Clustering**: We use k-means clustering to automatically group release groups into tiers based on their deltas. K-means works by:
   - Starting with k random cluster centers
   - Assigning each group to its nearest center
   - Recalculating centers based on group assignments
   - Repeating until stable

This creates natural tiers like "Excellent", "Good", "Fair" based on how well groups match our target ratio.

Let's look at two practical examples with different target ratios:

Sorry - you're absolutely right. Let me use exactly your headers:

- **Example 1:** For users prioritizing storage efficiency, targeting 10% compression:

| Tier | Group | Efficiency | Delta |
|------|-------|------------|-------|
| 1 | iVy | 9.37% | 0.63 |
| 1 | PSA | 7.89% | 2.11 |
| 2 | Vyndros | 16.08% | 6.08 |
| 2 | Chivaman | 16.80% | 6.80 |
| 2 | Amazon Prime (H.265) | 16.15% | 6.15 |
| 2 | Disney+ (H.265) | 20.32% | 10.32 |
| 3 | TAoE | 22.78% | 12.78 |
| 3 | QxR | 23.25% | 13.25 |
| 3 | BRiAN | 25.16% | 15.16 |
| 3 | Movies Anywhere (H.265) | 26.05% | 16.05 |
| 5 | MainFrame | 37.63% | 27.63 |
| 5 | NAN0 | 37.71% | 27.71 |

- **Example 2:** For users seeking a balance of quality and size:

| Tier | Group | Efficiency | Delta |
|------|-------|------------|-------|
| 1 | Movies Anywhere (H.265) | 26.05% | 1.05 |
| 1 | BRiAN | 25.16% | 0.16 |
| 1 | QxR | 23.25% | 1.75 |
| 1 | TAoE | 22.78% | 2.22 |
| 2 | Disney+ (H.265) | 20.32% | 4.68 |
| 3 | Amazon Prime (H.265) | 16.15% | 8.85 |
| 3 | Chivaman | 16.80% | 8.20 |
| 3 | Vyndros | 16.08% | 8.92 |
| 3 | MainFrame | 37.63% | 12.63 |
| 3 | NAN0 | 37.71% | 12.71 |
| 4 | iVy | 9.37% | 15.63 |
| 4 | PSA | 7.89% | 17.11 |

This system clearly shows how groups' effectiveness shifts based on your target ratio. For example, iVy and PSA excel at high compression (10%) with Tier 1 placement but fall to Tier 4 when targeting 25%, while groups like QxR and BRiAN show the opposite pattern, moving from Tier 3 to Tier 1. Streaming services show interesting variations too - Movies Anywhere performs better at higher bitrates (Tier 1 at 25%) while Amazon Prime maintains mid-tier performance in both scenarios.

This system clearly shows which groups consistently hit near your desired ratio. For example, QxR and TAoE excel at mid-range ratios around 25%, while groups like PSA and iVy are better choices for high-compression targets around 10%.

Streaming services tend to cluster in the middle range (15-25%), suggesting they optimize for a balance of quality and bandwidth efficiency.