This metric is aimed at identifying and ranking release groups based on their propensity to release an encode that meets a certain efficiency threshold.

## What is an Efficiency Threshold?

In it's simplest definition, it's just how big an encode is, compared to it's most likely source; typically a 1080p remux. For instance, if MovieA.encode is 10gb, and MovieA.remux is 40gb, then MovieA.encode's efficiency threshold is 25% (40/10 \*100)

## Key Metrics and Definitions

Before diving into efficiency thresholds, let's define some key terms:

**VMAF (Video Multimethod Assessment Fusion)**: A perceptual video quality metric developed by Netflix that combines multiple quality metrics to predict subjective video quality. It uses machine learning to match human perception of video quality, outputting scores from 0 to 100.

**BD-Rate (Bjøntegaard Delta Rate)**: A standardized method for comparing video codec efficiency. It measures the average bitrate difference between two encodings across a range of quality levels. For example, a BD-Rate of -30% means one codec achieves the same quality at 30% lower bitrate on average.

## Efficiency Thresholds Explained

An efficiency threshold represents the size ratio between an encoded video and its source material, typically expressed as a percentage. For example:
- Original remux size: 40GB
- Encoded size: 10GB
- Efficiency threshold: 25% (10GB/40GB × 100)

### Why Set a Maximum Threshold of 40%?

The 40% maximum threshold is established based on several key factors discovered through codec analysis:

1. **Sweet Spot for Quality-Size Balance**: 
   - At moderate bitrates (2-10 Mbps for 1080p), modern codecs like HEVC (H.265) achieve their optimal efficiency
   - This range typically results in file sizes well under 40% of the source while maintaining high perceptual quality (VMAF scores of 90+)

2. **Diminishing Returns**:
   - Based on the provided analysis, going above 40% of the source size rarely provides meaningful quality improvements
   - At higher bitrates (>10 Mbps for 1080p), both H.264 and H.265 approach transparent quality, making larger files unnecessary

3. **Codec Efficiency Data**:
   - HEVC typically achieves 20-40% bitrate savings compared to AVC (H.264) at the same quality level
   - This means if an H.264 encode is already efficient at 40% of source size, an HEVC encode could theoretically achieve the same quality at 24-32% of source size

4. **Practical Quality Considerations**:
   - VMAF scores in the 90+ range (considered excellent quality) are consistently achievable at bitrates that result in files below 40% of source size
   - The largest quality improvements occur in the moderate bitrate range, which naturally produces files well under the 40% threshold

## Using BD-Rate for Quality Assessment

BD-Rate analysis provides a more comprehensive view of encoding efficiency across different quality levels. When evaluating release groups or encoding settings:

1. **Quality Range Analysis**:
   - Calculate BD-Rate across a meaningful quality range (typically VMAF 80-95)
   - This captures performance across various scenes and complexity levels

2. **Efficiency Verification**:
   - Use BD-Rate to verify that encodes meeting the 40% threshold maintain competitive quality
   - Compare against reference encodes to ensure quality isn't sacrificed for size

3. **Optimization Opportunities**:
   - BD-Rate analysis can identify where encoders might be using more bits than necessary
   - Helps tune encoder settings to maintain quality while staying under the threshold

## Practical Implementation

When implementing these thresholds:

1. **Source Analysis**:
   - Consider the source material's characteristics (film grain, motion, complexity)
   - Adjust expectations based on content type while maintaining the 40% ceiling

2. **Quality Verification**:
   - Use VMAF scoring to verify that encodes meeting the threshold maintain acceptable quality
   - Target VMAF scores of 90+ for main content
   - Allow some flexibility for challenging content while maintaining the threshold

3. **Encoder Optimization**:
   - Use BD-Rate analysis to optimize encoder settings
   - Focus on the moderate bitrate range where efficiency gains are highest
   - Consider using HEVC for maximum efficiency within the threshold

The 40% threshold thus represents a carefully balanced maximum that:
- Ensures efficient use of storage/bandwidth
- Maintains high perceptual quality
- Takes advantage of modern codec efficiency
- Allows for consistent quality across different content types
- Provides room for encoder optimization within reasonable limits



https://medium.com/innovation-labs-blog/bjontegaard-delta-rate-metric-c8c82c1bc42c

https://www.mdpi.com/2079-9292/13/5/953
