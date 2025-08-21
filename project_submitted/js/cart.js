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
    