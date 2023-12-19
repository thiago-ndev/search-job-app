const botao = document.getElementById("confirm")
console.log(job_data_list)
botao.addEventListener("click", function () {
        function exibirMensagemErro() {
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: "Nenhum resultado encontrado, tente outros filtros!",
            showConfirmButton: false,
            timer: 3500,
            background: '#dee2e6',
        });
    }
    if (job_data_list == 'None'){
        exibirMensagemErro();

    }
});

