from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import get_products,insert_sales,get_stock,available_stock,create_user,check_user,get_sales_per_product,get_sales,get_data,get_stock_data
from flask_bcrypt import bcrypt
from functools import wraps



#flask instance
app = Flask(__name__)

app.secret_key = 'ramo'  # Set a secret key for session management and flash messages





@app.route("/")
def home():
    return render_template('index.html')

def login_required(f):
    @wraps(f)
    def protected(*args, **kwargs):
        if 'email' not in session:
            
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return protected
  

@app.route('/products')
@login_required
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
        flash("Product added successfully",'success')
        return redirect(url_for('products'))
    


@app.route('/sales')
def sales():
    sales = sales()  # This function should fetch sales data from your database or any data source  
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
            flash("Insufficient stock, cant complete the sale", "error")
            return redirect(url_for('sales'))
            insert_sales(new_sale)
        ("Sale added successfully")
        return redirect(url_for('sales'))

@app.route('/stock')
def stock():
    products = get_products()
    stock_data = get_stock() # This function should fetch stock data from your database or any data source
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
    sales_per_day= sales_per_day() # This function should fetch sales per day data from your database or any data source
    profit_per_day = profit_per_day()  # This function should fetch profit per day data from your database or any data source
    sales_per_product = sales_per_product() # This function should fetch sales per product data from your database or any data source
    profit_per_product = profit_per_product()  # This function should fetch profit per product data from your database or any data source

    day = [i[0] for i in sales_per_day]
    sales = [i[1] for i in sales_per_product]
    profit = [i[1] for i in profit_per_day]



    product_names = [i[0] for i in sales_per_product]
    sales_per_product = [i[1] for i in sales_per_product]
    profit_per_product = [i[1] for i in profit_per_product]


  

 

    
    return render_template('dashboard.html',day=day, sales_day=sales_per_day, profit_per_day=profit_per_day, product_name=product_names
    , sales_per_product=sales_per_product, profit_per_product=profit_per_product)
    

@app.route('/login'  , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        exiting_user = check_user(email)
        if not exiting_user:

                flash("user does not exist, please register",'danger')
        else:
            if bcrypt.check_password_hash(exiting_user[-1],password):
                flash("Login successful", "success")
                session[email] = email
                return redirect(url_for('dashboard'))   
            else:
                flash("password incorrect",'danger')
              
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
    
@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("logged out successfully",'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)





