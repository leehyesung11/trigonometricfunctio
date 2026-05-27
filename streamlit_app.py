import math
import streamlit as st
import pandas as pd
import altair as alt

st.title("🔵 삼각함수의 단위원")

st.markdown(
    """
    ## 단위원의 정의

    중심이 원점(0, 0)에 있고 반지름이 r인 원이 있다 하자. 각 θ에 대한 동경과 원의 교점의 좌표를 `P(x, y)`로 표현할 수 있습니다.
    이때 중심이 원점이고 반지름이 1인 원을 '단위원'이라 부릅니다. 뒤에 나올 삼각함수의 값의 변화를 이해할 때 단위원을 적용하면 보다 쉽게 이해할 수 있습니다.
    먼저 삼각함수에 대해 정의하고 갑시다.

    일반적으로 반지름이 `r`인 원에서 원 위의 점 `P(x, y)`는 다음 관계를 만족합니다:
    - `y / r = sin θ`
    - `x / r = cos θ`
    - `y / x = tan θ`

    이때 중요한 점은 각 `sin`, `cos`, `tan` 값이 반지름 `r`에 의존하는 것이 아니라 <span style="color:#d62728">각도 `θ`의 변화에 의존한다</span>는 것입니다.
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

theta_deg = st.slider("θ 값을 선택하세요 (각의 크기)", min_value=0, max_value=360, value=45, step=1)
theta_rad = math.radians(theta_deg)

cos_val = math.cos(theta_rad)
sin_val = math.sin(theta_rad)

if abs(cos_val) < 1e-12:
    tan_val = None
else:
    tan_val = math.tan(theta_rad)

st.markdown("---")

st.markdown(
    """
    ## 동적으로 움직이는 단위원

    슬라이더로 각도를 조절하면 단위원 위의 점 P와 각도 표시가 함께 움직입니다.
    """
)

point_x = 100 * cos_val
point_y = -100 * sin_val
arc_x = 40 * cos_val
arc_y = -40 * sin_val
large_arc_flag = 1 if theta_deg > 180 else 0
r_label_x = point_x * 0.5 + (-point_y / 100.0) * 12
r_label_y = point_y * 0.5 + (point_x / 100.0) * 12

svg = f'''
<svg width="360" height="360" viewBox="-180 -180 360 360" xmlns="http://www.w3.org/2000/svg">
  <circle cx="0" cy="0" r="100" fill="none" stroke="#1f77b4" stroke-width="4" />
  <line x1="-150" y1="0" x2="150" y2="0" stroke="#999" stroke-width="2" />
  <line x1="0" y1="-150" x2="0" y2="150" stroke="#999" stroke-width="2" />
  <path d="M 40 0 A 40 40 0 {large_arc_flag} 0 {arc_x:.2f} {arc_y:.2f}" fill="none" stroke="#d62728" stroke-width="4" />
  <line x1="0" y1="0" x2="{point_x:.2f}" y2="{point_y:.2f}" stroke="#2ca02c" stroke-width="4" />
  <circle cx="{point_x:.2f}" cy="{point_y:.2f}" r="6" fill="#2ca02c" />
  <text x="24" y="-8" font-size="18" fill="#d62728">θ</text>
  <text x="{r_label_x:.2f}" y="{r_label_y:.2f}" font-size="18" fill="#2ca02c">r</text>
  <text x="{point_x + 12:.2f}" y="{point_y + 4:.2f}" font-size="18" fill="#333">P(x, y)</text>
  <circle cx="0" cy="0" r="3" fill="#333" />
</svg>
'''

st.markdown(svg, unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    f"""
    ## θ = {theta_deg}° = {theta_rad:.3f} 라디안

    - `sin(θ) = {sin_val:.4f}`
    - `cos(θ) = {cos_val:.4f}`
    - `tan(θ) = {('undefined' if tan_val is None else f'{tan_val:.4f}')}`
    """
)

angles = list(range(0, 361, 5))
sin_curve = [math.sin(math.radians(a)) for a in angles]
cos_curve = [math.cos(math.radians(a)) for a in angles]
tan_curve = []
for a in angles:
    cos_a = math.cos(math.radians(a))
    if abs(cos_a) < 1e-12:
        tan_curve.append(float("nan"))
    else:
        tan_curve.append(math.tan(math.radians(a)))

sin_df = pd.DataFrame({"θ": angles, "값": sin_curve})
cos_df = pd.DataFrame({"θ": angles, "값": cos_curve})
tan_df = pd.DataFrame({"θ": angles, "값": tan_curve})
selected_df = pd.DataFrame({
    "θ": [theta_deg, theta_deg, theta_deg],
    "값": [sin_val, cos_val, tan_val if tan_val is not None and abs(tan_val) <= 10 else float("nan")],
    "함수": ["sin(θ)", "cos(θ)", "tan(θ)"]
})

st.markdown("### 삼각함수 그래프")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("sin(θ)")
    sin_chart = alt.Chart(sin_df).mark_line(color="#1f77b4").encode(
        x=alt.X("θ:Q", title="θ (degrees)", axis=alt.Axis(domainColor="black", labelColor="black", titleColor="black", tickColor="black", gridColor="#e6e6e6")),
        y=alt.Y("값:Q", title="sin(θ)", axis=alt.Axis(labelColor="#1f77b4", titleColor="#1f77b4", domainColor="#1f77b4", tickColor="#1f77b4", gridColor="#d3d3d3")),
        tooltip=[alt.Tooltip("θ:Q", title="θ"), alt.Tooltip("값:Q", title="sin(θ)")],
    )
    sin_point = alt.Chart(selected_df[selected_df["함수"] == "sin(θ)"]).mark_circle(color="#d62728", size=100).encode(
        x="θ:Q",
        y="값:Q",
        tooltip=[alt.Tooltip("θ:Q", title="θ"), alt.Tooltip("값:Q", title="sin(θ)")],
    )
    sin_zero_line = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(color="black", strokeWidth=2).encode(y="y:Q")
    st.altair_chart((sin_chart + sin_zero_line + sin_point).interactive(), use_container_width=True)
with col2:
    st.subheader("cos(θ)")
    cos_chart = alt.Chart(cos_df).mark_line(color="#2ca02c").encode(
        x=alt.X("θ:Q", title="θ (degrees)", axis=alt.Axis(domainColor="black", labelColor="black", titleColor="black", tickColor="black", gridColor="#e6e6e6")),
        y=alt.Y("값:Q", title="cos(θ)", axis=alt.Axis(labelColor="#2ca02c", titleColor="#2ca02c", domainColor="#2ca02c", tickColor="#2ca02c", gridColor="#d3d3d3")),
        tooltip=[alt.Tooltip("θ:Q", title="θ"), alt.Tooltip("값:Q", title="cos(θ)")],
    )
    cos_point = alt.Chart(selected_df[selected_df["함수"] == "cos(θ)"]).mark_circle(color="#d62728", size=100).encode(
        x="θ:Q",
        y="값:Q",
        tooltip=[alt.Tooltip("θ:Q", title="θ"), alt.Tooltip("값:Q", title="cos(θ)")],
    )
    cos_zero_line = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(color="black", strokeWidth=2).encode(y="y:Q")
    st.altair_chart((cos_chart + cos_zero_line + cos_point).interactive(), use_container_width=True)
with col3:
    st.subheader("tan(θ)")
    tan_chart = alt.Chart(tan_df).mark_line(color="#9467bd").encode(
        x=alt.X("θ:Q", title="θ (degrees)", axis=alt.Axis(domainColor="black", labelColor="black", titleColor="black", tickColor="black", gridColor="#e6e6e6")),
        y=alt.Y("값:Q", title="tan(θ)", scale=alt.Scale(domain=[-10, 10]), axis=alt.Axis(labelColor="#9467bd", titleColor="#9467bd", domainColor="#9467bd", tickColor="#9467bd", gridColor="#d3d3d3")),
        tooltip=[alt.Tooltip("θ:Q", title="θ"), alt.Tooltip("값:Q", title="tan(θ)")],
    )
    asymptotes = pd.DataFrame({"θ": [90, 270]})
    asymptote_lines = alt.Chart(asymptotes).mark_rule(color="#d62728", strokeDash=[4,4], size=2).encode(x="θ:Q")
    tan_point = alt.Chart(selected_df[selected_df["함수"] == "tan(θ)"]).mark_circle(color="#d62728", size=100).encode(
        x="θ:Q",
        y="값:Q",
        tooltip=[alt.Tooltip("θ:Q", title="θ"), alt.Tooltip("값:Q", title="tan(θ)")],
    )
    tan_zero_line = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(color="black", strokeWidth=2).encode(y="y:Q")
    st.altair_chart((tan_chart + asymptote_lines + tan_zero_line + tan_point).interactive(), use_container_width=True)
