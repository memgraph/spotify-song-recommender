<template>
  <v-card class="mx-auto">
    <v-toolbar color="primary" dark>
      <v-toolbar-title>{{ $store.state.playlist_name }}</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-playlist-edit</v-icon>
      </v-btn>
    </v-toolbar>

    <v-list two-line>
      <v-list-item-group v-model="selected" active-class="pink--text" multiple>
        <template v-for="(item, index) in items">
          <v-list-item :key="item.track_name">
            <template v-slot:default="{ active }">
              <v-list-item-content>
                <v-list-item-title v-text="item.track_name"></v-list-item-title>

                <v-list-item-subtitle
                  v-text="item.artist_name"
                ></v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-action>
                <v-list-item-action-text
                  v-text="item.action"
                ></v-list-item-action-text>

                <v-icon v-if="!active" color="grey lighten-1">
                  mdi-star-outline
                </v-icon>

                <v-icon v-else color="yellow darken-3"> mdi-star </v-icon>
              </v-list-item-action>
            </template>
          </v-list-item>

          <v-divider v-if="index < items.length - 1" :key="index"></v-divider>
        </template>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>
export default {
  name: "TrackBuilder",

  created() {},

  data: () => ({
    playlist: {
      playlist_id: 1,
      playlist_name: "My Playlist",
    },
    selected: [1, 2],
    items: [
      {
        action: "3:45",
        artist_name: "Rauw Alejandro",
        track_name: "Todo De Ti",
      },
      {
        action: "7:22",
        artist_name: "Kiss Me More (feat. SZA)",
        track_name: "Doja Cat",
      },
      {
        action: "4:15",
        artist_name: "Doja Cat",
        track_name: "Woman",
      },
      {
        action: "1:22",
        artist_name: "Farruko",
        track_name: "Pepas",
      },
      {
        action: "1:18",
        artist_name: "Billie Eilish",
        track_name: "Happier Than Ever",
      },
    ],
  }),
};
</script>
