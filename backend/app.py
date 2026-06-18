from flask import Flask, jsonify

app = Flask(__name__)

stocks = [
    {
        "id": 1,
        "name": "Apple",
        "price": 210,
        "sector": "Technology",
        "market_cap": "3T",
        "health_score": 95,
        "health_status": "Excellent"
    },
    {
        "id": 2,
        "name": "Tesla",
        "price": 180,
        "sector": "Automobile",
        "market_cap": "800B",
        "health_score": 88,
        "health_status": "Good"
    },
    {
        "id": 3,
        "name": "Microsoft",
        "price": 450,
        "sector": "Technology",
        "market_cap": "3.2T",
        "health_score": 97,
        "health_status": "Excellent"
    }
]

@app.route('/stocks')
def get_stocks():
    return jsonify(stocks)

if __name__ == '__main__':
    app.run(debug=True)