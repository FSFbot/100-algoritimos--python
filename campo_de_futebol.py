def calcular_campos_futebol(area_km2):
    area_m2 = area_km2 * 1000000
    area_campo_futebol = 105*68
    return area_m2 / area_campo_futebol

print(f'Area desmatada: {calcular_campos_futebol(1034):.2f} campos de futebol\n')
    