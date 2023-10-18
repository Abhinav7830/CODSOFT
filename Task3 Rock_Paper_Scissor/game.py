import flet as ft
import random

USER_PNG = ["rock.png","paper.png","scissor.png"]
COMPUTER_PNG = ["user_rock.png","user_paper.png","user_scissor.png"]


def main(page:ft.Page):
    page.bgcolor = "red"
    page.title = "Rock Paper Scissor"
    page.horizontal_alignment = "center"
    page.fonts = {
        "super_deset":"Super Dessert.ttf"
    }
    page.window_height = 800
    page.window_width = 1000

    page.window_max_height =800
    page.window_max_width=1000

    page.window_min_height=800
    page.window_min_width =100

    page.window_resizable = False
    page.padding=40
    
    global computer_score,user_score
    computer_score = 0
    user_score = 0

    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            computer_score+=0
            user_score+=0

        elif ((user_choice == 0 and computer_choice == 2)
            or (user_choice == 1 and computer_choice == 0)
            or (user_choice == 2 and computer_choice == 1)
        ):
            
            user_score+=1

        else:
           
            computer_score+=1

        score.content.controls[0].update()
        print(score.content.controls[0].text)
        score.content.controls[1].update()
        
            
        
    def get_input(result,value):
        print(f"User's Choice :{USER_PNG[value]}")
        computer_choice = random.randint(0,2)
        print(f"Computer's Choice :{COMPUTER_PNG[computer_choice]}")

        image.controls[1].src = COMPUTER_PNG[computer_choice]
        image.controls[1].visible = True
    
        image.controls[0].src = USER_PNG[value] 
        image.controls[0].visible = True
        page.update()

        determine_winner(value,computer_choice)
        

    audio1 = ft.Audio(
        src="bck_music.mp3", autoplay=True
    )
    page.overlay.append(audio1)
        

    page.add(ft.Text(value="Rock Paper Scissor",color="white",font_family="super_deset",size=50))
    page.add(
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("User",size=20,color="white",weight=500),
                    ft.Text("Computer",size=20,color="white",weight=500)
                ]
                ,alignment="center",
                spacing=300
            ),padding=30
        )
    )
    score =  ft.Container(
            content=ft.Row(
                controls=[
                    ft.ElevatedButton(text=f"{user_score}",bgcolor="blue",width=80,height=80,color="white"),
                    ft.ElevatedButton(text=f"{computer_score}",bgcolor="blue",width=80,height=80,color="white")
                ]
                ,alignment="center",
                spacing=300
            ),padding=15
        )
    page.add(score)
    
    image = ft.Row(
        controls = [
            ft.Image(
                src="paper.png",
                width=200,
                height=200,
                visible=False,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(200)),

            ft.Image(
                src="rock.png",
                width=200,
                height=200,
                visible= False,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(200))
        ],alignment="center",
                spacing=200
    )
    page.add(image)

    rock_button = ft.Container(
        content=ft.Row(
            controls = [
                ft.ElevatedButton("Rock",bgcolor="blue",width=150,height=70,color="white",on_click=lambda x:get_input("rock",0)),
                ft.ElevatedButton("Paper",bgcolor="blue",width=150,height=70,color="white",on_click=lambda x:get_input("paper",1)),
                ft.ElevatedButton("Scissor",bgcolor="blue",width=150,height=70,color="white",on_click=lambda x:get_input("scissor",2))
            ],alignment="right"
        ),margin=40
    )
    page.add(rock_button)


ft.app(target= main)