from django.apps import AppConfig


class IssuesConfig(AppConfig):
    name = "issues"


buyers_beforeSort = [
    "한펠 사무실",
    "한펠 공장",
    "(주)허니텍",
    "대한산업",
    "허니텍",
    "153양봉원",
    "가야농산",
    "강남양봉산업(천지)",
    "강원허니원영농조합",
    "강진양봉원",
    "거림양봉원",
    "거창양봉원",
    "경남양봉산업",
    "경주양봉조합",
    "고령양봉조합",
    "광주축협",
    "광주퓨리나",
    "구강회",
    "국화양봉원(올레)",
    "권혁순",
    "그린제너텍",
    "금호양봉원",
    "금호양봉원(남평)",
    "기언농장",
    "김상옥",
    "김수연",
    "김학은",
    "꿀벌동물병원",
    "꿀벌랜드",
    "꿀사랑협동조합",
    "남한강농장",
    "농심양봉산업",
    "농업회사법인화광코리아",
    "농협",
    "농협경제지주",
    "뉴트리온",
    "다인종합유통",
    "대성물산",
    "대전양봉원",
    "대주산업",
    "대한사료",
    "대한양봉진흥농원",
    "도흥농장",
    "동아원",
    "동원양봉원",
    "동화미생물연구소",
    "리브랩스",
    "멍이네 약용 곤충농원",
    "메디바이오넷",
    "메인양봉원",
    "메지온",
    "명작소컨설팅",
    "모던팜스",
    "문이네농장",
    "미래부",
    "미래축산",
    "미소팜",
    "바비스팩토리",
    "바우와우코리아",
    "박창섭",
    "박충호",
    "배가네양봉원",
    "배영갑",
    "배홍열",
    "백제양봉원",
    "보성파니피카",
    "부부양봉원",
    "부활양봉산업",
    "비트올",
    "산내양봉원",
    "산수기연",
    "산에들양봉원",
    "상주양봉원",
    "상주중앙양봉원",
    "서울사료",
    "서울축협",
    "서주양봉원",
    "선비벌꿀영농조합",
    "선진",
    "설봉영농조합법인",
    "설종수",
    "세미휘드텍",
    "세인리소스",
    "소대섭",
    "소브산칼륨",
    "수협사료",
    "순천양봉원",
    "신동아양봉산업",
    "심정희",
    "써미텍",
    "씨티씨바이오",
    "씨티씨바이오애니멀헬스",
    "아이원푸드",
    "아크",
    "안동양봉원",
    "애니포크",
    "엄병준",
    "에스웜",
    "에이디고창",
    "에이비알",
    "에이치디씨",
    "에이치엔에프",
    "에이티면역",
    "에이티바이오",
    "엔에이씨코리아",
    "여주꿀벌농원",
    "영덕양봉원",
    "영암매력한우TMR",
    "영주벌꿀",
    "예천양봉원",
    "오네스토펫푸드",
    "오션",
    "올바른",
    "완주양봉원",
    "우리와",
    "우성사료",
    "우성양봉원",
    "원삼양봉원",
    "원익진",
    "원주농협자재센터",
    "원트라",
    "웨스포피드",
    "유니바이오",
    "유성바이오",
    "유태민",
    "윤석민",
    "윤시호",
    "이경택",
    "이교춘",
    "이길수",
    "이노바텍",
    "이범희",
    "이영우",
    "이용성",
    "이지팜스",
    "이진혁",
    "이한석",
    "이현우피드",
    "이화팜텍",
    "자립농장",
    "자연양봉산업",
    "장수양봉원",
    "장창순",
    "전두천",
    "정선철",
    "정씨네양봉원",
    "정안양봉원",
    "정의수",
    "제이앤비",
    "제일사료",
    "조득희",
    "조성화",
    "조창하",
    "지부장",
    "참존농장",
    "천안시보조사업",
    "천일양봉원",
    "천지단향양봉원",
    "천호갑",
    "청호물산",
    "충주양봉원",
    "칠곡양봉영농조합",
    "칠곡제일양봉원",
    "칼스엔비티",
    "코리아펫푸드",
    "태형농장",
    "토비이앤텍",
    "티에이치이",
    "팜스코",
    "팜스코전남동부특약점",
    "펫퍼스",
    "펫퍼스 바이오켐",
    "평화양봉원",
    "퓨로바이오",
    "퓨리나",
    "피앤씨코리아",
    "피앤피에드텍",
    "하나로미네",
    "하나양봉원",
    "하선사료",
    "하스프",
    "하이독",
    "한국스마트사료",
    "한국양봉농협",
    "한국양봉산업",
    "한국양봉자재마트",
    "한남양봉원",
    "한닭",
    "한상열",
    "한양사료",
    "한일사료",
    "한탑",
    "해남양봉원",
    "해밀펫푸드",
    "현철농장",
    "호승글로벌",
    "화진벌꿀",
    "횡성양봉원",
    "효광에이에프",
    "효성양봉원",
    "Bayer Yakuhin, Ltd.",
    "DH바이탈피드",
    "DS피드",
    "Elanco",
    "ELANCO JAPAN",
    "ENT",
    "JK INTERMATIONAL",
    "L&P",
    "OEM",
    "VAC",
    "로버트(코코넛분말)",
    "안종훈(코코넛분말)",
    "맥주효모(중국)",
    "맥주효모(베트남)",
    "이덕호(대두박)",
    "구정본(젤라틴)",
    "민경신(젤라틴)",
    "야신(젤라틴)",
    "휘황(젤라틴)",
    "젤라틴",
    "변성타피오카",
    "팽화미",
    "등외",
    "밀가루",
    "미역분말",
    "바나나분말",
    "트리미딩",
    "약재",
    "구연산",
    "솔빈산칼륨",
    "프로피온산칼슘",
    "소이코밀",
    "ISP",
    "멀티락",
    "씨센스프리미엄",
    "디텍",
    "케르세틴",
    "렌틸콩",
    "커피화분",
    "인도화분",
    "파쇄미",
    "MSM",
    "황산칼슘",
    "신한프리믹스",
    "기타",
    "벌통(유디)",
    "벌통",
    "소초광",
    "대두박",
    "ANC",
    "국민은행",
    "기업은행",
    "양봉 기자재",
    "단미사료협회",
    "당사장님",
    "유승진대표님",
    "도드람양돈서비스",
    "CLA",
    "소야그린텍",
    "엠보스",
    "신한은행",
    "엠포피드",
    "유경지대",
    "윤병수회계사무소",
    "충남도청",
    "필리핀(수출)",
    "수출",
]

buyer = buyers_beforeSort.sort()