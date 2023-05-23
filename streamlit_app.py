import streamlit as st
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx

if st.button("Clear All"):
    # Clears all singleton caches:
    st.cache_resource.clear()

def _get_session():
    script_run_ctx = get_script_run_ctx()
    return script_run_ctx.session_id if script_run_ctx else ''

user_session = _get_session()
st.write(f'Session ID: {user_session}')

if 'counter' not in st.session_state:
    st.session_state.counter = 0

increment = st.button('Increment Count')
if increment:
    st.session_state.counter += 1

st.write(f'Count: {st.session_state.counter}')
