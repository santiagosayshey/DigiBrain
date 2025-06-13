This feature automatically searches for better quality versions of movies and TV shows you already have in oimproves your media library quality over time.. Think of it as a "set it and forget it" upgrade system that continuously 

## The Problem It Solves

Radarr and Sonarr already download media based on your quality preferences, but they have a limitation: they only search "forward." This means:

- If you change your quality settings today, they won't re-check movies you downloaded last month
- If you add a new indexer, they won't search it for upgrades to existing media
- If better releases become available later, they won't know unless you manually search

This feature forces Radarr and Sonarr to look again at your existing media and search for upgrades.

## How It Works

### The Basic Process

The feature works like a human clicking "search" on every movie or show, but with smart filtering and tracking:

1. **Get everything** - Fetch all movies/shows from Radarr/Sonarr
2. **Pick what needs upgrading** - Filter to items you want to search for
3. **Search for upgrades** - Tell Radarr/Sonarr to look for better versions
4. **Remember what you searched** - Tag items so you don't search them again tomorrow
5. **Repeat regularly** - Run this process on a schedule

### The Tag System

Tags are the key to making this work efficiently. Here's the lifecycle:

- Movies without an "upgraded" tag → Need to be searched
- After searching → Add "upgraded" tag
- Movies with "upgraded" tag → Skip next time
- Eventually → Remove all tags and start fresh (unattended mode)

This prevents the same movie from being searched every day while ensuring everything gets checked eventually.

## Implementation Architecture

### API Endpoints Used

The feature interacts with these endpoints:

**Information Gathering:**

- Get all movies: `GET /api/v3/movie`
- Get all series: `GET /api/v3/series`
- Get tag list: `GET /api/v3/tag`

**Command Execution:**

- Search movies: `POST /api/v3/command` with `MoviesSearch`
- Search series: `POST /api/v3/command` with `SeriesSearch`, `SeasonSearch`, or `EpisodeSearch`
- Tag items: `PUT /api/v3/movie/editor` or `/series/editor`

### Search Execution Differences

**Radarr** can search multiple movies in one command:

```json
{"name": "MoviesSearch", "movieIds": [1, 2, 3, 4, 5]}
```

**Sonarr** requires individual searches and offers three levels of granularity:

Series level (searches all seasons/episodes):

```json
{"name": "SeriesSearch", "seriesId": 1}
```

Season level (searches specific season only):

```json
{"name": "SeasonSearch", "seriesId": 1, "seasonNumber": 2}
```

Episode level (searches specific episodes):

```json
{"name": "EpisodeSearch", "episodeIds": [101, 102, 103]}
```

This difference impacts both scheduling strategy and search granularity options. While series-level searches are simpler to implement, season or episode-level searches offer more control over what gets searched.

## Scheduling and Rate Management

### The Challenge

When you trigger a search, Radarr or Sonarr contacts every configured indexer. These indexers have their own rate limits and response times. Too many searches too quickly can result in:

- Indexers blocking or throttling your requests
- Searches timing out or failing
- System resources being overwhelmed

The scheduling challenge is finding the sweet spot between searching frequently enough to find new upgrades quickly, while not overwhelming your indexers or system.

### Scheduling Considerations

**Application Differences** Since Radarr supports bulk searches but Sonarr doesn't, they have different throughput capabilities. Your scheduling strategy needs to account for this asymmetry.

**Library Size Impact** Large libraries present unique challenges. If you have thousands of items, even searching each one monthly requires significant daily throughput. The scheduler needs to balance coverage with capacity.

**Indexer Variations** Different indexers have different rate limits and response times. Your sustainable search rate is determined by your slowest or most restrictive indexer.

### Strategic Options

**Sequential vs Parallel** You can process one application at a time or interleave them. Sequential is simpler to implement and debug, while interleaving provides more even load distribution.

**Priority-Based Scheduling** Not all media needs the same search frequency. Recently added content might benefit from more frequent searches, while older content could be checked less often.

**Time-Based Distribution** Spreading searches throughout the day prevents burst loads. This is especially important if you share indexers with others or have time-based rate limits.

### Task System Integration

Your task system becomes the orchestrator, managing:

- Which application to process next
- How many items to process per run
- When to pause or resume operations
- How to handle the different search patterns between Radarr and Sonarr

The key is building a sustainable rhythm that eventually covers your entire library while respecting system and indexer constraints.

## Extending Beyond Upgrades

This same pattern works for any bulk operation:

**Rename Operations**

- Filter: Items with incorrect filenames
- Command: `RenameMovie` or `RenameSeries`
- Tag: "renamed"

**Metadata Refresh**

- Filter: Items not refreshed in 30 days
- Command: `RefreshMovie` or `RefreshSeries`
- Tag: "refreshed" with timestamp

The architecture remains the same - only the filter criteria and command change.