import streamlit as st

st.title("🔵 삼각함수의 단위원(Unit Circle)")

st.markdown(
    """
    ## 단위원의 정의

    
    단위원은 중심이 원점(0, 0)에 있고 반지름이 r인 원입니다. 이때, 각 θ에 대한 동경과 원의 교점의 좌표를 `P(x, y)`라고 하면,
    이 점의 좌표는 각도 `θ`에 따라 위치합니다.

    일반적으로 반지름이 `r`인 원에서 원 위의 점 `P(x, y)`는 다음 관계를 만족합니다:
    - `y / r = sin θ`
    - `x / r = cos θ`
    - `y / x = tan θ`

    이때 중요한 점은 각 `sin`, `cos`, `tan` 값이 반지름 `r`에 의존하는 것이 아니라 <span style="color:#d62728">각도 `θ`의 변화에 의존한다</span>는 것입니다.
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

st.markdown(
    """
    ## 단위원 그림

    아래 그림에서 파란 원은 단위원이고, 초록색 선은 원의 중심에서 원 위 점 `P(x, y)`까지의 반지름입니다.
    빨간 곡선은 각도 `θ`를 나타냅니다.
    """
)

svg = '''
<svg width="360" height="360" viewBox="-180 -180 360 360" xmlns="http://www.w3.org/2000/svg">
  <circle cx="0" cy="0" r="100" fill="none" stroke="#1f77b4" stroke-width="4" />
  <line x1="-150" y1="0" x2="150" y2="0" stroke="#999" stroke-width="2" />
  <line x1="0" y1="-150" x2="0" y2="150" stroke="#999" stroke-width="2" />
  <path d="M 40 0 A 40 40 0 0 0 28.28 -28.28" fill="none" stroke="#d62728" stroke-width="4" />
  <line x1="0" y1="0" x2="70.71" y2="-70.71" stroke="#2ca02c" stroke-width="4" />
  <circle cx="70.71" cy="-70.71" r="6" fill="#2ca02c" />
  <text x="48" y="-8" font-size="18" fill="#d62728">θ</text>
  <text x="36" y="-22" font-size="18" fill="#2ca02c">r</text>
  <text x="82" y="-64" font-size="18" fill="#333">P(x, y)</text>
  <circle cx="0" cy="0" r="3" fill="#333" />
</svg>
'''

st.markdown(svg, unsafe_allow_html=True)
