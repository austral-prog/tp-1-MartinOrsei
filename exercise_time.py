def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    minutos = (total_segundos // 60)
    hora = (minutos // 60)
    minutos_total = minutos // 60
    segundos_total = total_segundos - minutos_total * 60 - (hora * 60) * 60
    print(hora)
    print(minutos_total)
    print(segundos_total)
