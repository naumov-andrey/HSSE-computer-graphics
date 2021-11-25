# Курсовая работа

## Задание

Целью работы является визуализация динамических процессов, имитирующих
реальные.

Требуется при помощи стандартных функций библиотеки (OpenGL или DirectX)
изобразить указанные объекты, затем рассчитать и визуализировать передвижение
объекта, имитирующее реальное. Объекты должны быть текстурированы и
освещены одним или несколькими источниками света.

* Изобразить текстурированный икосаэдр, расположенный на плоскости.
* Реализовать освещение (один источник).
* Рассчитать и изобразить перекатывание икосаэдра по плоскости.

## Икосаэдр

В программе используется модель выпуклого правильного икосаэдра

20 граней, 30 ребер, 12 вершин\
Грани -- правильные треугольники

Возьмем длину ребра равную 1, тогда:\
Радиус вписанной сферы $\large r_i = \frac{1}{12} (3 \sqrt{3} + \sqrt{15})$\
Расстояние от центра до середины ребра $\large r_m = \frac{1}{4} (1 + \sqrt{5})$\
Радиус описанной сфера $\large R = \frac{1}{4} \sqrt{10 + 2 \sqrt{5}}$

Двугранный угол $\large \alpha = arccos(-\frac{\sqrt{5}}{3})$\
Угол между центрам фигуры до и после перекатывания $\large \beta = arccos(\frac{\sqrt{5}}{3})$

## Список использованных источников

1. Path planning for the Platonic solids on prescribed grids by edge-rolling [Электронный ресурс] URL: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0252613#pone-0252613-t002 (дата обращения 22.11.2021)