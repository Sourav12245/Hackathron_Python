i = int(input())
while i > 0:
    day, month, year = [n for n in input().split(" ")]

    # day = 28
    # month = 'October'
    # year = 2000

    # print('{}-{}-{} -->'.format(day, month, year), end=" ")


    day = int(day)
    year = int(year)

    if day == 2:
        day = day - 1
    else:
        if day != 1:
            day = day - 1
            # day = 0
        elif day == 1 and month == 'January':
            day = 31
            month = 'December'
            year = year - 1
            # day = 0

        elif day == 1 and month == 'March':
            if int(year) % 4 == 0:
                day = 29
                month = 'February'
            else:
                day = 28
                month = 'February'

        if int(year) == 1900 and month == 'February' and day == 29:
            day = 28
            month = 'February'
        if int(year) == 1500 and month == 'February' and day == 29:
            day = 28
            month = 'February'
        if int(year) == 1700 and month == 'February' and day == 29:
            day = 28
            month = 'February'



    # if year in main_year:
    #     day = 28
    #     month = 'February'
                # day = 0
        # elif day == 1:
        #     d = day_check(month)
        #     b = month_item.get(month)
        #     day = d
        #     month = b

        '''Create a month list. Which will have months that have 30 and 31 days.
        # this will just take care of the day.
        Month will be taken care in separate function
        case is valid for 1st of the month'''
        # 31- jan, march, may, july, aug, oct, dec
        # mon_31 = ['May', 'July', 'August', 'October', 'December']

        # 30- feb, april, june, sept, nov
        mon_30 = ['February', 'April', 'June', 'September', 'November','August']


        def day_check(m):
            if m in mon_30:
                return 31
            else:
                return 30


        month_item = {
            "February": "January",
            "March": "February",
            "April": "March",
            "May": "April",
            "June": "May",
            "July": "June",
            "August": "July",
            "September": "August",
            "October": "September",
            "November": "October",
            "December": "November",
            "January": "December",
        }

        if day == 1:
            d = day_check(month)
            b = month_item.get(month)
            day = d
            month = b

        # print(month_item.get('January'))

    print("{} {} {}".format(day, month, year))
    i = int(i) - 1
