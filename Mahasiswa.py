import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import sqlite3

koneksi = sqlite3.connect('kampus.db')
jembatan = koneksi.cursor()

sql_create = "CREATE TABLE IF NOT EXISTS mahasiswa(idmhs integer primary key autoincrement, nama text, nomorhp text);"
jembatan.execute(sql_create)

def tombolsave():
    sql_insert = f"INSERT INTO mahasiswa(nama,nomorhp) VALUES('{entry_nama.get()}','{entry_NoTelp.get()}');"
    jembatan.execute(sql_insert)
    koneksi.commit()
    entry_nama.delete(0,END)
    entry_NoTelp.delete(0,END)
    

def tombolview():
    app = ttk.Toplevel(title="Daftar Info Mahasiswa")
    columns = [
        {
            'text' : 'ID',
            'stretch' : False
        },
        {
            'text' : 'Nama',
            'stretch' : False
        },
        {
            'text' : 'No. Telp',
            'stretch' : False
        }
    ]
    sql_select = "SELECT * FROM mahasiswa"
    jembatan.execute(sql_select)
    arraymahasiswa = jembatan.fetchall()
    tabel = Tableview(master=app,
                    coldata=columns,
                    rowdata=arraymahasiswa,
                    paginated=True,
                    autofit=False,
                    searchable=True,
                    bootstyle=PRIMARY)
    tabel.pack(fill=BOTH, expand=NO, padx=10, pady=10)
    app.mainloop()

aplikasi = ttk.Window(themename='superhero')
aplikasi.geometry("400x400")
aplikasi.title("Info Kampus")

labelku = ttk.Label(aplikasi, text="Input Data Mahasiswa")
labelku.pack(pady=30)
labelku.config(font=("Bell MT", 20, 'bold'))

frame_nama = ttk.Frame(aplikasi)
frame_nama.pack(padx=10, pady=10, fill="x")
#--------------------- Frame Nama ---------------------------
label_nama = ttk.Label(frame_nama, text="Nama")
label_nama.pack(side="left", padx=10)
entry_nama = ttk.Entry(frame_nama)
entry_nama.pack(side='left',padx=5, fill="x",expand=True)


frame_NoTelp = ttk.Frame(aplikasi)
frame_NoTelp.pack(padx=10, pady=10, fill="x")
#--------------------- Frame No Telp ------------------------
label_NoTelp = ttk.Label(frame_NoTelp, text="No. Telp")
label_NoTelp.pack(side="left", padx=5)
entry_NoTelp = ttk.Entry(frame_NoTelp)
entry_NoTelp.pack(side="left",padx=5,fill="x",expand=True)


frame_tombol = ttk.Frame(aplikasi)
frame_tombol.pack(padx=10, pady=10, fill="x")
button_save = ttk.Button(frame_tombol, text="Save", bootstyle='success', command=tombolsave)
button_save.pack(side="left", padx=15)

button_view = ttk.Button(frame_tombol, text="View Data", bootstyle='info', command=tombolview)
button_view.pack(side="left", padx=10)

aplikasi.mainloop()
koneksi.close()