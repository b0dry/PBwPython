from datetime import datetime, timedelta

tmp = input()
result = datetime.strptime(tmp, '%d-%m-%Y')
result = result + timedelta(days=999)


print(f'{result.day}-{result.month}-{result.year}')
