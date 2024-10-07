import tiempo as t
import Masa as m
import Temperatura as tem

def menu_masa():    
    menu_num = int(input("Hola! Bienvenido al menu de conversor de masa, seleccione 1 para comenzar: "))
    x = 1
    if menu_num == 1:
        
        try:
            while x <= 1:
                    print("---------------MENU MASA----------------")
                    print("1) Kilos a Gramos")
                    print("2) Kilos a Toneladas")
                    print("3) Gramos a Kilos")
                    print("4) Gramos a Toneladas")
                    print("5) Toneladas a Kilos")
                    print("6) Toneladas a Gramos")
                    print("7) Volver")
                    print("8) Salir")
                    op = input("Seleccione una opción: ")
                    print("-----------------------------------")
                    print("-----------------------------------")

                    if op == "1":
                        sm = int(input("Ingrese los Kilos: "))
                        m.Kilo_Gram(sm)
                        chao = int(input("Si quiere volver [1], si deseacambiar de c cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_masa()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "2":
                        sh = int(input("Ingrese los Kilos: "))
                        m.Kilo_Ton(sh)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_masa()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "3":
                        ms = int(input("Ingrese los Gramos: "))
                        m.Gram_Kilo(ms)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_masa()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "4":
                        mh = int(input("Ingrese los Gramos: "))
                        m.Gram_Ton(mh)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_masa()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "5":
                        hs = int(input("Ingrese las Toneladas: "))
                        m.Ton_Kilo(hs)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_masa()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "6":
                        hm = int(input("Ingrese las Toneladas: "))
                        m.Ton_Gram(hm)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_masa()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "7":
                        ele_men()
                        break

                        
                    elif op == "8":
                            print("Hasta luego.")
                            x = x + 1
                    else:
                        print("Opción no valida.")
        except ValueError:
            print(input("Ingrese un valor valido: "))
            
def menu_temperatura():    
    menu_num = int(input("Hola! Bienvenido al menu de conversor de temperatura, seleccione 1 para comenzar: "))
    x = 1
    if menu_num == 1:
        
        try:
            while x <= 1:
                    print("---------------MENU TEMPERATURA----------------")
                    print("1) Celsius a Fahrenheit")
                    print("2) Celsius a Kelvin")
                    print("3) Fahrenheit a Celsius")
                    print("4) Fahrenheit a Kelvin")
                    print("5) Kelvin a Celsius")
                    print("6) Kelvin a Fahrenheit")
                    print("7) Volver")
                    print("8) Salir")
                    op = input("Seleccione una opción: ")
                    print("-----------------------------------")
                    print("-----------------------------------")

                    if op == "1":
                        sm = int(input("Ingrese los grados Celsius: "))
                        tem.celsius_fah(sm)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "2":
                        sh = int(input("Ingrese los grados Celsius: "))
                        tem.celsius_kel(sh)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "3":
                        ms = int(input("Ingrese los grados Fahrenheit: "))
                        tem.fahrenheit_cel(ms)
                        chao = int(input("Si quiere volver [1], si desea retirarse [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "4":
                        mh = int(input("Ingrese los grados Fahrenheit: "))
                        tem.fahrenheit_kel(mh)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "5":
                        hs = int(input("Ingrese los grados Kelvin: "))
                        tem.kelvin_cel(hs)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "6":
                        hm = int(input("Ingrese los grados Kelvin: "))
                        tem.kelvin_fah(hm)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "7":
                        ele_men()
                        break

                        
                    elif op == "8":
                            print("Hasta luego.")
                            x = x + 1
                    else:
                        print("Opción no valida.")
        except ValueError:
            print(input("Ingrese un valor valido: "))

def menu_tiempo():    
    menu_num = int(input("Hola! Bienvenido al menu de conversor de tiempo, seleccione 1 para comenzar: "))
    x = 1
    
    if menu_num == 1:
    
        try:
            while x <= 1:
                    print("---------------MENU TIEMPO----------------")
                    print("1) Segundos a minutos")
                    print("2) Segundos a horas")
                    print("3) Minutos a segundos")
                    print("4) Minutos a horas")
                    print("5) Horas a segundos")
                    print("6) Horas a minutos")
                    print("7) Volver")
                    print("8) Salir")
                    op = input("Seleccione una opción: ")
                    print("-----------------------------------")
                    print("-----------------------------------")

                    if op == "1":
                        sm = int(input("Ingrese los segundos: "))
                        t.seg_min(sm)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "2":
                        sh = int(input("Ingrese los segundos: "))
                        t.seg_hor(sh)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "3":
                        ms = int(input("Ingrese los minutos: "))
                        t.min_seg(ms)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men()
                            x = x + 1
                            
                    elif op == "4":
                        mh = int(input("Ingrese los minutos: "))
                        t.min_hor(mh)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "5":
                        hs = int(input("Ingrese las horas: "))
                        t.hor_seg(hs)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "6":
                        hm = int(input("Ingrese las horas: "))
                        t.hor_min(hm)
                        chao = int(input("Si quiere volver [1], si desea cambiar de convertidor [2]: "))
                        if chao == 1:
                            menu_tiempo()
                        elif chao == 2:
                            print("Hasta luego.")
                            ele_men2()
                            x = x + 1
                            
                    elif op == "7":
                        ele_men()
                        break

                        
                    elif op == "8":
                            print("Hasta luego.")
                            x = x + 1
                    else:
                        print("Opción no valida.")
        except ValueError:
            print(input("Ingrese un valor valido: "))

def ele_men():
    elegir = int(input("Escoja su convertidor, temperatura[1], masa[2] o tiempo[3]: "))
    try:
        if elegir == 3:
            menu_tiempo()
        elif elegir == 2:
            menu_masa()
            p = 0
        elif elegir == 1:
            menu_temperatura()
            
    except ValueError:
        print('ingrese num')

def ele_men2():
    elegir = int(input("Escoja su convertidor, temperatura[1], masa[2] o tiempo[3] o desea salir [4]: "))
    try:
        if elegir == 3:
            menu_tiempo()
        elif elegir == 2:
            menu_masa()
            p = 0
        elif elegir == 1:
            menu_temperatura()
        elif elegir == 4:
            print("Hasta la proxima.")
            exit()
            
    except ValueError:
        print('ingrese num')

ele_men()

