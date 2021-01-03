//hello
const app = new Vue({
    el: "#app",
    data: function() {
      return {};
    },
    methods: {
      search: function(e) {
        if(e.target.value.length) {
          axios.get(`/search/${e.target.value}/`)
          .then(res => {
            console.log(res.data);
          })
          .catch(err => {
            console.log(err);
          })
        }
      }
    }
});
