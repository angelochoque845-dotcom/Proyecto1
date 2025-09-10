from models import Alerta, db

db.connect()
db.create_tables([Alerta])

Alerta.create(tipo="Port Scan", host="192.168.1.10", severidad=2)
Alerta.create(tipo="DDoS", host="192.168.1.20", severidad=3)
Alerta.create(tipo="SQL Injection", host="192.168.1.30", severidad=5)

print("✅ Alertas insertadas en la BD")