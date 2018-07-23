#coding=GBK

# b = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
#      28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]


# a, b = 2, 1
# x, y = 2, 6
#
# s = str(round((float(a) / b), y + 1))
# c = s.index('.')
# print s
# while (len(s) - c - 1) < y:
#     s += '0'
# else:
#     print ''.join(s[x + c : y + c + 1])

# file_name = raw_input('input file_name:')
# f = open(file_name, 'w')
#
# # 让用户输入多行
# stopword = ''
# str = ''
# for line in iter(raw_input, stopword):
#     str += line + '\n'
#
# f.write(str)
# # print f.read()
# f.close()
# import re
# pat = re.compile(r'\b\[a-zA-Z]{3}\b') # 使用变量后与预期不符
#
# text = 'this is a long str not short one'
# r = re.findall(r'\b[a-zA-Z]{3}\b', text)
# print r


# text = 'What ever it is I don\'n care. How about it? There are 3 eggs.'

# def count_s(text):
#     import string
#     up = low = nums = oth = 0
#     for i in text:
#         if i.isupper():
#             up += 1
#         elif i.islower():
#             low += 1
#         elif i.isdigit():
#             nums += 1
#         else:
#             oth += 1
#     return (up, low, nums, oth)
# print count_s(text)


# def nums(*n):
#     return max(n), sum(n)
#
# print nums(1, 3, 5, -1, 9)

# def hun():
#     n = input('input a number:')
#     result = n // 100
#     return result
# while 1:
#     print hun()

# import random
# l = []
# for i in range(1000):
#     l.append(random.randint(0, 100))
# for j in set(l):
#     print j, ':', l.count(j)


# import csv
# with open('D:/python/practice/97.csv', 'r') as csvread:
#     reader = csv.DictReader(csvread)
#     column = [row['place'] for row in reader]
#     num = [row1['num'] for row1 in reader]
#
# print column, num
# print reader

# import csv
# csv_reader = csv.reader(open('D:/python/practice/97.csv', 'r'))
# column = [row for row in csv_reader]
# csv_reader = csv.reader(open('D:/python/practice/97.csv', 'r'))
# num = [row[0] for row in csv_reader]
# print column
# print num

# csv_reader = csv.reader(open('D:/python/practice/97.csv', 'r'))
# cols1 = []
# cols2 = []
# for row in csv_reader:
#     col1 = row[0]
#     col2 = row[1]
#
#     cols1.append(col1)
#     cols2.append(col2)
# print cols1
# print cols2

# def fibs(n):
#     if n == 1:
#         return (1,)
#     else:
#         r = [1, 1]
#
#         for i in range(n - 2):
#             fib = r[-1] + r[-2]
#             r.append(fib)
#         return tuple(r)
#
# print fibs(30)

# import random
# for i in random.randint(1, 9):
#     for j in random.randint(1, 9):
#         for k in random.randint(1, 9):
#             for l in random.randint(1, 9):
#                 print str(i) + str(j) + str(k) + str(l)
#                 break
# def rand_four():
#     i = random.randint(1, 9)
#     j = random.randint(1, 9)
#     k = random.randint(1, 9)
#     l = random.randint(1, 9)
#     return int(str(i) + str(j) + str(k) + str(l))
# print rand_four()

# 生成n位不含0的随机整数
# def rand_num(n):
#     import random
#     t = ''
#     for i in range(n):
#         i = str(random.randint(1, 9))
#         t += i
#     return int(t)
#
# print rand_num(4)

# import os
# print os.getcwd()
# print os.path

import random
# # for i in range(10):
# #     j = random.randrange(1000, 10000)
# #     print j
#
# f = random.choice(range(10))
# print f

# s = 'abcde'
# for i in [None] + range(-1, -5, -1):
#     print s[:i]

# print zip(range(5), range(3, 7))
# print map(i**2, range(5))
# t1 = 'bc'
# t2 = 'abcdef'
# print t1 in t2
# import keyword
# print keyword.kwlist

# f = [i**2 for i in range(5)]
# print f

# 创建数据库和表
import sqlite3
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
#
# c.execute('''DROP TABLE category''')
# c.execute('''create table category
#         (id int primary key, sort int, name text)''')
#
# c.execute('''create table book
#         (id int primary key,
#          sort int,
#          name text,
#          price real,
#          category int,
#          FOREIGN KEY (category) REFERENCES category(id))''')
#
# conn.commit()
# conn.close()

# 插入数据
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# books = [(1, 1, 'cook Recipe', 3.12, 1),
#          (2, 3, 'Python Intro', 17.5, 2),
#          (3, 2, 'OS Intro', 13.6, 2)]
# c.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")
#
# c.execute("INSERT INTO category VALUES (?, ?, ?)", [2, 2, 'computer'])
#
# c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)
#
# conn.commit()
# conn.close()

# 查询表
# conn = sqlite3.connect('test.db')
# c = conn.cursor()

# c.execute('select name from category order by sort')
# print c.fetchone()
# print c.fetchone()

# c.execute('select * from book where book.category=1')
# print c.fetchall()

# for row in c.execute('select name, price from book order by sort'):
#     print row

# 更新与删除表数据
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
#
# c.execute('update book set price=? where id = ?', (1000, 1))
# c.execute('delete from book where id = 2')
#
# conn.commit()
# conn.close()
# c.execute('drop table book') # 删除表

# for x in range(10):
#     print(' ' * (20 - x), *range(1, 1 + x))
import string

# for x in range(10):
#     print ' ' * (20 - x), str(range(1, 1 + x)).strip('[]')

# try:
#     open('abc.txt', 'r')
# except IOError:
#     print 'files not found!'
# finally:
#     print 'pass'

# for i in range(10):
#     if i % 2 == 0:
#         print pow(i, 2)

def adjust_srt(x, y = r'd:/output/new.src', z = 0):
    import re, datetime, os
    f0 = open(r'' + x, 'r')
    pat = r"\d\d:\d\d:\d\d"
    f1 = f0.read()
    l0 = re.findall(pat, f1)

    temp = []
    for i in l0:
        h = int(i[0: 2])
        m = int(i[3: 5])
        s = int(i[6:])
        delta = datetime.timedelta(seconds = z)
        t = datetime.datetime(2018, 07, 20, h, m, s) + delta
        t1 = datetime.datetime.strftime(t, '%H:%M:%S')
        temp.append(t1)

    result = []
    for i in range(len(temp)):
        f1 = f1.replace(l0[i], temp[i])

    if os.path.exists(y[0:10]):
        pass
        print "it's already exists"
    else:
        print 'make dir'
        os.mkdir(y[0:10])
    new = open(y, 'w')
    new.write(f1)
    f0.close()
    new.close()

adjust_srt(r'C:\Users\Administrator\Desktop\for_python\wt2.txt', z = 4)






