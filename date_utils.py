import datetime
def current_datetime():
    return datetime.now().date()

def format_date(date, format='%y-%m-%d'):
    return date.strftime(format)