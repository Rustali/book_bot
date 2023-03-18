BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    # Определяем список знаков препинания, которые могут быть окончанием страницы
    p_marks: list[str] = [',', '.', '!', ':', ';', '?']

    # Определяем кусок текста по заданным параметрам
    chunk: str = text[start:start+size]

    # Если кусок текста заканчивается на нужный знак, проверяем не попали ли в многоточие
    if chunk[-1] in p_marks:
        try:
            # Если следующий за нашим куском текста знак точка, то значит мы попали в многоточие,
            # обрезаем текст до следующего пробела и проверяем снова на соответствие последнего знака
            if text[start+size] == '.':
                while True:
                    i = chunk.rfind(' ')
                    chunk = chunk[:i].strip()
                    if chunk[-1] in p_marks:
                        return chunk, len(chunk)
            else:
                return chunk, len(chunk)
        # Если после нашего куска текста больше нет символов, значит конец текста и отправляем наш кусок
        except:
            return chunk, len(chunk)
    else:
        # Если последний знак в куске текста не входит в наш список,
        # то обрезаем текст до следующего пробела и проверяем снова на соответствие последнего знака
        while True:
            i = chunk.rfind(' ')
            chunk = chunk[:i].strip()
            if chunk[-1] in p_marks:
                return chunk, len(chunk)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path) as f:
        text = f.read()
    page: int = 1
    start: int = 0

    while start < len(text):
        page_text, page_len = _get_part_text(text, start, PAGE_SIZE)
        book[page] = page_text.lstrip()
        page += 1
        start += page_len


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
