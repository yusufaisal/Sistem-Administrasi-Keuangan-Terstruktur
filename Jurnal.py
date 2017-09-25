from collections import namedtuple

Jurnal = namedtuple("Jurnal","keterangan, deposit, profit, bulan, tahun")

def CreateJurnal(JurnalDB,PenerimaanDB, BelanjaDB):
    JurnalDB.
    for i in range(len(BelanjaDB)):
        KETERANGAN = BelanjaDB[i].keterangan
        DEPOSIT = BelanjaDB[i].deposit
        BULAN = BelanjaDB[i].bulan
        TAHUN = BelanjaDB[i].tahun

        jurnal_belanja = Jurnal(KETERANGAN, DEPOSIT, 0, BULAN, TAHUN)

        JurnalDB.append(jurnal_belanja)

    for j in range(len(PenerimaanDB)):
        KETERANGAN = PenerimaanDB[j].keterangan
        PROFIT = PenerimaanDB[j].profit
        BULAN = PenerimaanDB[j].bulan
        TAHUN = PenerimaanDB[j].tahun

        Jurnal_penerimaan = Jurnal(KETERANGAN, 0, PROFIT, BULAN, TAHUN)

        JurnalDB.append(Jurnal_penerimaan)
    print JurnalDB