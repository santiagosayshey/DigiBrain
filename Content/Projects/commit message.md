refactor(everything): various improvements from seraphys' working branch

- create(profile): 720p Quality
- create(format): 720p Quality tiers based on 720p GPPi data
- create(format): Unwanted groups for WEBRip, remux and general
- create(format): HDR formats for HLG, PQ
- create(format): Streaming services (Hotstar, IQIYI, Kocowa, Now, Showtime, TVING, VIKI, VIU, WAVVE, WeTV)
- create(format): Remux tiers
- create(format): WEBDL tiers
- create(format): Season Pack
- create(format): VP9 codec
- create(regex): Various release groups, notably Remux and WEBDL 

- tweak(format): Change from web-dl negation to bluray requirement inside group tiers
- tweak(format): Manual group ranking tweaks for 2160p quality
- tweak(format): Improved sorting. Tags / conditions are now alphabetical
- tweak(format): Add source negations to full disc to stop it from matching remuxes and web stuff
- tweak(format): Add streaming service rename conditions
- tweak(format): Revised x265/h265 usage to negate unwanted stuff rather than uprank wanted stuff

- remove(format): BeyondHD. Added to unwanted groups
- remove(format): Scene. Scoring now treats scene encodes as unknown and defaults to indexer priority. 

