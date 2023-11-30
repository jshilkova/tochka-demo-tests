<h1 align="center">Проект тестирования сайта банка Точка</h1>

---

Тестирую форму поиска [открытых вакансий](https://tochka.com/hr/vacancies/)

![vacancies_page](resources/images/vacancies_page.png)

---

### Автотестами проверила:

* [X]  Применение, изменение и сброс фильтра про направлению работы
* [X]  Применение и сброс фильра по опыту работы
* [X]  Что фильтр про городу скрывается при выборе удаленного формата работы
* [X]  Сброс фильтра по формату работы
* [X]  Применение фильтра про зарплате
* [X]  Применение комбинации из трех фильтров с нужной вакансией в результате
* [X]  Применение комбинации фильтров, которая дает пустую выдачу
* [X]  Переход на страницу вакансии из результатов поиска

---

### Технологии:

<table border="2">
  <tbody>
    <tr>
        <td>Python</td>
        <td>Pytest</td>
        <td>Selene</td>
        <td>Selenium</td>
        <td>Selenoid</td>
        <td>Jenkins</td>
        <td>Allure Reports</td>
        <td>Allure TestOps</td>
        <td>Telegram</td>
    </tr>
  </tbody>
</table>

<img src="resources/icons/python.svg" width="50">  
<img src="resources/icons/pytest.png" width="50">  
<img src="resources/icons/selene.png" width="55">
<img src="resources/icons/selenium.png" width="50">
<img src="resources/icons/jenkins.png" width="50">
<img src="resources/icons/selenoid.png" width="50">
<img src="resources/icons/allure_report.png" width="50">
<img src="resources/icons/allure_testops.png" width="50">
<img src="resources/icons/telegram.png" width="50">

---

### Запуск автотестов выполняется на сервере [Jenkins](https://jenkins.autotests.cloud/job/julia_shilkova-tochka_tests_demo/)

#### Параметры сборки

* `environment` - окружение для запуска тестов
* `comment` - комментарий

#### Чтобы запустить автотесты в Jenkins:

1. Открыть [проект](https://jenkins.autotests.cloud/job/julia_shilkova-tochka_tests_demo/)
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке
4. Добавить комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

![how to build](resources/images/howToBuild.png)

#### Чтобы запустить локально:

1. Задайте логин и пароль от учетной записи **selenoid.autotests.cloud** 
в переменных окружения `LOGIN` и `PASSWORD`
2. Импортируйте зависимости `pip install -r requirements.txt`
3. Запустите тесты `pytest .`
4. Сформируйте allure отчет `allure serve`

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

![telegram notification](resources/images/telegram_notification.png)

### Allure TestOps

Интегрировала проект с TestOps. Здесь можно посмотреть тест кейсы по фичам

![testOps cases](resources/images/testOps_test_cases.png)

а также общие результаты тестирования и долю автоматизированных кейсов

![testOps cases](resources/images/testOps_dashboard.png)







