import arcade

#crea una nueva ventana
arcade.open_window(800, 600, "Prueba")

#color de fondo
arcade.set_background_color(arcade.color.ANDROID_GREEN)
#
############
arcade.start_render()

#CAMPO DE FUTBOL

#porterias
arcade.draw_lrtb_rectangle_outline(10, 75, 340, 240, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_outline(715, 790, 340, 240, arcade.color.WHITE)

#areas de las porterias
arcade.draw_ellipse_outline(0, 290, 400, 370, arcade.color.WHITE)
arcade.draw_ellipse_outline(800, 290, 400, 370, arcade.color.WHITE)

#limites del campo
arcade.draw_lrtb_rectangle_outline(10, 790, 590, 10, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(390, 390, 590, 10, arcade.color.WHITE)

#centro del campo
arcade.draw_circle_outline(390, 290, 50, arcade.color.WHITE)



arcade.finish_render()
############


#mantiene la ventana abierta
arcade.run()