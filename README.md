# Решатель квадратных уравнений

Функция для решения квадратных уравнений

# Как использовать
Функция принимает три параметра - действительные числа.
Ответ может содержать:
- Два корня
- Один корень
- Ни одного
```
from quadratic_equation import get_roots

print(get_roots(1, 2, -3))
```
Вывод
```
(-3, 1)
```
-3 - первый корень<br>
1 - второй корень

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Пример запуска
Запуск тестов

```
python tests.py
```
Вывод
```
Ran 4 tests in 0.006s

OK
```
# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
