import json

# Factores tomados de la tabla original
f48 = 106.00 / 3000
f72 = 85.17 / 3000
f96 = 74.75 / 3000

def redondear(valor):
    return round(valor + 1e-9, 2)

tabla = []

for monto in range(3000, 200001, 100):
    tabla.append({
        "monto": monto,
        "plazos": {
            "48": redondear(monto * f48),
            "72": redondear(monto * f72),
            "96": redondear(monto * f96)
        }
    })

financiera = {
    "financieras": [
        {
            "id": "credifiel_gob",
            "nombre": "Credifiel",
            "convenio": ["gobierno"],
            "estado": "puebla",
            "plazos_permitidos": [48, 72, 96],
            "tabla": tabla,
            "reglas": {}
        }
    ]
}

with open("credifiel_gob.json", "w", encoding="utf-8") as f:
    json.dump(financiera, f, indent=2, ensure_ascii=False)

print("Archivo 'credifiel_gob.json' generado con éxito.")