# 게임에서 사용할 캐릭터를 정의합니다.
define m1 = Character('이우주') #남주1 연하 이우주
define m2 = Character('배진혁') #남주2 동갑 배진혁
define m3 = Character('지승현') #남주3 연상 지승현

define player_name = "플레이어이름"
define p = Character("player_name",dynamic = True,color="#0B6121")
##Character 일때 player_name은 변수랑 같아야함.

# 여기에서부터 게임이 시작합니다.
label start:

    $player_name = renpy.input("이름을 지정해주세요. 내 이름은")##화면에 내 이름은 나오고 다음칸에 입력받는 칸이 나온다.
    p "내 이름은 [player_name]"##p는 위에 선언한 캐릭터고, 대화창에 변수값을 나오게 할려면 [변수명]으로 사용한다.

    p "달님 올해는 꼭 모태솔로 탈출하게 해주세요 .." with fade
    "아침 7시 알람이 시끄럽게 울린다." with vpunch
    "..." "네가 미림이가 맞느냐"  with zoomin
    "..." "나는 어제 네가 불러낸 달의 요정이다.\n너의 소원을 들어주기 위해 네 앞에 나타났다."
    "..." "세 명의 남자 중 마음에 드는 한 명의 남자를 선택해라 그 남자가 너의 남자친구가 될 것이다."

    menu :
        "남자를 골라보자"

        "이우주":
            "아이돌 연습생 연하남 이우주를 선택했습니다."
            m1 "누나 안녕?ㅎㅎ"
        "배진혁":
            "같은 반 축구부 배진혁을 선택했습니다."
            m2 "[player_name] 안녕? ㅎㅎ"
        "지승현":
            "전교1등 선배 지승현을 선택했습니다."
            m3 "[player_name] 안녕? ㅎㅎ"
        

    return
