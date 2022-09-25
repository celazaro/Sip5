// Confirmación de eliminación de un paciente

(function() {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click',(e) => {
            const confirmacion = confirm ('¿Está seguro de eliminar un paciente?');
            if(!confirmacion) {
                e.preventDefault();
            };

        });
    
    });

})();


