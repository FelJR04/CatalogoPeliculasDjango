// Menú para pantallas pequeñas
const botonMenu = document.querySelector('.menu-toggle');
const menu = document.querySelector('#menu');
if (botonMenu && menu) {
  botonMenu.addEventListener('click', () => {
    const abierto = menu.classList.toggle('abierto');
    botonMenu.setAttribute('aria-expanded', String(abierto));
  });
}

// Búsqueda de títulos y colecciones
const buscar = document.querySelector('#buscar');
if (buscar) {
  buscar.addEventListener('input', () => {
    const texto = buscar.value.trim().toLocaleLowerCase();
    const tarjetas = [...document.querySelectorAll('.buscable')];
    let visibles = 0;
    tarjetas.forEach(tarjeta => {
      const coincide = (tarjeta.dataset.titulo || '').includes(texto);
      tarjeta.hidden = !coincide;
      if (coincide) visibles++;
    });
    const aviso = document.querySelector('#sin-resultados');
    if (aviso) aviso.hidden = visibles > 0 || tarjetas.length === 0;
  });
}
