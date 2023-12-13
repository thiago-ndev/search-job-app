function exibirMensagemErro() {
    Swal.fire({
        position: 'center',
        icon: 'error',
        title: "Nenhum resultado encontrado, tente outros filtros!",
        showConfirmButton: false,
        timer: 1500,
        background: '#dee2e6',
    });
}