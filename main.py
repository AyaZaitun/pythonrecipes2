try:
    from tkinter import *
    import webbrowser
    login = Tk()
    login.title("website recipes")
    login.geometry("410x410")
    bg = PhotoImage(file=r"C:\Users\Admin\pythonProject2\des.PNG")
    label1 = Label(login, image=bg)
    label1.place(x=0, y=0)
    def botton_login():
        username1 = username.get()
        password1 = password.get()
        if username1 == "recipes" and password1 == "1234":
            botton_login.config(text="next")
            choose = Tk()

            def botton_choose():
                choose1 = choose_entry.get()
                if choose1 == "1" or choose1 == "2":
                    if choose1 == "1":
                        botton_choose.config(text="next")
                        def open_link():
                            recipes_entry1 = recipes_entry.get()
                            webbrowser.open(f"https://en.wikipedia.org/wiki/{recipes_entry1}")
                        def botton_search():
                            recipes_entry1 = recipes_entry.get()
                            my_file = open("recipes.txt", "r")
                            all_data = my_file.readlines()
                            for i in all_data:
                                data = i.split(",")
                                if data[0] == recipes_entry1:
                                    botton_search.config(text="search")
                                    print(i)
                        def botton_next():
                            botton_next1.config(text="next")

                            def open_link():
                                recipes_entry1 = recipes_entry.get()
                                webbrowser.open(f"https://en.wikipedia.org/wiki/{recipes_entry1}")

                            def botton_search():
                                recipes_entry1 = recipes_entry.get()
                                my_file = open("Dessert.txt", "r")
                                all_data = my_file.readlines()
                                for i in all_data:
                                    data = i.split(",")
                                    if data[0] == recipes_entry1:
                                        botton_search.config(text="search")
                                        print(i)

                            def botton_next():
                                botton_next.config(text="next")

                                def open_link():
                                    recipes_entry1 = recipes_entry.get()
                                    webbrowser.open(f"https://en.wikipedia.org/wiki/{recipes_entry1}")

                                def botton_search():
                                    recipes_entry1 = recipes_entry.get()
                                    my_file = open("Snacks.txt", "r")
                                    all_data = my_file.readlines()
                                    for i in all_data:
                                        data = i.split(",")
                                        if data[0] == recipes_entry1:
                                            botton_search.config(text="search")
                                            print(i)

                                Snacks = Tk()
                                frame_Snacks = Frame(Snacks)
                                label_Snacks = Label(frame_Snacks,bg="#c9a0dc",text="write Snacks recipes name:")
                                recipes_entry = Entry(frame_Snacks)
                                botton_search = Button(Snacks, text="search", fg="white", bg="black",command=botton_search)
                                open_link = Button(Snacks, text="Go To Recipes Link", fg="white", bg="black",command=open_link)
                                frame_Snacks.pack()
                                label_Snacks.pack()
                                recipes_entry.pack()
                                botton_search.pack()
                                open_link.pack()
                                Snacks.mainloop()
                            dessert=Tk()
                            frame_dessert = Frame(dessert)
                            label_dessert = Label(frame_dessert,bg="#f88cae", text="write dessert recipes name:")
                            recipes_entry = Entry(frame_dessert)
                            botton_search = Button(dessert, text="search", fg="white", bg="black",command=botton_search)
                            open_link = Button(dessert, text="Go To Recipes Link", fg="white", bg="black", command=open_link)
                            botton_next = Button(dessert, text="Next", fg="white", bg="black", command=botton_next)
                            frame_dessert.pack()
                            label_dessert.pack()
                            recipes_entry.pack()
                            botton_search.pack()
                            open_link.pack()
                            botton_next.pack()
                            dessert.mainloop()
                        recipes = Tk()
                        frame_recipes = Frame(recipes)
                        label_recipes = Label(frame_recipes,bg="#e8f4ff", text="write recipes name:")
                        recipes_entry = Entry(frame_recipes)
                        botton_search = Button(recipes, text="search", fg="white", bg="black", command=botton_search)
                        open_link = Button(recipes, text="Go To Recipes Link", fg="white", bg="black", command=open_link)
                        botton_next1 = Button(recipes, text="Next", fg="white", bg="black", command=botton_next)
                        frame_recipes.pack()
                        label_recipes.pack()
                        recipes_entry.pack()
                        botton_search.pack()
                        open_link.pack()
                        botton_next1.pack()
                        recipes.mainloop()
                    if choose1 == "2":
                        botton_choose.config(text="next")

                        def botton_search():
                            recipes_entry1 = recipes_entry.get()
                            my_file = open("recipes.txt", "r")
                            all_data = my_file.readlines()
                            for i in all_data:
                                data = i.split(",")
                                if data[1] == recipes_entry1:
                                    print(i)
                                if data[2] == recipes_entry1:
                                    print(i)
                        def botton_next1():
                            botton_next1.config(text="Next")

                            def open_link():
                                recipes_entry1 = recipes_entry.get()
                                webbrowser.open(f"https://en.wikipedia.org/wiki/{recipes_entry1}")

                            def botton_search():
                                recipes_entry1 = recipes_entry.get()
                                my_file = open("Dessert.txt", "r")
                                all_data = my_file.readlines()
                                for i in all_data:
                                    data = i.split(",")
                                    if data[0] == recipes_entry1:
                                        botton_search.config(text="search")
                                        print(i)

                            def botton_next():
                                botton_next.config(text="next")
                                def open_link():
                                    recipes_entry1 = recipes_entry.get()
                                    webbrowser.open(f"https://en.wikipedia.org/wiki/{recipes_entry1}")

                                def botton_search():
                                    recipes_entry1 = recipes_entry.get()
                                    my_file = open("Snacks.txt", "r")
                                    all_data = my_file.readlines()
                                    for i in all_data:
                                        data = i.split(",")
                                        if data[0] == recipes_entry1:
                                            botton_search.config(text="search")
                                            print(i)
                                Snacks=Tk()
                                frame_Snacks = Frame(Snacks)
                                label_Snacks = Label(frame_Snacks,bg="#8ccaaa",text="write Snacks recipes name:")
                                recipes_entry = Entry(frame_Snacks)
                                botton_search = Button(Snacks, text="search", fg="white", bg="black",command=botton_search)
                                open_link = Button(Snacks, text="Go To Recipes Link", fg="white", bg="black",command=open_link)
                                frame_Snacks.pack()
                                label_Snacks.pack()
                                recipes_entry.pack()
                                botton_search.pack()
                                open_link.pack()
                                Snacks.mainloop()

                            dessert = Tk()
                            frame_dessert = Frame(dessert)
                            label_dessert = Label(frame_dessert,bg="#fff68f",text="write dessert recipes name:")
                            recipes_entry = Entry(frame_dessert)
                            botton_search = Button(dessert, text="search", fg="white", bg="black",command=botton_search)
                            open_link = Button(dessert, text="Go To Recipes Link", fg="white", bg="black",command=open_link)
                            botton_next = Button(dessert, text="Next", fg="white", bg="black", command=botton_next)
                            frame_dessert.pack()
                            label_dessert.pack()
                            recipes_entry.pack()
                            botton_search.pack()
                            open_link.pack()
                            botton_next.pack()
                            dessert.mainloop()
                        recipes = Tk()
                        frame_recipes = Frame(recipes)
                        label_recipes = Label(frame_recipes,bg="#ffd4e5", text="write the main  ingredients of recipes:")
                        recipes_entry = Entry(frame_recipes)
                        botton_search = Button(recipes, text="search", fg="white", bg="black", command=botton_search)
                        botton_next1 = Button(recipes, text="Next", fg="white", bg="black", command=botton_next1)
                        frame_recipes.pack()
                        label_recipes.pack()
                        recipes_entry.pack()
                        botton_search.pack()
                        botton_next1.pack()
                        recipes.mainloop()

            label_choose = Label(choose,bg="#d9d2e9",text="please choose enter 1 if you want the ingredients of recipes,2 if you will give us the main component like:Chicken,Rice,Meat:")
            label_choose.pack()
            frame_entry = Frame(choose)
            choose_entry = Entry(frame_entry)
            frame_entry.pack()
            choose_entry.pack()
            botton_choose = Button(choose, text="Next", command=botton_choose)
            botton_choose.pack()
            choose.mainloop()

        else:
            botton_login.config(text="fail")

    labelinput=Label(login,text="please Enter username=recipes and password=1234",font=("bold", 11))
    labelinput.pack()
    label_login = Label(login, text="Login:")
    label_login.pack(pady=5)
    frame_username = Frame(login)
    label_username = Label(frame_username, text="Username", font=("bold", 11))
    username = Entry(frame_username)
    frame_username.pack()
    label_username.pack()
    username.pack(pady=5)
    frame_password = Frame(login)
    label_password = Label(frame_password, text="Password", font=("bold", 11),)
    password = Entry(frame_password,show="*")
    frame_password.pack()
    label_password.pack()
    password.pack()
    botton_login = Button(login, text="Next", command=botton_login)
    botton_login.pack(pady=5)
    login.mainloop()
except:
    print("list index out of range")


