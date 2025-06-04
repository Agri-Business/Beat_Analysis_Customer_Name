from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

df = pd.read_csv("Beat Analysis.csv")
df.columns = df.columns.str.strip()

@app.route('/get_customer_data', methods=['GET'])
def get_customer_data():
    customer_name = request.args.get('Customer')

    if not customer_name:
        return jsonify({'error': 'Customer parameter is required'}), 400

    try:
        result = df[df['Customer_Name'].astype(str).str.lower() == customer_name.lower()]
        if result.empty:
            return jsonify({'message': 'No data found for this customer'}), 404
        return jsonify(result.to_dict(orient='records'))

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
