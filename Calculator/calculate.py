from tkinter import END, Tk, Canvas, Entry, Text, Button, PhotoImage


def main():
    button_image_1 = PhotoImage(
        file="assets/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(7),
        relief="flat",
        activebackground='black'
    )
    button_1.place(
        x=21.0,
        y=248.64697265625,
        width=61.10302734375,
        height=59.17755126953125
    )

    button_image_2 = PhotoImage(
        file="assets/button_2.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(8),
        relief="flat",
        activebackground='black'
    )
    button_2.place(
        x=101.29248046875,
        y=248.64697265625,
        width=61.10302734375,
        height=59.17755126953125
    )

    button_image_3 = PhotoImage(
        file="assets/button_3.png")
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(9),
        activebackground='black',
        relief="flat",
    )
    button_3.place(
        x=182.5947265625,
        y=248.64697265625,
        width=61.10302734375,
        height=59.17755126953125
    )

    button_image_4 = PhotoImage(
        file="assets/button_4.png")
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(1),
        relief="flat",
        activebackground='black'
    )
    button_4.place(
        x=21.0,
        y=399.599853515625,
        width=61.10302734375,
        height=59.177490234375
    )

    button_image_5 = PhotoImage(
        file="assets/button_5.png")
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(0),
        relief="flat",
        activebackground='black'
    )
    button_5.place(
        x=21.0,
        y=474.0,
        width=141.0,
        height=59.0
    )

    button_image_6 = PhotoImage(
        file="assets/button_6.png")
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(2),
        relief="flat",
        activebackground='black'
    )
    button_6.place(
        x=101.29248046875,
        y=399.599853515625,
        width=61.10302734375,
        height=59.177490234375
    )

    button_image_7 = PhotoImage(
        file="assets/button_7.png")
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(3),
        relief="flat",
        activebackground='black'
    )
    button_7.place(
        x=182.5947265625,
        y=399.599853515625,
        width=61.10302734375,
        height=59.177490234375
    )

    button_image_8 = PhotoImage(
        file="assets/button_8.png")
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click('.'),
        relief="flat",
        activebackground='black'
    )
    button_8.place(
        x=182.5947265625,
        y=473.822509765625,
        width=61.10302734375,
        height=59.177490234375
    )

    button_image_9 = PhotoImage(
        file="assets/button_9.png")
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(4),
        relief="flat",
        activebackground='black'
    )
    button_9.place(
        x=21.0,
        y=322.86962890625,
        width=61.10302734375,
        height=59.17755126953125
    )

    button_image_10 = PhotoImage(
        file="assets/button_10.png")
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(5),
        relief="flat",
        activebackground='black'
    )
    button_10.place(
        x=101.29248046875,
        y=322.86962890625,
        width=61.10302734375,
        height=59.17755126953125,
    )

    button_image_11 = PhotoImage(
        file="assets/button_11.png")
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click(6),
        relief="flat",
        activebackground='black'
    )
    button_11.place(
        x=182.5947265625,
        y=322.86962890625,
        width=61.10302734375,
        height=59.17755126953125
    )

    button_image_12 = PhotoImage(
        file="assets/button_12.png")
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click("-"),
        relief="flat",
        activebackground='black'
    )
    button_12.place(
        x=263.392578125,
        y=245.637939453125,
        width=61.10302734375,
        height=59.17755126953125,
    )

    button_image_13 = PhotoImage(
        file="assets/button_13.png")
    button_13 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=clear,
        relief="flat",
        activebackground='black'
    )
    button_13.place(
        x=21.5048828125,
        y=171.41522216796875,
        width=61.10302734375,
        height=59.17755126953125
    )

    button_image_14 = PhotoImage(
        file="assets/button_14.png")
    button_14 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat",
        activebackground='black'
    )
    button_14.place(
        x=101.79736328125,
        y=171.41522216796875,
        width=61.10302734375,
        height=59.17755126953125
    )

    button_image_15 = PhotoImage(
        file="assets/button_15.png")
    button_15 = Button(
        image=button_image_15,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click('/'),
        relief="flat",
        activebackground='black'
    )
    button_15.place(
        x=183.10009765625,
        y=171.41522216796875,
        width=61.10302734375,
        height=59.17755126953125
    )

    button_image_16 = PhotoImage(
        file="assets/button_16.png")
    button_16 = Button(
        image=button_image_16,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click('*'),
        relief="flat",
        activebackground='black'
    )
    button_16.place(
        x=263.89697265625,
        y=171.41522216796875,
        width=61.10302734375,
        height=59.17755126953125
    )

    button_image_17 = PhotoImage(
        file="assets/button_17.png")
    button_17 = Button(
        image=button_image_17,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_click('+'),
        relief="flat",
        activebackground='black'
    )
    button_17.place(
        x=263.89697265625,
        y=324.8756103515625,
        width=61.10302734375,
        height=94.2828369140625
    )

    button_image_18 = PhotoImage(
        file="assets/button_18.png")
    button_18 = Button(
        image=button_image_18,
        borderwidth=0,
        highlightthickness=0,
        command=operate,
        relief="flat",
        activebackground='black'
    )
    button_18.place(
        x=263.392578125,
        y=438.7171630859375,
        width=61.10302734375,
        height=94.2828369140625,
    )
    window.resizable(False, False)
    window.mainloop()


def button_click(num):
    current = display.get()
    display.insert(0 + len(current), str(num))


def clear():
    display.delete(0, END)


def back():
    length = len(display.get())
    display.delete(length - 1, length)

def operate():
    exp = display.get()
    try:
        result = eval(exp)
    except:
        result = 'Invalid Input'
    display.delete(0, END)
    display.insert(0, result)


if __name__ == '__main__':

    window = Tk()

    window.geometry("347x566")
    window.configure(bg="#000000")
    window.title('GS Calculator')
    window.iconbitmap("assets/calculator.ico")

    canvas = Canvas(
        window,
        bg="#000000",
        height=566,
        width=347,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        672.0,
        1150.0,
        fill="#17181A",
        outline="")

    entry_image_1 = PhotoImage(
        file="assets/entry_1.png")
    entry_bg_1 = canvas.create_image(
        173.0,
        81.0,
        image=entry_image_1
    )
    display = Entry(
        bd=0,
        bg="#2C2B2B",
        fg='#ffffff',
        highlightthickness=0,
        font=('helvetica', 24),
        justify='center'
    )
    display.place(
        x=21.0,
        y=33.0,
        width=304.0,
        height=94.0,
    )

    main()
