import mgp
import sys

from collections import OrderedDict
from typing import Dict, List


def grade_playlist(relevant_playlist: mgp.Vertex, relevant_tracks: List[int]) -> int:
    relevant_playlist_tracks = [
        out_edge.to_vertex.id for out_edge in relevant_playlist.out_edges
    ]
    return len(list(set(relevant_playlist_tracks).intersection(relevant_tracks)))


def grade_track(relevant_track: mgp.Vertex, graded_playlists: Dict[int, int]) -> int:
    return sum(
        graded_playlists.get(in_edge.from_vertex.id, 0)
        for in_edge in relevant_track.in_edges
    )


@mgp.read_proc
def get(
    context: mgp.ProcCtx,
    tracks: mgp.List[mgp.Vertex],
    relevant_playlists: List[mgp.Vertex],
    relevant_tracks: List[mgp.Vertex],
    number_of_tracks: int = 10,
) -> mgp.Record(result=mgp.Vertex, score=int):
    """Returns a list of track_ids that are similar to the tracks in the given
        playlist.
        Calculates similar tracks by calculating the proximity of each track to the
        given playlist.m
    MATCH (n: Playlist {pid: 10466})-[]->(m: Track),
    (relevant_playlists: Playlist)-[]->(m: Track),
    (relevant_playlists)-[]->(relevant_tracks: Track)
    WHERE relevant_tracks.track_uri != m.track_uri
    WITH COLLECT(m) as tracks, COLLECT(relevant_playlists) as relevant_playlists, COLLECT(relevant_tracks) as relevant_tracks
    CALL similar_tracks.get(tracks, relevant_playlists, relevant_tracks) YIELD result, score RETURN result, score;
    """
    track_ids = [track.id for track in tracks]

    # 1. Grade playlists according to how many relevant_tracks they have
    graded_playlists = dict()
    for relevant_playlist in relevant_playlists:
        graded_playlists[relevant_playlist.id] = grade_playlist(
            relevant_playlist, track_ids
        )

    # 2. Grade all tracks according to in how similar playlist they are
    recommended_tracks = dict()
    for relevant_track in relevant_tracks:
        recommended_tracks[
            grade_track(relevant_track, graded_playlists)
        ] = relevant_track
    sorted_recommended_tracks = OrderedDict(
        sorted(recommended_tracks.items(), reverse=True)
    )

    scored_recommended_tracks = []
    recommended_track_counter = 0
    for score, recommended_track in sorted_recommended_tracks.items():
        scored_recommended_tracks.append(
            mgp.Record(result=recommended_track, score=score)
        )
        recommended_track_counter += 1
        if recommended_track_counter >= number_of_tracks:
            break
    return scored_recommended_tracks
