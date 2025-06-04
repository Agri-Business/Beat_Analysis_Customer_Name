from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV data
df = pd.read_csv("Beat Analysis.csv")
df.columns = df.columns.str.strip()

@app.route('/get_customer_data', methods=['GET'])
def get_customer_data():
    customer_name = request.args.get('Customer')

    if not customer_name:
        return jsonify({'error': 'Customer parameter is required'}), 400

    try:
        result = df[df['Customer Name'].astype(str).str.lower() == customer_name.lower()]

        if result.empty:
            return jsonify({'message': 'No data found for this customer'}), 404

        output = result.to_dict(orient='records')
        return jsonify(output)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
