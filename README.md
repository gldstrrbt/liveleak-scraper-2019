# LiveLeak scraper experiment (2019)

Historical, abandoned prototype for scraping LiveLeak search-result metadata.

The script searches a short list of keywords, extracts item URLs, titles/text,
dates, uploaders, comment counts, and view counts, and writes those results to CSV.
It also contains a small `youtube_dl` helper for downloading a selected LiveLeak URL.

## Context

This was an exploratory 2019 experiment around discovering high-engagement video
content for possible automated compilation/social-posting workflows. The idea was
not taken forward into a production posting or monetization system.

Some of the search terms targeted violent accidents or conflict footage because
those categories were considered high-engagement / low-friction source material at
the time. No scraped CSV exports or downloaded media are included in this archive.

## Archive notes

LiveLeak shut down in 2021, so the scraper is preserved as historical source and is
not expected to work against the original site today.

The recovered file was lightly cleaned only to fix two obvious issues:
- initialize the `youtube_dl` object inside the download helper;
- rename the second duplicated `get_time_date()` definition to `get_tags()` so it
  no longer overwrites the first function.

No attempt was made to modernize the scraping logic.