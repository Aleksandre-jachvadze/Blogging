// Simple search/filter by student name
const searchInput = document.getElementById('searchInput');
const table = document.getElementById('studentsTable');

searchInput.addEventListener('keyup', function() {
    const filter = searchInput.value.toLowerCase();
    const rows = table.getElementsByTagName('tr');

    for (let i = 0; i < rows.length; i++) {
        const firstName = rows[i].getElementsByTagName('td')[0].textContent.toLowerCase();
        const lastName = rows[i].getElementsByTagName('td')[1].textContent.toLowerCase();
        if (firstName.includes(filter) || lastName.includes(filter)) {
            rows[i].style.display = '';
        } else {
            rows[i].style.display = 'none';
        }
    }
});
