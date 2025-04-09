class KTP:
    def __init__(self):
        self._nama = ""
        self._nik = ""
        self._tempat_lahir = ""
        self._tanggal_lahir = ""
        self._alamat = ""
        self._jenis_kelamin = ""
        self._agama = ""
        self._status_perkawinan = ""
        self._pekerjaan = ""
        self._kewarganegaraan = ""

    def set_nama(self, nama):
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong.")
        self._nama = nama

    def get_nama(self):
        return self._nama

    def set_nik(self, nik):
        if not nik.isdigit() or len(nik) != 16:
            raise ValueError("NIK harus terdiri dari 16 digit angka.")
        self._nik = nik

    def get_nik(self):
        return self._nik

    def set_tempat_lahir(self, tempat):
        if not tempat.strip():
            raise ValueError("Tempat lahir tidak boleh kosong.")
        self._tempat_lahir = tempat

    def get_tempat_lahir(self):
        return self._tempat_lahir

    def set_tanggal_lahir(self, tanggal):
        if not tanggal.strip():
            raise ValueError("Tanggal lahir tidak boleh kosong.")
        self._tanggal_lahir = tanggal

    def get_tanggal_lahir(self):
        return self._tanggal_lahir

    def set_alamat(self, alamat):
        if not alamat.strip():
            raise ValueError("Alamat tidak boleh kosong.")
        self._alamat = alamat

    def get_alamat(self):
        return self._alamat

    def set_jenis_kelamin(self, jenis):
        if jenis not in ["Laki-laki", "Perempuan"]:
            raise ValueError("Jenis kelamin harus 'Laki-laki' atau 'Perempuan'.")
        self._jenis_kelamin = jenis

    def get_jenis_kelamin(self):
        return self._jenis_kelamin

    def set_agama(self, agama):
        if not agama.strip():
            raise ValueError("Agama tidak boleh kosong.")
        self._agama = agama

    def get_agama(self):
        return self._agama

    def set_status_perkawinan(self, status):
        if status not in ["Belum Kawin", "Kawin", "Cerai"]:
            raise ValueError("Status perkawinan harus Belum Kawin, Kawin, atau Cerai.")
        self._status_perkawinan = status

    def get_status_perkawinan(self):
        return self._status_perkawinan

    def set_pekerjaan(self, pekerjaan):
        if not pekerjaan.strip():
            raise ValueError("Pekerjaan tidak boleh kosong.")
        self._pekerjaan = pekerjaan

    def get_pekerjaan(self):
        return self._pekerjaan

    def set_kewarganegaraan(self, kewarganegaraan):
        if kewarganegaraan.upper() not in ["WNI", "WNA"]:
            raise ValueError("Kewarganegaraan harus WNI atau WNA.")
        self._kewarganegaraan = kewarganegaraan.upper()

    def get_kewarganegaraan(self):
        return self._kewarganegaraan
