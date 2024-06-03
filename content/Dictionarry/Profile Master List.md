
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


|             | Quality                                                                                                          | Efficiency                                                                                                                                  | Compatibility                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Description | The level of detail, clarity, and overall fidelity of the audio or video. Higher levels indicate better quality. | The effectiveness in terms of resource usage, such as file size, bandwidth, and processing power. Higher levels indicate better efficiency. | The ability to work across different devices, platforms, and formats. Higher levels indicate better compatibility. |

|     | Quality | Efficiency | Compatibility                                                                                                            |
| --- | ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------ |
| 1   |         |            | Requires top of the line setup. All types of HDR, lossless audio, codecs and resolutions are allowed. Recommended to use |
| 2   |         |            |                                                                                                                          |
| 3   |         |            |                                                                                                                          |
| 4   |         |            |                                                                                                                          |
| 5   |         |            |                                                                                                                          |

