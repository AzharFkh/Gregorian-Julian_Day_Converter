import streamlit as st

st.set_page_config(
    page_title="Date Converter",
    page_icon="👋",
)

st.title("Date Converter")
st.markdown("### Pilih mode konversi tanggal berikut : ")
tipe_konversi = st.radio(
    "pilih opsi dibawah",
    ("Gregorian ke Julian Day", "Julian Day ke Gregorian")
)

bulan_map = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
    "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}

bulan_map_reverse = {v: k for k, v in bulan_map.items()}


class converter_date():
    def __init__(self, year = 2025, month=1, day=1, JD=None):
        self.year = year
        self.month = month
        self.day = day
        self.JD = JD

    def tahun_kabisat(self):
        """Return True if leap year, else False"""
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False

    def ke_JD(self):
        A = int(self.year / 100)

        if self.year > 1582:
            B = 2 + int(A / 4) - A
        elif self.year < 1582:
            B = 0
        else:  # tahun == 1582
            if self.month > 10 or (self.month == 10 and self.day >= 15):
                B = 2 + int(A / 4) - A
            else:
                B = 0

        kabisat = self.tahun_kabisat()

        if self.month == 2 and self.day > (29 if kabisat else 28):
            raise ValueError("Tanggal tidak valid untuk Februari di tahun ini")

        JD = 1720994.5 + int(365.25 * self.year) + int(30.6 * (self.month + 1)) + B + self.day
        return JD

    def ke_Gregorian(self):
        JD = self.JD + 0.5
        Z = int(JD)
        F = JD - Z

        if Z < 2299161:
            A = Z
        else:
            alpha = int((Z - 1867216.25) / 36524.25)
            A = Z + 1 + alpha - int(alpha / 4)

        B = A + 1524
        C = int((B - 122.1) / 365.25)
        D = int(365.25 * C)
        E = int((B - D) / 30.6001)

        day = B - D - int(30.6001 * E) + F
        if E < 14:
            month = E - 1
        else:
            month = E - 13

        if month > 2:
            year = C - 4716
        else:
            year = C - 4715

        self.day, self.month, self.year = int(day), month, year
        return self.day, self.month, self.year

if tipe_konversi == "Gregorian ke Julian Day":
    st.markdown("### Masukan tanggal Gregorian untuk dikonversi ke JD:")

    with st.form("dateToConvert"):
        hari = st.number_input("Masukan tanggal:", value=1, min_value=1, max_value=31, key="hari")
        bulan = st.selectbox(
            "Pilih bulan:",
            list(bulan_map.keys()),
            key="bulan"
        )
        tahun = st.number_input("Masukan tahun:", value=2025, min_value=-4713, max_value=2500, key="tahun")
        submit_Greg = st.form_submit_button("Konversi")

    if submit_Greg:
        bulan_angka = bulan_map[bulan]
        try:
            JD_Date = converter_date(tahun, bulan_angka, hari)
            st.success(f"Julian Day: {JD_Date.ke_JD()}")
        except ValueError as e:
            st.error(f"Error: {e}")


elif tipe_konversi == "Julian Day ke Gregorian":
    st.markdown("### Masukan Julian Day untuk dikonversi ke Gregorian:")

    with st.form("JDToDate"):
        JD = st.number_input("Masukan Julian Day:", value=2460676.5, step=0.5, key="JD")
        submit_JD = st.form_submit_button("Konversi")

    if submit_JD:
        JD_to_Date = converter_date(JD=JD)
        tanggal, bulan, tahun = JD_to_Date.ke_Gregorian()
        nama_bulan = bulan_map_reverse[bulan]
        st.success(f"Tanggal Gregorian : {tanggal}, {nama_bulan} {tahun}")