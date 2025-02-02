Hey everyone, medium-ish update today.

## Website 2.0

I've wanted to transition away from the old site / mkdocs for a while now as its quite hard to maintain and keep everything up to date, so I built a new site using Next that uses ISR to rebuild its content based on the database whenever it becomes stale. Basically this just means:
- Database gets an update -> website sees its data is stale -> it rebuilds itself with new data
- 