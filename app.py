from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    name = data.get('name', '')
    hourly_rate = float(data.get('hourly_rate', 0))
    month_hours = float(data.get('month_hours', 0))
    overtime_hours = float(data.get('overtime_hours', 0))
    tax_rate = float(data.get('tax_rate', 0))

    regular_pay = month_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    gross_salary = regular_pay + overtime_pay
    tax = gross_salary * (tax_rate / 100)
    net_salary = gross_salary - tax
    total_hours = month_hours + overtime_hours

    return jsonify({
        'name': name,
        'hourly_rate': hourly_rate,
        'month_hours': month_hours,
        'overtime_hours': overtime_hours,
        'tax_rate': tax_rate,
        'regular_pay': regular_pay,
        'overtime_pay': overtime_pay,
        'tax': tax,
        'net_salary': net_salary,
        'total_hours': total_hours
    })

if __name__ == '__main__':
    app.run(debug=True)
