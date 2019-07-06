# Variabel global untuk menyimpan data Buku
buku = []


# 1 fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print "haduh hekel ngapain mau hack wa sih"
        print "Hekel Ko Script Kidde ups:v"
    else:
        for indeks in range(len(buku)):
            print "[%d] %s" % (indeks, buku[indeks])


# 2 fungsi untuk menambah data
def insert_data():
    buku_baru = raw_input("Masukan Nomor korban :")
    buku.append(buku_baru)
    print "Nomor telepon salah sob!!"

# 3 fungsi untuk edit data
def hack_data():
    show_data()
    indeks = input("Masukan No Target :")
    if(indeks > len(buku)):
        print "Nomor telepon Togel iyaa?"
    
        
# 4 fungsi untuk menampilkan semua data
def berak_data():
    if len(buku) <= 0:
        print "Liat-liat ada Hekel lagi NgeHack wkwk"
    else:
        for indeks in range(len(buku)):
            print "[%d] %s" % (indeks, buku[indeks])

# 5 fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print "Hekel Ko Script Kidde ups:v"
    else:
        for indeks in range(len(buku)):
            print "[%d] %s" % (indeks, buku[indeks])

# 6 fungsi untuk edit data
def hack_data():
    show_data()
    indeks = input("Masukan No Target :")
    if(indeks > len(buku)):
        print "Nomor telepon Togel iyaa?"

#  7 fungsi untuk menambah data
def insert_data():
    buku_baru = raw_input("Masukan Nomor korban :")
    buku.append(buku_baru)
    print "Nomor telepon salah sob!!"

# 8 fungsi untuk menampilkan semua data
def rash_data():
    if len(buku) <= 0:
        print "Mau Metode apa hekel:v"
        print "cari di google sana"
    else:
        for indeks in range(len(buku)):
            print "[%d] %s" % (indeks, buku[indeks])


# fungsi untuk menampilkan menu
def show_menu():
    print "\n"
    print "######################################################"
    print            "Tools Mr ezaa Was Here"
    print "Website:https://anakwhitehat.blogspot.com"
    print  "Github:https://github.com/R23SH"
    print  "contant Me: 0838*****71"
    print  "Thanks Support: MWH Team CAT Team DPC Team UMC Team"
    print "######################################################"
    print "[1] Sadap Whatsapp"
    print "[2] Hack Facebook"
    print "[3] Hack Instagram"
    print "[4] carding Via amazon"
    print "[5] Hack Twitter"
    print "[6] Lacak Lokasi"
    print "[7] Website Phising"
    print "[8] Metode Deface Web"
    print "[9] SQL Injection"
    print "[10] Website Vuln"
    print "[11] membuat Web Server"
    print "[12] Metasploit"
    print "[13] Exit"
    
    menu = input("Silahkan Pilih Sob: ")
    print "\n"

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
       hack_data()
    elif menu == 4:
        berak_data()
    elif menu == 5:
        show_data()
    elif menu == 6:
        hack_data()
    elif menu == 7:
        insert_menu()
    elif menu == 8:
        rash_data()
    elif menu == 9:
        oh_data
        exit()  
    else:
        print "Mau Hack apa sih wkwk"


if __name__ == "__main__":

    while(True):
        show_menu() 