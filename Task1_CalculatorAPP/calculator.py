import flet 
from flet import *

def main(page:Page):
    #! Arithmetic functions

    def add(e):
            result.content.value = f"Result = {int(num1.content.value)+int(num2.content.value)}"
            result.visible = True
            page.update()

    def subtract(e):
            result.content.value = f"Result = {int(num1.content.value)-int(num2.content.value)}"
            result.visible = True
            page.update()

    def multiply(e):
            result.content.value = f"Result = {int(num1.content.value)*int(num2.content.value)}"
            result.visible = True
            page.update()

    def divide(e):
            try:
                result.content.value = f"Result ={int(num1.content.value)/int(num2.content.value)}"
                result.visible = True
                page.update()
            except:
                result.content.value = "Error"
                result.visible = True
                page.update()

    page.title = "Calculator"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.window_maximizable = False
    page.window_height = 600
    page.window_width = 00
    page.window_max_height=600
    page.window_max_width = 400
    page.window_min_width=400
    page.window_min_height = 600

      #! Header of the page
    headline = Text(value="Calculator",
                   font_family="Roboto",size=30,
                   text_align="center",
                   weight="bold"
                   
                   )
    page.add(headline)

    #! Input number 1 from the user

    num1 = Container(
            content=TextField(
                  label = "Enter number 1",
                  border_radius=20,
            ),
            padding = 20
      )
    #! Input number 2 from the user
    num2 = Container(
            content=TextField(
                  label = "Enter number 1",
                  border_radius=20,
            ),
            padding = 20
      )
    
    #! showing various arithmetic functions
    function_button = Row(
            controls=[Container(
                content = ElevatedButton(
                text = "+",
                bgcolor="blue",
                color = "white",
                on_click=add
                )),
                Container(
                content = ElevatedButton(
                text = "-",
                bgcolor="blue",
                color = "white",
                on_click=subtract
                ),
            
            ),
            Container(
                content = ElevatedButton(
                text = "x",
                bgcolor="blue",
                color = "white",
                on_click=multiply
                ),
            
            ),
            Container(
                content = ElevatedButton(
                text = "/",
                bgcolor="blue",
                color = "white",
                on_click=divide
                ),
            
            )],
            alignment="center"
      )
    #! printing the result
    result = Container(
                  content = Text(
                        value="Nil",
                        color = "white",
                        text_align="center",
                        selectable= True,
                        size= 20,
                  
            ),
            padding=20,
            visible=False,
            bgcolor="blue",
            margin=20,
            border_radius=20
      )
    #! managing all the container in one single column
    column = Column(
            controls = [
                  num1, num2,function_button,result
            ],horizontal_alignment="center"
           
      )
    page.add(column)


flet.app(target=main)