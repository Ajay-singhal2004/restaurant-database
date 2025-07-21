from guizero import App, Text, Picture
app = App("lord comander")
app.bg = "#FBFBD0"
wanted_text = Text(app, "lord comander")
wanted_text.text_size = 30
wanted_text.font = "Times New Roman"
cat = Picture(app, image="Screenshot 2025-03-14 143829.png")
app.display()