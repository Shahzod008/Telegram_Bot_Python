from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Расписание", callback_data="raspisanie")],
        [InlineKeyboardButton(text="Главное меню", callback_data="back")],
        [InlineKeyboardButton(text="Группа без учителя", url="https://t.me/+AJCy9bENpOIwNTZi")],
        [InlineKeyboardButton(text="Тех. поддержка", callback_data="tech_support")]])

kb_ras = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Понедельник", callback_data="ponidelnik")],
        [InlineKeyboardButton(text="Вторник", callback_data="vtornik")],
        [InlineKeyboardButton(text="Среда", callback_data="sreda")],
        [InlineKeyboardButton(text="Четверг", callback_data="chetverg")],
        [InlineKeyboardButton(text="Пятница", callback_data="pjatniza")],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
        [InlineKeyboardButton(text="В главное меню", callback_data="back")]])

kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Расписание", callback_data="raspisanie")],
        [InlineKeyboardButton(text="Доп. уроки", callback_data="dop_uroki")],
        [InlineKeyboardButton(text="Теория уроков", callback_data="lesson_theory")],
        [InlineKeyboardButton(text="Преподователи", callback_data="prepodovateli")],
        [InlineKeyboardButton(text="История класса", callback_data="Istorija_klassa")],
        [InlineKeyboardButton(text="Список учеников", callback_data="spisok_uchenikov")],
        [InlineKeyboardButton(text="Задачи", callback_data="inter_zadachi")],
        [InlineKeyboardButton(text="Группа без учителя", url="https://t.me/+AJCy9bENpOIwNTZi")],
        [InlineKeyboardButton(text="Календарь учебного года", callback_data="kalendar")],
        [InlineKeyboardButton(text="Тех. поддержка", callback_data="tech_support")]])

kb_back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="В главное меню", callback_data="back")]])

kb_teorija_uroka = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Албебра", callback_data="albebra")],
        [InlineKeyboardButton(text="Русиш", callback_data="rusish")],
        [InlineKeyboardButton(text="Геометриш", callback_data="geomerish")],
        [InlineKeyboardButton(text="Шизика", callback_data="fisish")],
        [InlineKeyboardButton(text="В главное меню", callback_data="back")]
    ]
)