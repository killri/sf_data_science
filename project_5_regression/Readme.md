# Проект 5. Задача регресии: прогнозирование длительности поещдки в Нью Йоркском такси

## Содержание
* Описание проекта
* Какую задачу мы решаем?
* Краткая информация о данных
* Этапы работы над проектом
* Результаты
* Выводы

## Описание проекта

Это реальный проект по задаче, которая была выложена на платформе Kaggle. Необходимо по данным о поездках в Нью-Йоркском такси построить модель, которая будет предсказывать длительность поездки.

## Какую задачу мы решаем?

Имея на входе дата сет из примерно 1,5 миллионов записей о поездках в такси, выполнить все этапы решения задачи машинного обучения:
* Предобработка
* Разведывательный анализ
* Отбор признаков
* Моделирование

*Оценка качества работы*

На обучающей платформе SkillFactory были размещены контрольные вопрсы по каждому шагу проекта. Это позволяло проверять правильность обработки данных на каждом этапе.

*Чему мы учимся/ что практикуем?*

* Учимся решать задачу машинного обучения последовательно от поставноки до моделирования
* Закрепляем навыки работы с библиотекой pandas, особенно на этапе предобработки данных
* Практикуем инструменты предобработки и моделировния регрессии библиотеки scikit-learn
* Строим и сравниваем 5 разных моделей с учетом точности на валидационных и тестовых данных. Проверяем модели на переобучение.

## Краткая информация о данных

Исходные данные - это таблица .csv из 1 458 644 строк и 11 столбцов. Признаки следующие:

**Данные о клиенте и таксопарке:**
* id - уникальный идентификатор поездки
* vendor_id - уникальный идентификатор поставщика (таксопарка), связанного с записью поездки

**Временные характеристики:**
* pickup_datetime - дата и время, когда был включен счетчик поездки
* dropoff_datetime - дата и время, когда счетчик был отключен

**Географическая информация:**
* pickup_longitude -  долгота, на которой был включен счетчик
* pickup_latitude - широта, на которой был включен счетчик
* dropoff_longitude - долгота, на которой счетчик был отключен
* dropoff_latitude - широта, на которой счетчик был отключен

**Прочие признаки:**
* passenger_count - количество пассажиров в транспортном средстве (введенное водителем значение)
* store_and_fwd_flag - флаг, который указывает, сохранилась ли запись о поездке в памяти транспортного средства перед отправкой поставщику. Y - хранить и пересылать, N - не хранить и не пересылать поездку.

**Целевой признак:**
* trip_duration - продолжительность поездки в секундах

## Шаги работы над проектом
1. Предобработка данных
    * первичное знакомство с признаками
    * Перевод признака формата datetime даты и времени начала поездки в признаки дня, времени, даты, маркера праздничного дня
    * Создание признаков связанных с координатами начала и конца поездки (длина маршрута osrm, число поворотов по короткому маршруту, расстояние Хаверсина и т.д.)
    * Создание признака гео-кластеров с помощью алгоритма kmeans
    * Добавление признаков, связанных с погодой на дату и время начала поездки
    * Убираем очевидные выбросы
2. Разведывательный анализ данных
    * Строим распределение целевого признака в логарифмированном формате
    * Строим распределение целевого признака в логарифмированном формате относительно части другиз признаков
    * Делаем гипотезы о значимости признаков дял моделирования
3. Отбор и преобразование признаков
    * Кодируем котигориальные признаки
    * Избавляемся от неинформативных признаков и утечки данных
    * Выбираем с помощью SelectKBest 25 самых значимых признаков
    * Делим выборку на обучающую и валидационную. Используем в проекте hold-out-валидацию.
    * Нормализуем признаки с помощью MinMaxScaler
4. Моделирование
    * Строим модели регрессии от простых типа аналитического решения линейной регресии до пары ансамблиевых моделей (случайный лес и градиентный бустинг)
    * Сравниваем модели по качеству на валидационной выборке и проверяем их на признаки переобучения.

## Результаты
* Все задания я сделаны. Понятно стало, что новые модели и подходы в ML появляются постоянно и стоит держать руку на пусльсе того, какие сейчас есть самые эффективные и актуальные инструменты.
* Данные предобработаны, создано более 20 новых признаков, отобрано 25 признаков для моделирвоания.
* Построены модели:
    * Линейная регрессия
    * Полиномиальная регрессия
    * Полиномиальная регрессия с регуляризацией L2
    * Дерево решений
    * Случайные лес
    * Градиентныей бустинг над деревьями решений
* Выбрана оптимальная модель, оценена целевая метрика. Проинтерпретирован показатель целевой метрики.
* Изучен пример улучшенного градиентного бустинга

## Заключение

* Это моя первая задача ML решенная от 0 до моделирования. И да, были подсказки "что делать", но не "как делать".