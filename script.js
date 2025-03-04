document.addEventListener("DOMContentLoaded", function () {
    fetchMasterTagList();
});

// Function to Fetch All Master Tags
function fetchMasterTagList() {
    fetch("https://capstone-backend-abew.onrender.com/master-tag-list") // ✅ Updated URL
        .then(response => response.json())
        .then(data => {
            displayTags(data);
        })
        .catch(error => console.error("Error fetching data:", error));
}

// Function to Display Tags in the Table
function displayTags(tags) {
    const tableBody = document.getElementById("masterTagListBody");
    tableBody.innerHTML = ""; // Clear previous data

    tags.forEach(tag => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${tag.Tag_No}</td>
            <td>${tag.Tag}</td>
            <td>${tag.Instrument_Type}</td>
            <td>${tag.PID_No}</td>
            <td>${tag.Datasheet_Type}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Function to Search Tags
function searchTags() {
    const query = document.getElementById("searchInput").value;
    fetch(`https://capstone-backend-abew.onrender.com/master-tag-list/search?q=${query}`) // ✅ Updated URL
        .then(response => response.json())
        .then(data => {
            displayTags(data);
        })
        .catch(error => console.error("Error searching data:", error));
}
