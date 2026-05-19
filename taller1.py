galones = float(input())

# caso especial para evitar la division por cero
if galones == 0:
    print("No data provided.")
else:
    total_km = 0
    total_galones = 0
    mejor = 0
    contador = 0
    contador_90 = 0

    while galones != 0:
        km = float(input())

        # validación para determinar el octanaje
        octanaje = int(input())
        while octanaje < 81 or octanaje > 98:
            print("OCTANAJE INVALIDO")
            octanaje = int(input())

        # aqui calculamos el rendimiento para cada entrada, dividiendo los km por los galones
        rendimiento = km / galones

        # estos son los acumuladores para el total de km, galones y el contador de entradas
        total_km += km
        total_galones += galones
        contador += 1

        if rendimiento > mejor:
            mejor = rendimiento

        if octanaje >= 90:
            contador_90 += 1

        # saquita la siguiente entrada de galones para el proximo ciclo
        galones = float(input())

    # con estos calculos obtenemos el promedio de rendimiento y el porcentaje de entradas con octanaje 90 o mas
    avg = total_km / total_galones
    extra = (contador_90 / contador) * 100

    # aqui imprimimos los resultados finales
    print(f"AVG: {avg}")
    print(f"BEST: {mejor}")
    print(f"EXTRA:{extra}")
