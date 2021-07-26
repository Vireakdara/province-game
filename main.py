import turtle
import pandas

screen = turtle.Screen()
screen.title("Cambodia Province Game")
img = "map.gif"
screen.addshape(img)
turtle.shape(img)
guessing = []

while len(guessing) < 25:

    guess_province = turtle.textinput(f"{len(guessing)}/25 Provinces", "What's another province name ?")
    title_guess_province = guess_province.title()
    data = pandas.read_csv("25_provinces.csv")
    all_provinces = data["provinces"].to_list()

    if title_guess_province == "Exit":
        break
    if title_guess_province in all_provinces:
        guessing.append(title_guess_province)
        print("working")
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        data_province = data[data.provinces == title_guess_province]
        print(data_province)
        t.goto(float(data_province.x), float(data_province.y))
        t.write(data_province.provinces.item(), align="center", font=("Arial", 8, "bold"))

# print(all_provinces)

screen.exitonclick()
