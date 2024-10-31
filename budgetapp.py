from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an in-memory database for the budget
# Normally you'd use a database, but for simplicity, we'll use lists here
budget_data = {
    "income": [],
    "expenses": []
}

@app.route('/')
def index():
    total_income = sum(item['amount'] for item in budget_data["income"])
    total_expenses = sum(item['amount'] for item in budget_data["expenses"])
    balance = total_income - total_expenses

    # Render budgetindex.html instead of index.html
    return render_template("budgetindex.html", 
                           income=budget_data["income"], 
                           expenses=budget_data["expenses"],
                           total_income=total_income, 
                           total_expenses=total_expenses, 
                           balance=balance)

@app.route('/add_income', methods=['POST'])
def add_income():
    source = request.form.get('source')
    amount = float(request.form.get('amount'))
    budget_data["income"].append({"source": source, "amount": amount})
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    category = request.form.get('category')
    description = request.form.get('description')
    amount = float(request.form.get('amount'))
    budget_data["expenses"].append({"category": category, "description": description, "amount": amount})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
