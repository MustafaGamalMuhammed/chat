//hello
const app = new Vue({
    el: "#app",
    data: function() {
      return {
        searchResults: [],
      };
    },
    methods: {
      search: function(e) {
        if(e.target.value.length) {
          axios.get(`/search/${e.target.value}/`)
          .then(res => {
            this.searchResults = res.data;
          })
          .catch(err => {
            console.log(err);
          })
        }
      },
      createFriendshipRequest: function(id) {
        axios.post('/create_friendship_request/', data={id:id})
        .then(res => {
          console.log(res);
        })
        .catch(err => {
          console.log(err);
        })
      },
      acceptFriendshipRequest: function(id) {
        axios.post('/accept_friendship_request/', data={id:id})
        .then(res => {
          console.log(res);
        })
        .catch(err => {
          console.log(err);
        })
      }
    },
    mounted: function() {
      axios.defaults.headers['X-CSRFToken'] = Cookies.get('csrftoken');
    }
});
