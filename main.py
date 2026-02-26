from flask import Flask,render_template, request, redirect, url_for
from database import get_products,get_sales,insert_sales




#flask instance
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    products = get_products()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = (product_name, buying_price, selling_price)
        insert_sales(new_product)
        print("Product added successfully")
        return redirect(url_for('products'))

@app.route('/sales')
def sales():
    sales = get_sales()  # This function should fetch sales data from your database or any data source  
    return render_template('sales.html',sales = sales)




@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


app.run(debug=True)





