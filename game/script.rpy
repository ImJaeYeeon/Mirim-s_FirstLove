# 게임에서 사용할 캐릭터를 정의합니다.
define g = Character('미림이') #주인공 미림이
define m1 = Character('연하남') #남주1 이름 미정
define m2 = Character('동갑남') #남주2 이름 미정
define m3 = Character('연상남') #남주3 이름 미정



# 여기에서부터 게임이 시작합니다.
label start:
    g "달님 올해는 꼭 모태솔로 탈출하게 해주세요 .." with fade
    "아침 7시 알람이 시끄럽게 울린다." with vpunch
    "..." "네가 미림이가 맞느냐"  with zoomin
    "..." "나는 어제 네가 불러낸 달의 요정이다.\n너의 소원을 들어주기 위해 네 앞에 나타났다."

    return
