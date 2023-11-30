# Проект тестирования сайта банка Точка</h1>

Проект демонстрирует организацию с нуля удобной инфраструктуры для внедрения автоматизации. 
С помощью Pytest и Selene реализована основа для добавления новых тестов, запуск тестов происходит в Jenkins,
отчёты о прохождении загружаются в Allure TestOpts, 
в Telegram приходят нотификации с результатами прогона.

Тестами покрыта форма поиска [открытых вакансий.](https://tochka.com/hr/vacancies/) 
Набор тестов не является полным, но тем не менее он разумный)

![vacancies_page](resources/images/vacancies_page.png)

---

### Автотестами проверяется:

* [X]  Применение, изменение и сброс фильтра про направлению работы
* [X]  Применение и сброс фильтра по опыту работы
* [X]  Скрытие фильтра про городу при выборе удаленного формата работы
* [X]  Сброс фильтра по формату работы
* [X]  Применение фильтра про зарплате
* [X]  Применение комбинации из трех фильтров с нужной вакансией в результате
* [X]  Применение комбинации фильтров, которая дает пустую выдачу
* [X]  Переход на страницу вакансии из результатов поиска

---

### Технологии:

| Python | Pytest | Selene | Selenium | Selenoid | Jenkins | Allure Reports | Allure TestOps | Telegram |
|--------|--------|--------|----------|----------|---------|-----------------|----------------|----------|
| <p align="center"><img src="resources/icons/python.svg" alt="Python" width="50"/></p> | <p align="center"><img src="resources/icons/pytest.png" alt="Pytest" width="50"/></p> | <p align="center"><img src="resources/icons/selene.png" alt="Selene" width="55"/></p> | <p align="center"><img src="resources/icons/selenium.png" alt="Selenium" width="50"/></p> | <p align="center"><img src="resources/icons/jenkins.png" alt="Jenkins" width="50"/></p> | <p align="center"><img src="resources/icons/selenoid.png" alt="Selenoid" width="50"/></p> | <p align="center"><img src="resources/icons/allure_report.png" alt="Allure Reports" width="50"/></p> | <p align="center"><img src="resources/icons/allure_testops.png" alt="Allure TestOps" width="50"/></p> | <p align="center"><img src="resources/icons/telegram.png" alt="Telegram" width="50"/></p> |

---

### Запуск автотестов выполняется на сервере [Jenkins](https://jenkins.autotests.cloud/job/julia_shilkova-tochka_tests_demo/)

#### Параметры сборки

* `environment` - окружение для запуска тестов
* `comment` - комментарий к запуску, будет указан в нотификации в Telegram

#### Чтобы запустить автотесты в Jenkins:

1. Открыть [проект](https://jenkins.autotests.cloud/job/julia_shilkova-tochka_tests_demo/)
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке
4. Добавить комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

![how to build](resources/images/howToBuild.png)

#### Чтобы запустить локально:

1. Задать логин и пароль от учетной записи **selenoid.autotests.cloud** 
в переменных окружения `LOGIN` и `PASSWORD`
2. Импортировать зависимости `pip install -r requirements.txt`
3. Запустить тесты `pytest .`
4. Сформировать allure отчет `allure serve`

### Allure отчёт

#### Общие результаты
![allure results](resources/images/allure_report.png)

#### Список тест кейсов
![test cases](resources/images/test_cases.png)

#### Пример подробного отчета о прохождении теста
Для каждого теста помимо шагов добалены скриншот, код страницы, видео прохождения и логи браузера,
чтобы легче находить причину, по которой упал тест.  

![test result](resources/images/scenario.png)

### Видео прохождения тестов
![video](resources/images/tests_video.gif)

###  Telegram бот
Результаты прохождения тестов приходят в чат в Telegram: так ответственные могут быстро узнавать о проблемах. 
В кратком отчете есть процент упавших тестов и ссылка на страницу с подробным allure отчетом.

<img src="resources/images/telegram_notification.png" width="400">

### Allure TestOps

Интегрировала проект с TestOps. Здесь можно посмотреть тест кейсы по фичам

![testOps cases](resources/images/testOps_test_cases.png)

а также общие результаты тестирования и долю автоматизированных кейсов

![testOps cases](resources/images/testOps_dashboard.png)







