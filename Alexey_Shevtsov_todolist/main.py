from todo_module import App, TodoList

def main():
    tdl = TodoList()
    app = App(tdl)
    app.Run()

if __name__ == '__main__':
    main()