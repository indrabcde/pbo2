import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='registrasi'
    )

    if connection.is_connected():
        print('Berhasil terhubung ke database MySQL')

except mysql.connector.Error as err:
    print(f'Error: {err}')

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('Koneksi ditutup')