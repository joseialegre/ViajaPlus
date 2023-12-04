document.addEventListener('DOMContentLoaded', function(event) {

    var formReservas = document.getElementById('formReservas');

    formReservas.addEventListener('click', function (event) {
        var target = event.target;

        if (target.id === 'ver-servicios') {
            var firstFormDiv = document.getElementById('first-form');
            var listServicesDiv = document.getElementById('list-services');
            obtenerServicios();
            firstFormDiv.classList.add('d-none');
            listServicesDiv.classList.remove('d-none');
        }

        if (target.id === 'volver-formulario') {
            var firstFormDiv = document.getElementById('first-form');
            var listServicesDiv = document.getElementById('list-services');
            listServicesDiv.classList.add('d-none');
            firstFormDiv.classList.remove('d-none');
        }
    })
})

function obtenerServicios() {
var itinerarioId = document.getElementById('itinerarios').value;

fetch('/obtener_servicios_itinerarios/' + itinerarioId + '/')
    .then(response => response.json())
    .then(data => {
    data.servicios.forEach(function (servicio){
        console.log(servicio)
    })
    })
    .catch(error => console.error('Error:', error));
}
