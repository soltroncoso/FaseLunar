from faseLunar.faselunar import FaseLunar

# Instancia un objeto de la clase FaseLunar

f = FaseLunar(19, 3, 1992)

# llama al método calcular fase de la luna
print(f.calcular_fase())

# llama al método calcular luz de la fase lunar
print(f.obtener_luz())

# llama al método emoji luna que muestra un emoji con la fase de la luna
f.emoji_luna()
