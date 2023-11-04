document.addEventListener('DOMContentLoaded', function() {

    var baseUrl = 'http://localhost:8000/';
    var deleteBtns = document.querySelectorAll('.delete-btn');
    var searchBtn = document.getElementById('search-btn');
    var searchForm = document.getElementById('search-form');
    var filter = document.getElementById('filter');

    deleteBtns.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();

            var delLink = this.getAttribute('href');
            var result = confirm('Quer deletar esta tarefa?');

            if(result) {
                window.location.href = delLink;
            }
        });
    });

    searchBtn.addEventListener('click', function() {
        searchForm.submit();
    });

    filter.addEventListener('change', function() {
        var filterValue = this.value;
        window.location.href = baseUrl + '?filter=' + filterValue;
    });

});
