function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

function deleteJourney(journey_slug) {
    if (confirm("Are you sure you want to delete this journey?")) {
        fetch(`${journey_slug}/delete/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCSRFToken(),
                "Content-Type": "application/json"
            }
        }).then(response => {
            if (response.ok) {
                window.location.href = `/journeys/`
                console.log("journey deleted.")
            }
        });
    }
}

function deleteLocation(journey_slug, location_slug) {
    if (confirm("Are you sure you want to delete this journey?")) {
        fetch(`locations/${location_slug}/delete/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCSRFToken(),
                "Content-Type": "application/json"
            }
        }).then(response => {
            if (response.ok) {
                window.location.href = `/journeys/${journey_slug}/`
                console.log("location deleted.")
            }
        });
    }
}

function deleteLocationPhoto(journey_slug, location_slug, photo_id) {
    if (confirm("Are you sure you want to delete this journey?")) {
        fetch(`location_photos/${photo_id}/delete/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCSRFToken(),
                "Content-Type": "application/json"
            }
        }).then(response => {
            if (response.ok) {
                window.location.href = `/journeys/${journey_slug}/locations/${location_slug}/`
                console.log("photo deleted.")
            }
        });
    }
}