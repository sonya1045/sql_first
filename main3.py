import sqlite3

db = sqlite3.connect('shop.db')

db.execute('''CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(63),
        price FLOAT)''')

db.execute('''CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity INTEGER,
        customer_id INTEGER)''')


return_info_list = db.execute('''SELECT name, SUM(price) FROM products 
        INNER JOIN orders ON orders.product_id = products.product_id
        WHERE orders.quantity > 10
        GROUP BY orders.quantity
''')

for info in return_info_list:
    print(info)
