const popupContainer = document.querySelector('.popup-container');
const closeBtn = document.querySelector('.close-btn');
const loginLink = document.querySelector('.login_btn');

// Open the popup when the login link is clicked
loginLink.addEventListener('click', function(e) {
  e.preventDefault();
  popupContainer.style.display = 'flex';
});

// Close the popup when the close button is clicked
closeBtn.addEventListener('click', function() {
  popupContainer.style.display = 'none';
});

// Close the popup when the user clicks outside the box
window.addEventListener('click', function(e) {
  if (e.target == popupContainer) {
    popupContainer.style.display = 'none';
  }
});
