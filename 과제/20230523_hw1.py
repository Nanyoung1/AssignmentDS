#경영학부, 20230523, 김난영
first_product=input("구매 물품1: ") #구매 물품1은 젤리로 한다.
second_product=input("구매 물품2: ") #구매 물품2는 사탕으로 한다.
jelly=int(input("젤리 가격: ")) #젤리 가격은 200원 
candy=int(input("사탕 가격: ")) #사탕 가격은 100원
jnum,cnum=input("젤리, 사탕 구매개수 입력: ").split(" ") #젤리는 2개, 사탕은 4개 구매 
jnum,cnum=int(jnum),int(cnum)
jprice=jelly*jnum #젤리 구매 금액 계산
cprice=candy*cnum #사탕 구매 금액 계산
print("총 구매 금액:",jprice+cprice,"원") #총 구매 금액 계산  


