largura = float(input('Largura da parede'))
altura = float(input('Altura  da parede'))
área = largura*altura
print('Sua parede tem a dimenção de{} x {} e sua área é de {}m quadrados;' .format(largura,altura,largura*altura))
print('Para pintar essa parede, você precisa de {}L de tinta' .format(área/2))
