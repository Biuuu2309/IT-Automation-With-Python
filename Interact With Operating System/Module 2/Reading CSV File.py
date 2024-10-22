import csv

f = open("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/data_hotel_booking.csv")

csv_f = csv.reader(f)
for row in csv_f:
    hotel, lead_time, reservation_status_date = row[0], row[2], row[-1]
    print(f'Hotel: {hotel}, Lead Time: {lead_time}, Reservation status date: {reservation_status_date}')
f.close()