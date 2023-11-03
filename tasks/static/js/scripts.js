document.addEventListener('DOMContentLoaded', function() {

    var deleteBtns = document.querySelectorAll('.delete-btn');
    var searchBtn = document.getElementById('search-btn');
    var searchForm = document.getElementById('search-form');
    
    deleteBtns.forEach(function(deleteBtn) {
        deleteBtn.addEventListener('click', function(e) {
            e.preventDefault();
            var delLink = this.getAttribute('href');
            var result = confirm('Quer deletar esta tarefa?');
            if(result) {
                window.location.href = delLink;
            }
        });
    });

    if (searchBtn) {
        searchBtn.addEventListener('click', function() {
            searchForm.submit();
        });
    }

});
