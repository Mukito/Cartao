from flet import *
import flet 

bgcolor = "#100b36"

class Card(UserControl):
    def build(self):
        return Container(
            Column([  # Usando uma coluna para empilhar os itens do cartão
                Container(
                    Image(src='assets/visa.png'),    
                    width=90,
                    margin=margin.only(250)
                ),
                Container(
                    Image(src='assets/chip5.png'),    
                    width=50,
                    margin=margin.only(20),
                    opacity=0.5
                ),
                Container(
                    Text(
                        "5784 1908 9371 7139",  # Número do cartão
                        color='white',
                        size=20,
                        weight='w500',
                    ),
                    margin=margin.only(20)
                ),
                Container(
                    Row([  # Colocando o nome e a data abaixo do número do cartão
                        Container(
                            Text(
                                "Fabiano Santos",  # Nome do titular
                                color='white',
                                size=18,
                                weight='w500',
                            ),
                            alignment=alignment.center_left,  # Nome à esquerda
                            margin=margin.only(left=20),
                        ),
                        Container(
                            Text(
                                "12/28",  # Data de validade
                                color='white',
                                size=18,
                                text_align='right',
                            ),
                            alignment=alignment.center_left,  # Alinha a data à esquerda, ao lado do nome
                            margin=margin.only(left=10),
                        ),
                    ], alignment="start", spacing=5),  # Coloca os itens à esquerda e reduz o espaçamento
                ),  
            ], spacing=0),
            width=376,
            height=232,
            top=100,
            left=100,
            bgcolor='#120f4f4f4',
            border_radius=12,
            blur=Blur(10, 10, BlurTileMode.REPEATED),
            shadow=BoxShadow(
                1,
                15,
                colors.BLUE_GREY_300,
                Offset(2, 2),
                ShadowBlurStyle.OUTER
            )
        )

class BackCircle(UserControl):
    def __init__(self, top, left, size):
        super().__init__()
        self.top = top
        self.left = left
        self.size = size
        self.bg = LinearGradient(
            colors=['#2fb8c5', "#284584"],
            begin=alignment.bottom_left,
            end=alignment.top_right,
        )

    def build(self):
        return Container(
            width=self.size,
            height=self.size,
            gradient=self.bg,
            border_radius=360,
            top=self.top,
            left=self.left
        )


body = Container(
    Stack([
        BackCircle(90, 180, 170),
        BackCircle(20, 20, 180),
        BackCircle(130, 20, 100),
        Card(),
    ]),
    width=576,
    height=432,
    bgcolor=bgcolor,
)


def manage(page: Page):
    page.window_min_width = 576
    page.window_min_height = 432
    page.window_max_width = 576
    page.window_max_height = 432

    page.window_width = 576
    page.window_height = 432

    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.padding = 0
    page.title = "Card Design"
    
    page.add(body)

flet.app(manage)
