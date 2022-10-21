"""Crear un programa usando decoradores para medir el tiempo de
ejecución"""

def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print("Antes de la ejecución de la función a decorar")
        result = funcion_b(*args, **kwargs)
        print("Después de la ejecución de la función a decorar")
        return result
    return funcion_c

@funcion_a
def division(a, b):
    return a / b
decorador = funcion_a(division)
decorador(10, 20)

def measure_time(function):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        result = function(*args, **kwargs)
        total = time.time() - start
        print("El tiempo en segundos que demora la operación es: {}".format(total))
        return result

    return wrapper

@measure_time
def division(a, b):
    import time
    time.sleep(1)
    return a / b

print("El resultado de la división de los números es: {}".format(division(100, 50)))