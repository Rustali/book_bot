from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


# Фильтр проверяет состоит ли callback_data из цифр
class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and callback.data.isdigit()


# Фильтр ловит callback_data на удаление закладок
class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and 'del' \
            in callback.data and callback.data[:-3].isdigit()
