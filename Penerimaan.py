from collections import namedtuple

SistemPenerimaan = namedtuple("SistemPenerimaan","keterangan, profit, bulan, tahun")

def CreatePenerimaan(DB):
    print "Data Penerimaan"
    keterangan = raw_input("Keterangan : ")
    profit = input("Profit : ")
    bulan = input("Bulan : ")
    tahun = input("Tahun : ")

    # Create Struck to add inputs
    Input = SistemPenerimaan(keterangan, profit, bulan, tahun)
    # Add to array DB
    DB.append(Input)