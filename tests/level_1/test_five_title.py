from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('Заголовок', 5) == 'Заголовок'
    assert change_copy_item("100 самых интересных мест в России") == \
        'Copy of 100 самых интересных мест в России'
    assert change_copy_item("Copy of 100 самых интересных мест в России (3)") == \
        'Copy of 100 самых интересных мест в России (4)'
    assert change_copy_item("Copy of 100 самых интересных мест в России") == \
        'Copy of 100 самых интересных мест в России (2)'
