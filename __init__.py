import streamlit as st


def inject_global_styles():
    st.markdown(
        """
        <style>
        :root {
            --bg: #0b0f14;
            --surface: #11161d;
            --surface-2: #151b23;
            --border: rgba(205,212,220,0.10);
            --text: #e8edf2;
            --muted: #98a4b3;
            --primary: #00b8a9;
            --success: #22c55e;
            --danger: #f43f5e;
            --warning: #f59e0b;
        }
        .stApp { background: radial-gradient(circle at top right, rgba(0,184,169,0.08), transparent 25%), #0b0f14; }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, rgba(17,22,29,0.98), rgba(11,15,20,0.98)); border-right: 1px solid rgba(205,212,220,0.08); }
        .block-container { padding-top: 1.2rem; padding-bottom: 2rem; }
        div[data-testid="stMetric"] {
            background: linear-gradient(180deg, rgba(17,22,29,0.96), rgba(13,18,24,0.96));
            border: 1px solid rgba(205,212,220,0.10);
            padding: 1rem;
            border-radius: 16px;
        }
        div[data-testid="stDataFrame"] {
            border: 1px solid rgba(205,212,220,0.10);
            border-radius: 16px;
            overflow: hidden;
        }
        .market-live {
            display:inline-flex;align-items:center;gap:.5rem;padding:.45rem .75rem;border-radius:999px;
            background:rgba(34,197,94,.14);color:#8ff0b4;border:1px solid rgba(34,197,94,.22);font-weight:700;
        }
        .market-closed {
            display:inline-flex;align-items:center;gap:.5rem;padding:.45rem .75rem;border-radius:999px;
            background:rgba(244,63,94,.12);color:#ff9fb1;border:1px solid rgba(244,63,94,.22);font-weight:700;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
