from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")


def is_weekday(dt: datetime) -> bool:
    return dt.weekday() < 5


def get_market_status(now: datetime | None = None) -> dict:
    now = now.astimezone(IST) if now else datetime.now(IST)
    market_open = now.replace(hour=9, minute=15, second=0, microsecond=0)
    market_close = now.replace(hour=15, minute=30, second=0, microsecond=0)
    live = is_weekday(now) and market_open <= now <= market_close

    if live:
        remaining = market_close - now
        secondary = f"Closes in {str(remaining).split('.')[0]} · Holiday logic ready"
        label = "🟢 MARKET LIVE"
    else:
        next_open = now
        while True:
            next_open = (next_open + timedelta(days=1)).replace(hour=9, minute=15, second=0, microsecond=0)
            if next_open.weekday() < 5:
                break
        secondary = f"Next open: {next_open.strftime('%a, %d %b %Y · %I:%M %p IST')} · Holiday hook pending"
        label = "🔴 MARKET CLOSED"

    return {
        "is_live": live,
        "label": label,
        "current_time_text": now.strftime("%a, %d %b %Y · %I:%M:%S %p IST"),
        "secondary_text": secondary,
    }
