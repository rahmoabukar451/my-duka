import psycopg2






conn  = psycopg2.connect(host='localhost',port='5432',user='postgres',password='ramo',dbname='myduka_db')

cur = conn.cursor()




def get_data(table):
    cur.execute(f"select * from {table} ")
    data = cur.fetchall()
    return data

data = get_data("sales")
print(data)

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(products)




 

cur.execute("insert into products (name,buying_price,selling_price)values('sumsung',20000,30000)")
conn.commit()
products=get_products()
print(products)


product1 = ('sumsung',20000,30000)
product2 = ('hp',30000,40000)


 

 
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales = get_sales()
print(sales)


def insert_sales(pid,quantity):
    cur.execute("insert into sales (pid,quantity) values (%s,%s)", (pid,quantity))
    conn.commit()

   # sale1 = (3,2)
   #  sale2 = (4,12)
    insert_sales(3,2)
    insert_sales(4,12)
    all_sales = get_sales()
    print(all_sales)




stock1 = (1,30)
stock2 = (2,50)


def get_stock(values):
        cur.execute("select * from stock where pid = %s and quantity = %s", values)
        stock = cur.fetchall()
        return stock
    
def get_stock_data():
        cur.execute("select * from stock")
        stock_data = cur.fetchall()
        return stock_data
 
stock_data = get_stock_data()
print("this is stock ",stock_data)


 
    


def get_sales_per_product():
    cur.execute("""
        select products.name as name , sum(sales.quantity * products.selling_price)as sales from 
        sales join products on products.id = sales.pid group by(name);
    """)
    sales_per_product = cur.fetchall()
    return sales_per_product



    def get_sales_per_day():
        cur.execute("""
        select date(sales.created_at) as day , sum(sales.quantity * products.selling_price)as sales from 
        sales join products on products.id = sales.pid group by(date);
    """)
        sales_per_day = cur.fetchall()
        return sales_per_day


    def get_profit_per_product():
        cur.execute("""
        select products.name as p_name , sum(sales.quantity * products.selling_price)as sales from 
        sales join products on products.id = sales.pid group by p_name
    """)
    profit_per_product = cur.fetchall()
    return profit_per_product
    
    
  
    def get_profit_per_day():
        cur.execute("""
        select date(sales.created_at) as day , sum(sales.quantity * products.selling_price)as sales from 
        sales join products on products.id = sales.pid group by(date);
    """)
    profit_per_day = cur.fetchall()
    return profit_per_day




def available_stock(pid):
    cur.execute("select sum(stock.quantity) from stock where.pid = %s", (pid,))
    total_stock = cur.fetchone()[0]

    cur.execute("select sum(sales.quantity) from sales where pid = %s", (pid,))
    total_sold = cur.fetchone()[0]

    return total_stock - total_sold


def create_user(values):
    cur.execute("insert into users (full_name, email, password) values (%s,%s,%s)", values)
    conn.commit()  

def check_user(email):
    cur.execute("select * from users where email = %s", (email,))
    user = cur.fetchone()
    return user 

user = check_user('rahmo@mail.com')
print(user)
(1,'rahmo','rahmo@mail.com','0114594969','$')




    