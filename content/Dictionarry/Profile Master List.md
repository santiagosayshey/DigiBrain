
| Profile          | Quality | Efficiency | Compatability | Description |
| ---------------- | ------- | ---------- | ------------- | ----------- |
| 2160p Remux      | 5       | 1          |               |             |
| 2160p Encode     | 5       | 2          |               |             |
| 1080p HDR Encode | 4       | 2          |               |             |
| 2160p WEB        | 4       |            |               |             |
| 1080p Encode     | 3       | 2          |               |             |
| 1080p Remux      | 3       | 1          |               |             |
| 1080p WEB        | 2       |            |               |             |
| 1080p HEVC       | 2       |            |               |             |
| 720p Encode      | 2       |            |               |             |
| SD Encode        | 1       |            |               |             |
| Minimal          | 1       |            |               |             |
| Compatible       | 1       |            |               |             |
- Profile Names changed to the 'priority'. This removes ambiguity with things like Optimal and Transparent, where in reality, transparent encodes are usually better than the remux.
- Minimal and compatible don't directly reference a resolution, as they are targeting specific A/V metrics
- 1080p HEVC doesn't prioritise a source, since it can grab an encode or WEB interchangeably. 



|     | Quality | Efficiency                                        | Compatability |
| --- | ------- | ------------------------------------------------- | ------------- |
| 1   |         | The biggest possible release at the given quality |               |
| 2   |         |                                                   |               |
| 3   |         |                                                   |               |
| 4   |         |                                                   |               |
| 5   |         |                                                   |               |
