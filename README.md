<h1 align="center">
  Spotify Playlist Recommendation Application
</h1>
<p align="center">Create playlists while being recommended songs that you will love!</p>

<p align="center">
  <a href="https://github.com/memgraph/spotify-song-recommender/LICENSE">
    <img src="https://img.shields.io/github/license/memgraph/spotify-song-recommender" alt="license" title="license"/>
  </a>
  <a href="https://github.com/memgraph/spotify-song-recommender/stargazers">
    <img src="https://img.shields.io/badge/maintainer-jbajic-yellow" alt="maintainer" title="maintainer"/>
  </a>
  <a href="https://github.com/memgraph/spotify-song-recommender/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="build" title="build"/>
  </a>
  <a href="#contributors-">
    <img src="https://img.shields.io/badge/all_contributors-3-green.svg?style=flat" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/memgraph/spotify-song-recommender">
    <img src="https://public-assets.memgraph.com/spotify-song-recommender/spotify-app-01.png" alt="demo" title="demo" style="width: 80%"/>
  </a>
</p>

<p align="center">
    <a href="https://twitter.com/intent/follow?screen_name=memgraphdb"><img
    src="https://img.shields.io/twitter/follow/memgraphdb.svg?label=Follow%20@memgraphdb"
    alt="Follow @memgraphdb" /></a>
</p>

## :clipboard: Description

The world of music is constantly growing. Year by year, it is harder to keep up
with trends and new songs that keep popping up. Luckily, there are enough people
listening to music that finding new songs in playlists from people with similar
tastes might not be so difficult after all. This project aims to serve as a
recommendation engine for people searching for new songs they will enjoy based
on the songs they currently listen to.

## :books: Dataset

The [Spotify playlist
dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)
contains 5 million song playlists from different users. Each playlist contains a
list of music tracks. The data model sample is given below:

<details>
  <summary align="center" style="color:gray;font-weight:900;align-items:center;display:flex">show dataset sample</summary>
  <p>
  <pre>
{
    "name": "musical",
    "collaborative": "false",
    "pid": 5,
    "modified_at": 1493424000,
    "num_albums": 7,
    "num_tracks": 12,
    "num_followers": 1,
    "num_edits": 2,
    "duration_ms": 2657366,
    "num_artists": 6,
    "tracks": [
        {
            "pos": 0,
            "artist_name": "Degiheugi",
            "track_uri": "spotify:track:7vqa3sDmtEaVJ2gcvxtRID",
            "artist_uri": "spotify:artist:3V2paBXEoZIAhfZRJmo2jL",
            "track_name": "Finalement",
            "album_uri": "spotify:album:2KrRMJ9z7Xjoz1Az4O6UML",
            "duration_ms": 166264,
            "album_name": "Dancing Chords and Fireflies"
        },
        // 10 tracks omitted
        {
            "pos": 11,
            "artist_name": "Mo' Horizons",
            "track_uri": "spotify:track:7iwx00eBzeSSSy6xfESyWN",
            "artist_uri": "spotify:artist:3tuX54dqgS8LsGUvNzgrpP",
            "track_name": "Fever 99\u00b0",
            "album_uri": "spotify:album:2Fg1t2tyOSGWkVYHlFfXVf",
            "duration_ms": 364320,
            "album_name": "Come Touch The Sun"
        }
    ],
}
  </pre>
  </p>
</details>

## :zap: Features

- Generate song recommendations -
  [similar_tracks.py](https://github.com/memgraph/spotify-song-recommender/blob/main/memgraph/query_modules/similar_tracks.py)
- Find a similar playlist -
  [similar_playlists.py](https://github.com/memgraph/spotify-song-recommender/blob/main/memgraph/query_modules/similar_playlists.py)
- Discover trendy songs -
  [trendy_tracks.py](https://github.com/memgraph/spotify-song-recommender/blob/main/memgraph/query_modules/trendy_tracks.py)

## :shipit: Installation

1. Download and install [ocker](https://www.docker.com/get-started)
2. Clone this repository, or download the files with GitHub.
3. Download the complete [Spotify
   dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge#dataset)
   and place the `.json` files in the directory `/producer/data` (the first
   file is already there, you can just replace it).

## :question: Usage

1. Run these commands in your favorite terminal/cmd:

```
docker-compose build
docker-compose up
```

2. Open the app on the address [localhost:80](localhost:80).

## Contributors ✨

Thanks goes to these wonderful people ([emoji
key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/jbajic"><img src="https://avatars.githubusercontent.com/u/11527103?v=4" width="100px;" alt=""/><br /><sub><b>Jure Bajic</b></sub></a></td>
    <td align="center"><a href="https://github.com/MasterMedo"><img src="https://avatars.githubusercontent.com/u/16375100?v=4" width="100px;" alt=""/><br /><sub><b>Mislav Vuletic
</b></sub></a></td> 
    <td align="center"><a href="https://github.com/dtomicevic"><img src="https://avatars.githubusercontent.com/u/3899768?v=4" width="100px;" alt=""/><br /><sub><b>Dominik Tomicevic</b></sub></a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the
[all-contributors](https://github.com/all-contributors/all-contributors)
specification. Contributions of any kind welcome!

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/⬆️back_to_top_⬆️-white" alt="Back to top" title="Back to top"/>
  </a>
</p>
