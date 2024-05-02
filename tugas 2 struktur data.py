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
peta.menambahkanKota("Kediri")
peta.menambahkanKota("Tulungagung")
peta.menambahkanKota("Blitar")
peta.menambahkanEdge("Surabaya", "Sidoarjo", 37.8 )
peta.menambahkanEdge("Sidoarjo", "Pasuruan", 43.8 )
peta.menambahkanEdge("Sidoarjo", "Malang", 69.8 )
peta.menambahkanEdge("Mojokerto", "Sidoarjo", 30.9 )
peta.menambahkanEdge("Lamongan", "Surabaya", 46.4 )
peta.menambahkanEdge("Bojonegoro", "Lamongan", 88.1 )
peta.menambahkanEdge("Kediri", "Mojokerto", 80.2 )
peta.menambahkanEdge("Blitar", "Malang", 76.1 )
peta.menambahkanEdge("Kediri", "Tulungagung", 35.1 )
peta.menambahkanEdge("Tulungagung", "Blitar", 29.2 )

peta.print()
