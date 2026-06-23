import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================

st.set_page_config(
    page_title="Kalkulator FPB & KPK",
    page_icon="🧮",
    layout="wide"
)

# =====================================
# RIWAYAT
# =====================================

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

# =====================================
# TEMA SOFT BLUE
# =====================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        180deg,
        #EAF6FF,
        #D9F0FF,
        #CBE8FF
    );
}

/* Judul */

h1{
    text-align:center;
    color:#0D47A1;
    text-shadow:1px 1px 3px white;
}

h2,h3{
    color:#1565C0;
}

p{
    color:#37474F;
}

/* Tombol */

.stButton > button{

    width:100%;
    height:60px;

    border-radius:18px;

    border:none;

    font-size:20px;

    font-weight:bold;

    color:white;

    background:linear-gradient(
        90deg,
        #ff6b6b,
        #feca57,
        #1dd1a1,
        #54a0ff,
        #5f27cd
    );

}

/* Sidebar */

[data-testid="stSidebar"]{

    background:linear-gradient(
        180deg,
        #E3F2FD,
        #D6EEFF,
        #C8E6FF
    );

}

/* Input */

.stNumberInput{

    background:white;

    padding:10px;

    border-radius:10px;

}

/* Kotak alert */

div[data-testid="stAlert"]{

    border-radius:12px;

}

</style>
""", unsafe_allow_html=True)

# =====================================
# FUNGSI FPB
# =====================================

def hitung_fpb(a, b):

    langkah = []

    while b != 0:

        q = a // b
        r = a % b

        langkah.append({

            "a": a,
            "b": b,
            "q": q,
            "r": r

        })

        a, b = b, r

    return a, langkah

# =====================================
# HEADER
# =====================================

logo1, logo2 = st.columns([1,6])

with logo1:

    st.image("logo_undiksha.png", width=100)

with logo2:

    st.title("🧮 Kalkulator FPB & KPK")
    st.write("### Menggunakan Algoritma Euclid")

st.markdown(
"""
Masukkan dua bilangan bulat positif untuk menghitung:

- ✅ FPB (Faktor Persekutuan Terbesar)
- ✅ KPK (Kelipatan Persekutuan Terkecil)
- ✅ Relatif Prima
"""
)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("📚 Materi")

    st.info("""

Materi yang digunakan

✅ FPB

✅ KPK

✅ Algoritma Euclid

✅ Bilangan Relatif Prima

