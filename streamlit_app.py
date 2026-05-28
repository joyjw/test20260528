import streamlit as window_manager  # 스트림릿 라이브러리 가져오기
import streamlit as st

# 1. 앱 제목 및 설명 (출력)
st.title("🏆 순위 예측기: 3등을 찾아라!")
st.write("친구들의 이름과 점수를 입력하면 정확하게 **3등**이 누구인지 찾아줍니다.")

# 2. 데이터 입력 받기 (입력)
# 사용자에게 여러 명의 데이터를 입력받기 편하도록 예시를 제공합니다.
raw_input = st.text_area(
    "이름과 점수를 예시처럼 입력해주세요 (한 줄에 한 명씩):",
    value="김철수 95\n이영희 88\n박민수 92\n최대박 79\n정소민 85"
)

# 실행 버튼
if st.button("3등 결과 확인하기 🔍"):
    
    # 데이터를 저장할 빈 리스트 생성
    players = []
    
    # 3. 반복문(Loop)을 활용해 입력된 문자열 처리
    lines = raw_input.strip().split("\n")
    for line in lines:
        if line.strip(): # 빈 줄이 아니라면
            try:
                # 공백을 기준으로 이름과 점수 분리
                name, score_str = line.split()
                score = int(score_str) # 점수를 정수로 변환
                players.append({"이름": name, "점수": score})
            except ValueError:
                st.error(f"⚠️ 입력 형식이 올바르지 않습니다: '{line}' (예: 홍길동 100)")
                st.stop()

    # 4. 조건문(Conditional)을 활용한 예외 처리
    # 3등을 구하려면 최소 3명 이상의 데이터가 필요합니다.
    if len(players) < 3:
        st.warning("⚠️ 3등을 찾으려면 최소 3명 이상의 이름과 점수를 입력해야 합니다.")
    
    else:
        # 점수를 기준으로 내림차순 정렬 (높은 점수가 1등)
        # 익명 함수(lambda)를 사용해 딕셔너리의 '점수'를 기준으로 정렬합니다.
        sorted_players = sorted(players, key=lambda x: x['점수'], reverse=True)
        
        # 전체 순위 출력
        st.subheader("📊 입력된 전체 순위")
        for rank, player in enumerate(sorted_players, start=1):
            st.write(f"**{rank}등**: {player['이름']} ({player['점수']}점)")
            
        st.write("---") # 구분선
        
        # 3등 찾기 (파이썬 인덱스는 0부터 시작하므로 3등은 인덱스 2번입니다)
        third_place = sorted_players[2]
        
        # 5. 최종 결과 출력 (출력 및 조건문 활용)
        st.success(f"🎉 오늘의 3등은 바로 **{third_place['이름']}**님입니다! ({third_place['점수']}점)")