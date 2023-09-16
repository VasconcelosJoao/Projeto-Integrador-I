import sqlite3
from datetime import datetime
import serial

# Conectar ao banco de dados SQLite (criará o arquivo se não existir)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Criar a tabela se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS measurements (
        id INTEGER PRIMARY KEY,
        temperature REAL,
        humidity REAL,
        timestamp TIMESTAMP
    )
''')

# Definir a data predefinida para interromper o loop
targetDate = datetime(2023, 9, 10, 10, 0, 0)

# Iniciar comunicação serial com o Arduino
try:
    arduino = serial.Serial('/dev/ttyACM0', 9600)
except serial.SerialException as e:
    print("Error opening serial port:", e)
    exit(1)

try:
    while datetime.now() < targetDate:
        # Ler os valores do Arduino
        data = arduino.readline().decode('utf-8').strip().split()
        if len(data) == 2:
            t, h = float(data[0]), float(data[1])
            timestamp = datetime.now()

            # Inserir os valores na tabela do banco de dados
            cursor.execute('INSERT INTO measurements (temperature, humidity, timestamp) VALUES (?, ?, ?)', (t, h, timestamp))
            conn.commit()

            print(f"Temperature: {t}°C, Humidity: {h}%, Timestamp: {timestamp}")

except KeyboardInterrupt:
    pass
finally:
    arduino.close()
    conn.close()
