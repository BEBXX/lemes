def show_topic(list_topic, dict_activity):
    '''
    Menampilkan setiap topik beserta detil aktifitasnya
    '''
    print('----Fungsi "show_topic" dijalankan----')
    #jawaban anda di bawah ini
    
    

def add_topic(list_topic, dict_activity, id_activity):
    '''
    Meminta data topik baru. Menambahkan topik baru ke list_topic.
    Tanya jika ingin sekaligus menambahkan actifitas. Jika menambahkan aktifitas, naikkan counter id_activity dengan 1,
    baru dijadikan sebagai key activity baru.

    Return id_activity yang terakhir digunakan

    '''
    print('----Fungsi "add_topic" dijalankan----')
    #jawaban anda di bawah ini
    

def delete_topic(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin dihapus.
    Lalu hapus topik beserta semua aktivitasnya, hapus juga data di activity, submission, dan grade untuk id aktivitas yang terdapat di topik ini
    '''
    print('----Fungsi "delete_topic" dijalankan----')
    #jawaban anda di bawah ini
    

def update_topic(list_topic):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Tampilkan data eksisting.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "update_topic" dijalankan----')
    #jawaban anda di bawah ini
    for i in range(0, len(list_topic)):
        print(f'{i+1}:', list_topic[i]['Title'])

    pilihan = int(input('Masukkan nomor topic yang ingin diupdate: ')) - 1
    while pilihan >= len(list_topic):
        pilihan = int(input('Masukkan nomor topic yang ingin diupdate: ')) - 1

    for j in list_topic[pilihan]:
        if j != 'Activities':
            print(j, '\t:', list_topic[pilihan][j])

    print('Masukkan data baru. Kosongkan jika tidak ingin diubah.')
    update_title = input('Masukkan Title: ')
    if update_title != '':
        list_topic[pilihan]['Title'] = update_title
    update_description = input('Masukkan Description: ')
    if update_description != '':
        list_topic[pilihan]['Description'] = update_description
        
    print('Update topic selesai')
    input('\n\nTekan Enter untuk kembali ke menu utama...')
    
    

def add_topic(list_topic, dict_activity, id_activity):
    '''
    Meminta data topik baru. Menambahkan topik baru ke list_topic.
    Tanya jika ingin sekaligus menambahkan actifitas. Jika menambahkan aktifitas, naikkan counter id_activity dengan 1,
    baru dijadikan sebagai key activity baru.

    Return id_activity yang terakhir digunakan
    '''
    #print('----Fungsi "add_topic" dijalankan----')
    #jawaban anda di bawah ini
    awal = id_activity

    judul = input("Masukan Title: ")
    deskripsi = input("Masukan Description: ")
    aktifitas = input("Ingin menambahkan activity (y/n)?")
    while aktifitas != 'y' and aktifitas != 'n':
        aktifitas = input('ingin menambahkan activity (y/n)?')
    while aktifitas == "y" :
        id_activity+=1
        title_activ = input("Masukan Title activity: ")
        type_activ = input("Masukan Type activity (assignment/material): ")
        while type_activ != 'assignment' and type_activ != ('material'):
           type_activ = input('Masukkan Type activity (assignment/material): ')
        desc_activ = input("Masukan Description activity: ")
        dict_activity[id_activity] = {'Title':title_activ, 'Type': type_activ, 'Deskription': desc_activ}
        aktifitas = input("ingin menambahkan activity (y/n)?")
        while aktifitas != 'y' and aktifitas != 'n':
            aktifitas = input('ingin menambahkan activity (y/n)?')
    else :
        print('add topic selesai')

    if awal != id_activity:
        a = []
        for i in range (awal+1, id_activity+1):
            a.append(int(i))
        list_topic.append({'Title': judul, 'Description': deskripsi, 'Aktivities': a})

    global LAST_ID_ACTIVITY
    LAST_ID_ACTIVITY = id_activity
    

def udpate_activity(list_topic, dict_activity):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "udpate_activity" dijalankan----')
    #jawaban anda di bawah ini
    


def delete_activity(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, minta inputan topik. 
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Hapus activity, submission, dan grade dengan id activity yang dipilih
    '''
    print('----Fungsi "delete_activity" dijalankan----')
    #jawaban anda di bawah ini
    
    
      

    



def print_topic_to_file(list_topic, dict_activity):
    '''
    Minta nama file.
    Print setiap detail topik, beserta list aktifitasnya ke file.
    '''

    print('----Fungsi "print_topic_to_file" dijalankan----')
    #jawaban anda di bawah ini

    




    
if __name__ == "__main__":
    #type_activity = ['assignment', 'material']
    #id_activity adalah variable global untuk id unik semua activity di semua topic
    LAST_ID_ACTIVITY = 2
    NIM_LOGIN = ''
    ADMIN_LOGIN = False


    #key pada dict_mhs['data'] adalah NIM
    dict_mhs = {'field' : [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                           ('Email', '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                           ('Password', '^[a-zA-Z0-9]{8,12}$')],
             'data' : {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                       '114': {'Nama': 'Joni', 'Email': 'joni@telU.com', 'Password': '12345678'},
                       '115': {'Nama': 'jeje', 'Email': 'jeje@telU.com', 'Password': '12345678'}

                       }           
            }

    #Value pada key 'Activities' berupa list berisi id_activity
    list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0, 1]},
                    {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}
                  ]

    # key pada dict_activity adalah id_activity 
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                         1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                         2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                         }

    # key pada dict_submission adalah id_activity 
    dict_submission = {0: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                        2: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'}
                       }

    # key pada dict_grade adalah id_activity 
    dict_grade = {0: {'113' : 100}
                        
                  }

    
     
