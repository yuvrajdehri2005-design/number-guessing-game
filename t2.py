student={
      'name':'yuvraj',
      'age':'15',
      'marks':[87,92,95,99,96],
      'subjects':['hindi','english','maths','science']
}


student['subjects'].append('social science')
student['city']='pathalgaon'

for key,value in student.items():
    print(key ,':',value)

