import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    layout='wide',
    initial_sidebar_state='collapsed',
    page_title='영화 속 신소재',
    page_icon='🎬'
)

data = [
    {
        'category': '해리포터:마법사의 돌',
        'url': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMTJfMTUz%2FMDAxNjEzMTM3NDMyMDMx.khJauiRcqi4FeZ7i141UkbegYgKRi-A4choGyu4IlDog.ikl1iZeu-dWC1vJLtYh2Ckkj2HONnFpKG0Ynt-zohicg.JPEG.fanta1209%2F256E6B33510BC5DF2D.jpg&type=sc960_832',
        'name': '어떤 영화일까?',
        'content': '자신이 마법사인걸 모르는 해리는 자신을 괴롭히고 구박하는 친척 밑에서 자랍니다. 그러다가 호그와트의 숲지기인 해그리드가 자신이 마법사라는걸 알려주고 호그와트에 입학해 론, 헤르미온느와 마법사의 돌로부터 볼드모트의 부활을 막습니다. 그리고 그 공로를 인정받아 그리핀도르가 우승하는데 힘을 보탭니다'
    },
    {
        'category': '해리포터:마법사의 돌',
        'url': 'https://postfiles.pstatic.net/MjAyMTA3MDhfNDAg/MDAxNjI1NzE0Mzk1ODE0.Oug9QpiJsSosQdWk05f58PLwB2wNFLgJpz8Se4uoG_Yg.jpcstUfTcQ1gWnoKoMPJfUy4kXVhbAgbHFmuVoKAWIkg.JPEG.smartnari/1.jpg?type=w966',
        'name': '어떤 물건일까?',
        'content': '착용하면 착용한 자의 몸을 투명하게 가려주는 망토. 마법사 세계 에서도 아주 귀한 물건으로 해리가 1학년 때 크리스마스 선물로 누군가에게 받았으며, 동봉된 편지를 통해 아버지 제임스 포터가 남긴 유품이라는 것 밝혀지면서 해리가 매우 아끼는 보물이 되었다.'
    },
    {
        'category': '해리포터:마법사의 돌',
        'url': 'https://postfiles.pstatic.net/MjAyMTA3MDhfMjUx/MDAxNjI1NzE0NDE0MTY2.Jt3GCoZOd1VpQNzctlTgjgGS3ett_id6_VAuYvF5HZog.DFZtCjORrt1uwbJGUS9iqrec_OeLNgoAI5Bq_yRBJM0g.JPEG.smartnari/2.jpeg?type=w966',
        'name': '어떤 소재로 구현할 수 있을까?',
        'content': '메타물질로 구현할 수 있고 메타물질은 빛이나 전자파보다 매우 작은 크기의 공간에 금속이나 유전물질을 반복적인 패턴으로 배열하여 만든 물질이다. 여기서 "메타"란 자연계에 존재하지 않는 특성을 가진 물질을 말한다.'
    },
    {
        'category': '해리포터:마법사의 돌',
        'url': 'https://postfiles.pstatic.net/MjAyMTA0MzBfMjky/MDAxNjE5NzY4NDc2Nzcx.u29ol2UNgkjHgIwUTMFfFh4rYbxJmaHI6o9dc7jIqJwg.PCWofp6NHlQJQBmdDJ8V891hmoZAsMRV003bmybREoUg.PNG.sciport2016/210502_%EB%A9%94%ED%83%80%EB%AC%BC%EC%A7%88_%EC%B9%B4%EB%93%9C%EB%89%B4%EC%8A%A4-06.png?type=w966',
        'name': '어떤 원리일까?',
        'content': '우리는 물체에 반사되어 나오는 빛을 통해 사물을 본다. 하지만, 메타물질을 이용하면 인위적으로 빛의 방향을 꺾어 빛이 물체의 표면을 따라 지나간다. 즉, 빛이 반사되어 물체를 볼 수 있는 것인데 반사되는 빛이 없기 때문에 우리의 눈에는 물체가 보이지 않게 되는 것이다'
    },
    {
    'category': '캡틴 아메리카',
    'url': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA3MjRfMTQ1%2FMDAxNjI3MTM0OTA1Nzgx.3nmP9yZdNecq-XQsWDmeGhF5zTHi2T1_pr7MtyH99EMg.7tBnouIhmkwBcHV2nShX7RsRZVzPw5tTjvjbmtplDU0g.JPEG.jeffbridges%2Fcapitanamerica1132.jpg&type=sc960_832',
    'name': '어떤 영화일까?',
    'content': '어벤져스와 관련된 사고로 부수적인 피해가 일어나자 정부는 어벤져스를 관리하고 감독하는 시스템인 일명 ‘슈퍼히어로 등록제’를 내놓는다. 어벤져스 내부는 정부의 입장을 지지하는 찬성파(팀 아이언맨)와 이전처럼 정부의 개입 없이 자유롭게 인류를 보호해야 한다는 반대파(팀 캡틴)로 나뉘어 대립하기 시작한다'
    },
    {
    'category': '캡틴 아메리카',
    'url': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fshopping.phinf.naver.net%2Fmain_3511322%2F35113226526.20221007175225.jpg&type=a340',
    'name': '어떤 물건일까?',
    'content': '마블 시네마틱 유니버스의 캡틴 아메리카가 사용하는 방패이자 캡틴 아메리카의 상징과도 같은 물건이고 형태나 구조 자체는 전형적인 타지(소형 원형 방패)에 속하지만 크기가 동체를 덮을 수 있을 정도로 크다.'
    },
    {
    'category': '캡틴 아메리카',
    'url': 'https://postfiles.pstatic.net/MjAxOTA0MTVfMTc5/MDAxNTU1MzE5OTg5NTg5.P5koxHAJ8UKB54drU77g6y-mXtK6Mw7_lk4CKnasrFIg.9Ean_mSa4Ok1FW3npjwQMGCK5zDU29RGzsbkabYf5Ksg.PNG.kims_pr/image01.png?type=w966',
    'name': '어떻게 만들어 졌을까?',
    'content': '캡틴 아메리카의 방패는 엑스맨에 나오는 울버린의 뼈와 손톱을 이루는 "아다만티움"과 블랙 팬서에 나오는 "비브라늄"이라는 희귀한 금속을 섞은 합금으로 만들어졌다. 비브라늄과 아다만티움의 합금으로 탄생한 방패는 파괴가 불가능하고, 가해지는 모든 에너지를 흡수한다. 캡틴 아메리카의 방패는 그을리거나 단 한 번도 손상되지 않는 강도를 보여주고 에너지 공격도 튕겨낸다. 여기서 합금이란 두가지 이상의 금속원소로 이루어진 금속이다'
    },
    {
    'category': '캡틴 아메리카',
    'url': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20150829_36%2Fjunhkim1226_14408371217732tS6U_PNG%2Fimg01.png&type=a340',
    'name': '현실에는 어떤 신소재 합금이 있을까?',
    'content': '일반적으로 금속은 한계치 이상의 힘을 가해 변형시키면 원래 형태로 돌아가지 않는다. 그런데 일정한 온도에서 형상을 기억시키면 그 온도보다 높거나 낮은 온도에서 아무리 변형을 시켜도 기억시킨 온도가 되면 기억시킨 형상으로 돌아가는 특성을 지닌 금속이 있다. 바로 "형상기억합금"이다.그리고 대표적인 형상기억합금으로는  니켈(Ni)-티타늄(Ti) 합금인 니티놀이 있다'
    },
    {
    'category': '엑스맨 탄생:울버린',
    'url': ' https://search.pstatic.net/sunny/?src=http%3A%2F%2Fimage.kyobobook.co.kr%2Fnewimages%2Fmusic%2Flarge%2F1494%2F2494117.jpg&type=sc960_832',
    'name': '어떤 영화일까?',
    'content': '어린 시절 눈앞에서 아버지를 잃은 상처, 그리고 사랑하는 연인까지 지켜내지 못했던 과거의 기억은 울버린을 더욱 강하게 만들어 울버린을 포함해 전세계에서 선발된 강력한 돌연변이들이 스페셜 팀을 구성하고, 울버린은 인간이 참아낼 수 있는 고통의 한계치를 넘는 지옥 같은 프로젝트를 통해 ‘웨폰 X’로 다시 태어난다'
    },
    {
    'category': '엑스맨 탄생:울버린',
    'url': 'http://cdn.mydaily.co.kr/FILES/201610/201610211413611125_1.jpg?20221109191045',
    'name': '어떤 능력일까?',
    'content': '울버린은 어떤 공격을 받든 상처가 나도 시간이 지나면 금새 스스로 치유되는 힐링팩터라는 초능력을 갖고있다'
    },
    {
    'category': '엑스맨 탄생:울버린',
    'url': 'https://postfiles.pstatic.net/MjAyMTA1MzBfMjQ1/MDAxNjIyMzg1OTk0Mzg3.R5YMEaoj0Ei9gvUsv0TmItUUu630T-0nmOQbRzJotVsg.XgoiUSPoskcuAAFIeh2IXNqgpBK_FToQlSPEWVrg2i8g.GIF.flcory429/3-GIF.gif?type=w773',
    'name': '어떤 소재로 구현할 수 있을까?',
    'content': '자가 치유 소재로 외부 환경에 의해 손상을 입은 고분자가 스스로 결함을 감지하여 자신의 구조를 복구하고, 원래의 기능을 회복할 수 있는 지능형 재료이다. 레깅스나 신발 밑창으로 주로 사용되던 열가소성 폴리우레탄을 기본 골격으로 하여 카보네이트라는 소재를 융합하여 자가 치유 소재를 구현했다. 여기서 카보네이트란 외부 충격을 받으면 단단해지고 충격이 없는 상황에서는 말랑해지는 소재이다'
    },
    {
    'category': '엑스맨 탄생:울버린',
    'url': 'https://postfiles.pstatic.net/MjAyMTA1MzBfMjQ1/MDAxNjIyMzg1OTcxMzg5.t9hzjZNTbW2yHpBcaf55L1w-mLrTKVotX2eSjNUBUE4g.lrhFdE6-dxb-9lYGDtb9EKYbRWXtWYS-VSzm_NohVAMg.PNG.flcory429/007.png?type=w773',
    'name': '어떤 원리일까?',
    'content': '외부 충격 시에는 물질 결합을 견고하게 하여 고체 결정(크리스탈)을 생성하여 충격으로부터 보호하는 등 외부 압력의 정도에 따라 단단한 고체와 말랑한 젤리 상태를 오가면서 충격 흡수를 조절하고 자유롭게 분자 결합을 하며 손상을 스스로 치유할 수 있다'
    }
]


def card_list(menu):
    result = ''
    for value in data:
        if value['category'] == menu:
            result = result + f"""
    <div class="col">
     <div class="card" style="width: 18rem;">
          <img src="{value['url']}" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{value['name']}</h5>
            <p class="card-text">{value['content']}.</p>
          </div>     
         </div>
     </div>
     """
    return result


menu = st.sidebar.selectbox('영화', ('해리포터:마법사의 돌', '캡틴 아메리카', '엑스맨 탄생:울버린'))
components.html(
    f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>

    <div class="container">
      <div class="row">

             {card_list(menu=menu)}

      </div>
    </div>

    """, height=6000
)
