document.addEventListener('DOMContentLoaded', function () {
    
    document.getElementById('ver-servicios').addEventListener('click', function () {
        
        var itinerarioId = document.getElementById('itinerarios').value;

        fetch('/obtener_servicios_itinerarios/' + itinerarioId + '/')
            .then(response => response.json())
            .then(data => {
                data.servicios.forEach(function (servicio){
                    alert('Servicio: ' + servicio.numero_servicio + ', Partida: ' + servicio.fecha_partida + ', Llegada: ' + servicio.fecha_llegada);
                })
            })
            .catch(error => console.error('Error:', error));
            });
});