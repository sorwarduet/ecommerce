
from datetime import datetime


def generate_order_id():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    new_order_id = ''
    for i in date_time:
        if i.isdigit():
            new_order_id += i

    return new_order_id
