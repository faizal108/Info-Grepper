const heartIcon = document.querySelector('#fav-btn i');
heartIcon.addEventListener('mouseover', function() {
    heartIcon.classList.remove('bx-heart');
    heartIcon.classList.add('bxs-heart');
});

heartIcon.addEventListener('mouseout', function() {
    heartIcon.classList.remove('bxs-heart');
    heartIcon.classList.add('bx-heart');
});