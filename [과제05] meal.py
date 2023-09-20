from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://jeju-s.jje.hs.kr/jeju-s")
soup = BeautifulSoup(html, "html.parser")
##container > div.main_content > div.meal_menu > ul > li 
# > 표시는 있든없든 상관없음

bap = soup.select(".meal_menu ul li")
print("="*50)
print( bap)
print("-"*50)

menu = ""

for m in bap:
   print( m.text.strip() ) #strip은 공백 없앰
   menu = m.text

menu = menu.split(" ") #공백 단위로 나눈 것을 ,로 나눔
print(menu)
print("="*50)


i=0
with open('data/meal.txt', 'w', encoding='utf-8') as f:
    f.write("다음은 오늘의 제주과학고등학교 점심식단이다. 점심식단 질문울 받으면 다음 데이터를 참고하여 대답한다. \n점심식단 시작")
    for m in menu:
        i+=1
        f.write(m)
        f.write("\n")
    f.write("점심식단 종료")