document.getElementById('checkout').onclick = function() {
    alert('Proceeding to checkout: \n' + cart.map(item => `${item.name} x ${item.quantity} 
    `).join('\n'));

    

   
};

 
