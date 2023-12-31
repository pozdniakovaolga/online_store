# online_store
Django homework 1.

Задание 1.
Для начала работы над задачей выполните первые шаги:
Настройте виртуальное окружение.
Создайте новый Django-проект.

Задание 2.
После успешного создания проекта сделайте первую настройку. Для этого:
Создайте первое приложение с названием 
catalog .
Внесите начальные настройки проекта.
Сделайте настройку урлов (URL-файлов) для нового приложения.

Задание 3.
Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.
Для создания шаблонов лучше использовать UIkit Bootstrap. 

Задание 4.
В приложении в контроллере реализуйте два контроллера:
 Контроллер, который отвечает за отображение домашней страницы.
 Контроллер, который отвечает за отображение контактной информации.

Дополнительное задание.
Реализуйте обработку сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные для обратной связи.


Критерии выполнения заданий
- Всё итоговое решение залили в github.com и сдали в виде ссылки на репозиторий.
- Создали отдельное приложение.
- Реализовали два контроллера.
- Адреса описали не внутри главного URL-файла, а вынесли в пространства имен.
- Добавили папку с шаблонами, в которой лежат два шаблона.


Django homework 2.

Задание 1
Подключите СУБД PostgreSQL для работы в проекте. Для этого: 
Создайте базу данных в ручном режиме. Внесите изменения в настройки подключения.

Задание 2
В приложении каталога создайте модели: Product, Category.
Опишите для них начальные настройки.

Задание 3
Для каждой модели опишите следующие поля:
Product:
наименование,
описание,
изображение (превью),
категория,
цена за покупку,
дата создания,
дата последнего изменения.
Category:
наименование,
описание.
Для поля с изображением необходимо добавить соответствующие настройки в проект, а также установить библиотеку для работы с изображениями 
Pillow .

Задание 4
Перенесите отображение моделей в базу данных с помощью инструмента миграций. Для этого:
Создайте миграции для новых моделей.
Примените миграции.
Внесите изменения в модель категорий, добавьте поле 
created_at
, примените обновление структуры с помощью миграций.
Откатите миграцию до состояния, когда поле 
created_at
 для модели категории еще не существовало, и удалите лишнюю миграцию.

Задание 5
Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.
При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания.

Задание 6
Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
Сформируйте фикстуры для заполнения базы данных.
Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных.
Последний пункт можно реализовать в связке с инструментом работы с фикстурами, можно описать вставку данных отдельными запросами.

Дополнительное задание.
В контроллер отображения главной страницы добавьте выборку последних 5 товаров и вывод их в консоль.
Создайте модель для хранения контактных данных и попробуйте вывести данные, заполненные через админку, на страницу с контактами.

Критерии выполнения заданий
Результат выполнения проекта залейте в GitHub и сдайте в виде ссылки на репозиторий.
Результаты работы по первому пункту в задании 6 прикрепите в виде скриншотов терминала.


Django homework 3.

Задание 1
Создайте новый контроллер и шаблон, которые будут отвечать за отображение отдельной страницы с товаром. На странице с товаром необходимо вывести всю информацию о товаре.
Для создания шаблонов используйте UI kit Bootstrap. При возникновении проблем возьмите за основу данный шаблон.

Задание 2
В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек отображаемое описание обрежьте после первых выведенных 100 символов.

Задание 3
Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый) шаблон и также подшаблон с главным меню.
При необходимости можно выделить больше общих шаблонов.

Задание 4
Для выводимого изображения на странице реализуйте шаблонный фильтр, который преобразует переданный путь в полный путь для доступа к медиафайлу:
<!-- Исходный вариант --> 
<img src="/media/{{ object.image }}" />
<!-- Итоговый вариант -->
<img src="{{ object.image|mediapath }}" />
Реализуйте описанный функционал с помощью шаблонного тега:
<!-- Исходный вариант -->
<img src="/media/{{ object.image }}" />
<!-- Итоговый вариант -->
<img src="{% mediapath object.image %}" />

Дополнительное задание.
Добавьте функционал создания продукта через внешний интерфейс, не используя стандартную админку.
Реализуйте постраничный вывод списка продуктов.


Django homework 4.

Задание 1
Продолжаем работать с проектом из предыдущего домашнего задания. Переведите имеющиеся контроллеры с FBV на CBV.

Задание 2
Создайте новую модель блоговой записи со следующими полями:
заголовок,
slug (реализовать через CharField),
содержимое,
превью (изображение),
дата создания,
признак публикации,
количество просмотров.
Для работы с блогом реализуйте CRUD для новой модели.

Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:
при открытии отдельной статьи увеличивать счетчик просмотров;
выводить в список статей только те, которые имеют положительный признак публикации;
при создании динамически формировать slug name для заголовка;
после успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.

Дополнительное задание.
Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.
