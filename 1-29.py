english_dict = dict()

english_dict['하나'] = 'one'
english_dict['둘'] = 'two'
english_dict['셋'] = 'three'
word = input("단어를 입력하시오: ")
print (english_dict[word])


import smtplib
from email.mime.text import MIMEText
me = 'abc@server.kr' # 보내는 사람 메일 주소
you = ['def1@server.com','def2@server.com','def3@server.com'] # 받는 사람 메일 주소
contents = '12월 20일에 동창회가 있으니 참석해주시기 바랍니다.'
msg = MIMEText(contents, _charset='euc-kr')
msg['Subject'] = '동창회 모임' 
msg['From'] = me
msg['To'] = you
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("자신의 아이디", "패스워드")
for i in range(len(you)):
    server.sendmail(me, you[i], msg.as_string())
    server.quit()