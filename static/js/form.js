document.addEventListener('DOMContentLoaded', function () {
    // Tu código JavaScript aquí
    var origenes = document.getElementById('origen-container');
    var destinos = document.getElementById('destino-container');
    var form = document.getElementById('formReservas'); // Asegúrate de reemplazar 'formReservas' con el ID de tu formulario

    document.getElementById('itinerarios').addEventListener('change', function () {
        var itinerarioId = this.value;

        fetch('/obtener_paradas_intermedias/' + itinerarioId + '/')
            .then(response => response.json())
            .then(data => {
                actualizarOpciones('origen', data.paradas_intermedias);
                actualizarOpciones('destino', data.paradas_intermedias);

                // Deshabilitar todos los destinos al inicio
                deshabilitarDestinos();
            })
            .catch(error => console.error('Error:', error));
    });

    function deshabilitarDestinos() {
        var radiosDestino = destinos.querySelectorAll('input[type="radio"]');
        radiosDestino.forEach(function (radio) {
            radio.disabled = true;
        });
    }

    function actualizarOpciones(selectId, opciones) {
        var container = document.getElementById(selectId + '-container');
        container.innerHTML = '';

        var tituloColumna = document.createElement('p');
        tituloColumna.appendChild(document.createTextNode('Seleccione ' + selectId));
        tituloColumna.classList.add('m-0', 'fw-bold');
        container.appendChild(tituloColumna);

        opciones.forEach(function (opcion, index) {
            var radioContainer = document.createElement('div'); // Contenedor para radiobutton y label

            var radio = document.createElement('input');
            radio.type = 'radio';
            radio.name = selectId + '-radio';
            radio.value = opcion.posicion;

            // Deshabilitar la última ciudad en origen y la primera ciudad en destino
            if ((selectId === 'origen' && index === opciones.length - 1) ||
                (selectId === 'destino' && index === 0)) {
                radio.disabled = true;
            }

            var label = document.createElement('label');
            label.appendChild(document.createTextNode(opcion.nombre));

            radioContainer.appendChild(label);
            radioContainer.appendChild(radio);
            radioContainer.classList.add('d-flex', 'align-items-center', 'justify-content-between');
            container.appendChild(radioContainer);

            // Agregar evento change para habilitar destinos según el origen seleccionado
            if (selectId === 'origen') {
                radio.addEventListener('change', function () {
                    deshabilitarDestinos();
                    habilitarDestinos(index + 1); // Habilitar destinos a partir de este índice
                    verificarSeleccion(); // Verificar si ambos radios están seleccionados
                });
            } else if (selectId === 'destino') {
                radio.addEventListener('change', function () {
                    verificarSeleccion(); // Verificar si ambos radios están seleccionados
                });
            }
        });
    }

    function habilitarDestinos(desdeIndice) {
        var radiosDestino = destinos.querySelectorAll('input[type="radio"]');
        radiosDestino.forEach(function (radio, index) {
            if (index >= desdeIndice) {
                radio.disabled = false;
            }
        });
    }

    function verificarSeleccion() {
        var radioOrigenSeleccionado = origenes.querySelector('input[type="radio"]:checked');
        var radioDestinoSeleccionado = destinos.querySelector('input[type="radio"]:checked');

        // Verificar si ambos radios de origen y destino están seleccionados
        if (radioOrigenSeleccionado && radioDestinoSeleccionado) {
            agregarBoton(); // Agregar el botón al formulario
        }
    }

    function agregarBoton() {
        var boton = document.createElement('button');
        boton.type = 'button';
        boton.textContent = 'Enviar';
        boton.addEventListener('click', function () {
            // Lógica para el botón (puedes agregar la funcionalidad que desees)
            alert('Botón presionado');
        });

        form.appendChild(boton);
    }
});