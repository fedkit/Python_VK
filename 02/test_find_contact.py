from find_contact import find_contact


# 1
contacts = [
    {'name': 'Александр Пушкин', 'phone': '+7 910 56-78', 'email': 'pushkin@example.com'},
    {'name': 'Стив Возняк', 'phone': '+7 123', 'email': 'iwoz@example.com'},
    {'name': 'Брюс Уэйн', 'phone': '+7 987 654', 'email': 'batman@example.com'},
    {'name': 'Бэтмен', 'phone': '+7 gotham', 'email': 'batman@example.com'},
]

assert find_contact(contacts, 'name', 'Дмитрий Менделеев') == []
assert find_contact(contacts, 'name', 'Пушкин') == []
assert find_contact(contacts, 'phone', '910') == []

assert find_contact(contacts, 'name', 'александр пушкин') == [
    {'name': 'Александр Пушкин', 'phone': '+7 910 56-78', 'email': 'pushkin@example.com'},
]

assert find_contact(contacts, 'email', 'batman@example.com') == [
    {'name': 'Брюс Уэйн', 'phone': '+7 987 654', 'email': 'batman@example.com'},
    {'name': 'Бэтмен', 'phone': '+7 gotham', 'email': 'batman@example.com'},
]


# 2
contacts = [
    {'name': 'Брюс Уэйн', 'phone': '+7 987 654', 'email': 'batman@example.com', 'city': 'Gotham'},
    {'name': 'Бэтмен', 'phone': '+7 gotham', 'email': 'batman@example.com', 'alias': 'Dark Knight'},
    {'name': 'Альфред', 'phone': '+7 111', 'email': 'alfred@wayne.com', 'role': 'butler'},
    {'name': 'Джокер', 'phone': '+7 222', 'email': 'joker@crime.com', 'enemy': 'Batman'},
    {'name': 'Гордон', 'phone': '+7 333', 'email': 'gordon@gotham.com', 'rank': 'commissar'},
]

assert find_contact(contacts, 'email', 'batman@example.com') == [
    {'name': 'Брюс Уэйн', 'phone': '+7 987 654', 'email': 'batman@example.com', 'city': 'Gotham'},
    {'name': 'Бэтмен', 'phone': '+7 gotham', 'email': 'batman@example.com', 'alias': 'Dark Knight'},
]


# 3
contacts = [
    {'name': 'Мария Кюри', 'phone': '+33 123', 'email': 'curie@science.com', 'birth_year': 1867},
    {'name': 'Чарльз Дарвин', 'phone': '+1 000', 'email': 'char@char.com', 'birth_year': 1809},
    {'name': 'Никола Тесла', 'phone': '+1 001', 'email': 'tesla@energy.com', 'birth_year': 1856},
]

assert find_contact(contacts, 'name', 'Дмитрий Менделеев') == []


# 4
contacts = [
    {'name': 'Александр Пушкин', 'phone': '+7 910 56-78', 'email': 'pushkin@example.com', 'country': 'Russia'},
]

assert find_contact(contacts, 'name', 'Пушкин') == []


# 5 
contacts = [
    {'name': 'Том Круз', 'phone': '+1 000', 'email': 'tom@tom.com', 'company': 'Hollywood', 'age': 60},
    {'name': 'Стив Джобс', 'phone': '+1 002', 'email': 'jobs@apple.com', 'company': 'Apple', 'age': 56},
    {'name': 'Билл Гейтс', 'phone': '+1 003', 'email': 'gates@microsoft.com', 'company': 'Microsoft', 'age': 68},
    {'name': 'Марк Цукерберг', 'phone': '+1 004', 'email': 'zuck@meta.com', 'company': 'Meta', 'age': 40},
    {'name': 'Никола Тесла', 'phone': '+1 001', 'email': 'tesla@energy.com', 'company': 'Lab', 'age': 86},
]

assert find_contact(contacts, 'phone', '+1 000') == [
    {'name': 'Том Круз', 'phone': '+1 000', 'email': 'tom@tom.com', 'company': 'Hollywood', 'age': 60},
]


# 6
contacts = [
    {'name': 'Стив Возняк', 'phone': '+7 123', 'email': 'iwoz@example.com', 'tag': 'engineer'},
    {'name': 'Брюс Уэйн', 'phone': '+7 987 654', 'email': 'batman@example.com', 'tag': 'hero'},
]

assert find_contact(contacts, 'phone', '910') == []
