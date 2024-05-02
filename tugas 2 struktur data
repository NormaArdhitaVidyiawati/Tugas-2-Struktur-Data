class map:
    def __init__(self):
        self.daftarKota = {}
    
    def menambahkanKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
    
    def print(self):
        for kota in self.daftarKota:
            print(f"{kota} -- {self.daftarKota[kota]}")
    
    def menambahkanEdge(self, kota1, kota2, jarak):
        if kota1 and kota2 in self.daftarKota:
            self.daftarKota[kota1][kota2] = jarak
            self.daftarKota[kota2][kota1] = jarak
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]

    def hapusJalan(self, kota1, kota2):
        if kota1 and kota2 in self.daftarKota:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]

peta = map()
peta.menambahkanKota("Surabaya")
peta.menambahkanKota("Sidoarjo")
peta.menambahkanKota("Mojokerto")
peta.menambahkanKota("Pasuruan")
peta.menambahkanKota("Malang")
peta.menambahkanKota("Lamongan")
