import psycopg2


conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='ramo',dbname='myduka_db')

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

cur.execute("insert into products(name,buying_price,selling_price)values('bread', 50, 60)")
conn.commit()
print(products)

product1 = ('sumsung',20000,30000)
product2 = ('hp',30000,40000)


def insert_products(product):
    cursor.execute("insert into products (name,cost,price)values(milk,sugar,mango)",products)
    conn.commit()


def get_sales_per_product():
    cur.execute("""
        select products.name as name , sum(sales.quantity * products.selling_price)as sales from 
        sales join products on products.id = sales.pid group by(name);
    """)
    sales_per_product = get_sales_per_product()
    print(sales_per_product)



    def get_sales_per_day():
        cur.execute("""
        select products.name as name , sum(sales.quantity * products.selling_price)as sales from 
        sales join products on products.id = sales.pid group by(name);
    """)
    sales_per_day = get_sales_per_day()
    print(sales_per_day)



    def get_profit_per_product():
        cur.execute("""
        select products.name as p_name , sum(sales.quantity * products.selling_price)as sales from 
        sales join products on products.id = sales.pid group by p_name
    """)
    get_profit_per_day
    print(get_sales_per_product)
    
    
  
    def get_profit_per_day():
        cur.execute("""
        select date(sales.created_at) as day , sum(sales.quantity * products.selling_price)as sales from 
        sales join products on products.id = sales.pid group by(date);
    """)
    get_profit_per_day
    print(get_sales_per_day)

    