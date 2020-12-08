def show_all_grade(dict_grade, dict_activity):
    '''
    Tampilkan setiap  aktifitas beserta list nilai mahasiswanya
    '''
    print('----Fungsi "show_all_grade" dijalankan----')
    for k, v in dict_grade.items():
        print(f'ID\t: {k}')
        print(f'Title\t:{dict_activity[k]["Title"]}')
        print(f'Nilai semua mahasiswa: ')
        print(f'{"NIM":<10}|Nilai')
        print('-'*15)
        for nim, nilai in v.items():
            print(f'{nim:<10}|{nilai}')
        print()

    input('\n\nTekan Enter untuk kembali ke menu...')


def show_mhs_not_graded(dict_submission, dict_grade):
    '''
    Tampilkan setiap nim mahasiswa yang memiliki setidaknya satu submission yang belum dinilai
    '''
    print('----Fungsi "show_mhs_not_graded" dijalankan----')
    print("List mahasiswa yang belum lengkap nilainya:")
    data1 = []
    for i in dict_submission:
        for j in dict_submission[i]:
            data1.append(j)
    data1.sort()
    
    for k in dict_grade:
        for l in dict_grade[k]:
            data1.remove(l)
    data1.sort()
    
    out = list(dict.fromkeys(data1))

    for i in out:
        print(i)


def add_grade_by_mhs(dict_submission, dict_activity, dict_grade):
    '''
    Minta nim 1 mahasiswa
    Cek nim tersebut di semua submission, lalu cek apakah sudah ada nilai. Jika belum, tampilkan detil assignment.
    Tampilkan jawaban mahasiswa, lalu minta nilainya.
    '''
    print('----Fungsi "add_grade_by_mhs" dijalankan----')
    #jawaban anda di bawah ini
            
        
def show_assignment_not_graded(dict_submission, dict_activity, dict_grade):
    '''
    Tampilkan setiap data activity assignment yang memiliki setidakinya satu submssion mahasiswa yang belum dinilai
    '''
    print('----Fungsi "show_assignment_not_graded" dijalankan----')
    print("List Assignment yang memiliki submision yang belum lengkep nilainya")
    print("ID", end="\t")
    print("Title")

    for i in dict_submission:
        try:
            if len(dict_submission[i]) != len(dict_grade[i]):
                print(i, end="\t")
                print(dict_activity[i]["Title"])
            else:
                continue
        except KeyError:
            print(i, end="\t")
            print(dict_activity[i]["Title"])
    input('\n\nTekan Enter untuk kembali ke menu utama...')
    
    

def add_grade_by_assignment(dict_submission, dict_grade):
    '''
    Minta ID assignment yang ingin dinilai.
    Tampilkan data nim mahasiswa beserta jawaban yang belum dinilai, lalu minta nilainya
    '''
    print('----Fungsi "add_grade_by_assignment" dijalankan----')
    #jawaban anda di bawah ini
    
          


def report_by_assignment(dict_submission, dict_activity, dict_grade):
    '''
    Tampilkan data rekapan untuk tiap assignment, berupa nilai rata-rata dari semua mahasiswa, banyaknya submission di assignment tersebut, dan banyak submission yang sudah dinilai
    '''
    print('----Fungsi "report_by_assignment" dijalankan----')
    #jawaban anda di bawah ini
    a = ""
    print(f'{"ID":<3}| {"Title":<22}| {"Rata2"} | {"#submission":<12}| #dinilai')
    print(f"{a:-<65}")
      
    daftar_id = []
    for i in dict_activity.keys():
      daftar_id.append(i)
    
    daftar_title = {}
    rata2 = {}
    daftar_tugas = {}
    daftar_dinilai = {}
    

    for i in daftar_id:
      daftar_title[i] = dict_activity[i]['Title']
      
    for i in daftar_id:
      if i in dict_grade.keys():
        rata2[i] = sum(dict_grade[i].values())/len(dict_grade[i])
      else:
        rata2[i] = 0
      
    for i in daftar_id:
      if i in dict_submission.keys():
        daftar_tugas[i] = len(dict_submission[i])
      else:
        daftar_tugas[i] = 0
    
    for i in daftar_id:
      if i in dict_grade.keys():
        daftar_dinilai[i] = len(dict_grade[i])
      else:
        daftar_dinilai[i] = 0

    for i in daftar_id:
      print(f"{i:<3}| {daftar_title[i]:<22}| {rata2[i]:<6}| {daftar_tugas[i]:<12}| {daftar_dinilai[i]} ")

def report_by_mhs(dict_submission, dict_grade):
    '''
    Tampilkan data rekapan untuk tiap mahasiswa, berupa nilai rata-rata untuk semua assignment, banyaknya submission oleh mahasiswa, dan banyaknya submission mahasiswa tersebut yang sudah dinilai.
    '''
    print('----Fungsi "report_by_mhs" dijalankan----')
    print("nim","Rata2","#submission","#dinilai", sep="\t| ")
    print("-"*50)

    submision = []
    for i in dict_submission:
        for j in dict_submission[i]:
            submision.append(j)
    submision.sort()

    dinilai = []
    for i in dict_grade:
        for j in dict_grade[i]:
            dinilai.append(j)
    dinilai.sort()

    nim = list(dict.fromkeys(submision))
    
    rata = []
    for i in nim:
        rata2 = []
        for j in dict_grade:  
            try :  
                rata2.append(float(dict_grade[j][i]))
            except KeyError:
                continue
        try:
            rata.append(sum(rata2)/len(rata2))
        except ZeroDivisionError:
            rata.append(0.0)        

    for i, j in zip(nim, rata):
        print(i,"\t|",j,"\t|", submision.count(i),"\t\t|", dinilai.count(i))
    

def print_grade_to_file(dict_grade, dict_activity):
    '''
    Minta nama file.
    Tulis semua data grade ke file.
    '''
    print('----Fungsi "print_grade_to_file" dijalankan----')
    #jawaban anda di bawah ini

    

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

  

