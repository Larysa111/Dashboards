import streamlit as st
from random import randint
import time

st.title("Farbspiel")

if "score" not in st.session_state:
    st.session_state["score"] = 0

# Отображение очков
st.sidebar.header("Очки")
st.sidebar.write(f"Угадано цветов: {st.session_state.score}")

def create_new_goal():
    st.session_state.goal_r = randint(0,255)
    st.session_state.goal_g = randint(0,255)
    st.session_state.goal_b = randint(0,255)
    st.session_state.r_value = 0 # Сброс значений пользователя при новой игре
    st.session_state.g_value = 0
    st.session_state.b_value = 0
    st.session_state.r_slider = 0
    st.session_state.g_slider = 0
    st.session_state.b_slider = 0
    st.session_state.hint_used = False # Сброс подсказки
    st.session_state.start_time = time.time() # Сброс таймера

# Инициализация состояния игры
if "goal_r" not in st.session_state:
    st.session_state.score = 0
    st.session_state.hint_used = False # Для отслеживания использования подсказки
    st.session_state.start_time = time.time() # Время начала раунда
    create_new_goal()

# Константы для таймера
TIME_LIMIT_SECONDS = 60   


if "goal_r" not in st.session_state:
    create_new_goal()

cols_colors = st.columns([1,2,1])

# Функции для синхронизации слайдеров и числовых полей
def update_slider_r():
    st.session_state.r_slider = st.session_state.r_value

def update_number_r():
    st.session_state.r_value = st.session_state.r_slider


def update_slider_g():
    st.session_state.g_slider = st.session_state.g_value 

def update_number_g():
    st.session_state.g_value = st.session_state.g_slider  


def update_slider_b():
    st.session_state.b_slider = st.session_state.b_value 

def update_number_b():
    st.session_state.b_value = st.session_state.b_slider             


with cols_colors[1]:
    col1, col2 = st.columns(2)
    col1.slider("🔴", 0, 255, key="r_slider", on_change=update_number_r)
    col2.number_input(" ", 0, 255, key="r_value", on_change=update_slider_r)
    col1, col2 = st.columns(2)
    col1.slider("🟢", 0, 255, key="g_slider", on_change=update_number_g)
    col2.number_input(" ", 0, 255, key="g_value", on_change=update_slider_g)
    col1, col2 = st.columns(2)
    col1.slider("🔵", 0, 255, key="b_slider", on_change=update_number_b)
    col2.number_input(" ", 0, 255, key="b_value", on_change=update_slider_b)

def circle_div(r, g, b):
    return f""" 
        <div style='
            width: 150px;
            height: 150px;
            background-color : rgb({r}, {g}, {b});
            border-radius: 50%;
            margin-top: 20px;
            margin-left: auto;
            margin-right: auto;
        '>
        </div>
        """

with cols_colors[0]:
    st.header("You")
    st.markdown(
        circle_div(st.session_state.r_value, st.session_state.g_value, st.session_state.b_value),
        unsafe_allow_html=True
    )
with cols_colors[2]:
    st.header("Ziel")
    st.markdown(
        circle_div(st.session_state.goal_r, st.session_state.goal_g, st.session_state.goal_b),
        unsafe_allow_html=True
    ) 


def distance(r1, g1, b1, r2, g2, b2)   :
    return max(0, 100 - abs(r1-r2) - abs(g1-g2) - abs(b1-b2))

d = distance(st.session_state.r_value, st.session_state.g_value, st.session_state.b_value, st.session_state.goal_r, st.session_state.goal_g, st.session_state.goal_b)
progress_bar = st.progress(d)   


# Логика таймера
elapsed_time = time.time() - st.session_state.start_time
remaining_time = max(0, TIME_LIMIT_SECONDS - int(elapsed_time))

timer_placeholder = st.empty()
timer_placeholder.metric("Осталось времени", f"{remaining_time} сек")

game_over = False
if remaining_time <= 0 and d < 100:
    st.error("Время вышло! Попробуйте еще раз.")
    game_over = True
elif d == 100:
    if not game_over: # Чтобы не увеличивать очки, если игра уже закончилась по таймеру
        st.balloons()
        st.success("Gewonnen 🎉")
        if not st.session_state.hint_used: # Очки только если подсказка не использовалась
            st.session_state.score += 1
        game_over = True # Игра завершена успешно

# Отображение очков
st.sidebar.header("Очки")
st.sidebar.write(f"Угадано цветов: {st.session_state.score}")

# Кнопка "Показать решение"
def Show_solution():
    st.session_state.r_value = st.session_state.goal_r
    st.session_state.g_value = st.session_state.goal_g
    st.session_state.b_value = st.session_state.goal_b
    # Обновляем слайдеры, чтобы они соответствовали числовым полям
    update_slider_r()
    update_slider_g()
    update_slider_b()
    st.session_state.hint_used = True # Отмечаем, что подсказка использована
    st.info(f"Целевой цвет: R:{st.session_state.goal_r}, G:{st.session_state.goal_g}, B:{st.session_state.goal_b}")


# Кнопка "Подсказка"
# Делаем кнопку подсказки недоступной, если игра завершена или подсказка уже использована
if st.button("Подсказка", on_click=Show_solution, disabled=game_over or st.session_state.hint_used):
    pass # Действие уже в on_click

# Кнопки управления игрой
st.button("Новая игра", on_click=create_new_goal)

# Автоматическое обновление таймера (если игра не завершена)
if not game_over and remaining_time > 0:
    time.sleep(1) # Ждем 1 секунду
    st.rerun() # Перезапускаем приложение для обновления таймера



