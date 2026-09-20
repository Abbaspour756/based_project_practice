import streamlit as st

from src.main import simulate_game

st.title("Monty hall simulation")

num_games = st.number_input("Enter the number of games to simulate"
                            , min_value=1, max_value=100000, value=1000
)

col1, col2 = st.columns(2)
col1.subheader("Win rate without switching")
col2.subheader("Win rate with switching")

chart1 = col1.line_chart(x=None, y=None, height=300)
chart2 = col2.line_chart(x=None, y=None, height=300)


wins_no_switch = 0
wins_switch = 0

for i in range(num_games):
    num_wins_without_switch, num_wins_with_switch = simulate_game(1)
    wins_no_switch += num_wins_without_switch
    wins_switch += num_wins_with_switch

    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])
