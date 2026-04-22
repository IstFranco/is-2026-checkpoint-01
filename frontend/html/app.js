const statusText = document.getElementById("status");
const tableBody = document.getElementById("teamTable");

fetch(`http://${window.location.hostname}:5000/api/team`)
    .then(response => {
        if (!response.ok) {
            throw new Error("Error en la respuesta del servidor");
        }
        return response.json();
    })
    .then(data => {
        statusText.textContent = "🟢 Backend Online";

        data.forEach(member => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${member.nombre}</td>
                <td>${member.legajo}</td>
                <td>${member.feature}</td>
                <td>${member.servicio}</td>
                <td>${member.estado}</td>
            `;

            tableBody.appendChild(row);
        });
    })
    .catch(error => {
        statusText.textContent = "🔴 Backend Offline";
        console.error("Error:", error);
    });
