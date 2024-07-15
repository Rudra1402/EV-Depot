function deleteBike(bikeId, bikeTitle) {
    if (window.confirm(`Are you sure you want to delete ${bikeTitle}`)) {
        fetch(`/bikes/delete/${bikeId}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken,
            },
        })
            .then(response => {
                document.getElementById(`bike-${bikeId}`).remove();
                alert(`${bikeTitle} deleted successfully!`);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
}

