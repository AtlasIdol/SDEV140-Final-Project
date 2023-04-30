import tkinter as tk
import random

# Establish variables to be used throughout
my_font = ("Lucida Console", 14)
width = 420
height = 340
# Set up the Intro Screen
intro_screen = tk.Tk()
intro_screen.title("Lottery")
intro_screen.resizable(False, False)
screen_width = intro_screen.winfo_screenwidth()
screen_height = intro_screen.winfo_screenheight()
x = (screen_width / 3) - (width / 3)  # This variable will be used throughout the program
y = (screen_height / 3) - (height / 3)  # This variable will be used throughout the program
intro_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))


def hoosier():
    intro_screen.destroy()
    hoosier_screen = tk.Tk()
    hoosier_screen.title("Lottery -- Lotto")
    hoosier_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    hoosier_screen.resizable(False, False)
    hoosier_frame = tk.Frame(hoosier_screen, relief=tk.GROOVE, borderwidth=2)
    hoosier_frame.pack(side=tk.TOP, pady=5)
    lbl_hoosier_1 = tk.Label(hoosier_frame, font=my_font, text="Welcome to Lotto!")
    lbl_hoosier_1.grid(row=0, column=1, columnspan=2, pady=5)
    lbl_hoosier_2 = tk.Label(hoosier_frame, font=my_font, text="Choose 6 numbers from 1 to 46")
    lbl_hoosier_2.grid(row=1, column=1, columnspan=2, pady=5)
    hoosier_entry_frame = tk.Frame(hoosier_screen, relief=tk.GROOVE, borderwidth=3)
    hoosier_entry_frame.pack(side=tk.TOP, pady=5)
    ent_hoosier_1 = tk.Entry(hoosier_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_hoosier_1.pack(side=tk.LEFT, padx=5)
    ent_hoosier_2 = tk.Entry(hoosier_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_hoosier_2.pack(side=tk.LEFT, padx=5)
    ent_hoosier_3 = tk.Entry(hoosier_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_hoosier_3.pack(side=tk.LEFT, padx=5)
    ent_hoosier_4 = tk.Entry(hoosier_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_hoosier_4.pack(side=tk.LEFT, padx=5)
    ent_hoosier_5 = tk.Entry(hoosier_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_hoosier_5.pack(side=tk.LEFT, padx=5)
    ent_hoosier_6 = tk.Entry(hoosier_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_hoosier_6.pack(side=tk.LEFT, padx=5)
    hoosier_result_frame = tk.Frame(hoosier_screen, relief=tk.GROOVE, borderwidth=2)
    hoosier_result_frame.pack(side=tk.TOP, pady=5)
    lbl_hoosier_result = tk.Label(hoosier_result_frame, font=my_font, text="Click the button to get the results")
    lbl_hoosier_result.pack(side=tk.TOP,  pady=5)

    def hoosier_lotto():
        hoosier_lotto_numbers = set()
        while len(hoosier_lotto_numbers) < 6:
            number = random.randint(1, 46)
            if not hoosier_lotto_numbers:
                hoosier_lotto_numbers.add(number)
            elif number not in hoosier_lotto_numbers:
                hoosier_lotto_numbers.add(number)

        lotto_numbers = list(hoosier_lotto_numbers)
        lotto_numbers.sort()
        lbl_hoosier_draw_1 = tk.Label(
            hoosier_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[0])
        lbl_hoosier_draw_1.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_hoosier_draw_2 = tk.Label(
            hoosier_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[1])
        lbl_hoosier_draw_2.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_hoosier_draw_3 = tk.Label(
            hoosier_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[2])
        lbl_hoosier_draw_3.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_hoosier_draw_4 = tk.Label(
            hoosier_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[3])
        lbl_hoosier_draw_4.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_hoosier_draw_5 = tk.Label(
            hoosier_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[4])
        lbl_hoosier_draw_5.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_hoosier_draw_6 = tk.Label(
            hoosier_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[5])
        lbl_hoosier_draw_6.pack(side=tk.LEFT, pady=5, padx=15)
        guess_list = list(str(ent_hoosier_1.get()))
        guess_list.append(str(ent_hoosier_2.get()))
        guess_list.append(str(ent_hoosier_3.get()))
        guess_list.append(str(ent_hoosier_4.get()))
        guess_list.append(str(ent_hoosier_5.get()))
        guess_list.append(str(ent_hoosier_6.get()))
        draw_list = list(str(lbl_hoosier_draw_1['text']))
        draw_list.append(str(lbl_hoosier_draw_2['text']))
        draw_list.append(str(lbl_hoosier_draw_3['text']))
        draw_list.append(str(lbl_hoosier_draw_4['text']))
        draw_list.append(str(lbl_hoosier_draw_5['text']))
        draw_list.append(str(lbl_hoosier_draw_6['text']))
        number_correct = 0
        for guess in guess_list:
            if guess in draw_list:
                number_correct += 1

        hoosier_final_frame = tk.Frame(hoosier_screen, relief=tk.GROOVE, borderwidth=2)
        hoosier_final_frame.pack(side=tk.TOP, pady=5)
        lbl_hoosier_final = tk.Label(
            hoosier_final_frame, font=my_font, text=f'You got {number_correct} correct!')
        lbl_hoosier_final.pack()

    btn_hoosier_result = tk.Button(
            hoosier_result_frame, font=my_font, text="Draw Lotto Numbers", command=hoosier_lotto)
    btn_hoosier_result.pack(side=tk.TOP, pady=5)


def mega():
    intro_screen.destroy()
    mega_screen = tk.Tk()
    mega_screen.title("Lottery -- Millions")
    mega_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    mega_screen.resizable(False, False)
    mega_frame = tk.Frame(mega_screen, relief=tk.GROOVE, borderwidth=2)
    mega_frame.pack(side=tk.TOP, pady=5)
    lbl_mega_1 = tk.Label(mega_frame, font=my_font, text="Welcome to Millions!")
    lbl_mega_1.grid(row=0, column=1, columnspan=2, pady=5)
    lbl_mega_2 = tk.Label(mega_frame, font=my_font, text="Choose 6 numbers from 1 to 70")
    lbl_mega_2.grid(row=1, column=1, columnspan=2, pady=5)
    mega_entry_frame = tk.Frame(mega_screen, relief=tk.GROOVE, borderwidth=3)
    mega_entry_frame.pack(side=tk.TOP, pady=5)
    ent_mega_1 = tk.Entry(mega_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_mega_1.pack(side=tk.LEFT, padx=5)
    ent_mega_2 = tk.Entry(mega_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_mega_2.pack(side=tk.LEFT, padx=5)
    ent_mega_3 = tk.Entry(mega_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_mega_3.pack(side=tk.LEFT, padx=5)
    ent_mega_4 = tk.Entry(mega_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_mega_4.pack(side=tk.LEFT, padx=5)
    ent_mega_5 = tk.Entry(mega_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_mega_5.pack(side=tk.LEFT, padx=5)
    ent_mega_6 = tk.Entry(mega_entry_frame, width=3, borderwidth=1, relief=tk.GROOVE, font=my_font)
    ent_mega_6.pack(side=tk.LEFT, padx=5)
    mega_result_frame = tk.Frame(mega_screen, relief=tk.GROOVE, borderwidth=2)
    mega_result_frame.pack(side=tk.TOP, pady=5)
    lbl_mega_result = tk.Label(mega_result_frame, font=my_font, text="Click the button to get the results")
    lbl_mega_result.pack(side=tk.TOP, pady=5)

    def mega_numbers():
        mega_draw_numbers = set()
        while len(mega_draw_numbers) < 6:
            number = random.randint(1, 46)
            if not mega_draw_numbers:
                mega_draw_numbers.add(number)
            elif number not in mega_draw_numbers:
                mega_draw_numbers.add(number)

        lotto_numbers = list(mega_draw_numbers)
        lotto_numbers.sort()
        lbl_mega_draw_1 = tk.Label(
            mega_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[0])
        lbl_mega_draw_1.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_mega_draw_2 = tk.Label(
            mega_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[1])
        lbl_mega_draw_2.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_mega_draw_3 = tk.Label(
            mega_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[2])
        lbl_mega_draw_3.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_mega_draw_4 = tk.Label(
            mega_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[3])
        lbl_mega_draw_4.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_mega_draw_5 = tk.Label(
            mega_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[4])
        lbl_mega_draw_5.pack(side=tk.LEFT, pady=5, padx=15)
        lbl_mega_draw_6 = tk.Label(
            mega_result_frame, width=3, relief=tk.GROOVE, font=my_font, text=lotto_numbers[5])
        lbl_mega_draw_6.pack(side=tk.LEFT, pady=5, padx=15)
        guess_list = list(str(ent_mega_1.get()))
        guess_list.append(str(ent_mega_2.get()))
        guess_list.append(str(ent_mega_3.get()))
        guess_list.append(str(ent_mega_4.get()))
        guess_list.append(str(ent_mega_5.get()))
        guess_list.append(str(ent_mega_6.get()))
        draw_list = list(str(lbl_mega_draw_1['text']))
        draw_list.append(str(lbl_mega_draw_2['text']))
        draw_list.append(str(lbl_mega_draw_3['text']))
        draw_list.append(str(lbl_mega_draw_4['text']))
        draw_list.append(str(lbl_mega_draw_5['text']))
        draw_list.append(str(lbl_mega_draw_6['text']))
        number_correct = 0
        for guess in guess_list:
            if guess in draw_list:
                number_correct += 1

        mega_final_frame = tk.Frame(mega_screen, relief=tk.GROOVE, borderwidth=2)
        mega_final_frame.pack(side=tk.TOP, pady=5)
        lbl_mega_final = tk.Label(
            mega_final_frame, font=my_font, text=f'You got {number_correct} correct!')
        lbl_mega_final.pack()

    btn_mega_result = tk.Button(mega_result_frame, font=my_font, text="Draw Millions Numbers", command=mega_numbers)
    btn_mega_result.pack(side=tk.TOP, pady=5)


def intro():
    intro_frame = tk.Frame(intro_screen)
    intro_frame.pack(side=tk.TOP, pady=5)
    lbl_intro = tk.Label(intro_frame, font=my_font, text="Choose a game to play")
    lbl_intro.grid(row=0, column=1, columnspan=2, pady=5)
    btn_hoosier = tk.Button(
        intro_frame, text="Lotto", font=my_font, width=15, height=13, bg="blue", fg="white", command=hoosier)
    btn_hoosier.grid(row=1, column=1, pady=5)
    btn_mega = tk.Button(
        intro_frame, text="Millions", font=my_font, width=15, height=13, bg="green", fg="white", command=mega)
    btn_mega.grid(row=1, column=2, pady=5)


intro()
intro_screen.mainloop()
