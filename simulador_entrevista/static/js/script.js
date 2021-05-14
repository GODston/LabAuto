// Se agrega la propiedad onclick en los items de la lista de entrevistas
document.querySelectorAll('.tr-entrevista').forEach(entrevista => {
    var entrevista_id = entrevista.getAttribute("id")
    entrevista.addEventListener('click', event => {
        window.location.href = '/interviews/' + entrevista_id;
    })
})

// Se agrega la propiedad onclick en los items de la lista de candidatos
document.querySelectorAll('.tr-candidatos').forEach(candidato => {
    var candidato_id = candidato.getAttribute("id")
    candidato.addEventListener('click', event => {
        window.location.href = '/candidates/' + candidato_id;
    })
})

// Boton para editar los datos generales de la entrevista
document.getElementById('btnEditarEntrevista').onclick = function() {
            
    if(this.textContent == 'Editar') {
        this.removeAttribute('class');
        this.setAttribute('class', 'btn btn-warning col-md-4')
        this.textContent = 'Cancelar'
        $('#btnActualizarEntrevista').css('display', 'block');
    } else {
        this.removeAttribute('class');
        this.setAttribute('class', 'btn btn-primary col-md-4')
        this.textContent = 'Editar'
        $('#btnActualizarEntrevista').css('display', 'none');
    }

    document.querySelectorAll('.form-entrevista-general').forEach(input => {
        input.disabled = !input.disabled;
    })
};

// Boton para agregar preguntas
document.getElementById('btnAgregarPreguntas').onclick = function() {
    
}

// Boton para editar las preguntas de la entrevista
document.getElementById('btnEditarPreguntas').onclick = function() {
    
    if(this.textContent == 'Editar') {
        this.removeAttribute('class');
        this.setAttribute('class', 'btn btn-warning')
        this.textContent = 'Cancelar'
        $('#btnAgregarPreguntas').css('display', 'none');
        $('#btnActualizarPreguntas').css('display', 'block');
        $('#btnEliminarPreguntas').css('display', 'block');
        $('.form-check-delete').css('display', 'block');
    } else {
        this.removeAttribute('class');
        this.setAttribute('class', 'btn btn-primary')
        this.textContent = 'Editar'
        $('#btnAgregarPreguntas').css('display', 'block');
        $('#btnActualizarPreguntas').css('display', 'none');
        $('#btnEliminarPreguntas').css('display', 'none');
        $('.form-check-delete').css('display', 'none');
    }

    document.querySelectorAll('.form-input-preguntas').forEach(input => {
        input.disabled = !input.disabled;
    })
};


// Boton para eliminar registros
// TODO: Agregar peticion para eliminar las preguntas
document.getElementById('btnEliminarPreguntas').onclick = function() {
    var preguntasEliminar = []
    document.querySelectorAll('.form-check-delete:checked').forEach(chkDelete => {
        preguntasEliminar.push(chkDelete.getAttribute('id'))
    })

    console.log(preguntasEliminar);
}