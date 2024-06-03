
| Profile          | Quality | Efficiency | Compatability | Notes                                                                                 |
| ---------------- | ------- | ---------- | ------------- | ------------------------------------------------------------------------------------- |
| 2160p Remux      | 5       | 1          | 1             |                                                                                       |
| 2160p Encode     | 4       | 2          | 2             | Quality score 4 because not consistent enough, but is more than capable of being a 5. |
| 2160p WEB        | 4       | 3          | 2             |                                                                                       |
| 1080p HDR Encode | 4       | 4          | 3             |                                                                                       |
| 1080p Encode     | 3       | 2          | 5             |                                                                                       |
| 1080p Remux      | 3       | 1          | 2             | Compatibility score of 2 because of lossless audio                                    |
| 1080p WEB        | 2       | 3          | 5             |                                                                                       |
| 1080p HEVC       | 2       | 5          | 4             |                                                                                       |
| 720p Encode      | 2       | 3          | 5             |                                                                                       |
| SD Encode        | 1       | 3          | 5             |                                                                                       |
| Minimal          | 1       | 4          | 4             |                                                                                       |
| Compatible       | 1       | 1          | 5             |                                                                                       |
- Profile Names changed to the 'priority'. This removes ambiguity with things like Optimal and Transparent, where in reality, transparent encodes are usually better than the remux.
- Minimal and compatible don't directly reference a resolution, as they are targeting specific A/V metrics
- 1080p HEVC doesn't prioritise a source, since it can grab an encode or WEB interchangeably. 

|     | Quality                                                   | Efficiency                                                  | Compatibility                                               |
| --- | --------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| 1   | Lowest acceptable quality. SD resolution, stereo audio.   | Lowest efficiency. Large file sizes, high bandwidth usage.  | Highest compatibility. Works on most devices and platforms. |
| 2   | Moderate quality. 720p to 1080p, basic 5.1 surround audio.| Low efficiency. Larger file sizes, moderate bandwidth usage.| High compatibility. Works on many devices and platforms.    |
| 3   | Good quality. 1080p, HD audio formats.                    | Moderate efficiency. Medium file sizes, manageable bandwidth.| Moderate compatibility. May have limitations on some devices.|
| 4   | Excellent quality. 4K resolution, immersive audio formats. | High efficiency. Smaller file sizes, optimized bandwidth usage.| Limited compatibility. Requires modern hardware and software.|
| 5   | Best possible quality. Lossless / spatial audio. HDR. 4k. | Highest efficiency. Smallest file sizes, minimal bandwidth usage.| Lowest compatibility. Requires specialized hardware and software.|

