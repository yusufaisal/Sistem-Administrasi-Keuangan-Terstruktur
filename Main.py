import Penerimaan
import Belanja
import Jurnal
import Posting

def login():
    username = raw_input("Username : ")
    password = raw_input("Password : ")
    if username=="admin" and password=="admin":
        return True

if __name__=='__main__':
    PenerimaanDB = []
    BelanjaDB = []
    JurnalDB = []

    # Login
    Session = login()

    if Session==True:
        pilihan = 1
        while (pilihan != "0"):
            print ""
            print "Menu:"
            print "1. Input Penerimaan"
            print "2. Input Belanja"
            print "3. Import Penerimaan & Belanja to Jurnal"
            print "4. Laporan Jurnal"
            print "5. Laporan Tutup Buku"
            print "0. Exit"
            pilihan = raw_input("Pilihan : ")

            if (pilihan == "1"):
                Penerimaan.CreatePenerimaan(PenerimaanDB)
            elif (pilihan == "2"):
                Belanja.CreateBelanja(BelanjaDB)
            elif (pilihan == "3"):
                Jurnal.CreateJurnal(JurnalDB,PenerimaanDB,BelanjaDB)
            elif (pilihan == "4"):
                None