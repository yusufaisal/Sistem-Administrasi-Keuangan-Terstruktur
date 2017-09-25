from collections import namedtuple

SistemBelanja = namedtuple("SistemBelanja", "keterangan deposit bulan tahun")

def CreateBelanja(DB):
    print "Data Belanja"
    keterangan = raw_input("Keterangan : ")
    deposit = input("Deposit : ")
    bulan = input("Bulan : ")
    tahun = input("Tahun : ")

    # Create Struct to add inputs
    Input = SistemBelanja(keterangan, deposit, bulan, tahun)
    # Add to array DB
    DB.append(Input)