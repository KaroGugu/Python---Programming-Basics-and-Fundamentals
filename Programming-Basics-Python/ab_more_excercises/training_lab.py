w = float(input())   # дължина в метри                # 15
h = float(input())  # широчина в метри              # 8.9


w_from_m_to_sm = w * 100
h_from_m_to_sm = h * 100

# Коридорът е широк поне 100 cm
corridor = 100

# Едно работно място заема 70 на 120 cm
w_area_for_desks = w_from_m_to_sm // 120            # - Коридор;  / 70см дължина на 1 работно място
h_area_for_desks = (h_from_m_to_sm - 100) // 70           # - Коридор;  / 120см ширина на 1 работно място

# заради входната врата (която е с отвор 160 cm) се губи точно 1 работно място
# заради катедрата (която е с размер 160 на 120 cm) се губят точно 2 работни места

desks = w_area_for_desks * h_area_for_desks - 3         # врата + катедра = 3 загубени работни места
print(int(desks))