function deleteBike(bikeId) {
    fetch(`/bikes/delete/${bikeId}`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrfToken,
        },
    })
        .then(response => {
            if (response.ok) {
                document.getElementById(`bike-${bikeId}`).remove();
                console.log(`Bike with ID ${bikeId} deleted successfully.`);
            } else {
                console.error(`Failed to delete bike with ID ${bikeId}.`);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}