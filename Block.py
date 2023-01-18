import arcade

arcade.open_window(600,600, 'Block of Colors')
arcade.set_background_color(arcade.color.WHITE_SMOKE)
arcade.start_render()


space = 40
margin = 130
for row in range(10):
    for column in range(10):
        i = column * space + margin
        j = row * space + margin
        if row%2 == 1 and column%2 == 1 or row%2 == 0 and column%2 == 0:
            arcade.draw_rectangle_filled(i,j,20,20,arcade.color.RED,45)
        else:
            arcade.draw_rectangle_filled(i,j,20,20,arcade.color.BLUE,45)


arcade.finish_render()
arcade.run()