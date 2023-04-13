function updateCardLayout() {
    const cardContainer = document.getElementById('card-container');
    const screenWidth = window.innerWidth;
  
    // Elimina todas las tarjetas existentes
    while (cardContainer.firstChild) {
      cardContainer.removeChild(cardContainer.firstChild);
    }
  
    // Agrega nuevas tarjetas en función del tamaño de la pantalla
    if (screenWidth > 1200) {
      // Pantalla grande, agrega 5 tarjetas
      for (let i = 1; i <= 5; i++) {
        const card = createCard(i);
        cardContainer.appendChild(card);
      }
    } else {
      // Pantalla pequeña, agrega 3 tarjetas
      for (let i = 1; i <= 3; i++) {
        const card = createCard(i);
        cardContainer.appendChild(card);
      }
    }
  }
  
  function createCard(id) {
    // Crea una nueva tarjeta con el id dado
    const card = document.createElement('div');
    card.classList.add('card', 'me-md-2');
    card.style.width = '33vw';
  
    const img = document.createElement('img');
    img.src = `img/${id}.png`;
    img.classList.add('card-img-top');
    card.appendChild(img);
  
    const body = document.createElement('div');
    body.classList.add('card-body', 'no-padding');
  
    const text = document.createElement('p');
    text.classList.add('card-text');
    text.textContent = 'Some quick example';
    body.appendChild(text);
  
    card.appendChild(body);
  
    return card;
  }
  
  // Actualiza el diseño de la tarjeta cuando se carga la página y cuando se cambia el tamaño de la ventana
  window.addEventListener('load', updateCardLayout);
  window.addEventListener('resize', updateCardLayout);
  
  