import streamlit as st
from converter_gregorian import GregorianConverter
from converter_hijriah import HijriahConverter

st.set_page_config(
    page_title="Date Converter",
    page_icon="👋",
)

st.title("Date Converter")
st.markdown("### Pilih mode konversi tanggal berikut : ")
tipe_konversi = st.radio(
    "pilih opsi dibawah",
    ("Gregorian ke Julian Day", "Julian Day ke Gregorian", 
     "Hijriah ke Julian Day", "Julian Day ke Hijriah", 
     "Gregorian ke Hijriah", "Hijriah ke Gregorian")
)

bulan_greg = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
    "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}
bulan_greg_reverse = {v: k for k, v in bulan_greg.items()}

bulan_hijriah = {
    "Muharram": 1, "Safar": 2, "Rabiul Awwal": 3, "Rabiul Akhir": 4,
    "Jumadil Ula": 5, "Jumadil Akhir": 6, "Rajab": 7, "Sya'ban": 8,
    "Ramadhan": 9, "Syawal": 10, "Dzulqa'dah": 11, "Dzulhijjah": 12
}
bulan_hijriah_reverse = {v: k for k, v in bulan_hijriah.items()}


# Gregorian → JD
if tipe_konversi == "Gregorian ke Julian Day":
    with st.form("GregJD"):
        hari = st.number_input("Masukan tanggal:", value=1, min_value=1, max_value=31, key="hari_greg_jd")
        bulan = st.selectbox("Pilih bulan:", list(bulan_greg.keys()), key="bulan_greg_jd")
        tahun = st.number_input("Masukan tahun:", value=2025, min_value=-4713, max_value=2500, key="tahun_greg_jd")
        submit_Greg = st.form_submit_button("Konversi")

    if submit_Greg:
        bulan_angka = bulan_greg[bulan]
        try:
            jd_val = GregorianConverter(year=tahun, month=bulan_angka, day=hari).to_JD()
            st.success(f"Julian Day: {jd_val}")
        except ValueError as e:
            st.error(f"Error: {e}")


# JD → Gregorian
elif tipe_konversi == "Julian Day ke Gregorian":
    with st.form("JDGreg"):
        JD = st.number_input("Masukan Julian Day:", value=2460676.5, step=0.5, key="jd_to_greg")
        submit_JD = st.form_submit_button("Konversi")

    if submit_JD:
        d, m, y = GregorianConverter(JD=JD).from_JD()
        st.success(f"Tanggal Gregorian : {d} {bulan_greg_reverse[m]} {y}")


# Hijriah → JD
elif tipe_konversi == "Hijriah ke Julian Day":
    with st.form("HijJD"):
        hari = st.number_input("Masukan tanggal:", value=1, min_value=1, max_value=30, key="hari_hij_jd")
        bulan = st.selectbox("Pilih bulan:", list(bulan_hijriah.keys()), key="bulan_hij_jd")
        tahun = st.number_input("Masukan tahun Hijriah:", value=1447, min_value=1, max_value=3000, key="tahun_hij_jd")
        submit_Hijriah = st.form_submit_button("Konversi")

    if submit_Hijriah:
        bulan_angka = bulan_hijriah[bulan]
        jd_val = HijriahConverter(year=tahun, month=bulan_angka, day=hari).to_JD()
        st.success(f"Julian Day: {jd_val}")


# JD → Hijriah
elif tipe_konversi == "Julian Day ke Hijriah":
    with st.form("JDHij"):
        JD = st.number_input("Masukan Julian Day:", value=2460676.5, step=0.5, key="jd_to_hij")
        submit_JD = st.form_submit_button("Konversi")

    if submit_JD:
        d, m, y = HijriahConverter(JD=JD).from_JD()
        st.success(f"Tanggal Hijriah : {d} {bulan_hijriah_reverse[m]} {y} H")


# Gregorian → Hijriah
elif tipe_konversi == "Gregorian ke Hijriah":
    with st.form("GregHij"):
        hari = st.number_input("Masukan tanggal:", value=1, min_value=1, max_value=31, key="hari_greg_hij")
        bulan = st.selectbox("Pilih bulan:", list(bulan_greg.keys()), key="bulan_greg_hij")
        tahun = st.number_input("Masukan tahun:", value=2025, min_value=-4713, max_value=2500, key="tahun_greg_hij")
        submit_GregHij = st.form_submit_button("Konversi")

    if submit_GregHij:
        bulan_angka = bulan_greg[bulan]
        jd_val = GregorianConverter(year=tahun, month=bulan_angka, day=hari).to_JD()
        d, m, y = HijriahConverter(JD=jd_val).from_JD()
        st.success(f"Tanggal Hijriah: {d} {bulan_hijriah_reverse[m]} {y} H (JD: {jd_val})")


# Hijriah → Gregorian
elif tipe_konversi == "Hijriah ke Gregorian":
    with st.form("HijGreg"):
        hari = st.number_input("Masukan tanggal:", value=1, min_value=1, max_value=30, key="hari_hij_greg")
        bulan = st.selectbox("Pilih bulan:", list(bulan_hijriah.keys()), key="bulan_hij_greg")
        tahun = st.number_input("Masukan tahun:", value=1446, min_value=1, max_value=2000, key="tahun_hij_greg")
        submit_HijGreg = st.form_submit_button("Konversi")

    if submit_HijGreg:
        bulan_angka = bulan_hijriah[bulan]
        jd_val = HijriahConverter(year=tahun, month=bulan_angka, day=hari).to_JD()
        d, m, y = GregorianConverter(JD=jd_val).from_JD()
        st.success(f"Tanggal Gregorian: {d} {bulan_greg_reverse[m]} {y} (JD: {jd_val})")
