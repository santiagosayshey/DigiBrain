
| #   | Profile           | Quality  | Compatibility | Immutability |
| --- | ----------------- | -------- | ------------- | ------------ |
|     | 2160p Remux       | Optimal  | Limited       | Flexible     |
|     | 2160p x265 Encode | High     | Limited       | Flexible     |
|     | 1080p HDR Encode  | High     | Adaptable     | Flexible     |
|     | 2160p h265 WEB    | Moderate |               | Flexible     |
|     | 1080p Remux       | Moderate |               | Fixed        |
|     | 1080p x264 Encode | Moderate |               | Flexible     |
|     | 1080p h265 WEB    | Balanced |               | Fixed        |
|     | 1080p h264 WEB    | Balanced |               | Flexible     |
|     | 720p x264 Encode  | Balanced |               | Fixed        |
|     | 1080p x265 Encode | Minimal  |               | Fixed        |
|     | SD x264 Encodes   | Minimal  |               | Fixed        |
|     | SD Xvid Encodes   | Minimal  |               | Fixed        |



> [!idea]+ Compatibility Levels
> - **Limited:** 3 or more of lossless audio, HDR, huge size or h265
> - **Adaptable:** 2 of lossless audio, HDR, high bitrate or h265
> - **Universal:**  1 of lossless audio, HDR, high bitrate or h265
> 


| #   | Desired Quality   | Quality | Compatibility |     | Name |
| --- | ----------------- | ------- | ------------- | --- | ---- |
| 1   | 2160p Remux       | Optimal | Limited       |     |      |
| 2   | 2160p x265 Encode | Optimal | Adaptable     |     |      |
| 3   | 1080p HDR Encode  | Optimal | Universal     |     |      |
| 4   | 2160p h265 WEB    | High    | Limited       |     |      |
| 5   | 1080p Remux       | High    | Adaptable     |     |      |
| 6   | 1080p x264 Encode | High    | Universal     |     |      |
| 7   | 1080p h265 WEB    | Medium  | Limited       |     |      |
| 8   | 1080p h264 WEB    | Medium  | Adaptable     |     |      |
| 9   | 720p x264 Encode  | Medium  | Universal     |     |      |
| 10  | 1080p x265 Encode | Minimal | Limited       |     |      |
| 11  | SD x264 Encodes   | Minimal | Adaptable     |     |      |
| 12  | SD Xvid Encodes   | Minimal | Universal     |     |      |

