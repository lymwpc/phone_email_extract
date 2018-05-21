#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
'''书中举例待复制的文本所在链接：https://nostarch.com/contactus.htm/
我们只需ctrl+a全选，然后ctrl+c复制就可以，此时文档数据已经在剪切板上，只是看不到而已。
'''
import pyperclip, re
# Create phone numbers regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)?         # separator
    (\d{3})              # first 3 digits
    (\s|-|\.)          # separator
    (\d{4})              # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)######注意的是三引号里有个()，此时它是groups[0]

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
#添加电话号码到序列matches中
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])#join属于序列list类型的方法，序列groups中1,3,5用-连接起来。
    if groups[8] != '':#判断是否有分机号，假如有的话,此时phoneNum后面需要加上' x' + groups[8]，否则不管
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
#添加邮箱地址到序列matches中	
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))#将序列matches中元素分行，并将其复制到剪切板中
    print('Copied to clipboard:')
    print('\n'.join(matches))#打印序列matches中元素，看其是否是否分行
else:
    print('No phone numbers or email addresses found.')

'''
语法：  'sep'.join(seq)

参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串

#对序列进行操作（使用':'作为分隔符）
>>> seq1 = ['hello','good','boy','doiido']
>>> print ':'.join(seq1)
hello:good:boy:doiido
'''
