def convert_to_nepali(english_date):
    # Split the English date into year, month, and day
    year, month, day = map(int, english_date.split('-'))

    # Mapping of English month lengths
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Nepali month names
    nepali_months = [
        'Baishakh', 'Jestha', 'Ashad', 'Shrawan', 'Bhadra', 'Ashwin',
        'Kartik', 'Mangsir', 'Poush', 'Magh', 'Falgun', 'Chaitra'
    ]

    # Days per month for a normal year in Nepali calendar
    nepali_month_lengths = [
        31, 31, 32, 31, 31, 30, 30, 30, 29, 29, 30, 30
    ]

    # Initial Nepali date
    nepali_year = 2000
    nepali_month = 9
    nepali_day = 17

    # Days between 1943 AD and English date
    total_days = 0
    for i in range(1943, year):
        total_days += 365
        if i % 4 == 0:
            total_days += 1

    for i in range(0, month - 1):
        total_days += month_lengths[i]

    if month > 2 and year % 4 == 0:
        total_days += 1

    total_days += day - 1

    # Nepali month length
    nepali_month_length = nepali_month_lengths[nepali_month - 1]

    # Adjust Nepali date
    while total_days > nepali_month_length:
        total_days -= nepali_month_length
        nepali_month += 1
        nepali_month_length = nepali_month_lengths[nepali_month - 1]
        if nepali_month > 12:
            nepali_year += 1
            nepali_month = 1

    nepali_day += total_days

    # Format the result
    nepali_date = f"{nepali_year}-{nepali_month}-{nepali_day}"
    nepali_month_name = nepali_months[nepali_month - 1]

    return nepali_date, nepali_month_name


# # Example usage
# english_date = "2024-04-03"
# nepali_date, nepali_month_name = convert_to_nepali(english_date)
# print("Nepali Date:", nepali_date)
# print("Nepali Month:", nepali_month_name)
