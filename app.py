import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

HINT_MESSAGES = {
    "Win": "🎉 Correct!",
    "Too High": "📉 Go LOWER!",
    "Too Low": "📈 Go HIGHER!",
}

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Debugged and playable.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

# Score + attempts metrics
m1, m2, m3 = st.columns(3)
attempts_left = attempt_limit - st.session_state.attempts
m1.metric("Score", st.session_state.score)
m2.metric("Attempts Left", attempts_left)
m3.metric("Difficulty", difficulty)

# Progress bar (fills as attempts are used; turns red in the last 2)
progress_pct = st.session_state.attempts / attempt_limit if attempt_limit > 0 else 0
bar_label = f"Attempts used: {st.session_state.attempts} / {attempt_limit}"
if attempts_left <= 2:
    bar_label = "⚠️ " + bar_label
st.progress(min(progress_pct, 1.0), text=bar_label)

st.subheader("Make a guess")
st.info(f"Guess a number between {low} and {high}.")

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.score = 0
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success(f"🏆 You won! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")
    else:
        st.error(f"💀 Game over. The secret was {st.session_state.secret}. Score: {st.session_state.score}")

if submit and st.session_state.status == "playing":
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append({"Guess": raw_guess, "Result": "❌ Invalid"})
        st.error(err)
    else:
        outcome = check_guess(guess_int, st.session_state.secret)
        st.session_state.history.append({"Guess": guess_int, "Result": HINT_MESSAGES[outcome]})

        if show_hint:
            if outcome == "Win":
                st.success(HINT_MESSAGES[outcome])
            elif outcome == "Too High":
                st.warning(HINT_MESSAGES[outcome])
            else:
                st.info(HINT_MESSAGES[outcome])

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.rerun()
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.rerun()

# Guess history table
if st.session_state.history:
    st.divider()
    st.subheader("📋 Guess History")
    st.table(st.session_state.history)

st.divider()
st.caption("Debugged by a human. Now actually playable.")
