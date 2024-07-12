function deleteCar(carId) {
    fetch(`/cars/delete/${carId}`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrfToken,
        },
    })
        .then(response => {
            if (response.ok) {
                document.getElementById(`car-${carId}`).remove();
                console.log(`Car with ID ${carId} deleted successfully.`);
            } else {
                console.error(`Failed to delete bike with ID ${carId}.`);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}