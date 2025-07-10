import flet as ft
from funçõesDeUso import estudoClicado, casualClicado, arteClicado, valor_random, retorno

retorno.fechar = False


gatoEstudo = """


        ⠀⠀⠀⠀⡏⢢⡁⠂⠤⣀⣀⣀⣀⣀ ⠤⠐⢈⡔⢹
        ⠀⠀⠀⠀⢿⡀⠙⠆⠀⠉⠀人 ⠉⠀⠰⠋⢀⡿
        ⠀⠀⠀⠀⠈⢷⠄⠀⠀⠀⠀⠀-⠀⠀⠀⠀⠠⡾⠁
        ⠀⠀⠀⠀⠀⠀⡏⠀--⠀⠀⠀⠀⠀⠀--⠀⢹
        ⣰⠊⠉⠉⠉⡇⠀⠢⣤⣄⠀⠀ ⣠⣤⠔⠀⢸
        ⠙⠓⠒⢦⠀⠱⣄⠀⠀⠀⠀.⠀⠀⠀⠀⣠⠎
        ⠀⠀⠀⠀⡇⠀⠀⠏⠑⠒⠀⠉⠀⠒⠊⠹
        ⡎⠉⢹⠀⠙⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⡏⠉⢱
        ⢧⡈⠛⠉⠉⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠉⠉⠋⢁⡼
        ⠀⢉⣿⠖⠚⠛⢋⢀⠀⠀⠀⠀⠀⠀⠀⡀⡙⠛⠓⠲⣿⣄
        ⠀⢸⡇⠀⠀⠀⡞⠁⠈⡃⠀⠀⠀⠀⢘⠁⠈⢳⠀⠀⠀⢸⡇
        ⠀⠈⢷⣄⠀⠀⠙⠦⠌⠑⠢⠤⠔⠊⠁⢠⠎⠀⠀⣠⡾⠁
        ⠀⠀⠀⠈⠛⠲⠤⣤⣀⣀⣀⣀⣠⣤⣚⣡⠤⠖⠛⠁"""

gatoCasual = """


        ⠀⠀⠀⠀⡏⢢⡁⠂⠤⣀⣀⣀⣀⣀ ⠤⠐⢈⡔⢹
        ⠀⠀⠀⠀⢿⡀⠙⠆⠀⠉⠀ - ⠉⠀⠰⠋⢀⡿
        ⠀⠀⠀⠀⠈⢷⠄⠀--⠀⠀⠀⠀⠀⠀-- ⠠⡾⠁  Dia bão,
        ⠀⠀⠀⠀⠀⠀⡏⠀⠢⣿⣄⠀⠀ .⣿⠔⠀⠀⢹    hein?
        ⣰⠊⠉⠉⠉⡇⠀⠀⠀⠀_-_.⠀⠀⠀⠀ ⢸    /
        ⠙⠓⠒⢦⠀⠱⣄⠀⠀⠀⠀  ⠀⠀⠀⠀⣠⠎
        ⠀⠀⠀⠀⡇⠀⠀⠏⠑⠒⠀⠉⠀⠒⠊⠹ _
            ⡶⠃⠀⠘⢦⠀⠀⠀⠀_⠀⠀⠀  ⡶ ⠘⢦⠀
         :⡈⣄⠀⠉⠉⠋⢁⡼⠀⠀⠀⠀:⡈⠛⠉⠉⠀⠋⢁⡼
        ⠀⢉⣿⠖⠚⠛⢋⢀⠀⠀⠀⠀⠀⡀⡙⠛⠓⠲⣿⣄
        ⠀⢸⡇°°°o ⠈⡃⠀⠀⠀⠀  ⠈⢳⠀o°°°⢸⡇
        ⠀⠈⢷⣄⠀O⠀  : ⣀⣀人   ⢠O⠎  ⣠⡾⠁
        ⠀⠀⠀⠈⠛⠲⠤⡇          ⣡⠤⠖⠛⠁"""


# gatoArte = """


