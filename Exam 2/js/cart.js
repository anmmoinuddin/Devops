let cart = [];

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    const cartItem = cart.find(item => item.id === productId);
    
    if (cartItem) {
        cartItem.quantity++;
    } else {
        cart.push({ ...product, quantity: 1 });
    }
    updateCartDisplay();
}

function updateCartDisplay() {
    const cartContainer = document.getElementById('cart-items');
    cartContainer.innerHTML = '';
    let totalPrice = 0;
    let discountedTotal = 0;
    let promoApplied = false;
    cart.forEach(item => {
        totalPrice += item.price * item.quantity;
        const cartItem = document.createElement('div');
        cartItem.innerHTML = `
            <h4>${item.name}</h4>
            <p>Price: $${item.price.toFixed(2)} x ${item.quantity}</p>
            <button onclick="removeFromCart(${item.id})" class="btn btn-danger">Remove</button>
            <button onclick="clearCart(${item.id})" class="btn btn-warning">clear the whole cart</button>
            <input type="number" value="${item.quantity}" min="1" onchange="updateQuantity(${item.id}, this.value)">
        `;
        cartContainer.appendChild(cartItem);
    });
document.getElementById('apply-promo').addEventListener('click', function() {
  const promoInput = document.getElementById('promo-code').value.trim().toLowerCase();
  const promoMessage = document.getElementById('promo-message');

  if (promoApplied) {
    promoMessage.textContent = "Promo code already applied.";
    return;
  }

  if (promoInput === 'ostad10') {
    // Apply 10% discount
    discountedTotal = totalPrice * 0.9;
    promoApplied = true;
    promoMessage.style.color = 'green';
    promoMessage.textContent = "Promo code applied: 10% discount!";
    updateTotalDisplay();
  } else if (promoInput === 'ostad50') {
    // Apply 50% discount
    discountedTotal = totalPrice * 0.5;
    promoApplied = true;
    promoMessage.style.color = 'green';
    promoMessage.textContent = "Promo code applied: 50% discount!";
    updateTotalDisplay();
  } else {
    // Invalid code
    promoMessage.style.color = 'red';
    promoMessage.textContent = "Invalid Promo Code.";
  }
});

    document.getElementById('total-display').innerText = `Total: $${totalPrice.toFixed(2)}`;
}

function updateQuantity(productId, quantity) {
    if (quantity < 1) return; // Prevent negative quantity
    const cartItem = cart.find(item => item.id === productId);
    if (cartItem) {
        cartItem.quantity = parseInt(quantity, 10);
    }
    updateCartDisplay();
}

function clearCart() {
    cart = [];
    updateCartDisplay();

    
}

function removeFromCart(itemId){
    cart=cart.filter(item => item.id !== itemId);
    updateCartDisplay();

}

function updateTotalDisplay() {
  // Assuming you have an element to display total, e.g.,
  const totalElement = document.getElementById('total-amount');
  totalElement.textContent = `$${discountedTotal.toFixed(2)}`;
}