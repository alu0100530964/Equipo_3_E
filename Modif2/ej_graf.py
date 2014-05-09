#!usr/bin/python
#!encoding:UTF-8


import pylab as dibujo

x = [1,2,3,4]
y = [10,20,30,40]
y2 = [5,15,25,35]
y3 = [7,12,22,33]
y4 = [12,25,33,39]

p1 = dibujo.subplot(211)
dibujo.title ('Porcentajes de error')
dibujo.plot (x, y, marker='o', linestyle=':',color='r', label='Linea 1')  #':' '--' '_' . Los colores son 'r'  junto a m b g c y.    Los marker son 'o' junto a s p * + . ^
dibujo.plot (x, y2, marker='*', linestyle='--',color='b', label='Linea 2')
dibujo.plot (x, y3, marker='+', linestyle='-',color='g', label='Linea 3')
dibujo.legend()
dibujo.xlim(0, 6)
dibujo.xticks(x)

p2 = dibujo.subplot(212)
dibujo.plot (x, y4, marker='^', linestyle=':',color='c', label='Linea 4')
dibujo.xlabel ('Intervalos')
dibujo.ylabel ('Tiempo en segundos')

dibujo.legend()






dibujo.show()
