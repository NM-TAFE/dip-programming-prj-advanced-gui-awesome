/**
 * otherControls.js
 *
 * This JavaScript file handles hotkeys and key bindings that are outside the video player view.
 **/

/**
 * Opens the home page.
 */
function openHomePage() {
    window.location.href = "/";
}

/**
 * Opens the settings page.
 */
function openSettingsPage() {
    window.location.href = "/settings";
}

/**
 * Opens the upload video page.
 */
function uploadVideo() {
    window.location.href = "/upload";
}

/**
 * Delete a video from user library after receiving confirmation
 * @param filename filename of video to delete
 */
function deleteVideo(filename) {
    let response = confirm("Are you sure you want to delete this video?");
    if (response === true) {
        window.location.href = `/delete_video/${filename}`;
    }
}

/**
 * Update Tesseract file path.
 * When Tesseract is installed, the file path must be updated in order for the OCR to work.
 * If Tesseract is not installed, show a message to the user.
 * This function opens the update_tesseract_path page.
 */
document.addEventListener('DOMContentLoaded', function () {
    const searchTesseractPath = document.getElementById("search-tesseract");
    const searchIDEPath = document.getElementById("search-ide");
    const message = document.getElementById("finding-tesseract");
    const cancelSearchButton = document.getElementById("cancel-search");
    const cancelSearchIDEButton = document.getElementById("cancel-search-ide");
    const alertMessageDiv = document.getElementById("alert-message");

    // If the message exists, show it to the user and remove it after 1 second
    if (message) {
        const alertContainer = document.createElement('div');
        alertContainer.innerHTML = `<p class="mb-3 text-red-500 text-xl">${message.innerHTML}</p>`;
        alertMessageDiv.appendChild(alertContainer);
        setTimeout(() => alertContainer.remove(), 1000);
        searchTesseractPath.remove();
        searchIDEPath.remove();
        cancelSearchButton.remove();
        cancelSearchIDEButton.remove();
    }

    // If the search button exists, show the alert message to the user and add event listeners to the buttons
    if (!message && (searchTesseractPath || searchIDEPath)) {
        const alertContainer = document.createElement('div');
        if (searchTesseractPath) {
                alertContainer.innerHTML = `
                    <p class="text-xl">We could not locate the Tesseract library.</p>
                    <p class="text-xl">Tesseract is required to run this program.</p>
                    <p class="text-xl">Would you like us to perform an automatic search on your local disk to find it?</p>
                    <p class="my-3 text-xl">If you prefer to set the path manually, please click "Cancel."</p>
                    <button class="w-1/6 mb-3 bg-red-500 hover:bg-red-300 text-white hover:text-red-500 px-2 py-1 rounded-md" id="confirm-search">Search</button>
                    <button class="w-1/6 mb-3 bg-red-500 hover:bg-red-300 text-white hover:text-red-500 px-2 py-1 rounded-md" id="cancel-search-manual">Cancel</button>
                `;
            } else if (searchIDEPath) {
                alertContainer.innerHTML = `
                    <p class="text-xl">We could not locate the PyCharm IDE.</p>
                    <p class="text-xl">This program requires an IDE to upload code snippets to.</p>
                    <p class="text-xl">Would you like us to perform an automatic search on your PC to find it?</p>
                    <p class="my-3 text-xl">If you prefer to set the path manually, please click "Cancel."</p>
                    <button class="w-1/6 mb-3 bg-red-500 hover:bg-red-300 text-white hover:text-red-500 px-2 py-1 rounded-md" id="confirm-search-ide">Search</button>
                    <button class="w-1/6 mb-3 bg-red-500 hover:bg-red-300 text-white hover:text-red-500 px-2 py-1 rounded-md" id="cancel-search-manual-ide">Cancel</button>
                `;
            }
        alertMessageDiv.appendChild(alertContainer);

        if (searchTesseractPath) {
            // Add event listener for the confirm button
        document.getElementById("confirm-search").addEventListener('click', function () {
            window.location.href = "/update_tesseract_path";
            searchTesseractPath.innerHTML = "<span><i class=\"fa-solid fa-circle-notch fa-spin mr-2\"></i>Searching for Tesseract</span>";
            cancelSearchButton.classList.remove("hidden");
            alertContainer.remove();
        });

        // Add event listener for the cancel button
        document.getElementById("cancel-search-manual").addEventListener('click', function () {
            searchTesseractPath.remove();
            cancelSearchButton.remove();
            alertContainer.remove();
        });

        // Add event listener for the cancel button (if it exists) - this is for the case where the user cancels the search
        if (cancelSearchButton) {
            cancelSearchButton.addEventListener('click', function () {
                // Send a Fetch request to cancel the search on the server
                fetch('/update_tesseract_path', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    body: 'cancel_search=true'
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        // Handle the response if needed
                        return response.json();
                    })
                    .catch(error => {
                        console.error('There was a problem with the fetch operation:', error);
                    });
            });
        }
        } else if (searchIDEPath) {
            document.getElementById("confirm-search-ide").addEventListener('click', function () {
                    window.location.href = "/update_ide_path";
                    searchIDEPath.innerHTML = "<span><i class=\"fa-solid fa-circle-notch fa-spin mr-2\"></i>Searching for PyCharm IDE</span>";
                    cancelSearchIDEButton.classList.remove("hidden");
                    alertContainer.remove();
                });

                document.getElementById("cancel-search-manual-ide").addEventListener('click', function () {
                    searchIDEPath.remove();
                    cancelSearchIDEButton.remove();
                    alertContainer.remove();
                });

                if (cancelSearchIDEButton) {
                    cancelSearchIDEButton.addEventListener('click', function () {
                        fetch('/update_ide_path', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/x-www-form-urlencoded'
                            },
                            body: 'cancel_search=true'
                        })
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            return response.json();
                        })
                        .then(data => {
                            searchIDEPath.innerHTML = `<span>${data.message}</span>`;
                            setTimeout(() => searchIDEPath.remove(), 3000);
                            cancelSearchIDEButton.classList.add("hidden");
                        })
                        .catch(error => console.error('There was a problem with the fetch operation:', error));
                    });
                }
        }
    }
});

/**
 * Mutes all UI sound effects and sound based feedback.
 *
 * NOT IMPLEMENTED
 * Note: It is critical this function name is not changed as the keybindings rely on it.
 */
function muteUiSounds() {

}

