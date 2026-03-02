from flask import Flask,render_template, request, redirect, url_for
from database import check_user, create_user, get_products,get_sales,insert_sales,get_stock_data,available_stock,get_sales_per_product




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

@app.route('/add-sales', methods=['GET', 'POST'])
def add_sales():
    if request.method == 'POST':
        pid = request.form['pid']
        quantity = request.form['quantity']

        new_sale = (pid, quantity)
        check_stock = available_stock(pid)
        if float(quantity) >  check_stock:
            print("Insufficient stock, cant complete the sale")
            return redirect(url_for('sales'))
            insert_sales(new_sale)
        print("Sale added successfully")
        return redirect(url_for('sales'))

@app.route('/stock')
def stock():
    products = get_products()
    stock_data = get_stock_data() # This function should fetch stock data from your database or any data source
    return render_template('stock.html', products=products, stock_data=stock_data)


@app.route('/add-stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        pid = request.form['pid']
        stock_quantity = request.form['quantity']

        new_stock = (pid, stock_quantity)
        insert_sales(new_stock)
        print("Stock added successfully")
        return redirect(url_for('stock'))
   
   
@app.route('/dashboard')
def dashboard():
    sales_data = sales_data  # This function should fetch sales per day data from your database or any data source
    profit_per_day = profit_per_day()  # This function should fetch profit per day data from your database or any data source
    sales_per_product = get_sales_per_product()  # This function should fetch sales per product data from your database or any data source
    profit_per_product = profit_per_product()  # This function should fetch profit per product data from your database or any data source

    day = [i[0] for i in sales_data]
    sales = [i[1] for i in sales_per_product]
    profit = [i[1] for i in profit_per_day]



    product_names = [i[0] for i in sales_per_product]
    sales_per_product = [i[1] for i in sales_per_product]
    profit_per_product = [i[1] for i in profit_per_product]


  

 

    
    return render_template('dashboard.html',day=day, sales_day=sales_data, profit_per_day=profit_per_day, product_name=product_names
    , sales_per_product=sales_per_product, profit_per_product=profit_per_product)
    

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']

        exiting_user = check_user(email)
        if not exiting_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = (full_name, email, phone_number, hashed_password)
        create_user(new_user)
        print("User created successfully")
        return redirect(url_for('login'))
    else:   
        print("user already exists, please login")
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)





