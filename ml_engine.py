def predict_intrusion(data):
    #Simula detección de intrusión segun patrones simples.
    #data: string con dirección IP o trafico simulado.
    #Retorna: "Intrusion detectada" o "Trafico normal"

    # Limpiamos espacios
    data = data.strip()
    # Lista de IPs sospechosas
    suspicious_ips = ["192.168.1.50", "10.0.0.99", "172.16.0.5"]
    # Lista de patrones de trafico sospechoso
    suspicious_patterns = ["malware", "scan", "ddos"]
    if data in suspicious_ips:
        return "Intrusión detectada"
    for pattern in suspicious_patterns:
        if pattern.lower() in data.lower():
            return "Intrusión detectada"
    return "Tráfico normal"
