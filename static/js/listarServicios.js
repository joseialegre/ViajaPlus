document.addEventListener('DOMContentLoaded', function(event) {
    var formReservas = document.getElementById('formReservas');

    formReservas.addEventListener('click', function (event) {
        var target = event.target;

        if (target.id === 'ver-servicios') {

            var campoDNI = document.getElementById('dniPasajero').value;
            if (campoDNI.trim() === '') {
                alert('Por favor, complete el campo DNI antes de continuar.');
                return;
            }

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

        if (target.id === 'enviar-formulario') {
            // Verificar que se haya seleccionado un servicio
            var selectedService = document.querySelector('input[name="servicio"]:checked');
            if (!selectedService) {
                alert('Por favor, selecciona un servicio antes de enviar el formulario.');
                return;
            }
            alert('La reserva se ha realizado con éxito.');
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
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric'};

        var label = document.createElement('label');
        label.classList.add('servicioLabel', 'rounded-3', 'my-2', 'p-2', 'd-flex','align-items-center');

        var input = document.createElement('input');
        input.type = 'radio';
        input.name = 'servicio';
        input.value = servicio.numero_servicio;

        label.appendChild(input);

        var servicioInfo = document.createElement('div');
        servicioInfo.classList.add('flex-fill')
        
        var title = document.createElement('h5');
        title.textContent = "Calidad " + servicio.calidad.toUpperCase();
        title.classList.add('fw-bold', 'text-end', 'm-0', 'p-0')
        servicioInfo.appendChild(title);

        var description0 = document.createElement('p');
        description0.textContent = "Servicio " + servicio.tipo.toUpperCase();
        description0.classList.add('fw-bold', 'text-end', 'm-0', 'p-0')
        servicioInfo.appendChild(description0);

        var description1 = document.createElement('p');
        description1.classList.add('text-end', 'text-wrap', 'm-0', 'p-0');
        description1.textContent = "Sale: " + datePartida.toLocaleDateString("es-ES", options);
        servicioInfo.appendChild(description1);

        var description2 = document.createElement('p');
        description2.classList.add('text-end', 'text-wrap', 'm-0', 'p-0');
        description2.textContent = "Llega: " + dateLlegada.toLocaleDateString("es-ES", options);
        servicioInfo.appendChild(description2);

        label.appendChild(servicioInfo);

        serviciosContainer.appendChild(label)
    });

    var doubleButton = document.createElement('div');
    doubleButton.classList.add('d-flex', 'align-items-center', 'justify-content-between');

    var buttonVolver = document.createElement('button');
    buttonVolver.type = 'button';
    buttonVolver.id = 'volver-formulario';
    buttonVolver.textContent = 'Volver';

    var buttonEnviar = document.createElement('button');
    buttonEnviar.type = 'submit';
    buttonEnviar.id = 'enviar-formulario';
    buttonEnviar.textContent = 'RESERVAR';

    doubleButton.appendChild(buttonVolver);
    doubleButton.appendChild(buttonEnviar);

    serviciosContainer.appendChild(doubleButton);
}
