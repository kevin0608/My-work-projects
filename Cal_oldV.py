#Defining a function
def Agency_Calculator():
    while True:
        try:
            num_events = int(input('Enter the number of events: '))
            break # This code only allows user to input integers before breaking the loop and proceding to the rest of the code
        except ValueError:
            print('Please enter a valid number.') #This code loops user to re enter a valid integer only.

    print('------------------------------')

    #Variables for Staffing Ration
    food_service = 20
    clearing = 50
    wine_waiters = 30
    bartenders = 50
    cloakroom = 100

    #Variables to for total staff combined in all events
    total_food_service_staff_combined = 0
    total_clearing_staff_combined = 0
    total_wine_waiters_staff_combined = 0
    total_bartenders_staff_combined = 0
    total_cloakroom_staff_combined = 0

    #Variables for total staffing cost categorically
    total_food_service_staff_cost = 0
    total_clearing_staff_cost = 0
    total_wine_waiters_staff_cost = 0
    total_bartenders_staff_cost = 0
    total_cloakroom_staff_cost = 0

    #Variable for total staff cost for all events
    total_staff_cost_for_all_events = 0

    #List of event names
    events_name_list = []

    #looped for the number of events and user inputs
    for event in range(num_events):
        print('Event ' + str(event + 1)) #Label of events looped
        event_name = input('Please enter the name of the event: ').upper() #asking user to input name of event and upper method capilised once recieved
        events_name_list.append(event_name) #this collect all the events name and make it into a list

        while True:
            try:
                guests = int(input('Please enter number of guests: ')) 
                break 
            except ValueError:
                print('Please enter a valid number.')

        while True:
            try:
                food_hours = int(input('Enter food server hours: '))
                break
            except ValueError:
                print('Please enter a valid number.')

        while True:
            try:
                clearing_hours = int(input('Enter clearing staff hours: '))
                break
            except ValueError:
                print('Please enter a valid number.')

        while True:
            try:
                wine_hours = int(input('Enter wine waiter hours: '))
                break
            except ValueError:
                print('Please enter a valid number.')

        while True:
            try:
                bartender_hours = int(input('Enter Bartender hours: '))
                break
            except ValueError:
                print('Please enter a valid number.')

        while True:
            try:
                cloakroom_hours = int(input('Enter cloakroom staff hours: '))
                break
            except ValueError:
                print('Please enter a valid number.')

        #Eqution for cloakroom variables
                
        remainder = guests % 100
        cloakroom_rounded = guests - remainder + 100

        #equation for staff cost
        food_Service_staff_cost = (guests // food_service) * 12 * food_hours
        clearing_staff_cost = (guests // clearing) * 11 * clearing_hours   
        wine_waiters_staff_cost = (guests // wine_waiters) * 12 * wine_hours
        bartender_staff_cost = (guests // bartenders) * 12.5 * bartender_hours
        if remainder >= 70:
            cloakroom_staff_cost = (cloakroom_rounded // cloakroom) * 11 * cloakroom_hours     
        else:
            cloakroom_staff_cost = (guests // cloakroom) * 11 * cloakroom_hours

        total_staff_cost = food_Service_staff_cost + clearing_staff_cost + wine_waiters_staff_cost + bartender_staff_cost + clearing_staff_cost

        #equation using inplace operator inside the loop to calculate total staff combined
        total_food_service_staff_combined += (guests // food_service)
        total_clearing_staff_combined += (guests // clearing)
        total_wine_waiters_staff_combined += (guests // wine_waiters)
        total_bartenders_staff_combined += (guests // bartenders) 
        if remainder >= 70:
            total_cloakroom_staff_combined += (cloakroom_rounded // cloakroom)
        else:
            total_cloakroom_staff_combined += (guests // cloakroom)

        #equation using inplace operator inside the loop for total of staff by category cost
        total_food_service_staff_cost += food_Service_staff_cost
        total_clearing_staff_cost += clearing_staff_cost
        total_wine_waiters_staff_cost += wine_waiters_staff_cost
        total_bartenders_staff_cost += bartender_staff_cost
        total_cloakroom_staff_cost += cloakroom_staff_cost

        #All events total Cost

        total_staff_cost_for_all_events += total_staff_cost

        #output of event's name, how much staff needed, and total staffing cost per event
        print(f'\n Event Name: {event_name}\n')

        print('******* NUMBER OF STAFF *******\n')

        if food_hours == 0:
            print(f'Food Service Staff: 0')
        else:
            print('Food Service Staff: ' + str(guests // food_service))
        if clearing_hours == 0:
            print(f'Clearing Staff: 0')
        else:
            print('Clearing Staff: ' + str(guests // clearing))
        if wine_hours == 0:
            print(f'Wine Waiter Staff: 0')
        else:
            print('Wine Waiter Staff: ' + str(guests // wine_waiters))
        if bartender_hours == 0:
            print(f'Bartender Staff: 0')
        else:
            print('Bartender Staff: ' + str(guests // bartenders))

        if cloakroom_hours == 0:
            print('Cloakroom Staff: 0')
        elif remainder >= 70:
            print('Cloakroom Staff: ' + str(cloakroom_rounded // cloakroom))
        else:
            print('Cloakroom Staff: ' + str(guests // cloakroom))

        print('\n******* STAFF COST*******\n')

        print(f'Food Service Staff Cost: £ {food_Service_staff_cost}')
        print(f'Clearing Staff Cost: £ {clearing_staff_cost}')
        print(f'Wine Waiter Staff Cost: £ {wine_waiters_staff_cost}')
        print(f'Bartender Staff Cost: £ {bartender_staff_cost}')
        print(f'Cloakroom Staff Cost: £ {cloakroom_staff_cost}\n')

        print(f'Total Staffing Cost: £ {total_staff_cost}\n')

     #output for total staffing, staffing cost and total cost for all events
    print('------------------------------')   
    print('******* TOTALS *******')

    print(f'\nEvents: {events_name_list}')
    
    print('\n***** STAFF ****\n')

    print(f'Total Food Service Staff: {total_food_service_staff_combined}')
    print(f'Total Clearing Staff: {total_clearing_staff_combined}')
    print(f'Total Wine Waiter Staff: {total_wine_waiters_staff_combined}')
    print(f'Total Bartender Staff: {total_bartenders_staff_combined}')
    print(f'Total Cloakroom Staff: {total_cloakroom_staff_combined}\n')

    print(f'***** STAFF COST *****\n')

    print(f'Total Service Staff Cost: £ {total_food_service_staff_cost}')
    print(f'Total Clearing Staff Cost: £ {total_clearing_staff_cost}')
    print(f'Total Wine Waiter Staff Cost: £ {total_wine_waiters_staff_cost}')
    print(f'Bartender Staff Cost: £ {total_bartenders_staff_cost}')
    print(f'Total Cloakroom Staff Cost: £ {total_cloakroom_staff_cost}\n')

    print(f'\n***** TOTAL EXPENSES *****\n')

    print(f'Total Staffing Events Cost: £ {total_staff_cost_for_all_events}')


Agency_Calculator()