class MesinTuring:
    def __init__(self, pita, aturan, state_awal, state_halt):
        self.pita = list(pita)
        self.kepala = 0
        self.state = state_awal
        self.aturan = aturan
        self.state_halt = state_halt
        self.context = {}  # Context untuk eksekusi kode Python

    def cetak_pita(self):
        # Tambahkan padding untuk memastikan lebar simbol seragam
        pita_str = ''
        for i, simbol in enumerate(self.pita):
            if simbol == '\n':
                pita_str += '| \\n '  # Tampilkan \n sebagai string literal
            else:
                pita_str += f'| {simbol:<2} '  # Padding kiri dan kanan
        pita_str += '|'

        # Cetak penunjuk kepala
        kepala_str = ''
        for i in range(len(self.pita)):
            if i == self.kepala:
                kepala_str += '  ^ '  # Pastikan panah sesuai padding
            else:
                kepala_str += '     '
        print(pita_str)
        print(kepala_str)


    def jalankan(self):
        langkah = 0
        while self.state != self.state_halt:
            simbol = self.pita[self.kepala] if self.kepala < len(self.pita) else ' '
            key = (self.state, simbol)
            aksi = self.aturan.get(key, None)
            if aksi is None:
                print(f"Langkah {langkah}: Tidak ada aksi untuk keadaan {self.state} dan simbol '{simbol}'. Mesin berhenti.")
                break

            # Proses aksi
            print(f"Langkah {langkah}:")
            print(f"  Keadaan saat ini: {self.state}")
            print(f"  Kepala membaca simbol: '{simbol}'")
            print(f"  Menulis simbol: '{aksi['tulis']}'")
            # Tulis simbol baru
            if self.kepala < len(self.pita):
                self.pita[self.kepala] = aksi['tulis']
            else:
                self.pita.append(aksi['tulis'])

            # Cetak pita dan posisi kepala
            self.cetak_pita()

            # Gerakkan kepala
            gerakan = aksi['gerak']
            self.kepala += 1 if gerakan == 'R' else -1
            self.kepala = max(0, self.kepala)  # Hindari indeks negatif

            # Ubah keadaan
            prev_state = self.state
            self.state = aksi['state_baru']
            print(f"  Kepala bergerak ke: {'Kanan' if gerakan == 'R' else 'Kiri'}")
            print(f"  Mengubah keadaan dari {prev_state} ke {self.state}\n")
            langkah += 1

        # Eksekusi pita
        if self.state == self.state_halt:
            kode = ''.join(self.pita).strip()
            print(f"Hasil eksekusi pita:\n{kode}\n")
            try:
                exec(kode, self.context)
                hasil = self.context.get("d", None)  # Ambil nilai variabel d
                print(f"Hasil eksekusi: {hasil}")
            except Exception as e:
                print(f"Kesalahan saat eksekusi pita: {e}")

# Pita input
input_pita = "a=5\nb=2\nc=3\nd=a+b-c\nprint(d)"

# Tabel instruksi (sesuai dengan perbaikan sebelumnya)
aturan = {
    ('q0', 'a'): {'tulis': 'a', 'gerak': 'R', 'state_baru': 'q0'},
    ('q0', '='): {'tulis': '=', 'gerak': 'R', 'state_baru': 'q1'},
    ('q1', '5'): {'tulis': '5', 'gerak': 'R', 'state_baru': 'q2'},
    ('q2', '\n'): {'tulis': '\n', 'gerak': 'R', 'state_baru': 'q0'},
    ('q0', 'b'): {'tulis': 'b', 'gerak': 'R', 'state_baru': 'q0'},
    ('q1', '2'): {'tulis': '2', 'gerak': 'R', 'state_baru': 'q2'},
    ('q0', 'c'): {'tulis': 'c', 'gerak': 'R', 'state_baru': 'q0'},
    ('q1', '3'): {'tulis': '3', 'gerak': 'R', 'state_baru': 'q2'},
    ('q0', 'd'): {'tulis': 'd', 'gerak': 'R', 'state_baru': 'q0'},
    ('q1', 'a'): {'tulis': 'a', 'gerak': 'R', 'state_baru': 'q1'},
    ('q1', '+'): {'tulis': '+', 'gerak': 'R', 'state_baru': 'q1'},
    ('q1', 'b'): {'tulis': 'b', 'gerak': 'R', 'state_baru': 'q1'},
    ('q1', '-'): {'tulis': '-', 'gerak': 'R', 'state_baru': 'q1'},
    ('q1', 'c'): {'tulis': 'c', 'gerak': 'R', 'state_baru': 'q1'},
    ('q1', '\n'): {'tulis': '\n', 'gerak': 'R', 'state_baru': 'q0'},
    ('q0', '+'): {'tulis': '+', 'gerak': 'R', 'state_baru': 'q0'},
    ('q0', '-'): {'tulis': '-', 'gerak': 'R', 'state_baru': 'q0'},
    ('q0', 'p'): {'tulis': 'p', 'gerak': 'R', 'state_baru': 'q3'},
    ('q3', 'r'): {'tulis': 'r', 'gerak': 'R', 'state_baru': 'q3'},
    ('q3', 'i'): {'tulis': 'i', 'gerak': 'R', 'state_baru': 'q3'},
    ('q3', 'n'): {'tulis': 'n', 'gerak': 'R', 'state_baru': 'q3'},
    ('q3', 't'): {'tulis': 't', 'gerak': 'R', 'state_baru': 'q4'},
    ('q4', '('): {'tulis': '(', 'gerak': 'R', 'state_baru': 'q5'},
    ('q5', 'd'): {'tulis': 'd', 'gerak': 'R', 'state_baru': 'q5'},
    ('q5', ')'): {'tulis': ')', 'gerak': 'R', 'state_baru': 'qH'},
}

# Jalankan Mesin Turing
state_awal = 'q0'
state_halt = 'qH'

mesin = MesinTuring(input_pita, aturan, state_awal, state_halt)
mesin.jalankan()