#         ⠀⠀⠀⠀⡏⢢⡁⠂⠤⣀⣀⣀⣀⣀ ⠤⠐⢈⡔⢹
#         ⠀⠀⠀⠀⢿⡀⠙⠆⠀⠉⠀ - ⠉⠀⠰⠋⢀⡿
#         ⠀⠀⠀⠀⠈⢷⠄⠀--⠀⠀ ⠀⠀--⠀ ⠠⡾⠁
#         ⠀⠀⠀⠀⠀⠀⡏⠀⠢⣿⣄⠀⠀ ⣿⠔⠀⠀⢹
#         ⣰⠊⠉⠉⠉⡇⠀   ,_-_. ⠀⠀ ⢸
#         ⠙⠓⠒⢦⠀⠱⣄⠀⠀⠀⠀  ⠀⠀⠀⠀⣠⠎
#         ⠀⠀⠀⠀⡇⠀⠀⠏⠑⠒⠀⠉⠀⠒⠊⠹
#             ⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠘⢦⠀      
#         :⡈⠛⠉⠉⠀⠀⣠           _.------.
#         ⢉⣿⠖⠚⠛⢋⢀           /  b a (__c>
#          ⡇°°°o ⠈⡃          ( c      " h \
#           ⢷⣄⠀O⠀  :          \ d e f g   /
#           ⠈⠛⠲⠤⡇    ⣀⣀人     `--.....-'"""

gatoArte = """



        ⠀⠀⠀⠀⡏⢢⡁⠂⠤⣀⣀⣀⣀⣀ ⠤⠐⢈⡔⢹
        ⠀⠀⠀⠀⢿⡀⠙⠆⠀⠉⠀ - ⠉⠀⠰⠋⢀⡿
        ⠀⠀⠀⠀⠈⢷⠄⠀--⠀⠀⠀⠀⠀⠀-- ⠠⡾⠁
        ⠀⠀⠀⠀⠀⠀⡏⠀⠢⣤⣄⠀⠀ .⣿⠔⠀⠀⢹
        ⣰⠊⠉⠉⠉⡇⠀⠀⠀⠀,_-_.⠀⠀⠀⠀ ⢸
        ⠙⠓⠒⢦⠀⠱⣄⠀⠀⠀⠀  ⠀⠀⠀⠀⣠⠎
        ⠀⠀⠀⠀⡇⠀⠀⠏⠑⠒⠀⠉⠀⠒⠊⠹    ,
             ⡶⠃⠀⠀⠀ ⠀⠀⠀ ⠀⠀⠀    ⠘⢦;;   
         :⡈⠛⠉⠉⠀⠀⣠ ⠀⠀          _.--//--.
         ⢉⣿⠖⠚⠛⢋⢀  ⠀⠀⠀   /  c// O⠀ (__
         ⡇°°°o ⠈⡃  ⠀⠀⠀     ( c//  ⠀⠀     " |
         ⢷⣄⠀O⠀  :  ⠀⠀⠀      \ ° o o O   / ⡾
         ⠈⠛⠲⠤⡇ -  ⣀⣀人 ⠀ /`.--.....-'⣡⠤⠖⠛⠁"""


TextoEstudo = "Escolha quando precisar de foco para estudar, seja para atividades teoricas ou práticas, para projetos pessoais ou não. "\
"Aqui serão desabilitados programas que possam te distrair, como jogos ou outras ferramentas de entretenimento.\n"+gatoEstudo

TextoCasual = "Nesse modo você pode mexer em todos os programas e aplicativos, sem limitações! "  \
"É ideal para momentos de lazer, ou quaisquer ocasiões que não exijam foco ou produtividade.\n"+gatoCasual

TextoArte = "Selecione essa opção para foco nos projetos artísticos. É semelhante ao modo de Estudo, mas focado nas aplicações de desenho.\n\n"+gatoArte

