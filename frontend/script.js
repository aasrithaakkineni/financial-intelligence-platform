function showMessage() {
    alert("Displaying processed ETL data");
}

window.onload = function () {
    document.getElementById("stockTable").innerHTML = `
        <tr>
            <td>1</td>
            <td>Apple</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Tesla</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Microsoft</td>
        </tr>
    `;
};