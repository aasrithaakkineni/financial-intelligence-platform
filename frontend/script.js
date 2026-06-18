function showMessage() {
    alert("Displaying processed ETL data");
}

window.onload = function () {
    document.getElementById("stockTable").innerHTML = `
        <tr>
            <td>1</td>
            <td>Apple</td>
            <td>210</td>
            <td>Technology</td>
            <td>3T</td>
        </tr>

        <tr>
            <td>2</td>
            <td>Tesla</td>
            <td>180</td>
            <td>Automobile</td>
            <td>800B</td>
        </tr>

        <tr>
            <td>3</td>
            <td>Microsoft</td>
            <td>450</td>
            <td>Technology</td>
            <td>3.2T</td>
        </tr>
    `;
};