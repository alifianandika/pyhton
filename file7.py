def convert_list(multilist):
  # Tulis kode fungsi convert_list() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
 detail = []
 for a in multilist:
    detail.extend(a)
 return detail
  

def get_nilai(filename, nama):
  # Tulis kode fungsi get_nilai() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  f = open(filename)
  for garis in f:
    data = garis.split()
    namanya = data[0]
    if(namanya.lower() ==  nama.lower()):
      nilai = float(data[1])
      return round(nilai)
    else:
      pass
  

def nilai_max(filename):
  # Tulis kode fungsi nilai_max() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # with open(filename, "r") as f:
  #   return max(f, key = lambda x: x.split()[1] )

  list_data = []
  list_nama = []
  f = open(filename)
  for n in f:
    data = n.split()
    nama = data[0]
    nilai = float(data[1])
    list_nama.append(nilai)
    list_data.append([nama, nilai])
  jum = len(list_data) -  1
  data_akhir = sorted(list_nama, key = float)
  for i in range(jum):
    if list_data[i][1] ==  data_akhir[jum]:
      return list_data[i][0], list_data[i][1]
    else:
      pass 





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = convert_list([[1,2], [3,4], [5,6]])
  print(f"convert_list([[1,2], [3,4], [5,6]]) = {r} \n(solusi: [1, 2, 3, 4, 5, 6])")
  print()
  r = get_nilai('nilai1.txt','joni')
  print(f"get_nilai('nilai1.txt','joni') = {r} \n(solusi: 76)")
  print()
  r = get_nilai('nilai2.txt','joni')
  print(f"get_nilai('nilai2.txt','joni') = {r} \n(solusi: None)")
  print()
  r = nilai_max('nilai1.txt')
  print(f"nilai_max('nilai1.txt') = {r} \n(solusi: ('Zack', 88.05)")
  print()
  r = nilai_max('nilai2.txt')
  print(f"nilai_max('nilai2.txt') = {r} \n(solusi: ('Arya', 90.00)")
  print()

if __name__ == '__main__':
  test()
