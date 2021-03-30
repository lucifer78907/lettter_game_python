from ltters import *

painter = lttrs()
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title("Letter Maker")
screen.listen()
screen.onkey(painter.letter_a, "a")
screen.onkey(painter.letter_b, "b")
screen.onkey(painter.letter_c, "c")
screen.onkey(painter.letter_d, "d")
screen.onkey(painter.letter_e, "e")
screen.onkey(painter.letter_f, "f")
screen.onkey(painter.letter_g, "g")
screen.onkey(painter.letter_h, "h")
screen.onkey(painter.letter_i, "i")
screen.onkey(painter.letter_j, "j")
screen.onkey(painter.letter_k, "k")
screen.onkey(painter.letter_l, "l")
screen.onkey(painter.letter_m, "m")
screen.onkey(painter.clear_scr, "0")
screen.exitonclick()
