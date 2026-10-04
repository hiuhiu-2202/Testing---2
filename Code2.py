import string

def homeCredit (income: float, credit: float, loan: string):
    
    if income < 0.00 or credit < 0  or loan not in ['TRUE', 'FALSE']:
        return "Invalid"

    if income > 10.00 and credit >= 200 and loan == 'FALSE':     # Bug: Đổi income >= 10.00 thành income > 10.00
        return "Duyệt khoản vay"

    if credit >= 200 and loan == 'TRUE':                          # Bug: Đổi credit < 200 thành credit >= 200
        return "Từ chối khoản vay - có nợ xấu"

    if credit < 200 and loan == 'TRUE':                           # Bug: Đổi loan == 'FALSE' thành loan == 'TRUE'
        return "Từ chối khoản vay - điểm tín dụng thấp"

    if credit < 200 and loan == 'FALSE':                          # Bug: Đổi loan == 'TRUE' thành loan == 'FALSE'
        return "Từ chối khoản vay - hồ sơ xấu"

    if income < 10.00 and credit >= 200 and loan == 'FALSE':
        return "Yêu cầu bổ sung hồ sơ"
            