function deleteCar(carId, carTitle) {
    if (window.confirm(`Are you sure you want to delete ${carTitle}`)) {
        fetch(`/cars/delete/${carId}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken,
            },
        })
            .then(response => {
                console.log(`Successfully deleted car with ID: ${carId}`);

                // Remove the car element from the DOM
                document.getElementById(`car-${carId}`).remove();

                // Update the car count
                const countElement = document.getElementById('count');
                const currentCount = parseInt(countElement.textContent);
                console.log(`Current car count: ${currentCount}`);  // Log current count
                countElement.textContent = (currentCount - 1).toString();
                console.log(`Updated car count: ${countElement.textContent}`);  // Log updated count


                alert(`${carTitle} deleted successfully!`);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
}