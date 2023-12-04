document.addEventListener('DOMContentLoaded', function(event) {
    var formReservas = document.getElementById('formReservas');

    formReservas.addEventListener('click', function (event) {
        var target = event.target;

        if (target.id === 'ver-servicios') {
            var firstFormDiv = document.getElementById('first-form');
            var listServicesDiv = document.getElementById('list-services');
            
            obtenerServicios(function (servicios) {
                createServiceCards(servicios);
                firstFormDiv.classList.add('d-none');
                listServicesDiv.classList.remove('d-none');
            });
        }

        if (target.id === 'volver-formulario') {
            var firstFormDiv = document.getElementById('first-form');
            var listServicesDiv = document.getElementById('list-services');
            listServicesDiv.classList.add('d-none');
            firstFormDiv.classList.remove('d-none');
        }
    })
})

// Modificar la función para que acepte una función de retorno (callback)
function obtenerServicios(callback) {
    var itinerarioId = document.getElementById('itinerarios').value;

    fetch('/obtener_servicios_itinerarios/' + itinerarioId + '/')
        .then(response => response.json())
        .then(data => {
            // Llamando a la función de retorno con los datos obtenidos
            callback(data.servicios);
        })
        .catch(error => console.error('Error:', error));
}

function createServiceCards(servicios) {
    var serviciosContainer = document.getElementById('list-services');

    // Limpiar el contenedor de cards
    serviciosContainer.innerHTML = '';

    // Crear una card para cada servicio
    servicios.forEach(function (servicio) {
        var dateLlegada = new Date(servicio.llegada);
        var datePartida = new Date(servicio.partida);
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };

        var label = document.createElement('label');
        label.classList.add('rounded-3', 'my-2', 'p-2', 'd-flex','align-items-center');
        label.style = 'background: rgba( 255, 255, 255, 0.2 ); box-shadow: 0 8px 32px 0 rgba(19, 20, 27, 0.37)';

        var input = document.createElement('input');
        input.type = 'radio';
        input.name = 'radio-servicio';
        input.value = servicio.calidad;

        label.appendChild(input);

        var servicioInfo = document.createElement('div');
        servicioInfo.classList.add('flex-fill')
        
        var title = document.createElement('h5');
        title.textContent = "Servicio " + servicio.calidad;
        title.classList.add('fw-bold', 'text-end', 'm-0')
        servicioInfo.appendChild(title);

        var description0 = document.createElement('p');
        description0.textContent = "Servicio " + servicio.tipo;
        description0.classList.add('fw-bold', 'text-end', 'm-0')
        description0.style = 'font-size: 0.8rem';
        servicioInfo.appendChild(description0);

        var description1 = document.createElement('p');
        description1.classList.add('text-end', 'text-wrap', 'm-0');
        description1.style = 'font-size: 0.8rem';
        description1.textContent = "Sale: " + datePartida.toLocaleDateString("es-ES", options);
        servicioInfo.appendChild(description1);

        var description2 = document.createElement('p');
        description2.classList.add('text-end', 'text-wrap', 'm-0');
        description2.style = 'font-size: 0.8rem';
        description2.textContent = "Llega: " + dateLlegada.toLocaleDateString("es-ES", options);
        servicioInfo.appendChild(description2);

        label.appendChild(servicioInfo);

        serviciosContainer.appendChild(label)
    });
}
