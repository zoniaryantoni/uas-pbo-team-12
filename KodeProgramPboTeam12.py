from tkinter import *
from tkinter import messagebox

class PemesananMakananGUI:

    def __init__(self, window):
        self.window = window
        self.window.title("Pemesanan Makanan")
        self.window.configure(bg="light blue")
        self.window.geometry("400x200")

        # Daftar menu dan harga
        self.daftar_menu = {
            "Nasi Goreng": 15000,
            "Mie Goreng": 12000,
            "Ayam Bakar": 20000,
            "Sate Ayam": 15000,
            "Gado-Gado": 10000,
            "Rendang": 25000
        }


        # Membuat label dan dropdown untuk pesanan
        self.label_pesanan = Label(window, text="Pesanan:")
        self.label_pesanan.pack()
        self.dropdown_pesanan = OptionMenu(window, StringVar(), *self.daftar_menu.keys())
        self.dropdown_pesanan.pack()

        # Membuat label dan input untuk jumlah pesanan
        self.label_jumlah = Label(window, text="Jumlah:")
        self.label_jumlah.pack()
        self.entry_jumlah = Entry(window)
        self.entry_jumlah.pack()

        # Membuat tombol pesan
        self.tombol_pesan = Button(window, text="Pesan", command=self.pesan_makanan)
        self.tombol_pesan.pack()

        # Membuat label untuk output pesanan
        self.label_output = Label(window, text="")
        self.label_output.pack()

    def pesan_makanan(self):
        pesanan = self.dropdown_pesanan.cget("text")
        jumlah = self.entry_jumlah.get()

        if pesanan.strip() == "" or jumlah.strip() == "":
            self.label_output.config(text="Silakan isi nama dan jumlah pesanan!")
            return

        try:
            jumlah = int(jumlah)
        except ValueError:
            self.label_output.config(text="Jumlah pesanan harus berupa angka!")
            return

        if pesanan not in self.daftar_menu:
            self.label_output.config(text="Pesanan tidak valid!")
            return

        harga = self.daftar_menu[pesanan]
        total_harga = harga * jumlah

        # Proses pemesanan makanan di sini
        # Anda bisa menambahkan kode logika untuk mengirim pesanan ke sistem atau melakukan tindakan lain sesuai kebutuhan

        # Contoh output untuk tujuan demonstrasi
        output_text = f"Terima kasih !, Pesanan Anda untuk {jumlah} {pesanan} telah diterima.\n" \
                      f"Total harga: Rp {total_harga}"

        self.label_output.config(text=output_text)


def check_login():
    username = username_entry.get()
    alamat = password_entry.get()

    # Lakukan pengecekan login dengan username dan password yang sudah ditentukan
    if username  and alamat  :
        # Jika login berhasil, tampilkan pesan sukses dan buka jendela pemesanan makanan
        messagebox.showinfo("Selamat Datang ", "Halo, " + username + "!")
        login_window.destroy()  # Tutup jendela login
        # Membuat jendela utama
        window = Tk()

        # Membuat objek GUI pemesanan makanan
        pemesanan_gui = PemesananMakananGUI(window)

        # Menjalankan GUI
        window.mainloop()
    else:
        # Jika login gagal, tampilkan pesan error
        messagebox.showerror("Silahkan diisi","Tolong diisi")


# Membuat jendela login
login_window = Tk()
login_window.geometry("400x200")
login_window.title("Login Admin")
login_window.configure(bg="blue")
label = Label(login_window, text="Silahkan Masukkan Nama  dan Alamat Anda",bg="blue" ,font=('Verdana bold', 12))
label.pack(pady=20)

# Membuat frame untuk input login
frame_login = Frame(login_window)
frame_login.pack()

# Menambahkan input untuk username dan password
username_label = Label(frame_login, text="Nama:", bg="blue")
username_label.grid(row=0, column=0, sticky=W, pady=10)
username_entry = Entry(frame_login, width=20)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = Label(frame_login, text="Alamat:", bg="blue")
password_label.grid(row=1, column=0, sticky=W, pady=10)
password_entry = Entry(frame_login,  width=20)
password_entry.grid(row=1, column=1)

# Menambahkan button login
login_button = Button(frame_login, text="Masuk", command=check_login)
login_button.grid(row=2, column=1, padx=10, pady=10)

# Menjalankan jendela login
login_window.mainloop()