""")

    st.markdown("---")

    st.subheader("👨‍🎓 Identitas")

    st.write("Universitas Pendidikan Ganesha")

    st.write("Program Studi Pendidikan Matematika")

# =====================================
# INPUT
# =====================================

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    a = st.number_input(

        "Masukkan Bilangan Pertama",

        min_value=1,

        step=1

    )

with col2:

    b = st.number_input(

        "Masukkan Bilangan Kedua",

        min_value=1,

        step=1

    )

st.markdown("")

hitung = st.button("🧮 Hitung FPB & KPK")

# =====================================
# PROSES
# =====================================

if hitung:

    a = int(a)

    b = int(b)

    fpb, langkah = hitung_fpb(a, b)

    kpk = abs(a*b)//fpb

    # simpan riwayat

    st.session_state.riwayat.append({

        "a":a,

        "b":b,

        "fpb":fpb,

        "kpk":kpk

    })

    st.markdown("---")

    st.subheader("📊 Hasil Perhitungan")

    hasil1, hasil2 = st.columns(2)

    with hasil1:

        st.success(f"✅ FPB = {fpb}")

    with hasil2:

        st.success(f"🎯 KPK = {kpk}")

    if fpb == 1:

        st.success("✨ Kedua bilangan merupakan bilangan relatif prima.")

    else:

        st.warning("⚠ Kedua bilangan bukan merupakan bilangan relatif prima.")
          # =====================================
    # LANGKAH ALGORITMA EUCLID
    # =====================================

    st.markdown("---")
    st.subheader("📖 Langkah Algoritma Euclid")

    for i, item in enumerate(langkah, start=1):

        with st.expander(f"📌 Langkah {i}", expanded=True):

            st.write(f"**Bilangan yang dibagi :** {item['a']}")
            st.write(f"**Bilangan pembagi :** {item['b']}")
            st.write(f"**Hasil bagi :** {item['q']}")
            st.write(f"**Sisa :** {item['r']}")

            st.latex(
                f"{item['a']}={item['q']}\\times{item['b']}+{item['r']}"
            )

            if item["r"] != 0:

                st.info(
                    f"Karena sisa pembagian masih {item['r']}, maka proses dilanjutkan menggunakan pasangan ({item['b']}, {item['r']})."
                )

            else:

                st.success(
                    "Sisa pembagian sudah bernilai 0 sehingga proses Algoritma Euclid selesai."
                )

    # =====================================
    # MENENTUKAN FPB
    # =====================================

    st.markdown("---")
    st.subheader("🎯 Menentukan FPB")

    st.write(
        "FPB diperoleh dari sisa pembagian terakhir sebelum sisa menjadi 0."
    )

    x = a
    y = b

    while y != 0:

        st.write(
            f"FPB({x}, {y}) → FPB({y}, {x % y})"
        )

        x, y = y, x % y

    st.success(
        f"Jadi FPB({a}, {b}) = {fpb}"
    )

    # =====================================
    # MENENTUKAN KPK
    # =====================================

    st.markdown("---")

    st.subheader("🎯 Menentukan KPK")

    st.write(
        "Setelah memperoleh FPB, KPK dihitung menggunakan rumus:"
    )

    st.latex(
        r"KPK(a,b)=\frac{a\times b}{FPB(a,b)}"
    )

    st.write("Substitusi nilai:")

    st.latex(
        rf"KPK({a},{b})=\frac{{{a}\times{b}}}{{{fpb}}}"
    )

    st.latex(
        rf"=\frac{{{a*b}}}{{{fpb}}}"
    )

    st.latex(
        rf"={kpk}"
    )

    st.success(
        f"Jadi KPK({a}, {b}) = {kpk}"
    )

    # =====================================
    # INFORMASI BILANGAN
    # =====================================

    st.markdown("---")

    st.subheader("🧠 Informasi Bilangan")

    col1, col2 = st.columns(2)

    with col1:

        if a % 2 == 0:
            st.info(f"🔵 {a} merupakan bilangan genap.")
        else:
            st.info(f"🟠 {a} merupakan bilangan ganjil.")

    with col2:

        if b % 2 == 0:
            st.info(f"🔵 {b} merupakan bilangan genap.")
        else:
            st.info(f"🟠 {b} merupakan bilangan ganjil.")

    st.success(f"FPB = {fpb}")

    st.success(f"KPK = {kpk}")

# =====================================
# RIWAYAT PERHITUNGAN
# =====================================

st.markdown("---")

st.subheader("📜 Riwayat Perhitungan")

if len(st.session_state.riwayat) == 0:

    st.info("Belum ada riwayat perhitungan.")

else:

    nomor = 1

    for item in reversed(st.session_state.riwayat):

        st.write(
            f"**{nomor}.** "
            f"{item['a']} dan {item['b']} "
            f"→ FPB = **{item['fpb']}** | "
            f"KPK = **{item['kpk']}**"
        )

        nomor += 1

    if st.button("🗑 Hapus Riwayat"):

        st.session_state.riwayat.clear()

        st.rerun()

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;padding:15px;">
        <h4 style="color:#1565C0;">
            🏫 Universitas Pendidikan Ganesha
        </h4>

        <p>
            Aplikasi Kalkulator FPB & KPK menggunakan
            <b>Algoritma Euclid</b>
        </p>

        <p style="color:gray;">
            Dibuat menggunakan Python & Streamlit
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
