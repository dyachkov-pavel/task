def black_box(page: int):
    if page <= 7922400:
        return True
    else:
        return False


def binary_search_right_border(start, end):
    mid = (start + end) // 2
    if black_box(mid):
        return binary_search_right_border(mid+1, end)
    return mid


def binary_search_left_border(start, end):
    mid = (start + end) // 2
    if not black_box(mid):
        return binary_search_left_border(start, mid-1)
    return mid


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.

    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_box) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.

    Уточнение:
        black_box возвращает True, если страница последняя
                  возвращает False, если страница не последняя.


    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """

    left = 0
    right = 10000000
    while right - left > 1:
        right = binary_search_right_border(left, right)
        left = binary_search_left_border(left, right)
    print(left)


if __name__ == '__main__':
    main()
