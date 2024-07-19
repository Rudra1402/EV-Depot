function deleteTruck(truckId, truckTitle) {
    if (window.confirm(`Are you sure you want to delete ${truckTitle}`)) {
        fetch(`/trucks/delete/${truckId}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken,
            },
        })
            .then(response => {
                document.getElementById(`truck-${truckId}`).remove();
                alert(`${truckTitle} deleted successfully!`);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
}

