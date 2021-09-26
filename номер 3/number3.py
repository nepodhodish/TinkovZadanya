import numpy as np
import plotly.graph_objects as go









#Диапазон по x и по y для поиска экстремума
#Нам нужен этот диапазон, т.к. генераторы случайных чисел могут придумать число строго в заданных рамках
#Тем более мощность компьютера у нас ограничена, поэтому ограничиваем границы поиска.
lowx = -5
highx = 5
lowy = -5
highy = 5


#Далее мы отрисуем график с помощью библиотеки plotly
#Шаг сетки по x и y
kx = (highx-lowx)/100 
ky = (highy-lowy)/100 
#Наша функция, принимающая две переменные
def func(x, y): 
    return np.exp((x+y)/2) * (x**2 - 4*y**2)**3
X = np.arange(lowx, highx, kx)
Y = np.arange(lowy, highy, ky)
X, Y = np.meshgrid(X, Y)
Z = func(X, Y)
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
fig.update_layout(width=1000, height=1000)
fig.show()





#Наша функция, но принимающая массив a = [x,y] - так удобней 
def f4(a):
	return np.exp((a[0]+a[1])/2) * (a[0]**2 - 4*a[1]**2)**3
#Функция поиска градиента, состоящего из двух частных производных (по x и по y)
def proizv(func, epsilon):
	def grad_func(b):
		return np.array([(func(np.array([b[0]+epsilon, b[1]]))-func(np.array([b[0], b[1]])))/epsilon, (func(np.array([b[0], b[1]+epsilon]))-func(np.array([b[0], b[1]])))/epsilon])
	return grad_func
#Функция градиентного спуска - поиск локальных экстремумов в диапазоне по x (lowx;highx), по y (lowy;highy)
def grad_descent(func,lowx,highx,lowy,highy,ekstrem):
	best = np.array([])
	#Далее представлены глобальные коэффиценты, которые влияют на процесс градиентного спуска
	e = 1 #Вличина шага
	step = 100 # Количество итераций спуска
	atemp = 1000 #Количество попыток
	
	first_atemp = True
	pr = proizv(func,10**-10)
	
	
	for i in range(atemp):
		#Создаем случайную точку в указанном диапазоне
		x = np.random.uniform(lowx,highx,1)
		y = np.random.uniform(lowy,highy,1)
		a = np.array([x[0],y[0]])
		
		for o in range(step):
			#Проверяем - не уйдёт ли наша точка изи диапазона после очередного шага
			if(((a[0] - e*pr(a)[0] >= lowx) & (a[0] - e*pr(a)[0] <= highx)) & ((a[1] - e*pr(a)[1] >= lowy) & (a[1] - e*pr(a)[1] <= highy))):
				a = a - e*pr(a)
				
		#Сравниваем попытки и ищем наилучший результат
		if(first_atemp == True):
			best = a
			first_atemp = False
		elif(first_atemp == False):
			if((func(best) < func(a)) & (ekstrem == True)):
				best = a
			elif((func(best) > func(a)) & (ekstrem == False)):
				best = a
	return best

#Если itog = True, то мы ищем максимум, если False, то ищем минимум
itog = True 
#Получаем экстреум в виде списка b = [x,y]
b = grad_descent(f4,lowx,highx,lowy,highy,itog) 

if(itog == True):
	print('Мы нашли максимум функции')
elif(itog == False):
	print('Мы нашли минимум функции')
print("x = ",b[0])
print("y = ",b[1])
print("f(x,y)",f4(b))






