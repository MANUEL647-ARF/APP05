import flet as ft
from abc import update_abstractmethods

def cal_suma(txtnum1,txtnum2,lblresultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        resultado=num1+num2
        lblresultado,value=f"Resultado: {resultado}"
    except ValueError:
        lblresultado,value="Error ingresa valores correctos"
        
def cal_resta(txtnum1,txtnum2,lblresultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        resultado=num1-num2
        lblresultado,value=f"Resultado: {resultado}"
    except ValueError:
        lblresultado,value="Error ingresa valores correctos"
        
def cal_multiplicacion(txtnum1,txtnum2,lblresultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        resultado=num1*num2
        lblresultado,value=f"Resultado: {resultado}"
    except ValueError:
        lblresultado,value="Error ingresa valores correctos"
        
def cal_division(txtnum1,txtnum2,lblresultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        resultado=num1/num2
        lblResultado,value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado,values="Error ingresa valores correctos"
    except ZeroDivisionError:
        lblResultado,value="Error división por cero" 


def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor="green"
    
    txtnum1=ft.TextField(label="Ingresa el primer número",color="yellow")
    txtnum2=ft.TextField(label="Ingresa el segundo número",color="yellow")
    lblresultado=ft.Text("Resultado: ",color="yellow")
    
    
    def on_cal_suma(e):
        cal_suma(txtnum1, txtnum2, lblresultado)
    page.update()

    def on_cal_resta(e):
        cal_resta(txtnum1, txtnum2, lblresultado)
    page.update()

    def on_cal_multiplicacion(e):
        cal_multiplicacion(txtnum1, txtnum2, lblresultado)
    page.update()
        

    def on_cal_division(e):
        cal_division(txtnum1, txtnum2, lblresultado)
    page.update()

    def limpiar(e):
        txtnum1.value=""
        txtnum2.value=""
        lblresultado.value="Rresultado: "
        page.update()

    btnsuma=ft.ElevatedButton(text="+",on_click=on_cal_suma)
    btnresta=ft.ElevatedButton(text="-",on_click=on_cal_resta)
    btnmultiplicacion=ft.ElevatedButton(text="*",on_click=on_cal_multiplicacion)
    btndivision=ft.ElevatedButton(text="/",on_click=on_cal_division)
    btnlimpiar=ft.ElevatedButton(text="limpiar",on_click=limpiar)

    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtnum1,
                txtnum2
            ],alignment="center"),
        ]),
        ft.Row(controls=[lblresultado],alignment="center"),
        ft.Row(controls=[
            btnsuma,
            btnresta,
            btnmultiplicacion,
            btndivision
        ],alignment="center")
    )
    


ft.app(main)
