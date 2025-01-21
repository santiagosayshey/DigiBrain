---
title: home
slug: home
author: santiagosayshey
created: 2025-01-21
tags: [home, wiki]
---
# Hello!

Welcome to Dictionarry! This project aims to wiki-fy and simplify media automation in Radarr / Sonarr through extensive, data driven documentation, custom formats and quality profiles.

## Motivation

Navigating the world of **niche quality terms** like "Remux", or "HEVC" or "Dolby Vision" can be quite daunting when all you want to do is setup a media server to watch some content. If often **feels like you need a masters in audio / video just to grab the latest blockbuster.** Dictionarry aims not to answer these questions, but **abstract them into more approachable ones** that don't require extensive knowledge or experience. 

## How?

Dictionarry leverages two key features of Radarr and Sonarr to simplify media automation:

1. **Custom Formats** - Think of these as smart filters that scan release titles for specific patterns. They help identify important characteristics of your media, such as:
   - Video quality (4K, HDR, Dolby Vision)
   - Audio formats (Atmos, DTS, TrueHD)
   - Source types (Remux, Web-DL, Blu-ray)
   - Potential issues (upscaled content, poor encodes)

2. **Quality Profiles** - These act like a scoring system that ranks releases based on their Custom Format matches. You can:
   - Prioritize what matters most to you
   - Automatically upgrade to better versions
   - Avoid problematic releases

Think of Dictionarry as your personal car-buying expert: Instead of researching every technical specification and test-driving dozens of vehicles, you get access to a curated showroom of pre-vetted options that match what you're looking for. Whether you want "maximum quality 4K HDR remuxes with Atmos," "efficient x265 encodes that save space," "transparent 1080p releases," or anything in between, Dictionarry's database of tested profiles and formats handles the technical decisions for you.
## Tooling

The database by itself, does nothing. Custom Formats and Quality Profiles need to be imported and configured in your individual arr installations. Rather than leaving you to manually implement everything, we've created `Profilarr` to automate this process.

### Profilarr

Profilarr is a configuration management tool for Radarr and Sonarr that can interface with ANY remote configuration database (not just Dictionarry's!). It automatically:

- Pulls new updates from your chosen configuration database
- Imports them to your arr installation
- Manages version control of your configurations

Built on top of git, Profilarr treats your configurations like code, allowing you to:

- Track changes over time
- Maintain your own customizations while still receiving database updates
- Resolve conflicts when they arise

The architecture was specifically built like this to put user choice first. We believe that:

- Your media setup should reflect your needs, not our opinions
- Updates should enhance your configuration, not override it
- Different users have different requirements (storage constraints, hardware capabilities, quality preferences)
- The ability to customize should never be sacrificed for convenience

Profilarr empowers you to use Dictionarr's database as a foundation while maintaining the freedom to adapt it to your specific needs.no 