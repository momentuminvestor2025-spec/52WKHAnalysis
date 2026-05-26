import streamlit as st


def render_sidebar(status: dict):
    st.markdown("## NSE Terminal")
    badge_class = "market-live" if status["is_live"] else "market-closed"
    st.markdown(f"<div class='{badge_class}'>{status['label']}</div>", unsafe_allow_html=True)
    st.caption(status["current_time_text"])
    st.caption(status["secondary_text"])
    st.divider()
    st.markdown("### Workspace")
    st.write("- 52W High Scanner")
    st.write("- Historical Analytics")
    st.write("- Most Active + Overlap")
    st.write("- Scrape Monitor")
    st.divider()
    st.markdown("### Quick filters")
    st.selectbox("Watchlist", ["All Symbols", "Large Caps", "F&O Universe", "Momentum Names"])
    st.selectbox("Lookback Window", ["1 Month", "3 Months", "6 Months", "1 Year"], index=2)


def render_header_metrics():
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("52W High Symbols Today", "89", "+14 vs previous trading day")
    c2.metric("First-Time Appearances", "17", "Highlighted with NEW badge")
    c3.metric("Same-Day Overlaps", "11", "52W High ∩ Most Active")
    c4.metric("Scraper Health", "99.2%", "Retries and validation enabled")
