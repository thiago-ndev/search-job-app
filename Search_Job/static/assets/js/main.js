const botao = document.getElementById("confirm")
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





document.getElementById("download-btn").addEventListener('click', function () {
    console.log(1);
    const table = document.getElementById('tabela');
    const rows = table.getElementsByTagName('tr');
    let data = [];

    // Coletando dados da tabela
    for (let i = 1; i < rows.length; i++) {
        let cells = rows[i].getElementsByTagName('td');
        let rowData = {
            "Vaga": cells[0].innerText,
            "Empresa": cells[1].innerText,
            "Link da vaga": cells[2].innerText,
            "Estado": cells[3].innerText,
            "Cidade": cells[4].innerText,
            "Home Office": cells[5].innerText,
//            "País": cells[6].innerText
        };
        data.push(rowData);
        console.log(data)
    }

    // Enviando dados via POST para o backend
    fetch('/download-excel/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'  // Inclua o CSRF token se necessário
        },
        body: JSON.stringify(data)
    })
    .then(response => response.blob())
    .then(blob => {
        // Criando URL para o arquivo blob e forçando download
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'tabela_vagas.xlsx';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
    })
    .catch(error => console.error('Erro:', error));
});