const maxLength = 50;
const descriptions=document.querySelectorAll('.miniText');


window.onload = function() {
    
    descriptions.forEach((element,index) => {
        const trimmedText = element.textContent.substring(0, maxLength) + (element.textContent.length > maxLength ? '...' : '');
        document.querySelectorAll('.miniText')[index].textContent = trimmedText;
    });
    
    const menuIcon = document.querySelector('.menu-icon');
    const menuEls = document.querySelector('.menu-els');
  
  menuIcon.addEventListener('click', function() {
    // this.parentElement.classList.toggle('responsive');
    menuEls.classList.toggle('responsive');
    
  });
}
