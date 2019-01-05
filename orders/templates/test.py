import psycopg2
  



conn=psycopg2.connect(database='lyl_orders',user='freedmj',password='13279131790',host='47.75.115.19',port='5432')
cur=conn.cursor()
cur.execute("select * from orders where created_at between 1543974678 and 1543974709")
rows=cur.fetchall()
print(rows)
conn.commit()
cur.close()
conn.close()