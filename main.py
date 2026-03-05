from task import Task, ImportantTask
from manager import TaskManager


def demonstrate_advanced_features():
    """Демонстрация всех продвинутых возможностей"""
    print("=== ДЕМОНСТРАЦИЯ ПРОДВИНУТЫХ ВОЗМОЖНОСТЕЙ ===\n")

    # Создаем менеджер задач
    manager = TaskManager("Рабочие задачи")

    # 1. Демонстрация обработки ошибок
    print("1. ОБРАБОТКА ОШИБОК:")
    manager.add_task("не задача")  # Ошибка типа
    manager.add_task(Task("Купить молоко"))  # OK
    manager.add_task(Task("Купить молоко"))  # Дубликат

    # 2. Добавляем разные задачи
    print("\n2. ДОБАВЛЕНИЕ ЗАДАЧ:")
    manager.add_task(Task("Сделать отчет", "Заполнить таблицы", "высокий"))
    manager.add_task(ImportantTask("Встреча с клиентом", "Подготовить презентацию", "завтра 10:00"))

    # 3. Демонстрация магических методов
    print("\n3. МАГИЧЕСКИЕ МЕТОДЫ:")
    print(f"Количество задач: {len(manager)}")
    print(f"Первая задача: {manager[0]}")
    print(f"'Купить молоко' в списке? {'Да' if 'Купить молоко' in manager else 'Нет'}")

    # 4. Создание задачи из строки (статический метод)
    print("\n4. СОЗДАНИЕ ИЗ СТРОКИ:")
    task_str = "Позвонить партнеру | Обсудить контракт | высокий"
    new_task = Task.create_from_string(task_str)
    if new_task:
        manager.add_task(new_task)
        print(f"Создана задача: {new_task}")

    # 5. Сохранение в файл
    print("\n5. СОХРАНЕНИЕ В ФАЙЛ:")
    manager.save_to_file("my_tasks.json")

    # 6. Загрузка из файла (создаем новый менеджер)
    print("\n6. ЗАГРУЗКА ИЗ ФАЙЛА:")
    loaded_manager = TaskManager.load_from_file("Загруженные задачи", "my_tasks.json")
    loaded_manager.show_all_tasks()

    # 7. Демонстрация работы с исключениями
    print("\n7. РАБОТА С ИНДЕКСАМИ:")
    task = manager.get_task_by_index(10)  # Несуществующий индекс
    print(f"Результат поиска индекса 10: {task}")

    task = manager.get_task_by_index("два")  # Неверный тип
    print(f"Результат поиска индекса 'два': {task}")

    # 8. Демонстрация фильтрации
    print("\n8. ФИЛЬТРАЦИЯ ЗАДАЧ:")
    high_priority = manager.get_tasks_by_priority("высокий")
    print(f"Задачи с высоким приоритетом ({len(high_priority)}):")
    for task in high_priority:
        print(f"  - {task}")

    # 9. Отмечаем задачу выполненной
    print("\n9. ВЫПОЛНЕНИЕ ЗАДАЧИ:")
    if len(manager) > 0:
        manager[0].mark_completed()

    # 10. Итоговая статистика
    print("\n10. ИТОГОВАЯ СТАТИСТИКА:")
    print(manager)
    print(f"\nВыполненные задачи: {len(manager.get_completed_tasks())}")
    print(f"Невыполненные задачи: {len(manager.get_pending_tasks())}")


def test_static_methods():
    """Тестирование статических методов класса Task"""
    print("\n=== ТЕСТИРОВАНИЕ СТАТИЧЕСКИХ МЕТОДОВ ===\n")

    # Тест validate_priority
    print("Проверка приоритетов:")
    for priority in ["низкий", "средний", "высокий", "сверхвысокий"]:
        is_valid = Task.validate_priority(priority)
        print(f"  {priority}: {'✅' if is_valid else '❌'}")

    # Тест get_priority_emoji
    print("\nЭмодзи приоритетов:")
    for priority in ["низкий", "средний", "высокий", "неизвестный"]:
        emoji = Task.get_priority_emoji(priority)
        print(f"  {priority}: {emoji}")


def test_inheritance():
    """Тестирование наследования"""
    print("\n=== ТЕСТИРОВАНИЕ НАСЛЕДОВАНИЯ ===\n")

    # Создаем важную задачу
    important = ImportantTask(
        "Дипломный проект",
        "Завершить главу 3",
        "понедельник"
    )

    print("Создана важная задача:")
    print(important)
    print()

    # Устанавливаем напоминание
    important.set_reminder()
    print(f"После установки напоминания: {important}")
    print()

    # Полная информация
    print("Детальная информация:")
    print(important.get_info())


def main():
    """Главная функция"""
    print("=" * 60)
    print("         ФИНАЛЬНОЕ ТЕСТИРОВАНИЕ TASK MANAGER")
    print("=" * 60)

    # Тестируем все возможности
    demonstrate_advanced_features()
    test_static_methods()
    test_inheritance()

    print("\n" + "=" * 50)
    print("ПРОЕКТ УСПЕШНО ЗАВЕРШЕН!")
    print("=" * 50)


if __name__ == "__main__":
    main()