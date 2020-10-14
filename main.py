from application.salary import salary
from application.db.people import people
from datetime import datetime,date

print(datetime.now().strftime('%d/%m/%Y'))

Bill = salary
Bill.calculate_salary(Bill)

John = people
John.get_employees(John)



