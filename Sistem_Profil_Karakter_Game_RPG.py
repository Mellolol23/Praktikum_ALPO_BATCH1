# 1. Membuat variabel profil karakter
nama_hero = "The Abbys"
level = 10
hp = 95.5
is_alive = True

inventory = ["Pedang", "Busur", "Perisai"]

atribut = {
    "kekuatan": 80,
    "kelincahan": 65
}

# 2. Menampilkan seluruh informasi karakter
print("=== PROFIL KARAKTER RPG ===")
print("Nama Hero:", nama_hero)
print("Level:", level)
print("HP:", hp)
print("Status Hidup:", is_alive)
print("Inventory:", inventory)
print("Atribut:", atribut)

# 3. Menampilkan tipe data setiap variabel
print("\n=== TIPE DATA ===")
print("Tipe nama_hero:", type(nama_hero))
print("Tipe level:", type(level))
print("Tipe hp:", type(hp))
print("Tipe is_alive:", type(is_alive))
print("Tipe inventory:", type(inventory))
print("Tipe atribut:", type(atribut))

# 4. Aksi karakter
# Menambahkan item baru ke inventory
inventory.append("Ramuan HP")

# Mengubah level menjadi float dan menambahkan 0.5
level = float(level)
level = level + 0.5

# 5. Menampilkan informasi terbaru
print("\n=== PROFIL KARAKTER TERBARU ===")
print("Nama Hero:", nama_hero)
print("Level:", level)
print("HP:", hp)
print("Status Hidup:", is_alive)
print("Inventory:", inventory)
print("Atribut:", atribut)
