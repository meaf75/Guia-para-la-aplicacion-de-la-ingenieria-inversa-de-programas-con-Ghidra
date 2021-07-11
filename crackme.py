CLAVE_DEL_PROGRAMA_MALIGNO : str = "estaEsLaClaveDeSeguridadParaDetenerLaEjecucion";

# Pilo la clave por medio de una entrada de consola
print("Ingrese Contraseña: ", end="");
textoIngresado : str = input();

if(textoIngresado != CLAVE_DEL_PROGRAMA_MALIGNO):
    # La clave ingresada por el usuario no es valida, detener ejecucion
    print("Clave invalida")
    exit();

# Todo está bien, continuar
print("Clave valida, deteniendo ejecucion")
