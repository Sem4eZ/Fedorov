# Fedorov

### Задача 2.3.2

Скриншот - все тесты пройдены (unittests):

![](скрин232.jpg)

Скриншот - все тесты пройдены (doctests):

![](скрин2322.jpg)

### Задача 2.3.3

- Запустил профилизатор в PyCharm, обнаружилось, что одни из самых затратных функций - check_published (изменение формата даты) и formatting_str (очищение строки от лишних символов).

![datatime](https://user-images.githubusercontent.com/106344305/206180335-870b2830-d700-4733-8512-23dceff98b46.png)

- Попробовал осуществить изменение формата даты несколькими способами (метод check_published):
1) С использованием библиотеки dateutil

```py
def check_published(date):
   return parse(date).strftime('%d.%m.%Y')
```

- Время работы в профилизаторе:

![parse](https://user-images.githubusercontent.com/106344305/206182321-61993f1c-7b20-490b-b5f3-a946d1da65f1.png)


2) С помощью форматирования строки

```py
def check_published(date):
  date = date[:date.find('T')].split('-')
  return '.'.join(reversed(date))
```
- Время работы в профилизаторе:

![строка](https://user-images.githubusercontent.com/106344305/206182418-b38fc18c-7923-40b4-82c7-063b09e0dfc5.png)


3) C использованием библиотеки datetime (первоначальная версия)

```py
def check_published(date):
  return datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').strftime('%d.%m.%Y')
```
- Время работы в профилизаторе:

![datatime](https://user-images.githubusercontent.com/106344305/206182600-9885410d-164a-40bb-8f46-81794ca236ae.png)

- Оказалось, что быстрее работает второй способ, но было решено сохранить первую версию с использованием библиотеки datetime, так как читабельность кода лучше.

- Попробовал осуществить изменение метода очищения строки от лишних символов (метод formatting_str)

```py
def formatting_str(self, raw_html):
  for i in range(len(raw_html)):
      while raw_html[i].find('<') > -1:
          index1 = raw_html[i].find('<')
          index2 = raw_html[i].find('>')
          raw_html[i] = raw_html[i][:index1] + raw_html[i][index2 + 1:]
      if '\n' not in raw_html[i]:
          raw_html[i] = " ".join(raw_html[i].split())
  return raw_html
```

- Время работы в профилизаторе:

![formatting](https://user-images.githubusercontent.com/106344305/206183485-76460f7c-fda0-4cf6-853f-4e36bb18c747.png)

- Время работы в профилизаторе первоначальной версии:

![datatime](https://user-images.githubusercontent.com/106344305/206183601-34088a5e-84a2-4781-866d-0401b8523463.png)

- Оказалось, что обе версии работают примерно одинаково, поэтому было решено оставить старую версию метода.

### Задача 3.2.1
- В результате сформировались файлы по годам.

![](сскрин231.jpg)

### Задача 3.2.2

- Время работы без многопоточности:

![2022-12-11](https://user-images.githubusercontent.com/106344305/206901258-768835a1-7577-4cb7-bcb8-16ca63890164.png)

- Время работы с использованием multiprocessing:

![2022-12-11 (1)](https://user-images.githubusercontent.com/106344305/206901282-cfeb984c-c233-4863-9b3c-67168112ec99.png)

- Можно заметить, что время выполнения уменьшилось примерно на 10 секунд.


