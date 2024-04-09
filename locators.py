from selenium.webdriver.common.by import By


class StellarBurgersLocators:

    REGISTER_NAME_ACCOUNT = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") # Указаное имя при регистрации
    REGISTER_EMAIL_ACCOUNT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") # Указаный  email при регистрации
    PASSWORD_ACCOUNT = (By.XPATH, "//input[@type = 'password']") # Указаный пароль при регистрации
    CORRECT = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка ввойти при вводе логина и пароля или регистрации
    EMAIL_ACCOUNT = (By.XPATH, "//div[@class = 'input__container']/descendant::label[text() = 'Email']/following-sibling::input") # Поле ввода еmail


    BUTTON_LOGIN_IN_ACCOUNT = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]") # Кнопка войти в аккаунт
    BUTTON_EXIT = (By.XPATH, "//button[contains(text(), 'Выход')]") # Кнопка "выход" из личного кабинета
    BUTTON_PERSSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") # Кнопка перехода в личный кабинет
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # Кнопка оформить заказ
    BUTTON_REGISTER_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") # Кнопка зарегестрироваться
    ARIA_CURRENT = (By.XPATH, "//a[contains(@href, '/account/profile')]") # Кнопка профиль в "Личном кабинете"



    LINK_REGISTER_ACCOUNT = (By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]") # Ссылка на форму регистрации
    LINK_ENTER_DESIGNER = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # Нажатие на ссылку "конструктор"
    LINK_ENTER_LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']") # Нажатие на лого
    LINK_ENTER_ACCOUNT = (By.XPATH, "//a[contains(text(), 'Войти')]") # Ссылка ввойти в форме востановления пароля
    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[contains(@href, '/forgot-password')]") # Ссылка востановить пароль"


    TEXT_DESIGNER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]") # Текст "Соберите бургер" на главной странице
    TEXT_ENTER = (By.XPATH, "//h2[text() = 'Вход']") # Текст вход над логином и паролем
    TEXT_ERROR_INCORRECT_PASSWORD = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") # Текст не корректного пароля
    TEXT_FILING = (By.XPATH, "//h2[text() = 'Начинки']") # Заголовок "Начинки"
    TEXT_SAUCE = (By.XPATH, "//h2[text() = 'Соусы']") # Заголовок "Соусы"
    TEXT_BURGERS = (By.XPATH, "//h2[text() = 'Булки']") # Заголовок "Булки"


    TAB_FILING = (By.XPATH, "//span[contains(text(), 'Начинки')]") # Вкладка "Начинки"
    TAB_SAUCE = (By.XPATH, "//span[contains(text(), 'Соусы')]") # Вкладка "Соусы"
    TAB_BURGERS = (By.XPATH, "//span[contains(text(), 'Булки')]") # Вкладка "Булки"




