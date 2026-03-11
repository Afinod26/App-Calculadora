import json

# Factores tomados de la tabla del PDF
f48 = 111.22 / 3000
f72 = 90.39 / 3000
f96 = 79.97 / 3000
f120 = 73.72 / 3000

def redondear(valor):
    return round(valor + 1e-9, 2)

tabla = []
for monto in range(3000, 250001, 1000):
    tabla.append({
        "monto": monto,
        "plazos": {
            "48": redondear(monto * f48),
            "72": redondear(monto * f72),
            "96": redondear(monto * f96),
            "120": redondear(monto * f120)
        }
    })

financiera = {
    "id": "idfinanciero_salud_compra_deuda",
    "nombre": "ID Financiero",
    "convenio": ["salud_compra_deuda"],
    "estado": "puebla",
    "plazos_permitidos": [48, 72, 96, 120],
    "tabla": tabla,
    "reglas": {}
}

with open("idfinanciero_salud_compra_deuda.json", "w", encoding="utf-8") as f:
    json.dump({"financieras": [financiera]}, f, indent=2, ensure_ascii=False)

print("Archivo generado: idfinanciero_salud_compra_deuda.json")