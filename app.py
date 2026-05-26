import pandas as pd


def get_52w_high_data() -> pd.DataFrame:
    rows = [
        ["POLYCAB", "Polycab India Ltd", 7884.20, "2026-05-26", 1, True, "2026-05-26", "https://www.tradingview.com/chart/?symbol=NSE%3APOLYCAB"],
        ["RELIANCE", "Reliance Industries Ltd", 3188.40, "2026-05-26", 5, False, "2026-01-14", "https://www.tradingview.com/chart/?symbol=NSE%3ARELIANCE"],
        ["SRF", "SRF Ltd", 2931.90, "2026-05-26", 3, False, "2026-02-11", "https://www.tradingview.com/chart/?symbol=NSE%3ASRF"],
        ["ABB", "ABB India Ltd", 8023.30, "2026-05-26", 4, False, "2026-02-28", "https://www.tradingview.com/chart/?symbol=NSE%3AABB"],
    ]
    return pd.DataFrame(rows, columns=["symbol", "company_name", "current_price", "date", "historical_count", "is_new", "first_seen_date", "tradingview_url"])


def get_historical_analytics() -> pd.DataFrame:
    rows = [
        ["RELIANCE", "Reliance Industries Ltd", 5, "2026-05-26", "Rising breakout frequency"],
        ["ABB", "ABB India Ltd", 4, "2026-05-26", "Consistent leadership"],
        ["SRF", "SRF Ltd", 3, "2026-05-26", "Multi-month recurrence"],
        ["COFORGE", "Coforge Ltd", 3, "2026-05-21", "Momentum cooling"],
    ]
    return pd.DataFrame(rows, columns=["symbol", "company_name", "total_historical_count", "last_appeared_date", "trend_note"])


def get_most_active_data() -> pd.DataFrame:
    rows = [
        ["RELIANCE", "Reliance Industries Ltd", "18.42M", "2026-05-26", "Overlap", 12, "https://www.tradingview.com/chart/?symbol=NSE%3ARELIANCE"],
        ["ABB", "ABB India Ltd", "3.22M", "2026-05-26", "Overlap", 8, "https://www.tradingview.com/chart/?symbol=NSE%3AABB"],
        ["SBIN", "State Bank of India", "24.86M", "2026-05-26", "Not matched", 19, "https://www.tradingview.com/chart/?symbol=NSE%3ASBIN"],
        ["TATAMOTORS", "Tata Motors Ltd", "29.31M", "2026-05-26", "Not matched", 16, "https://www.tradingview.com/chart/?symbol=NSE%3ATATAMOTORS"],
    ]
    return pd.DataFrame(rows, columns=["symbol", "company_name", "volume", "date", "match_status", "historical_activity_count", "tradingview_url"])
