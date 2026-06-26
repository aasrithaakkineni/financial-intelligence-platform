function showMessage() {
    alert("Displaying processed ETL data");
}

const stocks = [
    {
        id: 1,
        name: "Apple",
        price: 210,
        sector: "Technology",
        marketCap: "3T",
        healthScore: 95,
        healthStatus: "Excellent",
        revenue: "394B",
        netProfit: "97B"
    },
    {
        id: 2,
        name: "Tesla",
        price: 180,
        sector: "Automobile",
        marketCap: "800B",
        healthScore: 88,
        healthStatus: "Good",
        revenue: "96B",
        netProfit: "15B"
    },
    {
        id: 3,
        name: "Microsoft",
        price: 450,
        sector: "Technology",
        marketCap: "3.2T",
        healthScore: 97,
        healthStatus: "Excellent",
        revenue: "245B",
        netProfit: "88B"
    }
];

function displayTable(data) {
    let table = document.getElementById("stockTable");
    table.innerHTML = "";

    data.forEach(stock => {
        table.innerHTML += `
        <tr>
            <td>${stock.id}</td>
            <td>${stock.name}</td>
            <td>${stock.price}</td>
            <td>${stock.sector}</td>
            <td>${stock.marketCap}</td>
            <td>${stock.healthScore}</td>
            <td>${stock.healthStatus}</td>
            <td>${stock.revenue}</td>
            <td>${stock.netProfit}</td>
        </tr>`;
    });
}

window.onload = function () {
    displayTable(stocks);

    document.getElementById("companySelect").addEventListener("change", function () {
        let selected = this.value;

        if (selected === "") {
            displayTable(stocks);
        } else {
            let filtered = stocks.filter(stock => stock.name === selected);
            displayTable(filtered);
        }
    });
};

function searchCompany() {
    let input = document.getElementById("searchInput").value.toLowerCase();

    let filtered = stocks.filter(stock =>
        stock.name.toLowerCase().includes(input)
    );

    displayTable(filtered);
}