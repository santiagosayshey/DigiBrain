
| Profile          | Quality | Efficiency | Compatability | Notes                                                                                 |
| ---------------- | ------- | ---------- | ------------- | ------------------------------------------------------------------------------------- |
| 2160p Remux      | 5       | 1          | 1             |                                                                                       |
| 2160p Encode     | 4       | 2          | 2             | Quality score 4 because not consistent enough, but is more than capable of being a 5. |
| 2160p WEB        | 4       | 3          | 2             |                                                                                       |
| 1080p HDR Encode | 4       | 4          | 3             |                                                                                       |
| 1080p Encode     | 3       | 2          | 4             |                                                                                       |
| 1080p Remux      | 3       | 1          | 2             | Compatibility score of 2 because of lossless audio                                    |
| 1080p WEB        | 2       | 3          | 5             |                                                                                       |
| 1080p HEVC       | 2       | 5          | 3             |                                                                                       |
| 720p Encode      | 2       | 3          | 5             |                                                                                       |
| SD Encode        | 1       | 3          | 5             |                                                                                       |
| Minimal          | 1       | 4          | 3             |                                                                                       |
| Compatible       | 1       | 1          | 5             |                                                                                       |
- Profile Names changed to the 'priority'. This removes ambiguity with things like Optimal and Transparent, where in reality, transparent encodes are usually better than the remux.
- Minimal and compatible don't directly reference a resolution, as they are targeting specific A/V metrics
- 1080p HEVC doesn't prioritise a source, since it can grab an encode or WEB interchangeably. 


|             | Quality                                                                                                          | Efficiency                                                                                                                                  | Compatibility                                                                                                                                                                                                   |
| ----------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description | The level of detail, clarity, and overall fidelity of the audio or video. Higher levels indicate better quality. | The effectiveness in terms of resource usage, such as file size, bandwidth, and processing power. Higher levels indicate better efficiency. | The ability to work across different devices, platforms, and formats. Higher levels indicate better compatibility.<br><br>Measured by determining if releases have: HDR, Lossless audio, HEVC or 4k resolution. |

|     | Quality | Efficiency | Compatibility                                                                                                                                                                                                                        |
| --- | ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   |         |            | Requires a top-of-the-line setup. Includes all types of HDR, lossless audio, video codecs, and resolutions. No single device can directly play every possible combination of these A/V metrics. You will run into issues eventually. |
| 2   |         |            | Includes 3 of the 4 compatibility metrics at most. An Nvidia Shield Pro *should* be able to handle everything here. 1080p Remuxes are included here as they often have TrueHD + Atmos / DTS-X.                                       |
| 3   |         |            | Includes 1 of the 4 metrics.                                                                                                                                                                                                         |
| 4   |         |            |                                                                                                                                                                                                                                      |
| 5   |         |            |                                                                                                                                                                                                                                      |

