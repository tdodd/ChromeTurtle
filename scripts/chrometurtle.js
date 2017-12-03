(function() {

   var videos = document.querySelectorAll('li');

   for (var video of videos) {
      video.addEventListener('click', function (event) {

         var movieSrc = event.target.dataset.movieSrc;
         var source = document.querySelector('#video-src');
         var video = document.querySelector('#player');
         source.setAttribute('src', movieSrc);
         player.play();

      });
   }

})();