#önce kütüphaneyi trinter ile içeri atıyoruz
import tkinter as tk
#burada buton işlevi ekliyoruz
def button_click(symbol):
    if symbol == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Hata!")
    elif symbol == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, symbol)
#burada ise arayüz oluşturuyoruz
root = tk.Tk()
root.title("pyhton hesap makinesii")
root.geometry("300x400")
root.configure(bg="#FF0000")
#burada ekranın yüksekliği felan filan var
display = tk.Entry(root, width=30, borderwidth=5, bg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#tuşları oluşturup renk veriyoruz
buttons = [
    ("7", "#c9c9c9"), ("8", "#c9c9c9"), ("9", "#c9c9c9"), ("/", "#ffa500"),
    ("4", "#c9c9c9"), ("5", "#c9c9c9"), ("6", "#c9c9c9"), ("*", "#ffa500"),
    ("1", "#c9c9c9"), ("2", "#c9c9c9"), ("3", "#c9c9c9"), ("-", "#ffa500"),
    ("0", "#c9c9c9"), (".", "#c9c9c9"), ("=", "#008000"), ("+", "#ffa500"),
    ("C", "#ff6347")
]
#butonları ekrana yerleştirme ve aktif ederek işi bitirıyoruz
row_num = 1
col_num = 0
for button_symbol, button_color in buttons:
    tk.Button(root, text=button_symbol, padx=20, pady=20, bg=button_color, command=lambda symbol=button_symbol: button_click(symbol)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num == 4:
        col_num = 0
        row_num += 1

root.mainloop()
