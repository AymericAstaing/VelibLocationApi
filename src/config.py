
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'sql4415733'
app.config['MYSQL_DATABASE_PASSWORD'] = 'abQQKVZzcU'
app.config['MYSQL_DATABASE_DB'] = 'sql4415733'
app.config['MYSQL_DATABASE_HOST'] = 'sql4.freemysqlhosting.net'
mysql.init_app(app)