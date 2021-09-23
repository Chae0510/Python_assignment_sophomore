real_id='lovePython!'
real_pwd='p12345'

id=input('아이디를 입력하세요 : ')


#아이디와 비밀번호가 모두 일치하는 경우
if id == real_id:
    pwd=input('비밀번호를 입력하세요. :')
    if pwd == real_pwd:
        print('lovePython!님 환영합니다~!!')

#아이디는 일치하지만 비밀번호가 틀린 경우
    else:
        print('비밀번호가 틀립니다.')

#아이디가 틀린 경우
else:
    print('아이디를 찾을 수 없습니다.')

