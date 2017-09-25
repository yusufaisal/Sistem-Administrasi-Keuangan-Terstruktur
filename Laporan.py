class jurnal:
    def __init__(self,keterangan,deposit,profit,bulan,tahun):
        self.ket = keterangan
        self.dep = deposit
        self.profit = profit
        self.bln = bulan
        self.thn = tahun

def inputJurnal(DB):
    jurnal0 = jurnal("Perbaikan SC",250000000,0,1,2017)
    DB.append(jurnal0)
    jurnal1 = jurnal("Tes Mahasiswa Baru",0,1000000000,2,2017)
    DB.append(jurnal1)
    jurnal2 = jurnal("Denda Cetak KSM",0,500000000,3,2017)
    DB.append(jurnal2)
    jurnal3 = jurnal("Perbaikan GSG",750000000,0,4,2017)
    DB.append(jurnal3)
    jurnal4 = jurnal("Ujian Tengah Semester",600000000,0,5,2017)
    DB.append(jurnal4)
    jurnal5 = jurnal("Perbaikan Gedung Rektorat", 800000000, 0, 5, 2017)
    DB.append(jurnal5)

JurnalDB = []
inputJurnal(JurnalDB)

bulan = input ("Bulan: ")
tahun = input ("Tahun: ")

print "Bln/Tahun ||Profit     ||Deposit    ||Keterangan"
for j in range(len(JurnalDB)):
    if ((bulan == JurnalDB[j].bln) & (tahun == JurnalDB[j].thn)):
        print JurnalDB[j].bln,"/",JurnalDB[j].thn,"   ",JurnalDB[j].profit,"     ",JurnalDB[j].dep,"  ||  ",JurnalDB[j].ket