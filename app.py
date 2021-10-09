from flask import Flask, render_template, request, redirect, url_for
#untuk MySQL pake dibawah ini
from flask_mysqldb import MySQL
from flask_ngrok import run_with_ngrok

#untuk postgreSQL pake dibawah ini
'''
import psycopg2
import psycopg2.extras
'''

app =  Flask(__name__)

'''jalanin ngeroknya pake ini'''
#run_with_ngrok(app)

#setingan MySQL

app.config['SECRET_KEY'] = '$KKEJHI3NNOI'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_senangbantu'
mysql = MySQL(app)


#setingan postgreSQL
'''
app.SECRET_KEY = "$KKEJHI3NNOI"
DB_HOST = "localhost"
DB_NAME = "db_senangbantu"
DB_USER = "postgres"
DB_PASS = "123"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
'''


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * , datediff(tanggal_akhir_ajakan,CURRENT_DATE()) as sisa_hari FROM `tb_ajakan`")
    data1 = cur.fetchall()

    cur.execute("SELECT * , datediff(tanggal_akhir_ajakan,CURRENT_DATE()) as sisa_hari FROM `tb_ajakan` ORDER BY `status_ajakan` LIMIT 3")
    data2 = cur.fetchall()
    cur.close()
    return render_template('home.html', ajakan=data1, datateratas=data2)


if __name__ == '__main__':
    app.run(debug=True)
    ''' dan ini juga dijalankan '''
    #app.run()