// my_profile.js

document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.querySelector(".edit-user-info");
    const saveButton = document.querySelector(".save-user-info");
    const formFields = document.querySelectorAll("form input[type='text']");

    let editMode = false;

    editButton.addEventListener("click", function () {
        editMode = !editMode;
        formFields.forEach((field) => {
            field.disabled = !editMode;
        });

        if (editMode) {
            editButton.style.display = "none";
            saveButton.style.display = "inline-block";
        } else {
            editButton.style.display = "inline-block";
            saveButton.style.display = "none";
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
        const editBioButton = document.querySelector(".edit-bio");
        const bioText = document.querySelector(".bio-text");
        const bioEditForm = document.querySelector(".bio-edit-form");
        const bioTextarea = document.querySelector("#bio");

        let bioEditMode = false;

        editBioButton.addEventListener("click", function () {
            bioEditMode = !bioEditMode;
            bioText.style.display = bioEditMode ? "none" : "block";
            bioEditForm.style.display = bioEditMode ? "block" : "none";
            bioTextarea.value = bioText.innerText.trim(); // Set textarea value from bio text

            if (bioEditMode) {
                editBioButton.style.display = "none";
            } else {
                editBioButton.style.display = "inline-block";
            }
        });

        // Handle cancel button
        const cancelButton = document.querySelector(".cancel-bio");
        cancelButton.addEventListener("click", function () {
            bioEditMode = false;
            bioText.style.display = "block";
            bioEditForm.style.display = "none";
            editBioButton.style.display = "inline-block";
        });
    });


    document.addEventListener("DOMContentLoaded", function () {
        const profilePhotoInput = document.querySelector("#profile-photo-upload");
        const profilePhotoPreview = document.querySelector("#profile-photo-preview");
    
        profilePhotoInput.addEventListener("change", function () {
            const file = profilePhotoInput.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    profilePhotoPreview.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    });


document.addEventListener("DOMContentLoaded", function () {
    const profilePhotoContainer = document.querySelector(".profile-photo-container");
    const profilePhotoInput = document.querySelector("#profile-photo-input");
    const profilePhotoForm = document.querySelector("#profile-photo-form");

    profilePhotoContainer.addEventListener("click", function () {
        profilePhotoInput.click();
    });

    profilePhotoInput.addEventListener("change", function () {
        profilePhotoForm.submit();
    });
});

function changeProfilePhoto() {
    document.getElementById("profile-photo").style.display = "none";
    document.getElementById("profile-photo-upload").style.display = "block";
    document.querySelector('.btn-secondary').style.display = "none";
    document.querySelector('.btn-primary').style.display = "block";
}

function openFileInput() {
    document.getElementById("profile-photo-upload").click();
}