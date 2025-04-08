#20230523/ 김난영/ 경영학부
import random
t_members = ["Mike", "Tom", "David", "Mark", "Alice", "Jane", "Sara", "John"] #팀원 8명
result = ["Pass", "Fail"] #random을 했을 때 Pass와 Fail 둘 중 하나의 값이 출력되게 하기 위해서 적성검사 통과 여부를 리스트로 지정
team = {t_members[0]:random.choice(result), t_members[1]:random.choice(result), t_members[2]:random.choice(result), t_members[3]:random.choice(result), t_members[4]:random.choice(result), t_members[5]:random.choice(result), t_members[6]:random.choice(result), t_members[7]:random.choice(result)} #인덱스를 사용해 key값을 하나씩 지정하고, random.choice로 위의 result리스트에서 하나의 요소가 랜덤으로 추출되게 딕셔너리 작성 
print(team)
klist = list(team.keys()) #인덱스 이용을 위해 리스트로 변환 
vlist = list(team.values())
print("적성검사를 통과한 팀원 수는 모두 %s명입니다."%(vlist.count("Pass"))) #리스트 내에 있는 요소들 중 Pass개수를 반환하기 위해 리스트.count(요소) 사용 
if vlist.count("Pass") >= 4: #적성검사 통과된 팀원 수가 4명 이상인 경우
    print("적성검사를 통과한 팀원들 이름은 다음과 같습니다.")
    n = []
    for k, v in team.items(): #team딕셔너리를 반복하면서 value값이 Pass일때 그에 해당하는 이름(key 값)을 n리스트에 추가함 
        if v == "Pass":
            n.append(k)
    print(" ".join(n)) #join함수를 이용해서 n리스트의 요소들을 하나의 문자열로 합침. 
else: #적성검사 통과된 팀원 수가 4면 미만인 경우
    print("적성검사 통과인원 부족으로 팀은 보류되었습니다.")
