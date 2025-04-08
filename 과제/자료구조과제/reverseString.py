from linkedStack import LinkedStack #교수님이 제공해주신 코드 6-13의 linkedstack활용

def reverse(s):   #문자열을 뒤집는 함수 정의
    st = LinkedStack() #빈 스택 생성
    for ch in s:
        st.push(ch) #문자열의 각 문자를 스택에 하나씩 push함

    out = "" #결과를 담을 변수 설정
    while not st.isEmpty():
        out += st.pop() #스택에서 문자를 하나씩 pop해서 문자열의 순서를 뒤집음
    return out #뒤집힌 문자열 return

def main(): #문자를 입력받고, 문자를 출력하기
    input_str = input("문자열을 입력하세요: ") #문자 입력받음
    reversed_str = reverse(input_str) #입력받은 문자를 함수를 사용해 뒤집기
    print("뒤집힌 문자열:", reversed_str) #결과 출력하기

if __name__ == "__main__":
    main()
