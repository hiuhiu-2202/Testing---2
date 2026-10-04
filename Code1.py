import string

def deliveryFee (price: float, distance: float, member: string):
    
    if price < 0.000 or distance < 0.00 or distance > 30.00 or member not in ['VIP', 'NORMAL']:
        return "Invalid"

    if price > 500000.000:             # Bug: Đổi price >= 500000.000 thành price > 500000.000
        return "Freeship"

    else:
        if member == 'NORMAL':     # Bug: Đổi member == 'VIP' thành member == 'NORMAL'
            if distance <= 10.00:
                return "10.000đ"
            else:
                return "20.000đ"
    
        else:
            if distance <= 10.00:
                return "20.000đ"
            else:
                return "30.000đ"

            