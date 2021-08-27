import Vue from "vue";
import Vuex from "vuex";
import SongService from "@/services/SongService";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    playlist_id: null,
    playlist_name: null,
    tracks: [],
  },
  mutations: {
    SET_PLAYLIST(state, id, name) {
      state.id = id;
      state.name = name;
    },
  },
  actions: {
    createPlaylist(context) {
      SongService.postCreatePlaylist("default").then((res) => {
        context.commit("SET_PLAYLIST", res.data.playlist_id, "default");
      });
    },
  },
});
