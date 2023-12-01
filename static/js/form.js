document.addEventListener('DOMContentLoaded', function () {
    // Tu código JavaScript aquí
    document.getElementById('itinerarios').addEventListener('change', function () {
        var itinerarioId = this.value;

        fetch('/obtener_paradas_intermedias/' + itinerarioId + '/')
            .then(response => response.json())
            .then(data => {
                actualizarOpciones('origen', data.paradas_intermedias);
                actualizarOpciones('destino', data.paradas_intermedias);
            })
            .catch(error => console.error('Error:', error));
    });
    document.getElementById('reservar-btn').addEventListener('click', function () {
        var itinerarioId = document.getElementById('itinerarios').value;

        fetch('/obtener_servicios_itinerarios/' + itinerarioId + '/')
            .then(response => response.json())
            .then(data => {
                data.servicios.forEach(function (servicio) {
                    alert('Servicio: ' + servicio.numero_servicio + ', Partida: ' + servicio.fecha_partida + ', Llegada: ' + servicio.fecha_llegada);
                })
            })
            .catch(error => console.error('Error:', error));
    });
});

function actualizarOpciones(selectId, opciones) {
    var container = document.getElementById(selectId + '-container');
    container.innerHTML = '';

    var tituloColumna = document.createElement('p');
    tituloColumna.appendChild(document.createTextNode('Seleccione ' + selectId));
    tituloColumna.classList.add('m-0', 'fw-bold')
    container.appendChild(tituloColumna);
    
    opciones.forEach(function (opcion) {
        var checkboxContainer = document.createElement('div'); // Contenedor para checkbox y label

        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.name = selectId + '-checkbox';  
        checkbox.value = opcion.posicion;

        var label = document.createElement('label');
        label.appendChild(document.createTextNode(opcion.nombre));

        checkboxContainer.appendChild(label);
        checkboxContainer.appendChild(checkbox);
        checkboxContainer.classList.add('d-flex', 'align-items-center', 'justify-content-between');
        container.appendChild(checkboxContainer);
    });
    
}