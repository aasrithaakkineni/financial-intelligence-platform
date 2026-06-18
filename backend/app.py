from flask import Flask, jsonify

app = Flask(__name__)

stocks = [
    {
        "id": 1,
        "name": "Apple",
        "price": 210,
        "sector": "Technology",
        "market_cap": "3T"
    },
    {
        "id": 2,
        "name": "Tesla",
        "price": 180,
        "sector": "Automobile",
        "market_cap": "800B"
    },
    {
        "id": 3,
        "name": "Microsoft",
        "price": 450,
        "sector": "Technology",
        "market_cap": "3.2T"
    }
]

@app.route('/stocks')
def get_stocks():
    return jsonify(stocks)

if __name__ == '__main__':
    app.run(debug=True)