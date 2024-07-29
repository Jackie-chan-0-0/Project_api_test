import requests

class Test_location():
    """Работа с новой локацией."""


    def test_create_new_location(self):
        """Создание новой локации из предыдущего домашнего задания."""

        base_url = "https://rahulshettyacademy.com"# базовая url.
        key = "?key=qaclick123"# Параметр для всех запросов.

        """Создание новой локации."""
        post_resourse = "/maps/api/place/add/json"# Ресурс метода POST.

        post_url = base_url + post_resourse + key
        print(post_url)

        json_for_create_new_location = {
            "location": {

                "lat": -38.383494,

                "lng": 33.427362

            }, "accuracy": 50,

            "name": "Frontline house",

            "phone_number": "(+91) 983 893 3937",

            "address": "29, side layout, cohen 09",

            "types": [

                "shoe park",

                "shop"

            ],

            "website": "http://google.com",

            "language": "French-IN"
        }

        for location in range(5):
            result_post = requests.post(post_url, json = json_for_create_new_location)
            print(result_post.text)
            print(f"Статус код: {result_post.status_code}")  # С помощью данной команды мы можем получить наш статус код.
            assert 200 == result_post.status_code# Сравниваем, что система нам выдала статус код 200.
            print("Успешно!!! Создана новая локация.")

            check_post = result_post.json()
            check_info_post = check_post.get("status")
            print(f"Статус код ответа: {check_info_post}") # С помощью данной команды получаем наш статус код ответа.
            assert check_info_post == "OK"# Сравниваем статус код ответа.
            print("Статус ответа верен.")
            place_id = check_post.get("place_id")
            print(f"Place id: {place_id}")
            """Сохраняем place_id в наш текстовый документ"""
            file = open('place_id.txt', 'a')
            file.write(f'{place_id}\n')
            file.close()
            print("Place-id успешно записан в текстовый документ.")

        """Читаем place_id из нашего текстового документа"""
        file = open('place_id.txt', 'r')
        content = file.readlines()
        place_id_last = content[-1]
        p_id_last = place_id_last.rstrip('\n')
        print(p_id_last)
        print(f"Place-id успешно взят из текстового документа: {p_id_last}")

        """Проверка создания новой локации."""
        get_resourse = "/maps/api/place/get/json"# Ресурс метода GET.
        get_url = f"{base_url + get_resourse + key}&place_id={p_id_last}"
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Статус код: {result_get.status_code}")  # С помощью данной команды получаем наш статус код.
        assert 200 == result_get.status_code# Сравниваем, что система нам выдала статус код 200.
        print("Успешно!!! Проверка создания новой локации прошла успешно.")

    def test_delete_location(self):
        """Удаление нужных локаций и добавление существующих place-id в новый текстовый файл."""
        """Читаем place_id из нашего текстового документа"""
        file = open('place_id.txt', 'r')
        content = file.readlines()
        p_id_1 = content[-5]
        p_id_2 = content[-4]
        p_id_3 = content[-3]
        p_id_4 = content[-2]
        p_id_5 = content[-1]
        place_id_list_delete = [p_id_2, p_id_4]
        print(place_id_list_delete)
        place_id_list = [p_id_1, p_id_2, p_id_3, p_id_4, p_id_5]
        print(place_id_list)
        print(f"Place-id успешно взяты из текстового документа.")

        base_url = "https://rahulshettyacademy.com"  # базовая url.
        key = "?key=qaclick123"  # Параметр для всех запросов.

        """Удаление 2-го и 4-го place-id"""
        delete_resourse = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        for p_id in place_id_list_delete:
            place_id = p_id.rstrip('\n')
            json_for_delete_location = {
                "place_id": place_id
            }
            result_delete = requests.delete(delete_url, json=json_for_delete_location)
            print(result_delete.text)
            print(f"Статус код: {result_delete.status_code}")  # С помощью данной команды мы можем получить наш статус код.
            assert 200 == result_delete.status_code  # Сравниваем, что система нам выдала статус код 200.
            print(f"Успешно!!! Удаление {place_id} прошло успешно.")

        """Отбор существующих и несуществующих локаций и запись существующих в отдельный файл."""
        get_resourse = "/maps/api/place/get/json"  # Ресурс метода GET.
        for p_id in place_id_list:
            place_id = p_id.rstrip('\n')
            get_url = f"{base_url + get_resourse + key}&place_id={place_id}"
            print(get_url)
            result_g = requests.get(get_url)
            result_get = result_g.status_code
            print(f"Статус код: {result_get}.")
            if result_get == 200:
                assert 200 == result_get
                print("Успешно. Статус код верен.")
                file = open('place_id_200.txt', 'a')
                file.write(f'{p_id}\n')
                file.close()
                print("Place-id существует и успешно записан в текстовый документ.")
            else:
                assert 404 == result_get
                print("Успешно. Статус код верен.")
                print("Place-id не записан в текстовый документ, т.к его не существует.")

np = Test_location()
np.test_create_new_location()
np_2 = Test_location()
np_2.test_delete_location()