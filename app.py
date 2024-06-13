import flet as ft
from decimal import Decimal

output_types = [
    {'operator':'AC','color':ft.colors.BLACK,'background': ft.colors.BLUE_100},
    {'operator':'±','color':ft.colors.BLACK,'background': ft.colors.BLUE_100},
    {'operator':'%','color':ft.colors.BLACK,'background': ft.colors.BLUE_100},
    {'operator':'/','color':ft.colors.BLACK45,'background': ft.colors.YELLOW},
    {'operator':'7','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'8','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'9','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'*','color':ft.colors.BLACK45,'background': ft.colors.YELLOW},
    {'operator':'4','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'5','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'6','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'-','color':ft.colors.BLACK45,'background': ft.colors.YELLOW},
    {'operator':'1','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'2','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'3','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'+','color':ft.colors.BLACK45,'background': ft.colors.YELLOW},
    {'operator':'0','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'.','color':ft.colors.BLACK45,'background': ft.colors.GREY},
    {'operator':'=','color':ft.colors.BLACK45,'background': ft.colors.YELLOW},
]

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.title = "Calculator"
    page.window_resizable = False
    page.window_width = 275
    page.window_height = 390
    page.window_always_on_top = True
    
    result = ft.Text(value='0', color=ft.colors.WHITE, size=25)
    
    def calculate(operator, value_after):
        try:
            value = eval(value_after)
        
            if operator == '%':
                value /= 100
            elif operator == '±':
                value = -value
            
        except:
            return 'Error'
            
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')
    
    def select(e):
        value_after = result.value if result.value not in ('0','Error') else ''
        value = e.control.content.value
        
        if value.isdigit():
            value = value_after + value
        elif (value == 'AC'):
            value = '0'
        else:
            if value_after and value_after[-1] in ('/', '*', '-', '+', '.'):
                value_after = value_after[:-1]
                
            value = value_after + value
            
            if value[-1] in ('=','%','±'):
                value = calculate(operator=value[-1],value_after=value_after)
        
        result.value = value
        result.update()
        
    
    output = ft.Row(
        width=250,
        controls=[result],
        alignment='end'
    )
    
    button_input = [ft.Container(
        content=ft.Text(value=btn['operator'], color=btn['color']),
        width=50,
        height=50,
        bgcolor=btn['background'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
    ) for btn in output_types]
    
    keyboard = ft.Row(
        width=260,
        wrap=True,
        controls=button_input,
        alignment ='end'
    )
    
    page.add(output, keyboard) 

if __name__ == '__main__':
    ft.app(target=main)