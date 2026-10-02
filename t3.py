total = 0
student = {
    'name': 'yuvraj',
    'age': 15,
    'marks': [87, 92, 95, 99, 96],
    'subject': 'maths',
    'city': 'pathalgaon',
    'subjects': ['maths']
}
for mark in student['marks']:
    total = total + mark

print(total)
