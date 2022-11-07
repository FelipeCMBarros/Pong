import turtle # modulo turtle para fazer o pop up
import winsound # modulo que permite acesso ao seu sistema operacional para uso de audios

jan = turtle.Screen()
jan.title("Pong - Por Felipe Barros")
jan.bgcolor("black")
jan.setup(width = 800, height = 600)
jan.tracer(0)  # Impede a janela de atualizar

# definindo o pop up como "jan" e definindo suas propriedades, nesse caso, título, tamanho e cor do fundo.

#Pontuação:

score_a = 0
score_b = 0
# No pong, existem 3 objetos principais, Paddle A, Paddle B e a bola, seguem eles a seguir:

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()  # Impede o paddle de deixar um traço quando ele se move
paddle_a.goto(-350, 0)  # Localização do paddle em coordenadas x e y

# Paddle B (Igual ao A, apenas com coordenadas diferentes)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Bola (Retirado a função de esticar)
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
# Move a bola pela quantidade de pixels colocada, ou seja, define a velocidade
bola.dx = 0.09
bola.dy = 0.09

#Pen (Turtle)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Time New Roman", 24, "normal"))
# Controles são feitos com funções

def paddle_a_up():  # Descobre e manipula as coordenadas de y de acordo com o input do jogador
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():  # Descobre e manipula as coordenadas de y de acordo com o input do jogador
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():  # Descobre e manipula as coordenadas de y de acordo com o input do jogador
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():  # Descobre e manipula as coordenadas de y de acordo com o input do jogador
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
jan.listen()  # Faz com que a janela aceite um tipo de input
jan.onkeypress(paddle_a_up, "w")  # Chama a função se a tecla em questão for pressionada
jan.onkeypress(paddle_a_down, "s")
jan.onkeypress(paddle_b_up, "Up")
jan.onkeypress(paddle_b_down, "Down")

# Main game loop:
while True:
    jan.update()
    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Limite da tela
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1  # Inverte a direção
        winsound.PlaySound("wall_bounce", winsound.SND_ASYNC|winsound.SND_NODEFAULT)

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1  # Inverte a direção
        winsound.PlaySound("wall_bounce", winsound.SND_ASYNC|winsound.SND_NODEFAULT)

    if bola.xcor() > 390:
        bola.goto(0, 0)  # Reset na posição da bola para o centro ao marcar um ponto para o B
        bola.dx *= -1
        score_a = score_a + 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Time New Roman", 24, "normal"))
        winsound.PlaySound("point_bounce", winsound.SND_ASYNC|winsound.SND_NODEFAULT)

    if bola.xcor() < -390:
        bola.goto(0, 0)  # Reset na posição da bola para o centro ao marcar um ponto para o A
        bola.dx *= -1
        score_b = score_b +1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Time New Roman", 24, "normal"))
        winsound.PlaySound("point_bounce", winsound.SND_ASYNC|winsound.SND_NODEFAULT)

    # Colisão entre paddle A e bola via condicionais

    if bola.xcor() < -340 and bola.xcor() > -350 and (bola.ycor() < paddle_a.ycor() + 40 and bola.ycor() > paddle_a.ycor() - 50):
        bola.setx(-340)
        bola.dx *= -1
        winsound.PlaySound("paddle_bounce", winsound.SND_ASYNC|winsound.SND_NODEFAULT)
    # Colisão entre paddle B e bola via condicionais

    if bola.xcor() > 340 and bola.xcor() < 350 and (bola.ycor() < paddle_b.ycor() + 40 and bola.ycor() > paddle_b.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1
        winsound.PlaySound("paddle_bounce", winsound.SND_ASYNC|winsound.SND_NODEFAULT)