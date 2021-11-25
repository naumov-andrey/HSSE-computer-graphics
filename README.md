# Компьютерная графика

## Лаб. работа 1

### Задание

1. Изобразить каркасный конус высотой 25, основание конуса - окружность с радиусом 5
и центром в точке O (10,10), и каркасную сферу радиусом 5 и центром в точке O
(20,20).

2. Совместить центр основания конуса и центр сферы.

3. Изобразить тор и цилиндр. Размеры и местоположение примитивов задать
самостоятельно.

4. Промасштабировать тор с коэффициентом 1.5, повернуть цилиндр на alpha = 90 градусов вокруг оси
Z относительно начала координат.

## Лаб. работа 2

### Задание

Требуется разработать программу, изображающую заданный набор из трех предметов
с указанными свойствами материалов и параметры источника освещения. При этом в
качестве базового набора объектов выступают 3D примитивы, указанные в вашем варианте
задания №1. Следует наделить один из объектов свойствами прозрачности (значение
параметра должно быть от 0,9 до 0,5). Другой выбранный объект должен имитировать
отполированную поверхность (shininess, значение указывается максимальным). В качестве
такого объекта следует выбирать примитивы с выпуклыми поверхностями, например -
цилиндр, тор, конус, сферу, чайник. Третий объект должен быть диффузно-рассеивающим,
матовым
В сцене обязательно должен быть как минимум один источник освещения, с
возможностью менять его параметры: местоположение, интенсивность, цвет
освещения.
Окончательный этап – текстурирование одного из объектов. Возможно при этом
также использовать микроискажение нормалей при помощи bump-mapping

## Лаб. работа 3

### Задание

Цель задания - отобразить изменение формы объекта, т.е. осуществить преобразование
одного трехмерного объекта в другой. Изменение должно быть плавным, пошаговым,
предусмотреть не менее 8 шагов морфирования. Задание выполняется при помощи
библиотек OpenGL или DirectX
Объекты должны изображать узнаваемые предметы, однако могут при этом быть
комбинацией примитивных форм. В сцену должен быть включен источник освещения.
Материалы объектов, определяющие отражение света поверхностью объекта, требуется
задать самостоятельно. 

## Курсовая работа

### Задание

Целью работы является визуализация динамических процессов, имитирующих
реальные.

Требуется при помощи стандартных функций библиотеки (OpenGL или DirectX)
изобразить указанные объекты, затем рассчитать и визуализировать передвижение
объекта, имитирующее реальное. Объекты должны быть текстурированы и
освещены одним или несколькими источниками света.

* Изобразить текстурированный икосаэдр, расположенный на плоскости.
* Реализовать освещение (один источник).
* Рассчитать и изобразить перекатывание икосаэдра по плоскости.
