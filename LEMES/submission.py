def show_assignment_not_submit(dict_activity, dict_submission, nim):
    '''
    Fungsi menampilkan semua submission yang belum disubmit oleh mahasiswa dengan nim tertentu.
    Untuk setiap activity bertipe assignment, fungsi melakukan pengecekan apakah nim sudah ada di data submission untuk id activity tersebut. Jika nim belum ada, artinya belum melakukan submission, maka tampilkan detil submission tersebut.
    '''
    print('----Fungsi "show_assignment_not_submit" dijalankan----')
    

def show_nim_not_submit(dict_mhs, dict_submission, dict_activity):
    '''
    Fungsi menampilkan semua nim yang memiliki setidaknya satu activity bertipe assignment yang belum disubmit jawabannya.
    Cek untuk setiap activity bertipe assignment apakah setiap mahasiswa ada di data submission, jika belum kumpulkan nim tersebut, lalu tampilkan semua nim tanpa ada nim yang muncul lebih dari 1 kali.
    '''
    print('----Fungsi "show_nim_not_submit" dijalankan----')


def show_my_submission(dict_submission, nim=''):
    print(f'{"Assignment ID":<15}| Jawaban')
    print('-'*50)
    for k, v in dict_submission.items():
        if nim in v:
            print(f'{k:<15}| {v[nim]}')
    input('\n\nTekan Enter untuk kembali ke menu utama...')

def submit_assignment(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik. 
    Lalu menampilkan semua activity bertipe assignment di topik tersebut, lalu meminta user memilih activity assignment.
    Jika nim sudah submit di assignment yang dipilih, maka tampilkan pesan batal submit.
    Jika nim belum submit, minta jawaban assignment dan simpan jawaban di data submission.
    '''
    
    print('----Fungsi "submit_assignment" dijalankan----')
    

def update_submission(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik.
    Lalu menampilkan detil activity bertipe assignment di topik tersebut yang telah dijawab oleh mahasiswa nim, meminta user memilih assignment.
    Tampilkan jawaban eksisting, lalu minta jawaban baru. Jika tidak jadi update cukup dikosongkan maka tidak dilakukan perubahan jawaban.
    '''
    print('----Fungsi "update_submission" dijalankan----')


def delete_submission(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik.
    Lalu menampilkan detil activity bertipe assignment di topik tersebut yang telah dijawab oleh mahasiswa nim, meminta user memilih assignment.
    Hapus assignment tersebut.
    '''
    print('----Fungsi "delete_submission" dijalankan----')
    

def print_submissions_to_file(dict_submission, dict_activity):
    '''
    Minta nama file dari user. Lalu print semua data submission ke file tersebut.
    '''
    print('----Fungsi "print_submissions_to_file" dijalankan----')

    

    
                    
      
    

if __name__ == "__main__":
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



    