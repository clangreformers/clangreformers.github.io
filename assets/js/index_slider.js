
document.addEventListener('DOMContentLoaded', function () {
    var bannerCarousel = document.getElementById('bannerCarousel');

    if (bannerCarousel) {
        bannerCarousel.addEventListener('slide.bs.carousel', function (e) {
            // e.to is the index of the slide being transitioned to
            var targetIndex = e.to;

            // Get content tabs
            var contentShugu = document.getElementById('content-shugu');
            var contentShuowen = document.getElementById('content-shuowen');

            if (targetIndex === 0) {
                // Show Shugu, Hide Shuowen
                contentShugu.style.display = 'block';
                contentShuowen.style.display = 'none';
            } else if (targetIndex === 1) {
                // Show Shuowen, Hide Shugu
                contentShugu.style.display = 'none';
                contentShuowen.style.display = 'block';
            }
        });
    }
});
