link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_exists(browser):
    browser.get(link)
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert button, "Кнопка добавления в корзину не найдена!"


# Использовал find_elementS_, чтобы можно было сюда присобачить assert.
# Если элемент "кнопка" не найден, метод вернет пустой список,
# что при булевом преобразовании будет False, а если
# не пустой - True. Для проверки корректности работы assert можете изменить
# имя класса в селекторе, например, на "btn-add-to-basket1".
