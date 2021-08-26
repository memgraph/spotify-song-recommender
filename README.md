<h1 align="center">
  Spotify Playlist recommendation application
</h1>
<p align="center">Create playlists while being recommended songs that you will love!</p>

<p align="center">
  <a href="https://github.com/memgraph/boolean-pundits/LICENSE">
    <img src="https://img.shields.io/github/license/memgraph/boolean-pundits" alt="license" title="license"/>
  </a>
  <a href="https://github.com/memgraph/boolean-pundits">
    <img src="https://img.shields.io/github/languages/code-size/memgraph/boolean-pundits" alt="build" title="build"/>
  </a>
  <a href="https://github.com/memgraph/boolean-pundits/stargazers">
    <img src="https://img.shields.io/badge/maintainer-jbajic-yellow" alt="maintainer" title="maintainer"/>
  </a>
</p>

<p align="center">
  <a href="https://github.com/memgraph/boolean-pundits">
    <img src="" alt="demo" title="demo"/>
  </a>
</p>

## :clipboard: description
The world of music is constantly growing. Year by year, it is harder to keep up with trends and new songs that keep popping up. Luckily, there are enough people listening to music that finding new songs in playlists from people with similar taste might not be so difficult after all. This project aims to serve as a recommendation engine for people searching for new songs they will enjoy based on the songs they currently listen to.

## :books: dataset
The Spotify playlist dataset contains 5 million song playlists from different users. Each playlist contains a list of music tracks. The data model sample is given below:
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

## :zap: features

## :shipit: installation
1. Download and install [docker](https://www.docker.com/get-started)
2. Clone this repository, or download the files with GitHub

## :question: usage
2. Run a simple command in your favourite terminal/cmd:
```
docker-compose up
```

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/⬆️back_to_top_⬆️-white" alt="Back to top" title="Back to top"/>
  </a>
</p>
