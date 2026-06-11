import pytest
from todo_module import TodoList, BadNameError, BadPriorityError, BadIdError



#Create
def test_create_success():
    todo = TodoList()
    assert todo.create("CorrectName", 10) is True


def test_create_bad_name():
    todo = TodoList()
    with pytest.raises(BadNameError):
        todo.create("short", 10)


def test_create_bad_priority_low():
    todo = TodoList()
    with pytest.raises(BadPriorityError):
        todo.create("ValidName", 0)


def test_create_bad_priority_high():
    todo = TodoList()
    with pytest.raises(BadPriorityError):
        todo.create("ValidName", 101)



#Read
def test_read_success():
    todo = TodoList()
    todo.create("ValidName", 10)
    task = todo.read(1)
    assert task.tname == "ValidName"
    assert task.tpriority == 10


def test_read_bad_id_negative():
    todo = TodoList()
    with pytest.raises(BadIdError):
        todo.read(-1)


def test_read_bad_id_not_exists():
    todo = TodoList()
    with pytest.raises(BadIdError):
        todo.read(999)



# Update
def test_update_bad_id():
    todo = TodoList()
    with pytest.raises(BadIdError):
        todo.update(1, "ValidName", 10)