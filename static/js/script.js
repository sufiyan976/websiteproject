
function searchproducts(){
  const searchInput = document.querySelector('#search');
  const searchButton = document.querySelector('#button');
  const productList = document.querySelector('#productList');

  searchButton.addEventListener('click', function() {
    const searchTerm = searchInput.value.toLowerCase();
    const products = productList.querySelectorAll('.product');

  // Hide all products
   products.forEach(function(product) {
     product.style.display = 'none';
   });

  // Show matching products
    products.forEach(function(product) {
      if (product.textContent.toLowerCase().indexOf(searchTerm) !== -1) {
        product.style.display = 'block';
      }
    });
  });
}


function searchproducts1(){
  const searchInput = document.querySelector('#search1');
  const searchButton = document.querySelector('#button1');
  const productList = document.querySelector('#productList');

  searchButton.addEventListener('click', function() {
    const searchTerm = searchInput.value.toLowerCase();
    const products = productList.querySelectorAll('.product');

  // Hide all products
   products.forEach(function(product) {
     product.style.display = 'none';
   });

  // Show matching products
    products.forEach(function(product) {
      if (product.textContent.toLowerCase().indexOf(searchTerm) !== -1) {
        product.style.display = 'block';
      }
    });
  });
}