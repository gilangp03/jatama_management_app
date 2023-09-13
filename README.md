Checklist Tugas 2

No 1. Berikut langkah yang dibuat saat mengerjakan project ini

1. Buatlah folder project django yang ingin dibuat
2. Buka terminal dan install python
3. Install python virtual environment pada terminal. Jalankan python virtual environment agar project tidak mengalami konflik dependencies bila dibuka di perangkat dengan versi python yang lain
4. Buka terminal pada folder project django, lalu jalankan perintah " django-admin startproject "namafolder""
5. Buka folder project django yang telah dibuat dengan vscode. Buka terminal, lalu jalankan perintah python "manage.py startapp "nama aplikasi""
6. Buka settings.py pada folder project yang telah dibuat, tambahkan 'nama aplikasi' pada array INSTALLED_APPS
7. Buat folder baru pada folder main pada project django yang telah dibuat dengan nama templates. Isilah folder tersebut dengan file html yang ingin ditampilkan. Dalam hal ini, kami membuat 2 file html dengan nama main.html dan inventory.html.
8. Buka file models.py pada folder main
9. Buatlah kelas model yang ingin ditampilkan dalam aplikasi
10. Migrasikan data model lokal dengan menjalankan perintah "python manage.py makemigrations" untuk membuat model migrasi, lalu jalankan perintah "python manage.py migrate" untuk melakukan migrasi ke database lokal.
11. Buka file views.py, impor render dari package django.shortcuts lalu tambahkan fungsi yang meminta http dan merender page yang diinginkan
12. Buka file html yang ingin menampilkna data dari models.py, lalu masukkan {{variabel yang diinginkan}} pada file html
13. Untuk mengatur routing url aplikasi, buat file python dalam folder main dengan nama urls.py. Isi urls.py dengan mengimport path dari django.urls dan fungsi dari main.views yang ingin dibuat urlnya. Buatlah variabel nama aplikasi, kemudian buat array urlpatterns yang berisi path url yang ingin dibuat.
14. Untuk mengatur routing url project, buka urls.py pada folder project django, lalu import path dan fungsi include dari django.urls. Tambahkan "path('', include('main.urls'))," pada array urlpatterns mengimport url dari aplikasi main dan mengarahkan pada rute yang ditulis dalam berkas urls.py di folder main
15. Buatlah repository baru di Github
16. pada folder proyek django, jalankan perintah pada terminal
git init ., untuk menginisiasi repo lokal
git remote add origin "link repo github" untuk menghubungkan repository lokal dengan repository github yangtelah dibuat sebelumnya.
17. git add . untuk menambahkan progres repo, lalu tambahkan git commit -m "Pesan commit" untuk menambahkan pesan progres dari repository lokal. Lalu git push origin main untuk mempush dan mengirimkan file repository lokal ke repository github yang telah dibuat sebelumnya. 

No 2 ![Alt text](pbp2.png)

No 3. Penggunaan virtual environment sebelum membuat project django sangat membantu karena virtual environment dapat mengisolasi projek, mempertahahkan dependencies yang dibutuhkan dalam project django yang dibuat, dan menghubungkan pip packages yang dibutuhkan. Hal ini bertujuan agar tidak memunculkan konflik antar package dan dependencies karena project tersebut dibuka di perangkat dengan versi python yang berbeda. Kita bisa membuat project django tanpa virtual environment, akan tetapi ini lebih memunculkan resiko untuk terjadinya konflik antar dependencies dan package apabila project yang dibuat tanpa mengaktifkan virtual environment dibuka di perangkat lain yang versi python nya berbeda.

No 4. MVC adalah desain arsitektur yang memisahkan aplikasi menjadi tiga bagian, yaitu model, view, dan controller. Bagian model mengatur dan mengorganisasikan data pada database yang digunakan dalam aplikasi. Kemudian bagian view digunakan untuk me-render dalam bentuk GUI. Bagian controller berfungsi menghubungkan views dan model. Controller hanya memerintahkan bagian model dan berinteraksi dengan bagian view.
Sama seperti MVC, MVT merupakan desain arsitektur yang membagi aplikasi menjadi tiga bagian, yaitu bagian model, view, dan controller. MVT merupakan turunan dari desain arsitektur MVC. Bagian model berfungsi sebagai interaktor terhadap data aplikasi yang bertugas me-maintance data aplikasi. Bagian ini berisi data struktur logik dan ditampilkan dalam bentuk database. Bagian view sebagai pengontrol apa yang akan ditampilkan saat merender aplikasi dan menerima permintaan HTTP dan mengembalikan respon HTTP. Bagian template merupakan bagian front-end dari aplikasi yang berisi file HTML
MVVM, yaitu Model View ViewModel, yaitu desain arsitektur perangkat lunak yang terdiri dari tiga bagian. Yaitu Model, View, dan ViewModel. Bagian model berfungsi melakukan aktivitas abstraksi data yang digunakan. Bagian View berfungsi untuk memberikan informasi kepada bagian ViewModel setelah menerima respon dari user. Bagian ViewModel berfungsi menghubungkan antara data yang diberikan oleh user dengan Model dan merepresentasikan data yang disimpan pada bagian model.