def main(page: ft.Page):

    #Parâmetros gerais da janela
    page.title = "Janela Bonita"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 600

    page.window.full_screen=True

    page.add(ft.Text("Bem-vindo!", size=80))
    page.add(ft.Text("Selecione um modo de inicialização:\n\n", size=30))

    #Estilo dos botões
    estilo = ft.ButtonStyle(
                color={
                    ft.ControlState.HOVERED: ft.Colors.with_opacity(1.0, "#d1e3f8"),
                    ft.ControlState.FOCUSED: ft.Colors.PINK,
                    ft.ControlState.DEFAULT: ft.Colors.with_opacity(1.0, "#a0cafd"),
                },
                bgcolor={ft.ControlState.FOCUSED: ft.Colors.PINK_200, "": ft.Colors.with_opacity(0.5, "#23272c"),
                         ft.ControlState.HOVERED: ft.Colors.with_opacity(0.5, "#171a1d"),
                         ft.ControlState.DEFAULT: ft.Colors.with_opacity(0.5, "#23272c")},
                padding={ft.ControlState.HOVERED: 20},
                overlay_color=ft.Colors.TRANSPARENT,
                elevation={"pressed": 0, "": 0},
                animation_duration=500,
                side={
                    ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.with_opacity(0.5, "#23272c")),
                    ft.ControlState.HOVERED: ft.BorderSide(2, ft.Colors.with_opacity(0.5, "#23272c"))
                },
                shape={
                    ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
                },

                
            )

    #Configiração dos botões
    botaoEstudo = ft.Container(
                    ft.ElevatedButton( 
                        width = 350, expand = True,
                        content= ft.Column ([ft.Text(value = "Estudo", size = 50)]), 
                        on_click= lambda e: (estudoClicado(e), page.window.destroy() if retorno.fechar else None),
                        tooltip="Foco, camarada!", 
                        style = estilo 
                        ), 
                    alignment=ft.Alignment(0, -1)
                    )

    botaoCasual = ft.Container(
                    ft.ElevatedButton( 
                        width = 350, expand = True,
                        content= ft.Column ([ft.Text(value = "Casual", size = 50)]), 
                        on_click=lambda e: (casualClicado(e), page.window.destroy() if retorno.fechar else None),
                        tooltip="Sem stress!", 
                        style = estilo 
                        ), 
                    alignment=ft.Alignment(0, -1)
                    )

    botaoArte = ft.Container(
                    ft.ElevatedButton( 
                        width = 350, expand = True,
                        content= ft.Column ([ft.Text(value = "Arte", size = 50)]), 
                        on_click=lambda e: (arteClicado(e), page.window.destroy() if retorno.fechar else None),
                        tooltip="Hora do projeto!", 
                        style = estilo 
                        )
                    )
    
    #Configuração das caixas de texto
    caixaEstudo = ft.Container(ft.Text(TextoEstudo, size = 15),
                    height = 500, margin = 20, padding = 20, width = 350, bgcolor=ft.Colors.with_opacity(0.5, "#23272c"))
        
    caixaCasual = ft.Container(ft.Text(TextoCasual, size = 15),
                     height = 500, margin = 20, padding = 20, width = 350, bgcolor=ft.Colors.with_opacity(0.5, "#23272c"))
    
    caixaArte= ft.Container(ft.Text(TextoArte, size = 15),
                    height = 500, margin = 20, padding = 20, width = 350, bgcolor=ft.Colors.with_opacity(0.5, "#23272c"))
                         

    #Organização dos botões e caixas de texto em colunas
    colunaEstudo = ft.Column(
        controls=[
            botaoEstudo,
            caixaEstudo
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    colunaCasual = ft.Column(
    controls=[
        botaoCasual,
        caixaCasual
    ],
    alignment=ft.MainAxisAlignment.START,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    colunaArte = ft.Column(
        controls=[botaoArte,
                  caixaArte
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    #Organização das colunas
    row_options = ft.Row(controls=[colunaEstudo, colunaCasual, colunaArte],
                        spacing=20, alignment=ft.MainAxisAlignment.CENTER)

    #Adição das colunas na página
    page.add(row_options)

    #Adição de uma frase aleatória
    page.add(ft.Text('\n\n'+valor_random(), size=15))

    
ft.app(main)