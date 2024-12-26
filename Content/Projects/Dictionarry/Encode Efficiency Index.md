# Understanding Encoding Efficiency Thresholds

This metric helps identify and rank release groups based on their ability to produce encodes that meet specific efficiency standards.

## What is an Efficiency Threshold?

In its simplest form, it's the size of an encode compared to its likely source (typically a 1080p remux). For example, if MovieA.encode is 10GB and MovieA.remux is 40GB, then MovieA.encode's efficiency threshold is 25% (10GB/40GB × 100).

## Why Is This Important?

... somehow get to why w

## Why Set a Maximum Threshold of 40%?

The 40% ceiling is based on where HEVC's efficiency advantages are most pronounced. Below this threshold:

- HEVC achieves its largest bitrate savings (20-40% vs AVC) in the mid-bitrate region (~2-10 Mbps for 1080p)
- This is where HEVC's advanced features (block partitioning, motion estimation, and quantization) provide the biggest advantage
- Beyond this region, both codecs begin to saturate at near-transparent quality, making larger files unnecessary
- At these optimal bitrates, HEVC consistently delivers VMAF scores of 90+ while staying well under 40% of source size

## Key Terms

**VMAF**: Netflix's video quality metric that outputs scores from 0-100, using machine learning to match human perception.

**BD-Rate**: Measures average bitrate difference between two encodings across quality levels. A BD-Rate of -30% means one codec achieves the same quality at 30% lower bitrate.

The 40% threshold represents a practical maximum that ensures quality while taking advantage of modern codec efficiency. BD-Rate analysis across VMAF scores of 80-95 helps verify that encodes maintain competitive quality within this limit.


https://medium.com/innovation-labs-blog/bjontegaard-delta-rate-metric-c8c82c1bc42c

https://www.mdpi.com/2079-9292/13/5/953
