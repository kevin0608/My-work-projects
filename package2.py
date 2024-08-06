import tkinter as tk
from tkinter import ttk
# import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from tabulate import tabulate
import pandas as pd

staff_ratios = {'food_waiter' : 25, 
                'clearing' : 50, 
                'wine_waiters' : 30, 
                'bartenders' : 50, 
                'cloakroom': 100,
                'barback' : 200
                }
staff_rates = {'food_waiter' : 15.53, 
               'wine_waiter' : 16.20, 
               'bartender' : 16.89,
               'cloakroom' : 15.53,
               'barback' : 15.53, 
               'hostess' : 18.50,
               'porter' : 15.53}

def validate_numeric_input(input_str):
            try:
                # Try converting to integer
                int_value = int(input_str)
                return int_value
            except ValueError:
                try:
                    # Try converting to float
                    float_value = float(input_str)
                    return float_value
                except ValueError:
                    return None

class EventDDR:
    def __init__(self, hostess, ddr_meeting_rooms, event_name, event_type, guests, event_start, event_lunch, event_end, morning_team_hours, evening_team_hours, cloakroom_hours, hostess_hours, event_date):
        self.hostess = hostess
        self.room = ddr_meeting_rooms
        self.name = event_name
        self.type = event_type
        self.guests = guests
        self.event_start = event_start
        self.event_lunch = event_lunch
        self.event_end = event_end
        self.morning_team_hours = morning_team_hours
        self.evening_team_hours = evening_team_hours
        self.cloakroom_hours = cloakroom_hours
        self.hostess_hours = hostess_hours
        self.event_date = event_date
    
        self.calculate_staff()
        self.calculate_staff_cost()
    
    # Function to calculate time format into integers as hours
    def time_to_int(time_str):
        # Split the time string into hours and minutes
        hours, minutes = map(int, time_str.split(':'))

        # Convert the time to total minutes
        total_minutes = hours * 60 + minutes
        return total_minutes
    
    def calculate_morning_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDDR.time_to_int(start_time_str)
        end_time = EventDDR.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 60
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_cloakroom_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDDR.time_to_int(start_time_str)
        end_time = EventDDR.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 60
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def event_duration(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDDR.time_to_int(start_time_str)
        end_time = EventDDR.time_to_int(end_time_str)

        start_time = start_time 
        end_time = end_time 
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
            
    def calculate_staff(self):
        self.morn_num_food_staff= 0
        self.eve_num_food_staff= 0
        self.num_cloakroom_staff = 0
        self.morn_num_food_staff += int(self.room)
        self.num_hostess_staff = int(self.hostess)

        self.hot_food_staff = round(self.guests / 30)

        if self.guests <= 80:
            self.morn_num_food_staff += 4
            self.num_cloakroom_staff += 1
            if self.type == 'DDR BOWL':
                self.eve_num_food_staff += 1
                self.eve_num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.eve_num_food_staff += 2

        elif self.guests > 80 and self.guests <= 100:
            self.morn_num_food_staff += 7
            self.num_cloakroom_staff += 1
            if self.type == 'DDR BOWL':
                self.eve_num_food_staff += 1
                self.eve_num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.eve_num_food_staff += 3

        elif self.guests > 100 and self.guests <= 150:
            self.morn_num_food_staff += 7
            if self.guests > 100:
                self.morn_num_food_staff += 2
            elif self.guests == 150:
                self.morn_num_food_staff += 3
            self.num_cloakroom_staff += 1
            if self.type == 'DDR BOWL':
                self.eve_num_food_staff += 2
                self.eve_num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.eve_num_food_staff += 4

        elif self.guests > 150 and self.guests <= 200:
            self.morn_num_food_staff += 6
            if self.guests >= 150:
                self.morn_num_food_staff += 4
            elif self.guests == 200:
                self.morn_num_food_staff += 4
            self.num_cloakroom_staff += 2
            if self.type == 'DDR BOWL':
                self.eve_num_food_staff += 2
                self.eve_num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.eve_num_food_staff += 4

        elif self.guests > 200 and self.guests <= 250:
            self.morn_num_food_staff += 13
            if self.guests > 200:
                self.num_cloakroom_staff += 2
            elif self.guests > 250 and self.guests <= 300:
                self.num_cloakroom_staff += 3
            if self.type == 'DDR BOWL':
                self.eve_num_food_staff += 3
                self.eve_num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.eve_num_food_staff += 5
        
        elif self.guests > 250 and self.guests <= 300:
            self.morn_num_food_staff += 13
            self.num_cloakroom_staff += 3
            if self.type == 'DDR BOWL':
                self.eve_num_food_staff += 3
                self.eve_num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.eve_num_food_staff += 5
        # totals
        self.ddr_total_staff_combined = sum([self.morn_num_food_staff, self.eve_num_food_staff, self.num_cloakroom_staff, self.num_hostess_staff])
        self.total_num_food_staff = self.morn_num_food_staff + self.eve_num_food_staff

    def calculate_staff_cost(self):

        self.food_service_staff_cost = round((self.morn_num_food_staff * self.morning_team_hours * staff_rates['food_waiter']) + (self.eve_num_food_staff * 8 * staff_rates['food_waiter']), 2)
        self.cloakroom_staff_cost = round(self.num_cloakroom_staff * self.cloakroom_hours * staff_rates['cloakroom'], 2)
        self.meeting_room_staff_cost = round(int(self.room) * self.morning_team_hours * staff_rates['food_waiter'], 2)

        self.morn_staff_cost = round(self.morn_num_food_staff * self.morning_team_hours * staff_rates['food_waiter'], 2)
        self.eve_staff_cost = round(self.eve_num_food_staff * self.evening_team_hours * staff_rates['food_waiter'], 2)
        self.hostess_staff_cost = round(self.num_hostess_staff * self.hostess_hours * staff_rates['hostess'], 2)

        self.total_staff_cost = round(sum([self.food_service_staff_cost, self.cloakroom_staff_cost, self.meeting_room_staff_cost, self.hostess_staff_cost]), 2)


class EventDinner:
    def __init__(self, event_name, event_type, guests, event_start, event_dessert, event_end, food_staff75_hours, food_staff25_hours, wine_staff_hours, bartender_hours, barback_hours, cloak_hours):
        self.name = event_name
        self.type = event_type
        self.guests = guests
        self.event_start = event_start
        self.event_lunch = event_dessert
        self.event_end = event_end

        self.food_staff75_hours = food_staff75_hours
        self.food_staff25_hours = food_staff25_hours
        self.wine_staff_hours = wine_staff_hours
        self.bartender_hours = bartender_hours
        self.barback_hours = barback_hours
        self.cloak_hours = cloak_hours

        self.calculate_staff()
        self.calculate_staff_cost()

    def time_to_int(time_str):
        # Split the time string into hours and minutes
        hours, minutes = map(int, time_str.split(':'))

        # Convert the time to total minutes
        total_minutes = hours * 60 + minutes
        return total_minutes
    
    def calculate_food75_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDinner.time_to_int(start_time_str)
        end_time = EventDinner.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 60
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_food25_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDinner.time_to_int(start_time_str)
        end_time = EventDinner.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 60
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_wine_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDinner.time_to_int(start_time_str)
        end_time = EventDinner.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 60
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_bartender_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDinner.time_to_int(start_time_str)
        end_time = EventDinner.time_to_int(end_time_str)

        start_time = start_time - 120
        end_time = end_time + 120
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_barback_team_time(start_time_str, end_time_str):
        start_time = EventDinner.time_to_int(start_time_str)
        end_time = EventDinner.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 120
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_cloack_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDinner.time_to_int(start_time_str)
        end_time = EventDinner.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 60
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def event_duration(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDinner.time_to_int(start_time_str)
        end_time = EventDinner.time_to_int(end_time_str)

        start_time = start_time 
        end_time = end_time 
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours

    def calculate_staff(self):
            
            self.num_food_staff = 0
            self.num_clearing_staff = 0
            self.num_cloakroom_staff = 0
            self.num_barback_staff = 0
            self.num_sides_staff = 0

            if self.guests < 170:
                self.num_sides_staff += 4
            elif self.guests < 240:
                self.num_sides_staff += 6
            elif self.guests < 310:
                self.num_sides_staff += 8
            elif self.guests < 400:
                self.num_sides_staff += 10
        
        
            self.num_food_staff = round(self.guests / staff_ratios['food_waiter'])

            self.num_clearing_staff = round(self.guests / staff_ratios['clearing'])
            self.num_food_staff += round(self.guests / staff_ratios['clearing'])  

            self.num_wine_staff = round(self.guests / staff_ratios['wine_waiters'])
            self.num_bartenders_staff = round(self.guests / staff_ratios['bartenders'])

            self.num_barback_staff = self.guests / staff_ratios['barback']
            if self.num_barback_staff < 1:
                self.num_barback_staff = 0
            self.num_barback_staff = round(self.num_barback_staff)

            remainder = self.guests % 100
            cloakroom_rounded = self.guests - remainder + 100

            if remainder >= 30:
                self.num_cloakroom_staff += (cloakroom_rounded // staff_ratios['cloakroom'])
            else:
                self.num_cloakroom_staff += (self.guests // staff_ratios['cloakroom'])

            self.total_staff_combined = sum([self.num_food_staff, 
                                         self.num_wine_staff, self.num_bartenders_staff, self.num_barback_staff, 
                                         self.num_cloakroom_staff])
            self.num_food_staff75 = round(self.num_food_staff * 0.75)
            self.num_food_staff25 =round(self.num_food_staff * 0.25)

    def calculate_staff_cost(self):
        
            self.food_service_staff75_cost = round(self.num_food_staff75 * self.food_staff75_hours * staff_rates["food_waiter"], 2)
            self.food_service_staff25_cost = round(self.num_food_staff25 * self.food_staff25_hours * staff_rates["food_waiter"], 2)
            self.food_service_staff100_cost = round(self.food_service_staff75_cost + self.food_service_staff25_cost, 2)

            # Nobu Menu
            self.sides_staff_cost = round(self.num_sides_staff * self.food_staff75_hours * staff_rates["food_waiter"], 2)

            self.wine_waiters_staff_cost = round(self.num_wine_staff * self.wine_staff_hours * staff_rates["wine_waiter"], 2)
            self.bartenders_staff_cost = round(self.num_bartenders_staff * self.bartender_hours * staff_rates["bartender"], 2)
            self.barback_staff_cost = round(self.num_barback_staff * self.barback_hours * staff_rates["barback"], 2)
            self.cloakroom_staff_cost = round(self.num_cloakroom_staff * self.cloak_hours * staff_rates["cloakroom"], 2)
            
            self.total_staff_cost = round(sum([self.food_service_staff100_cost,
                                        self.wine_waiters_staff_cost, self.bartenders_staff_cost, self.barback_staff_cost,
                                        self.cloakroom_staff_cost]), 2)

class EventReception:
    def __init__(self, event_name, event_type, guests, event_start, event_end, food_staff_hours, wine_staff_hours, bartender_hours, barback_hours, cloak_hours):
        self.name = event_name
        self.type = event_type
        self.guests = guests
        self.event_start = event_start
        self.event_end = event_end

        self.food_staff_hours = food_staff_hours
        self.wine_staff_hours = wine_staff_hours
        self.bartender_hours = bartender_hours
        self.barback_hours = barback_hours
        self.cloak_hours = cloak_hours

        self.calculate_staff()
        self.calculate_staff_cost()

    def time_to_int(time_str):
        # Split the time string into hours and minutes
        hours, minutes = map(int, time_str.split(':'))

        # Convert the time to total minutes
        total_minutes = hours * 60 + minutes
        return total_minutes

    
    def calculate_food_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventReception.time_to_int(start_time_str)
        end_time = EventReception.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 60
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_wine_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventReception.time_to_int(start_time_str)
        end_time = EventReception.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 60
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_bartender_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventDinner.time_to_int(start_time_str)
        end_time = EventDinner.time_to_int(end_time_str)

        start_time = start_time - 120
        end_time = end_time + 120
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_barback_team_time(start_time_str, end_time_str):
        start_time = EventReception.time_to_int(start_time_str)
        end_time = EventReception.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 120
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def calculate_cloack_team_time(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventReception.time_to_int(start_time_str)
        end_time = EventReception.time_to_int(end_time_str)

        start_time = start_time - 60
        end_time = end_time + 60
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours
    
    def event_duration(start_time_str, end_time_str):
        # Convert start and end times to integers
        start_time = EventReception.time_to_int(start_time_str)
        end_time = EventReception.time_to_int(end_time_str)

        start_time = start_time 
        end_time = end_time 
        # If end time is before start time, it means it spans across midnight
        if end_time < start_time:
            end_time += 24 * 60  # Add 24 hours to end time
        
        # Calculate time difference in minutes
        time_difference = end_time - start_time
        
        # Convert time difference to hours
        time_difference_hours = time_difference / 60
        
        return time_difference_hours

    def calculate_staff(self):
            
            self.num_food_staff = 0
            self.num_clearing_staff = 0
            self.num_cloakroom_staff = 0
            self.num_barback_staff = 0
        
            self.num_food_staff = round(self.guests / staff_ratios['food_waiter'])

            self.num_clearing_staff = round(self.guests / staff_ratios['clearing'])
            self.num_food_staff += round(self.guests / staff_ratios['clearing'])  

            self.num_wine_staff = round(self.guests / staff_ratios['wine_waiters'])
            self.num_bartenders_staff = round(self.guests / staff_ratios['bartenders'])

            self.num_barback_staff = self.guests / staff_ratios['barback']
            if self.num_barback_staff < 1:
                self.num_barback_staff = 0
            self.num_barback_staff = round(self.num_barback_staff)

            remainder = self.guests % 100
            cloakroom_rounded = self.guests - remainder + 100

            if remainder >= 30:
                self.num_cloakroom_staff += (cloakroom_rounded // staff_ratios['cloakroom'])
            else:
                self.num_cloakroom_staff += (self.guests // staff_ratios['cloakroom'])

            self.total_staff_combined = sum([self.num_food_staff, 
                                         self.num_wine_staff, self.num_bartenders_staff, self.num_barback_staff, 
                                         self.num_cloakroom_staff])

    def calculate_staff_cost(self):
        
            self.food_service_staff_cost = round(self.num_food_staff * self.food_staff_hours * staff_rates["food_waiter"], 2)
            self.wine_waiters_staff_cost = round(self.num_wine_staff * self.wine_staff_hours * staff_rates["wine_waiter"], 2)
            self.bartenders_staff_cost = round(self.num_bartenders_staff * self.bartender_hours * staff_rates["bartender"], 2)
            self.barback_staff_cost = round(self.num_barback_staff * self.barback_hours * staff_rates["barback"], 2)
            self.cloakroom_staff_cost = round(self.num_cloakroom_staff * self.cloak_hours * staff_rates["cloakroom"], 2)
            
            self.total_staff_cost = round(sum([self.food_service_staff_cost,
                                        self.wine_waiters_staff_cost, self.bartenders_staff_cost, self.barback_staff_cost,
                                        self.cloakroom_staff_cost]), 2)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Events Agency Calculator')
        self.create_widgets()

         # Varialbes for total staff in category
        self.total_food_service_staff_combined = 0
        self.total_clearing_staff_combined = 0
        self.total_wine_waiters_staff_combined = 0
        self.total_bartender_staff_combined = 0
        self.total_barback_staff_combined = 0
        self.total_cloakroom_staff_combined = 0
        self.total_hostess_staff_combined = 0
        self.total_porter_staff_combined = 0
        self.total_guests_combined = 0

         # Variables for total staffing cost by category
        self.total_food_service_staff_cost = round(0, 2)
        self.total_clearing_staff_cost = round(0, 2)
        self.total_wine_waiters_staff_cost = round(0, 2)
        self.total_bartender_staff_cost = round(0, 2)
        self.total_barback_staff_cost = round(0, 2)
        self.total_cloakroom_staff_cost = round(0, 2)
        self.total_hostess_staff_cost = round(0, 2)
        self.total_porter_staff_cost = round(0, 2)

        #total staff combined and cost for all events
        self.total_staff_combined_for_all_events = 0
        self.total_staff_cost_for_all_events = round(0, 2)

        #Clipboard list
        self.tsv_list = []

        # lists
        self.events_name_list = []
        self.event_type_list = []
        self.guests_list = []
        self.event_durations_list = []
        self.event_date_list = []
        self.event_staff_total_count_list = []
        self.event_total_cost_list = []

        #sub overview DDR Bowl lists
        self.ddr_bowl_events_name_list = []
        self.ddr_bowl_event_type_list = []
        self.ddr_bowl_event_durations_list = []
        self.ddr_bowl_event_date_list = []
        self.ddr_bowl_guests_list = []
        self.ddr_bowl_event_staff_total_count_list = []
        self.ddr_bowl_event_total_cost_list = []

        self.total_ddr_bowl_guests_list = 0
        self.total_ddr_bowl_event_staff_total_count_list = 0
        self.total_ddr_bowl_event_total_cost_list = 0

        #sub overview DDR Buffet lists
        self.ddr_buffet_events_name_list = []
        self.ddr_buffet_event_type_list = []
        self.ddr_buffet_event_durations_list = []
        self.ddr_buffet_event_date_list = []
        self.ddr_buffet_guests_list = []
        self.ddr_buffet_event_staff_total_count_list = []
        self.ddr_buffet_event_total_cost_list = []

        self.total_ddr_buffet_guests_list = 0
        self.total_ddr_buffet_event_staff_total_count_list = 0
        self.total_ddr_buffet_event_total_cost_list = 0

        #sub overview Dinner lists
        self.dinner_events_name_list = []
        self.dinner_event_type_list = []
        self.dinner_event_durations_list = []
        self.dinner_event_date_list = []
        self.dinner_guests_list = []
        self.dinner_event_staff_total_count_list = []
        self.dinner_event_total_cost_list = []

        self.total_dinner_guests_list = 0
        self.total_dinner_event_staff_total_count_list = 0
        self.total_dinner_event_total_cost_list = 0

        #sub overview Dinner Nobu Menu lists
        self.dinner_nm_events_name_list = []
        self.dinner_nm_event_type_list = []
        self.dinner_nm_event_durations_list = []
        self.dinner_nm_event_date_list = []
        self.dinner_nm_guests_list = []
        self.dinner_nm_event_staff_total_count_list = []
        self.dinner_nm_event_total_cost_list = []

        self.total_dinner_nm_guests_list = 0
        self.total_dinner_nm_event_staff_total_count_list = 0
        self.total_dinner_nm_event_total_cost_list = 0

        #sub overview reception lists
        self.reception_events_name_list = []
        self.reception_event_type_list = []
        self.reception_event_durations_list = []
        self.reception_event_date_list = []
        self.reception_guests_list = []
        self.reception_event_staff_total_count_list = []
        self.reception_event_total_cost_list = []

        self.total_reception_guests_list = 0
        self.total_reception_event_staff_total_count_list = 0
        self.total_reception_event_total_cost_list = 0

        # Override variables
        self.AM_food_add_ovr = 0
        self.PM_food_add_ovr = 0
        self.food_add_ovr = 0
        self.wine_add_ovr = 0
        self.bar_add_ovr = 0
        self.barback_add_ovr = 0
        self.cloakroom_add_ovr = 0
        self.hostess_add_ovr = 0
        self.porter_add_ovr = 0

        self.AM_food_sub_ovr = 0
        self.PM_food_sub_ovr = 0
        self.food_sub_ovr = 0
        self.wine_sub_ovr = 0
        self.bar_sub_ovr = 0
        self.barback_sub_ovr = 0
        self.cloakroom_sub_ovr = 0
        self.hostess_sub_ovr = 0
        self.porter_sub_ovr = 0

        # Graph values
        # self.x = np.array(self.events_name_list)
        # self.y = np.array(self.event_total_cost_list)

    def clear_fields(self):
        
        self.event_name_entry.delete(0, tk.END)
        self.guests_entry.delete(0, tk.END)
        self.event_time_start_entry.delete(0, tk.END)
        self.event_time_lunchdinner_entry.delete(0, tk.END)
        self.event_time_end_entry.delete(0, tk.END)
        self.event_date_entry.delete(0, tk.END)
        self.ddr_meeting_rooms_entry.delete(0, tk.END)
        self.hostess_entry.delete(0, tk.END)
        self.porter_entry.delete(0, tk.END)
        self.food_waiter_entry.delete(0, tk.END)
        self.output_text.delete(1.0, tk.END)
        

         # Varialbes for total staff in category
        self.total_food_service_staff_combined = 0
        self.total_wine_waiters_staff_combined = 0
        self.total_bartender_staff_combined = 0
        self.total_barback_staff_combined = 0
        self.total_cloakroom_staff_combined = 0
        self.total_hostess_staff_combined = 0
        self.total_porter_staff_combined = 0
        self.total_guests_combined = 0

         # Variables for total staffing cost by category
        self.total_food_service_staff_cost = 0
        self.total_wine_waiters_staff_cost = 0
        self.total_bartender_staff_cost = 0
        self.total_barback_staff_cost = 0
        self.total_cloakroom_staff_cost = 0
        self.total_hostess_staff_cost = 0
        self.total_porter_staff_cost = 0

        #total staff combined and cost for all events
        self.total_staff_combined_for_all_events = 0
        self.total_staff_cost_for_all_events = 0

        # lists
        self.events_name_list = []
        self.event_type_list = []
        self.guests_list = []
        self.event_durations_list = []
        self.event_date_list = []
        self.event_staff_total_count_list = []
        self.event_total_cost_list = []

        #sub overview DDR Bowl lists
        self.ddr_bowl_events_name_list = []
        self.ddr_bowl_event_type_list = []
        self.ddr_bowl_event_durations_list = []
        self.ddr_bowl_event_date_list = []
        self.ddr_bowl_guests_list = []
        self.ddr_bowl_event_staff_total_count_list = []
        self.ddr_bowl_event_total_cost_list = []

        self.total_ddr_bowl_guests_list = 0
        self.total_ddr_bowl_event_staff_total_count_list = 0
        self.total_ddr_bowl_event_total_cost_list = 0

        #sub overview DDR Buffet lists
        self.ddr_buffet_events_name_list = []
        self.ddr_buffet_event_type_list = []
        self.ddr_buffet_event_durations_list = []
        self.ddr_buffet_event_date_list = []
        self.ddr_buffet_guests_list = []
        self.ddr_buffet_event_staff_total_count_list = []
        self.ddr_buffet_event_total_cost_list = []

        self.total_ddr_buffet_guests_list = 0
        self.total_ddr_buffet_event_staff_total_count_list = 0
        self.total_ddr_buffet_event_total_cost_list = 0

        #sub overview Dinner lists
        self.dinner_events_name_list = []
        self.dinner_event_type_list = []
        self.dinner_event_durations_list = []
        self.dinner_event_date_list = []
        self.dinner_guests_list = []
        self.dinner_event_staff_total_count_list = []
        self.dinner_event_total_cost_list = []

        self.total_dinner_guests_list = 0
        self.total_dinner_event_staff_total_count_list = 0
        self.total_dinner_event_total_cost_list = 0

        #sub overview Dinner Nobu Menu lists
        self.dinner_nm_events_name_list = []
        self.dinner_nm_event_type_list = []
        self.dinner_nm_event_durations_list = []
        self.dinner_nm_event_date_list = []
        self.dinner_nm_guests_list = []
        self.dinner_nm_event_staff_total_count_list = []
        self.dinner_nm_event_total_cost_list = []

        self.total_dinner_nm_guests_list = 0
        self.total_dinner_nm_event_staff_total_count_list = 0
        self.total_dinner_nm_event_total_cost_list = 0

        #sub overview reception lists
        self.reception_events_name_list = []
        self.reception_event_type_list = []
        self.reception_event_durations_list = []
        self.reception_event_date_list = []
        self.reception_guests_list = []
        self.reception_event_staff_total_count_list = []
        self.reception_event_total_cost_list = []

        self.total_reception_guests_list = 0
        self.total_reception_event_staff_total_count_list = 0
        self.total_reception_event_total_cost_list = 0

    def create_widgets(self):   

        # Labels and entries for each event 
        self.event_frame = ttk.Frame(self.root)
        self.event_frame.grid(padx=0, pady=0)

        # Event type option menu
        self.event_types = ["Dinner", "Dinner Nobu Menu", "DDR Bowl", "DDR Buffet", "Reception", "Set up"]
        self.event_type_label = ttk.Label(self.event_frame, text="Event Type:")
        self.event_type_label.grid(row=0, column=0)
        self.event_type_var = tk.StringVar(root)
        self.event_type_var.set(self.event_types[0])
        self.event_type_dropdown = ttk.Combobox(self.event_frame, textvariable=self.event_type_var, values=self.event_types, width=2)
        self.event_type_dropdown.grid(row=0, column=1)

        # Override drop down options
        self.override_hrs = ["DDR AM FW", "DDR PM FW", "Food Waiter","Wine Waiter", "Bartender", "Barback", "Cloakroom", "Porter", "Hostess"]
        self.override_hrs_var = tk.StringVar(root)
        self.override_hrs_var.set(self.override_hrs[0])
        self.override_hrs_dropdown = ttk.Combobox(self.event_frame, textvariable=self.override_hrs_var, values=self.override_hrs, width=8)
        self.override_hrs_dropdown.grid(row=2, column=13, columnspan=2)

        # Sub Overview drop down options
        self.sub_overview = ["Dinner", "Dinner Nobu Menu", "DDR Bowl", "DDR Buffet", "Reception"]
        self.sub_overview_var = tk.StringVar(root)
        self.sub_overview_var.set(self.sub_overview[0])
        self.sub_overview_dropdown = ttk.Combobox(self.event_frame, textvariable=self.sub_overview_var, values=self.sub_overview, width=8)
        self.sub_overview_dropdown.grid(row=2, column=15)

        #Phasu credit label
        # self.Phasu = ttk.Label(self.event_frame, text="Credits to Phasu", font=8)
        # self.Phasu.grid(row=9, column=15)

         # DDR Meeting rooms / Hostess
        self.DDR_label = ttk.Label(self.event_frame, text="DDR")
        self.DDR_label.grid(row=1, column=7)

        self.ddr_meeting_rooms_label = ttk.Label(self.event_frame, text="Meeting Rooms:")
        self.ddr_meeting_rooms_label.grid(row=2, column=6)
        self.ddr_meeting_rooms_entry = ttk.Entry(self.event_frame, width=5)
        self.ddr_meeting_rooms_entry.grid(row=2, column=7)

        self.additional_staffing_label= ttk.Label(self.event_frame, text="Additional Staffing")
        self.additional_staffing_label.grid(row=1, column=10)

        self.hostess_label= ttk.Label(self.event_frame, text="Hostess:")
        self.hostess_label.grid(row=3, column=6)
        self.hostess_entry = ttk.Entry(self.event_frame, width=5)
        self.hostess_entry.grid(row=3, column=7)

        self.food_waiter_label= ttk.Label(self.event_frame, text="Food Waiter:")
        self.food_waiter_label.grid(row=2, column=9, columnspan=1, sticky='E')
        self.food_waiter_entry = ttk.Entry(self.event_frame, width=5)
        self.food_waiter_entry.grid(row=2, column=10)

        self.porter_label= ttk.Label(self.event_frame, text="Porter:")
        self.porter_label.grid(row=3, column=9, columnspan=1, sticky='E')
        self.porter_entry = ttk.Entry(self.event_frame, width=5)
        self.porter_entry.grid(row=3, column=10)

        self.event_name_label = ttk.Label(self.event_frame, text="Event Name:")
        self.event_name_label.grid(row=1, column=0)
        self.event_name_entry = ttk.Entry(self.event_frame, width=14)
        self.event_name_entry.grid(row=1, column=1)

        self.event_date_label = ttk.Label(self.event_frame, text="Date:")
        self.event_date_label.grid(row=1, column=2)
        self.event_date_entry = ttk.Entry(self.event_frame, width=9)
        self.event_date_entry.grid(row=1, column=2, columnspan=4)

        self.event_type_dropdown.config(width=12)
   
        self.guests_label = ttk.Label(self.event_frame, text="Guests:")
        self.guests_label.grid(row=2, column=0)
        self.guests_entry = ttk.Entry(self.event_frame, width=14)
        self.guests_entry.grid(row=2, column=1)

        # event timing labels and entry fields
        self.event_time_label = ttk.Label(self.event_frame, text="Event Time:")
        self.event_time_label.grid(row=3, column=0)

        self.lunchdinner_timing_label = ttk.Label(self.event_frame, text="Start")
        self.lunchdinner_timing_label.grid(row=4, column=1)
        self.event_time_start_entry = ttk.Entry(self.event_frame, width=14)
        self.event_time_start_entry.grid(row=3, column=1)
    
        self.lunchdinner_timing_label = ttk.Label(self.event_frame, text="Lunch|Dessert")
        self.lunchdinner_timing_label.grid(row=4, column=2)
        self.event_time_lunchdinner_entry = ttk.Entry(self.event_frame, width=14)
        self.event_time_lunchdinner_entry.grid(row=3, column=2)

        self.end_timing_label = ttk.Label(self.event_frame, text="End")
        self.end_timing_label.grid(row=4, column=3)
        self.event_time_end_entry = ttk.Entry(self.event_frame, width=14)
        self.event_time_end_entry.grid(row=3, column=3)

         # Button to calculate
        self.add_events_button = ttk.Button(self.event_frame, text="Calculate", command=self.calculate_expenses, width=12)
        self.add_events_button.grid(row=0, column=13)
        root.bind('<Return>', self.calculate_expenses)

        # Button to clear fields
        self.total_button = ttk.Button(self.event_frame, text="Overview", command=self.overview_reports, width=12)
        self.total_button.grid(row=0, column=14)

        # Button to clear fields
        self.clear_button = ttk.Button(self.event_frame, text="Clear", command=self.clear_fields, width=10)
        self.clear_button.grid(row=0, column=15)

         # Button to add
        self.add_button = ttk.Button(self.event_frame, text="Add", command=self.add, width=3)
        self.add_button.grid(row=4, column=10)

        # Override Feature
        self.override_label= ttk.Label(self.event_frame, text="Override Hrs")
        self.override_label.grid(row=1, column=13)
        self.override_hrs_entry = ttk.Entry(self.event_frame, width=5)
        self.override_hrs_entry.grid(row=2, column=13)


        self.addovr_button = ttk.Button(self.event_frame, text="+", command=self.add_ovr, width=1)
        self.addovr_button.grid(row=3, column=13)

        self.subovr_button = ttk.Button(self.event_frame, text="-", command=self.sub_ovr, width=1)
        self.subovr_button.grid(row=4, column=13)

        self.sub_overview_button = ttk.Button(self.event_frame, text="Print", command=self.suboverview_reports)
        self.sub_overview_button.grid(row=3, column=15)

        copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=5, column=0, sticky="s")
        

        # Output text box
        output_label = ttk.Label(root, text="")
        output_label.grid(row=1, column=0, sticky="w")

        self.output_text = tk.Text(root, height=58, width=150, font=("Courier", 12))
        self.output_text.grid(row=2, column=0, columnspan=6, sticky='nsew')

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(root, command=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=2, column=6, sticky='ns')

        self.output_text.tag_configure("green", foreground="green")
        self.output_text.tag_configure("red", foreground="red")
        self.output_text.tag_configure("yellow", foreground="yellow")
        self.output_text.tag_configure("purple", foreground="purple")
        self.output_text.tag_configure("orange", foreground="orange")

    def copy_to_clipboard(self):

        tsv_ddr1 = self.ddr_clipboard1.to_csv(sep='\t', index=False, header=False)
        tsv_ddr2 = self.ddr_clipboard2.to_csv(sep='\t', index=False, header=False)
        tsv_ddr3 = self.ddr_clipboard3.to_csv(sep='\t', index=False, header=False)
        tsv_ddr4 = self.ddr_clipboard4.to_csv(sep='\t', index=False, header=False)
        tsv_ddr5 = self.ddr_clipboard5.to_csv(sep='\t', index=False, header=False)

        self.tsv_list.append(tsv_ddr1)
        self.tsv_list.append(tsv_ddr2)
        self.tsv_list.append(tsv_ddr3)
        self.tsv_list.append(tsv_ddr4)
        self.tsv_list.append(tsv_ddr5)

        self.tsv_string = '\n'.join(self.tsv_list)

        root.clipboard_clear()
        root.clipboard_append(self.tsv_string)
        root.update()  

    def add(self):

        num_food_waiter = 0
        num_porter_staff = 0

        event_name = self.event_name_entry.get().upper()
        event_type = self.event_type_var.get().upper()
        event_date = self.event_date_entry.get()
        guests = self.guests_entry.get()
        
        # try:
        food_waiter = self.food_waiter_entry.get()
        if not food_waiter:
            food_waiter = 0
        
            
        porter = self.porter_entry.get()
        if not porter:
            porter = 0

        num_food_waiter += int(food_waiter)
        num_porter_staff += int(porter)

        food_waiter_hours = 8
        porter_hours = 8

        food_waiter_cost = num_food_waiter * food_waiter_hours * staff_rates["food_waiter"]
        porter_cost = num_porter_staff * porter_hours * staff_rates["porter"]

        additional_staffing_staff_combined = (num_food_waiter + num_porter_staff)
        additional_staffing_staff_cost = round(food_waiter_cost + porter_cost, 2)

        self.total_food_service_staff_combined += num_food_waiter
        self.total_porter_staff_combined += num_porter_staff

        self.total_staff_combined_for_all_events += additional_staffing_staff_combined
        self.total_staff_cost_for_all_events += additional_staffing_staff_cost

        self.total_food_service_staff_cost += food_waiter_cost
        self.total_porter_staff_cost += porter_cost

        self.events_name_list.append(event_name)
        self.event_type_list.append(event_type)
        self.guests_list.append(guests)
        self.event_staff_total_count_list.append(additional_staffing_staff_combined)
        self.event_date_list.append(event_date)
        self.event_durations_list.append("N/A")
        self.event_total_cost_list.append(additional_staffing_staff_cost)

        self.output_text.insert(tk.END, f'----------------------------------------------------------------------------- ADDITIONAL STAFFING -------------------------------------------------------------------------------\n','orange')
        event_data = [["Event Name", "Event Type", "Number of Guests", "Date"],
                      [event_name, event_type, guests, event_date]]

        additional_staffing_data = [["Staff", "Number of Staff","Rates Per Hour","Hours", "Cost"],
                                    ["Food Waiter", num_food_waiter, staff_rates["food_waiter"], food_waiter_hours, food_waiter_cost],
                                    ["Porter", num_porter_staff, staff_rates["porter"], porter_hours, porter_cost],
                                    ["Totals", additional_staffing_staff_combined, "","", additional_staffing_staff_cost]]
        event_table = tabulate(event_data, headers="firstrow", tablefmt="fancy_grid") + "\n\n"
        additional_staffing_table = tabulate(additional_staffing_data, headers="firstrow", tablefmt="fancy_grid") + "\n\n"
        self.output_text.insert(tk.END, event_table)
        self.output_text.insert(tk.END, additional_staffing_table )

        self.event_name_entry.delete(0, tk.END)
        self.guests_entry.delete(0, tk.END)
        self.event_time_start_entry.delete(0, tk.END)
        self.event_time_lunchdinner_entry.delete(0, tk.END)
        self.event_time_end_entry.delete(0, tk.END)
        self.event_date_entry.delete(0, tk.END)
        self.ddr_meeting_rooms_entry.delete(0, tk.END)
        self.hostess_entry.delete(0, tk.END)
        self.porter_entry.delete(0, tk.END)
        self.food_waiter_entry.delete(0, tk.END)

    def add_ovr(self):
        
        add_ovr_type = self.override_hrs_var.get()

        if add_ovr_type == "DDR AM FW":
            self.AM_food_add_ovr += float(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif add_ovr_type == "DDR PM FW":
            self.PM_food_add_ovr += float(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif add_ovr_type == "Food Waiter":
            self.food_add_ovr += float(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif add_ovr_type == "Wine Waiter":
            self.wine_add_ovr += float(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif add_ovr_type == "Bartender":
            self.bar_add_ovr += float(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif add_ovr_type == "Barback":
            self.barback_add_ovr += float(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif add_ovr_type == "Cloakroom":
            self.cloakroom_add_ovr += float(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif add_ovr_type == "Hostess":
                self.hostess_add_ovr += float(self.override_hrs_entry.get())
                self.override_hrs_entry.delete(0, tk.END)

    def sub_ovr(self):

        sub_ovr_type = self.override_hrs_var.get()

        if sub_ovr_type == "DDR AM FW":
            self.AM_food_sub_ovr += float(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif sub_ovr_type == "DDR PM FW":
            self.PM_food_sub_ovr += float(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif sub_ovr_type == "Food Waiter":
            self.food_sub_ovr += int(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif sub_ovr_type == "Wine Waiter":
            self.wine_sub_ovr += int(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif sub_ovr_type == "Bartender":
            self.bar_sub_ovr += int(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif sub_ovr_type == "Barback":
            self.barback_sub_ovr += int(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif sub_ovr_type == "Cloakroom":
            self.cloakroom_sub_ovr += int(self.override_hrs_entry.get())
            self.override_hrs_entry.delete(0, tk.END)
        elif sub_ovr_type == "Hostess":
                self.hostess_sub_ovr += int(self.override_hrs_entry.get())
                self.override_hrs_entry.delete(0, tk.END)
    
    def calculate_expenses(self, event=None): 

        event_name = self.event_name_entry.get().upper()
        event_type = self.event_type_var.get().upper()
        event_date = self.event_date_entry.get()

        if event_type == 'DDR BOWL' or event_type == 'DDR BUFFET':
            try:
                guests_entry = self.guests_entry.get()
                if not guests_entry:
                    raise ValueError("Guests entry is missing")
                guests = validate_numeric_input(guests_entry)
                if guests is None:
                    raise ValueError('Guests must be numeric')
                
                event_start_entry = self.event_time_start_entry.get()
                if not event_start_entry:
                    raise ValueError("Event 'Start' entry is missing")
                event_start = event_start_entry
                if event_start is None:
                    raise ValueError("Event 'Start' must be in HH:MM format")
                
                event_DDR_lunch_entry = self.event_time_lunchdinner_entry.get()
                if not event_DDR_lunch_entry:
                    raise ValueError("DDR 'Lunch/Dinner Dessert' entry is missing")
                event_lunch = event_DDR_lunch_entry
                if event_lunch is False:
                    raise ValueError("DDR 'Lunch/Dinner Dessert' must be in HH:MM format")
                
                event_end_entry = self.event_time_end_entry.get()
                if not event_end_entry:
                    raise ValueError("Event 'End' entry is missing")
                event_end = event_end_entry
                if event_end is None:
                    raise ValueError("Event 'End' must be in HH:MM format")

                        
            except ValueError as e:
                self.output_text.insert(tk.END, f'Error: {e} "\n', "red")

            ddr_meeting_rooms = self.ddr_meeting_rooms_entry.get()
            if not ddr_meeting_rooms:
                ddr_meeting_rooms = 0
            hostess = self.hostess_entry.get()
            if not hostess:
                hostess = 0

            # Staff hours & Override hrs
            morning_team_hours = 0
            evening_team_hours = 8
            cloakroom_hours = 0
            hostess_hours = 0

            morning_team_hours += round(EventDDR.calculate_morning_team_time(event_start, event_lunch), 1)
            if self.AM_food_add_ovr > 0:
                morning_team_hours += self.AM_food_add_ovr
            elif self.AM_food_sub_ovr > 0:
                morning_team_hours -= self.AM_food_sub_ovr

            if self.PM_food_add_ovr > 0:
                evening_team_hours += self.PM_food_add_ovr
            elif self.PM_food_sub_ovr > 0:
                evening_team_hours -= self.PM_food_sub_ovr
            
            cloakroom_hours = round(EventDDR.calculate_cloakroom_time(event_start, event_end), 1)
            if self.cloakroom_add_ovr > 0:
                cloakroom_hours += self.cloakroom_add_ovr
            elif self.cloakroom_sub_ovr > 0:
                cloakroom_hours -= self.cloakroom_sub_ovr
            hostess_hours = round(EventDDR.calculate_cloakroom_time(event_start, event_end), 1)
            if self.hostess_add_ovr > 0:
                hostess_hours += self.hostess_add_ovr
            elif self.hostess_sub_ovr > 0:
                hostess_hours -= self.hostess_sub_ovr    
            elif hostess == 0:
                hostess_hours = 0
            
            event = EventDDR(hostess,ddr_meeting_rooms, event_name, event_type, guests, event_start, event_lunch, event_end, morning_team_hours, evening_team_hours, cloakroom_hours, hostess_hours, event_date)

            # Duration
            duration = EventDDR.event_duration(event_start, event_end)
            # Add to list
            self.events_name_list.append(event_name)
            self.event_type_list.append(event_type)
            self.event_durations_list.append(duration)
            self.event_date_list.append(event_date)
            self.guests_list.append(guests)

            # Add to sub ddr bowl/Buffet overview list 
            if event_type == "DDR BOWL":
                self.ddr_bowl_events_name_list.append(event_name)
                self.ddr_bowl_event_type_list.append(event_type)
                self.ddr_bowl_event_durations_list.append(duration)
                self.ddr_bowl_event_date_list.append(event_date)
                self.ddr_bowl_guests_list.append(guests)

            elif event_type == "DDR BUFFET":
                self.ddr_buffet_events_name_list.append(event_name)
                self.ddr_buffet_event_type_list.append(event_type)
                self.ddr_buffet_event_durations_list.append(duration)
                self.ddr_buffet_event_date_list.append(event_date)
                self.ddr_buffet_guests_list.append(guests)

            #DDR Variables
            hot_food_staff = event.hot_food_staff

            # Calculate total staffing by category  
            morn_num_food_staff = event.morn_num_food_staff 
            eve_num_food_staff = event.eve_num_food_staff
            num_cloakroom_staff = event.num_cloakroom_staff

            total_staff_combined = event.total_num_food_staff

            self.total_food_service_staff_combined += total_staff_combined
            self.total_cloakroom_staff_combined += num_cloakroom_staff
            self.total_hostess_staff_combined += event.num_hostess_staff

            # Calculate total staffing cost by category
            morn_food_staff_cost = event.morn_staff_cost
            eve_food_staff_cost = event.eve_staff_cost
            food_service_staff_cost = event.food_service_staff_cost
            cloakroom_staff_cost = event.cloakroom_staff_cost
            total_staff_cost = event.total_staff_cost
            
            self.total_food_service_staff_cost += food_service_staff_cost
            self.total_cloakroom_staff_cost += cloakroom_staff_cost
            self.total_hostess_staff_cost += event.hostess_staff_cost

            self.total_guests_combined += guests

            #total staff combined and cost for all events
            self.total_staff_combined_for_all_events += event.ddr_total_staff_combined
            self.event_staff_total_count_list.append(event.ddr_total_staff_combined)

            if event_type == "DDR BOWL":
                self.ddr_bowl_event_staff_total_count_list.append(event.ddr_total_staff_combined)
            elif event_type == "DDR BUFFET":
                self.ddr_buffet_event_staff_total_count_list.append(event.ddr_total_staff_combined)

            self.total_staff_cost_for_all_events += total_staff_cost
            self.event_total_cost_list.append( "£" + str(total_staff_cost))

            if event_type == "DDR BOWL":
                self.ddr_bowl_event_total_cost_list.append(total_staff_cost)
            elif event_type == "DDR BUFFET":
                self.ddr_buffet_event_total_cost_list.append(total_staff_cost)

            # update sub overview totals list
            if event_type == "DDR BOWL":
                self.total_ddr_bowl_guests_list = sum(self.ddr_bowl_guests_list)
                self.total_ddr_bowl_event_staff_total_count_list = sum(self.ddr_bowl_event_staff_total_count_list)
                self.total_ddr_bowl_event_total_cost_list = sum(self.ddr_bowl_event_total_cost_list)
            elif event_type == "DDR BUFFET":
                self.total_ddr_buffet_guests_list = sum(self.ddr_buffet_guests_list)
                self.total_ddr_buffet_event_staff_total_count_list = sum(self.ddr_buffet_event_staff_total_count_list)
                self.total_ddr_buffet_event_total_cost_list = sum(self.ddr_buffet_event_total_cost_list)

            # Ovr hrs column
            AM_food_ovr_hrs_column = 0
            PM_food_ovr_hrs_column = 0
            cloakroom_ovr_hrs_column = 0
            hostess_ovr_hrs_column = 0

            if self.AM_food_add_ovr > 0:
                AM_food_ovr_hrs_column += self.AM_food_add_ovr
            elif self.AM_food_sub_ovr > 0:
                AM_food_ovr_hrs_column -= self.AM_food_sub_ovr
            if self.PM_food_add_ovr > 0:
                PM_food_ovr_hrs_column += self.PM_food_add_ovr
            elif self.PM_food_sub_ovr > 0:
                PM_food_ovr_hrs_column -= self.PM_food_sub_ovr
            if self.cloakroom_add_ovr > 0:
                cloakroom_ovr_hrs_column += self.cloakroom_add_ovr
            elif self.cloakroom_sub_ovr > 0:
                cloakroom_ovr_hrs_column -= self.cloakroom_sub_ovr
            if self.hostess_add_ovr > 0:
                hostess_ovr_hrs_column += self.hostess_add_ovr
            elif self.hostess_sub_ovr  < 0:
                hostess_ovr_hrs_column -= self.hostess_sub_ovr
                

            #---------------------------------------------------------------- OUTPUT ------------------------------------------------------------------------------

            self.output_text.insert(tk.END, f'------------------------------------------------------------------------------------- DDR ---------------------------------------------------------------------------------------\n','orange')
            event_data = [
                ["Event Name", "Event Type", "Number of Guests", "Start Time", "Lunch", "End Time", "Duration", "Date"],
                [event_name, event_type, guests, event_start, event_lunch, event_end, str(duration) + "Hrs", event_date]
            ]

            staff_data = [
                ["Type of Staff", "Number of Staff", "Rates Per Hour","Hours","Ovr Hrs", "Total Cost"],
                ["AM Food Waiter", morn_num_food_staff,'£' + str(staff_rates['food_waiter']), morning_team_hours, AM_food_ovr_hrs_column, '£' + str(morn_food_staff_cost)],
                ["PM Food Waiter", eve_num_food_staff,'£' + str(staff_rates['food_waiter']), evening_team_hours, PM_food_ovr_hrs_column, '£' + str(eve_food_staff_cost)],
                ["Cloakroom", num_cloakroom_staff, '£' + str(staff_rates['cloakroom']),cloakroom_hours, cloakroom_ovr_hrs_column, '£' + str(cloakroom_staff_cost)],
                ["Hostess", event.num_hostess_staff, '£' + str(staff_rates['hostess']), hostess_hours, hostess_ovr_hrs_column, '£' + str(event.hostess_staff_cost)],
                ["Total", event.ddr_total_staff_combined,"", "", "", '£' + str(total_staff_cost)]
            ]
            staff_time_rules = [["Staff", "In", "Out"],
                                ["AM Food Waiter", "1.5 hrs before event", "1 hr after Lunch"],
                                ["PM Food Waiter", "", ""],
                                ["Cloakroom", "1.5 hrs before event", "1 hr after the event"],
                                ["Hostess", "1.5 hrs before event", "1 hr after the event"],
                                ]
              # Format and display event data
            event_table = tabulate(event_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*6) + "\n\n"
            self.output_text.insert(tk.END, event_table)

            staff_table = tabulate(staff_data, headers="firstrow", tablefmt='fancy_grid')
            staff_time_rules_table = tabulate(staff_time_rules, headers="firstrow", tablefmt='fancy_grid') + "\n\n"

            # Split table strings into rows
            staff_table_rows = staff_table.split("\n")
            staff_time_rules_table_rows = staff_time_rules_table.split("\n")
            # Combine rows element-wise
            combined_rows = [row1 + " " + row2 for row1, row2 in zip(staff_table_rows, staff_time_rules_table_rows)]
            # Join combined rows into a single string
            combined_table_str = "\n".join(combined_rows)
            # Format and display staff data
            # staff_table = tabulate(staff_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*4) + "\n\n" 
            self.output_text.insert(tk.END, combined_table_str + "\n\n") 

            # Clipboard
            self.ddr_clipboard1 = pd.DataFrame(event_data ) 
            self.ddr_clipboard2 = pd.DataFrame(staff_data)
            self.ddr_clipboard3 = pd.DataFrame(staff_time_rules)  

            #--------------------------------------------------- DDR allocation conditioning ------------------------------------------------------
            if guests <= 80:
                allocations_data = [["Morning Allocations", "Number of Allocations"],
                                        ["Coffee Station", 1],
                                        ["Buffet Station", 1],
                                        ["Water Station", 1],
                                        ["Cloakroom", 1],
                                        ["Clearing", 1],
                                        ["Meeting Rooms", ddr_meeting_rooms],
                                        ["Hostess", hostess]]
                allocation_table = tabulate(allocations_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                self.output_text.insert(tk.END, allocation_table)
                self.ddr_clipboard4 = pd.DataFrame(allocations_data) 
                if event_type == "DDR BOWL":
                    bowl_lunch_data = [["Bowl Lunch Allocation", "Number of Allocations"],
                                        ["Additional Clearing", 1],
                                        ["Hot Food", hot_food_staff]]
                    bowl_lunch_table = tabulate(bowl_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, bowl_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(bowl_lunch_data)
                elif event_type == "DDR BUFFET":
                    buffet_lunch_data = [["Buffet Lunch Allocation", "Number of Allocations"],
                                        ["Buffet Food Runners", 2]]
                    buffet_lunch_table = tabulate(buffet_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, buffet_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(buffet_lunch_data)

            elif guests > 80 and guests <= 100:
                allocations_data = [["Morning Allocations", "Number of Allocations"],
                                        ["Coffee Station", 2],
                                        ["Buffet Station", 2],
                                        ["Water Station", 1],
                                        ["Cloakroom", 1],
                                        ["Clearing", 2],
                                        ["Meeting Rooms", ddr_meeting_rooms],
                                        ["Hostess", hostess]]
                allocation_table = tabulate(allocations_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                self.output_text.insert(tk.END, allocation_table)
                self.ddr_clipboard4 = pd.DataFrame(allocations_data)
                if event_type == "DDR BOWL":
                    bowl_lunch_data = [["Bowl Lunch Allocation", "Number of Allocations"],
                                        ["Additional Clearing", 1],
                                        ["Hot Food", hot_food_staff]]
                    bowl_lunch_table = tabulate(bowl_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, bowl_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(bowl_lunch_data)
                elif event_type == "DDR BUFFET":
                    buffet_lunch_data = [["Buffet Lunch Allocation", "Number of Allocations"],
                                        ["Buffet Food Runners", 3]]
                    buffet_lunch_table = tabulate(buffet_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, buffet_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(buffet_lunch_data)

            elif guests > 100 and guests <=150:
                
                if guests < 150:
                    allocations_data = [["Morning Allocations", "Number of Allocations"],
                                        ["Coffee Station", 2],
                                        ["Coffee Runner", 1],
                                        ["Buffet Station", 2],
                                        ["Water Station", 1],
                                        ["Cloakroom", 1],
                                        ["Clearing", 2],
                                        ["Meeting Rooms", ddr_meeting_rooms],
                                        ["Hostess", hostess]]
                    allocation_table = tabulate(allocations_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, allocation_table)
                    self.ddr_clipboard4 = pd.DataFrame(allocations_data)
                elif guests == 150:
                    allocations_data = [["Morning Allocations", "Number of Allocations"],
                                        ["Coffee Station", 2],
                                        ["Coffee Runner", 1],
                                        ["Buffet Station", 2],
                                        ["Water Station", 1],
                                        ["Cloakroom", 1],
                                        ["Clearing", 3],
                                        ["Meeting Rooms", ddr_meeting_rooms],
                                        ["Hostess", hostess]]
                    allocation_table = tabulate(allocations_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, allocation_table)
                    self.ddr_clipboard4 = pd.DataFrame(allocations_data)
                if event_type == "DDR BOWL":
                    bowl_lunch_data = [["Bowl Lunch Allocation", "Number of Allocations"],
                                        ["Additional Clearing", 2],
                                        ["Hot Food", hot_food_staff]]
                    bowl_lunch_table = tabulate(bowl_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, bowl_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(bowl_lunch_data)
                elif event_type == "DDR BUFFET":
                    buffet_lunch_data = [["Buffet Lunch Allocation", "Number of Allocations"],
                                        ["Buffet Food Runners", 4]]
                    buffet_lunch_table = tabulate(buffet_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, buffet_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(buffet_lunch_data)

            elif guests > 150 and guests <=200:
                if guests > 150 and guests < 200:
                    allocations_data = [["Morning Allocations", "Number of Allocations"],
                                            ["Coffee Station", 2],
                                            ["Coffee Runner", 1],
                                            ["Buffet Station", 2],
                                            ["Water Station", 1],
                                            ["Cloakroom", 2],
                                            ["Clearing", 3],
                                            ["Meeting Rooms", ddr_meeting_rooms],
                                            ["Hostess", hostess]]
                    allocation_table = tabulate(allocations_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, allocation_table)
                    self.ddr_clipboard4 = pd.DataFrame(allocations_data)
                elif guests == 200:
                    allocations_data = [["Morning Allocations", "Number of Allocations"],
                                        ["Coffee Station", 2],
                                        ["Coffee Runner", 1],
                                        ["Buffet Station", 2],
                                        ["Water Station", 1],
                                        ["Cloakroom", 2],
                                        ["Clearing", 4],
                                        ["Meeting Rooms", ddr_meeting_rooms],
                                        ["Hostess", hostess]]
                    allocation_table = tabulate(allocations_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, allocation_table)
                    self.ddr_clipboard4 = pd.DataFrame(allocations_data)
                if event_type == "DDR BOWL":
                    bowl_lunch_data = [["Bowl Lunch Allocation", "Number of Allocations"],
                                        ["Additional Clearing", 2],
                                        ["Hot Food", hot_food_staff]]
                    bowl_lunch_table = tabulate(bowl_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, bowl_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(bowl_lunch_data)
                elif event_type == "DDR BUFFET":
                    buffet_lunch_data = [["Buffet Lunch Allocation", "Number of Allocations"],
                                        ["Buffet Food Runners", 4]]
                    buffet_lunch_table = tabulate(buffet_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, buffet_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(buffet_lunch_data)

            elif guests > 200 and guests <= 250:
                allocations_data = [["Morning Allocations", "Number of Allocations"],
                                        ["Coffee Station", 3],
                                        ["Coffee Runner", 1],
                                        ["Buffet Station", 3],
                                        ["Water Station", 2],
                                        ["Cloakroom", 2],
                                        ["Clearing", 4],
                                        ["Meeting Rooms", ddr_meeting_rooms],
                                        ["Hostess", hostess]]
                allocation_table = tabulate(allocations_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                self.output_text.insert(tk.END, allocation_table)
                self.ddr_clipboard4 = pd.DataFrame(allocations_data)
                if event_type == "DDR BOWL":
                    bowl_lunch_data = [["Bowl Lunch Allocation", "Number of Allocations"],
                                        ["Additional Clearing", 3],
                                        ["Hot Food", hot_food_staff]]
                    bowl_lunch_table = tabulate(bowl_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, bowl_lunch_table  )
                    self.ddr_clipboard5 = pd.DataFrame(bowl_lunch_data)
                elif event_type == "DDR BUFFET":
                    buffet_lunch_data = [["Buffet Lunch Allocation", "Number of Allocations"],
                                        ["Buffet Food Runners", 5]]
                    buffet_lunch_table = tabulate(buffet_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, buffet_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(buffet_lunch_data) 
            elif guests > 250 and guests <= 300:
                allocations_data = [["Morning Allocations", "Number of Allocations"],
                                    ["Coffee Station", 3],
                                    ["Coffee Runner", 1],
                                    ["Buffet Station", 3],
                                    ["Water Station", 2],
                                    ["Cloakroom", 3],
                                    ["Clearing", 4],
                                    ["Meeting Rooms", ddr_meeting_rooms],
                                    ["Hostess", hostess]]
                allocation_table = tabulate(allocations_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                self.output_text.insert(tk.END, allocation_table)
                self.ddr_clipboard4 = pd.DataFrame(allocations_data)
                if event_type == "DDR BOWL":
                    bowl_lunch_data = [["Bowl Lunch Allocation", "Number of Allocations"],
                                        ["Additional Clearing", 3],
                                        ["Hot Food", hot_food_staff]]
                    bowl_lunch_table = tabulate(bowl_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, bowl_lunch_table  )
                    self.ddr_clipboard5 = pd.DataFrame(bowl_lunch_data)
                elif event_type == "DDR BUFFET":
                    buffet_lunch_data = [["Buffet Lunch Allocation", "Number of Allocations"],
                                        ["Buffet Food Runners", 5]]
                    buffet_lunch_table = tabulate(buffet_lunch_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                    self.output_text.insert(tk.END, buffet_lunch_table )
                    self.ddr_clipboard5 = pd.DataFrame(buffet_lunch_data)        
           
            # Clear entry fields
            self.event_name_entry.delete(0, tk.END)
            self.guests_entry.delete(0, tk.END)
            self.event_time_start_entry.delete(0, tk.END)
            self.event_time_lunchdinner_entry.delete(0, tk.END)
            self.event_time_end_entry.delete(0, tk.END)
            self.event_date_entry.delete(0, tk.END)
            self.hostess_entry.delete(0, tk.END)
            self.ddr_meeting_rooms_entry.delete(0, tk.END)

            # Reset Override hours
            self.AM_food_add_ovr = 0
            self.PM_food_add_ovr = 0
            self.food_add_ovr = 0
            self.wine_add_ovr = 0
            self.bar_add_ovr = 0
            self.barback_add_ovr = 0
            self.cloakroom_add_ovr = 0
            self.hostess_add_ovr = 0
            self.porter_add_ovr = 0

            self.AM_food_sub_ovr = 0
            self.PM_food_sub_ovr = 0
            self.food_sub_ovr = 0
            self.wine_sub_ovr = 0
            self.bar_sub_ovr = 0
            self.barback_sub_ovr = 0
            self.cloakroom_sub_ovr = 0
            self.hostess_sub_ovr = 0
            self.porter_sub_ovr = 0
            
        #---------------------------------------------------------------- Dinner event type ------------------------------------------------------------------------------

        elif event_type == 'DINNER' or event_type == 'DINNER NOBU MENU':
            try:
                guests_entry = self.guests_entry.get()
                if not guests_entry:
                    raise ValueError("Guests entry is missing")
                guests = validate_numeric_input(guests_entry)
                if guests is None:
                    raise ValueError('Guests must be numeric')
                
                event_start_entry = self.event_time_start_entry.get()
                if not event_start_entry:
                    raise ValueError("Event 'Start' entry is missing")
                event_start = event_start_entry
                if event_start is None:
                    raise ValueError("Event 'Start' must be in HH:MM format")
                
                event_dessert_entry = self.event_time_lunchdinner_entry.get()
                if not event_dessert_entry:
                    raise ValueError("DDR 'Lunch/Dessert' entry is missing")
                event_dessert = event_dessert_entry
                if event_dessert is False:
                    raise ValueError("DDR 'Lunch/Dinner Dessert' must be in HH:MM format")
                
                event_end_entry = self.event_time_end_entry.get()
                if not event_end_entry:
                    raise ValueError("Event 'End' entry is missing")
                event_end = event_end_entry
                if event_end is None:
                    raise ValueError("Event 'End' must be in HH:MM format")
            
            except ValueError as e:
                self.output_text.insert(tk.END, f'Error: {e} "\n', "red")
                
            # Staff timings + Override hrs
            food_staff75_hours = 0
            food_staff25_hours = 0
            wine_staff_hours = 0
            bartender_hours = 0
            barback_hours = 0
            cloak_hours = 0

            food_staff75_hours += EventDinner.calculate_food75_team_time(event_start, event_dessert)
            food_staff25_hours += EventDinner.calculate_food25_team_time(event_start, event_end)
            if self.food_add_ovr > 0:
                food_staff75_hours += self.food_add_ovr
                food_staff25_hours += self.food_add_ovr
            elif self.food_sub_ovr > 0:
                food_staff75_hours -= self.food_sub_ovr
                food_staff25_hours -= self.food_sub_ovr
            wine_staff_hours = EventDinner.calculate_wine_team_time(event_start, event_end)
            if self.wine_add_ovr > 0:
                wine_staff_hours += self.wine_add_ovr
            elif self.wine_sub_ovr > 0:
                wine_staff_hours -= self.wine_sub_ovr
            bartender_hours += EventDinner.calculate_bartender_team_time(event_start, event_end)
            if self.bar_add_ovr > 0:
                bartender_hours += self.bar_add_ovr
            elif self.bar_sub_ovr > 0:
                bartender_hours -= self.bar_sub_ovr
            barback_hours += EventDinner.calculate_barback_team_time(event_start, event_end)
            if self.barback_add_ovr > 0:
                barback_hours += self.barback_add_ovr
            elif self.barback_sub_ovr > 0:
                barback_hours -= self.barback_sub_ovr
            cloak_hours += EventDinner.calculate_cloack_team_time(event_start, event_end)
            if self.cloakroom_add_ovr > 0:
                cloak_hours += self.cloakroom_add_ovr
            elif self.cloakroom_sub_ovr > 0:
                cloak_hours -= self.cloakroom_sub_ovr

            duration = EventDDR.event_duration(event_start, event_end)    

            event = EventDinner(event_name, event_type, guests, event_start, event_dessert, event_end, food_staff75_hours, food_staff25_hours, wine_staff_hours, bartender_hours, barback_hours, cloak_hours)

            # add to the list
            self.events_name_list.append(event_name)
            self.event_type_list.append(event_type)
            self.event_durations_list.append(duration)
            self.event_date_list.append(event_date)
            self.guests_list.append(guests)

            # add to the sub overview list
            if event_type == "DINNER":
                self.dinner_events_name_list.append(event_name)
                self.dinner_event_type_list.append(event_type)
                self.dinner_event_durations_list.append(duration)
                self.dinner_event_date_list.append(event_date)
                self.dinner_guests_list.append(guests)
            elif event_type == "DINNER NOBU MENU":
                self.dinner_nm_events_name_list.append(event_name)
                self.dinner_nm_event_type_list.append(event_type)
                self.dinner_nm_event_durations_list.append(duration)
                self.dinner_nm_event_date_list.append(event_date)
                self.dinner_nm_guests_list.append(guests)

            # Override hrs
            # add_ovr_hrs = self.add_ovr()
            # sub_ovr_hrs = self.sub_ovr()

            # number of staff
            num_food_staff75 = event.num_food_staff75
            num_food_staff25 = event.num_food_staff25
            num_food_staff = event.num_food_staff

            num_clearing_staff = event.num_clearing_staff
            num_wine_staff = event.num_wine_staff
            num_bartenders_staff = event.num_bartenders_staff
            num_barback_staff = event.num_barback_staff
            num_cloakroom_staff = event.num_cloakroom_staff

            total_staff_combined = event.total_staff_combined
            if event_type == "DINNER":
                self.event_staff_total_count_list.append(total_staff_combined)
                self.dinner_event_staff_total_count_list.append(total_staff_combined)

            self.total_food_service_staff_combined += num_food_staff
            self.total_clearing_staff_combined += num_clearing_staff
            self.total_wine_waiters_staff_combined += num_wine_staff        
            self.total_bartender_staff_combined += num_bartenders_staff
            self.total_barback_staff_combined += num_barback_staff
            self.total_cloakroom_staff_combined += num_cloakroom_staff

            # Calculate total staffing cost by category
            food_service_staff75_cost = event.food_service_staff75_cost
            food_service_staff25_cost = event.food_service_staff25_cost
            food_service_staff_cost = event.food_service_staff100_cost
            wine_waiters_staff_cost = event.wine_waiters_staff_cost
            bartenders_staff_cost = event.bartenders_staff_cost
            barback_staff_cost = event.barback_staff_cost
            cloakroom_staff_cost = event.cloakroom_staff_cost

            total_staff_cost = event.total_staff_cost
            if event_type == "DINNER":
                self.event_total_cost_list.append( "£" + str(total_staff_cost))
                self.dinner_event_total_cost_list.append(total_staff_cost)

            # update sub overview totals list
            if event_type == "DINNER":
                self.total_dinner_guests_list = sum(self.dinner_guests_list)
            elif event_type == "DINNER NOBU MENU":
                self.total_dinner_nm_guests_list = sum(self.dinner_nm_guests_list)
            self.total_dinner_event_staff_total_count_list = sum(self.dinner_event_staff_total_count_list)
            self.total_dinner_event_total_cost_list = sum(self.dinner_event_total_cost_list)
                

            self.total_food_service_staff_cost += food_service_staff_cost
            self.total_wine_waiters_staff_cost += wine_waiters_staff_cost
            self.total_bartender_staff_cost += bartenders_staff_cost
            if num_barback_staff == 0:
                self.total_barback_staff_cost += 0
            else:
                self.total_barback_staff_cost += barback_staff_cost
            self.total_cloakroom_staff_cost += cloakroom_staff_cost

            #total staff combined and cost for all events
            self.total_staff_combined_for_all_events += total_staff_combined

            self.total_staff_cost_for_all_events += total_staff_cost

            self.total_guests_combined += guests

            #Allocation variables
            food_waiter_AL = num_food_staff - num_clearing_staff
            clearing_AL = num_clearing_staff

            # Ovr hrs column
            food75_ovr_hrs_column = 0
            food25_ovr_hrs_column = 0
            wine_ovr_hrs_column = 0
            bartender_ovr_hrs_column = 0
            barback_ovr_hrs_column = 0
            cloakroom_ovr_hrs_column = 0

            if self.food_add_ovr > 0:
                food75_ovr_hrs_column += self.food_add_ovr
                food25_ovr_hrs_column += self.food_add_ovr
            elif self.food_sub_ovr > 0:
                food75_ovr_hrs_column -= self.food_sub_ovr
                food25_ovr_hrs_column -= self.food_sub_ovr
            if self.wine_add_ovr > 0:
                wine_ovr_hrs_column += self.wine_add_ovr
            elif self.wine_sub_ovr > 0:
                wine_ovr_hrs_column -= self.wine_sub_ovr
            if self.bar_add_ovr > 0:
                bartender_ovr_hrs_column += self.bar_add_ovr
            elif self.bar_sub_ovr > 0:
                bartender_ovr_hrs_column -= self.bar_sub_ovr
            if self.barback_add_ovr > 0:
                barback_ovr_hrs_column += self.barback_add_ovr
            elif self.barback_sub_ovr > 0:
                barback_ovr_hrs_column -= self.barback_sub_ovr
            if self.cloakroom_add_ovr > 0:
                    cloakroom_ovr_hrs_column += self.cloakroom_add_ovr
            elif self.cloakroom_sub_ovr > 0:
                    cloakroom_ovr_hrs_column -= self.cloakroom_sub_ovr
            
            #---------------------------------------------------------------- DINNER OUTPUT --------------------------------------------------------------------------------------------------
            if event_type == "DINNER":
                self.output_text.insert(tk.END, f'----------------------------------------------------------------------------------- DINNER --------------------------------------------------------------------------------------\n', 'orange')
                event_data = [
                    ["Event Name", "Event Type", "Number of Guests", "Start Time", "Dessert", "End Time", "Duration", "Date"],
                    [event_name, event_type, guests, event_start, event_dessert, event_end, str(duration) + "Hrs", event_date]
                ]

                staff_data = [
                    ["Type of Staff", "Number of Staff", "Rates Per Hour","Hours","Ovr Hrs", "Total Cost"],
                    ["Food Waiter 75%", num_food_staff75,'£' + str(staff_rates['food_waiter']), food_staff75_hours, food75_ovr_hrs_column, '£' + str(food_service_staff75_cost)],
                    ["Food Waiter 25%", num_food_staff25,'£' + str(staff_rates['food_waiter']), food_staff25_hours, food25_ovr_hrs_column, '£' + str(food_service_staff25_cost)],
                    ["Wine Waiter", num_wine_staff,'£' + str(staff_rates['wine_waiter']), wine_staff_hours , wine_ovr_hrs_column, '£' + str(wine_waiters_staff_cost)],
                    ["Bartender", num_bartenders_staff,'£' + str(staff_rates['bartender']), bartender_hours, bartender_ovr_hrs_column, '£' + str(bartenders_staff_cost)],
                    ["Barback", num_barback_staff,'£' + str(staff_rates['barback']), barback_hours, barback_ovr_hrs_column, '£' + str(barback_staff_cost)],
                    ["Cloakroom", num_cloakroom_staff, '£' + str(staff_rates['cloakroom']),cloak_hours, cloakroom_ovr_hrs_column, '£' + str(cloakroom_staff_cost)],
                    ["Total", total_staff_combined,"", "", "", '£' + str(total_staff_cost)]
                ]
                staff_time_rules = [["Staff", "In", "Out"],
                                    ["Food Waiter 75%", "1.5 hrs before event", "1 hr after dessert"],
                                    ["Food Waiter 25%", "1.5 hrs before event", "1 hr after the event"],
                                    ["Wine Waiter", "1.5 hrs before event", "1 hr after the event"],
                                    ["Bartender", "2 hrs before the event", "2 hrs after the event"],
                                    ["Barback", "1 hr before event", "2 hrs after the event"],
                                    ["Cloakroom", "1.5 hrs before event", "1 hr after the event"],]
                event_table = tabulate(event_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*6) + "\n\n"
                self.output_text.insert(tk.END, event_table)
                staff_table = tabulate(staff_data, headers="firstrow", tablefmt='fancy_grid')
                staff_time_rules_table = tabulate(staff_time_rules, headers="firstrow", tablefmt='fancy_grid')  + "\n\n"
                
                # Split table strings into rows
                staff_table_rows = staff_table.split("\n")
                staff_time_rules_table_rows = staff_time_rules_table.split("\n")
                # Combine rows element-wise
                combined_rows = [row1 + " " + row2 for row1, row2 in zip(staff_table_rows, staff_time_rules_table_rows)]
                # Join combined rows into a single string
                combined_table_str = "\n".join(combined_rows)
                
                self.output_text.insert(tk.END, combined_table_str)

                food_waiter_allocation_data = [["Food Waiter", "Reception Allocation"],
                                            ["Food", food_waiter_AL],
                                            ["Clearing", clearing_AL]]
                food_waiter_allocation_table = tabulate(food_waiter_allocation_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                self.output_text.insert(tk.END, "\n\n" + food_waiter_allocation_table )

                # Clear entry fields
                self.event_name_entry.delete(0, tk.END)
                self.guests_entry.delete(0, tk.END)
                self.event_time_start_entry.delete(0, tk.END)
                self.event_time_end_entry.delete(0, tk.END)
                self.event_time_lunchdinner_entry.delete(0, tk.END)
                self.event_date_entry.delete(0, tk.END)

                # Reset Override hours
                self.AM_food_add_ovr = 0
                self.PM_food_add_ovr = 0
                self.food_add_ovr = 0
                self.wine_add_ovr = 0
                self.bar_add_ovr = 0
                self.barback_add_ovr = 0
                self.cloakroom_add_ovr = 0
                self.hostess_add_ovr = 0
                self.porter_add_ovr = 0

                self.AM_food_sub_ovr = 0
                self.PM_food_sub_ovr = 0
                self.food_sub_ovr = 0
                self.wine_sub_ovr = 0
                self.bar_sub_ovr = 0
                self.barback_sub_ovr = 0
                self.cloakroom_sub_ovr = 0
                self.hostess_sub_ovr = 0
                self.porter_sub_ovr = 0

            elif event_type == "DINNER NOBU MENU":
                total_staff_combined += event.num_sides_staff
                total_staff_cost += event.sides_staff_cost
                self.total_food_service_staff_combined += event.num_sides_staff
                self.total_staff_combined_for_all_events += event.num_sides_staff
                self.total_staff_cost_for_all_events += event.sides_staff_cost
                self.event_staff_total_count_list.append(total_staff_combined)
                self.dinner_nm_event_staff_total_count_list.append(total_staff_combined)
                self.event_total_cost_list.append( "£" + str(total_staff_cost))
                self.dinner_nm_event_total_cost_list.append(total_staff_cost)
                self.total_dinner_nm_event_staff_total_count_list = sum(self.dinner_nm_event_staff_total_count_list)
                self.total_dinner_nm_event_total_cost_list = sum(self.dinner_nm_event_total_cost_list)
                self.output_text.insert(tk.END, f'------------------------------------------------------------------------------ DINNER NOBU MENU ---------------------------------------------------------------------------------\n','orange')
                event_data = [
                    ["Event Name", "Event Type", "Number of Guests", "Start Time", "Dessert", "End Time", "Duration", "Date"],
                    [event_name, event_type, guests, event_start, event_dessert, event_end, str(duration) + "Hrs", event_date]
                ]

                staff_data = [
                    ["Type of Staff", "Number of Staff", "Rates Per Hour","Hours", "Ovr Hrs", "Total Cost"],
                    ["Food Waiter 75%", num_food_staff75,'£' + str(staff_rates['food_waiter']), food_staff75_hours, food75_ovr_hrs_column, '£' + str(food_service_staff75_cost)],
                    ["Food Waiter 25%", num_food_staff25,'£' + str(staff_rates['food_waiter']), food_staff25_hours, food25_ovr_hrs_column, '£' + str(food_service_staff25_cost)],
                    ["Food Waiter Sides", event.num_sides_staff,'£' + str(staff_rates['food_waiter']), food_staff75_hours, food75_ovr_hrs_column, '£' + str(event.sides_staff_cost)],
                    ["Wine Waiter", num_wine_staff,'£' + str(staff_rates['wine_waiter']), wine_staff_hours, wine_ovr_hrs_column, '£' + str(wine_waiters_staff_cost)],
                    ["Bartender", num_bartenders_staff,'£' + str(staff_rates['bartender']), bartender_hours, bartender_ovr_hrs_column, '£' + str(bartenders_staff_cost)],
                    ["Barback", num_barback_staff,'£' + str(staff_rates['barback']), barback_hours, barback_ovr_hrs_column, '£' + str(barback_staff_cost)],
                    ["Cloakroom", num_cloakroom_staff, '£' + str(staff_rates['cloakroom']),cloak_hours, cloakroom_ovr_hrs_column, '£' + str(cloakroom_staff_cost)],
                    ["Total", total_staff_combined,"", "", "", '£' + str(round(total_staff_cost, 2))]
                ]
                staff_time_rules = [["Staff", "In", "Out"],
                                    ["Food Waiter 75%", "1.5 hrs before event", "1 hr after dessert"],
                                    ["Food Waiter 25%", "1.5 hrs before event", "1 hr after the event"],
                                    ["Food Waiter Sides", "1.5 hrs before event", "1 hr after the event"],
                                    ["Wine Waiter", "1.5 hrs before event", "1 hr after the event"],
                                    ["Wartender", "2 hrs before the event", "2 hrs after the event"],
                                    ["Barback", "1 hr before event", "2 hrs after the event"],
                                    ["Cloakroom", "1.5 hrs before event", "1 hr after the event"]]
                event_table = tabulate(event_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*6) + "\n\n"
                self.output_text.insert(tk.END, event_table)
                staff_table = tabulate(staff_data, headers="firstrow", tablefmt='fancy_grid')
                staff_time_rules_table = tabulate(staff_time_rules, headers="firstrow", tablefmt='fancy_grid')  + "\n\n"
                
                # Split table strings into rows
                staff_table_rows = staff_table.split("\n")
                staff_time_rules_table_rows = staff_time_rules_table.split("\n")
                # Combine rows element-wise
                combined_rows = [row1 + " " + row2 for row1, row2 in zip(staff_table_rows, staff_time_rules_table_rows)]
                # Join combined rows into a single string
                combined_table_str = "\n".join(combined_rows)
                
                self.output_text.insert(tk.END, combined_table_str)

                food_waiter_allocation_data = [["Food Waiter", "Reception Allocation"],
                                            ["Food", food_waiter_AL],
                                            ["Clearing", clearing_AL]]
                food_waiter_allocation_table = tabulate(food_waiter_allocation_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
                self.output_text.insert(tk.END, "\n\n" + food_waiter_allocation_table )

                # Clear entry fields
                self.event_name_entry.delete(0, tk.END)
                self.guests_entry.delete(0, tk.END)
                self.event_time_start_entry.delete(0, tk.END)
                self.event_time_end_entry.delete(0, tk.END)
                self.event_time_lunchdinner_entry.delete(0, tk.END)
                self.event_date_entry.delete(0, tk.END)

                # Reset Override hours
                self.AM_food_add_ovr = 0
                self.PM_food_add_ovr = 0
                self.food_add_ovr = 0
                self.wine_add_ovr = 0
                self.bar_add_ovr = 0
                self.barback_add_ovr = 0
                self.cloakroom_add_ovr = 0
                self.hostess_add_ovr = 0
                self.porter_add_ovr = 0

                self.AM_food_sub_ovr = 0
                self.PM_food_sub_ovr = 0
                self.food_sub_ovr = 0
                self.wine_sub_ovr = 0
                self.bar_sub_ovr = 0
                self.barback_sub_ovr = 0
                self.cloakroom_sub_ovr = 0
                self.hostess_sub_ovr = 0
                self.porter_sub_ovr = 0
         #---------------------------------------------------------------- Reception event type ------------------------------------------------------------------------------

        elif event_type == 'RECEPTION':
            try:
                guests_entry = self.guests_entry.get()
                if not guests_entry:
                    raise ValueError("Guests entry is missing")
                guests = validate_numeric_input(guests_entry)
                if guests is None:
                    raise ValueError('Guests must be numeric')
                
                event_start_entry = self.event_time_start_entry.get()
                if not event_start_entry:
                    raise ValueError("Event 'Start' entry is missing")
                event_start = event_start_entry
                if event_start is None:
                    raise ValueError("Event 'Start' must be in HH:MM format")
                
                event_end_entry = self.event_time_end_entry.get()
                if not event_end_entry:
                    raise ValueError("Event 'End' entry is missing")
                event_end = event_end_entry
                if event_end is None:
                    raise ValueError("Event 'End' must be in HH:MM format")
            
            except ValueError as e:
                self.output_text.insert(tk.END, f'Error: {e} "\n', "red")
                
            # Staff timings + Override hrs
            food_staff_hours = 0
            wine_staff_hours = 0
            bartender_hours = 0
            barback_hours = 0
            cloak_hours = 0

            food_staff_hours += EventReception.calculate_food_team_time(event_start, event_end)
            if self.food_add_ovr > 0:
                food_staff_hours += self.food_add_ovr
            elif self.food_sub_ovr > 0:
                food_staff_hours -= self.food_sub_ovr
            wine_staff_hours += EventReception.calculate_wine_team_time(event_start, event_end)
            if self.wine_add_ovr > 0:
                wine_staff_hours += self.wine_add_ovr
            elif self.wine_sub_ovr > 0:
                wine_staff_hours -= self.wine_sub_ovr
            bartender_hours += EventReception.calculate_bartender_team_time(event_start, event_end)
            if self.bar_add_ovr > 0:
                bartender_hours += self.bar_add_ovr
            elif self.bar_sub_ovr > 0:
                bartender_hours -= self.bar_sub_ovr
            barback_hours += EventReception.calculate_barback_team_time(event_start, event_end)
            if self.barback_add_ovr > 0:
                barback_hours += self.barback_add_ovr
            elif self.barback_sub_ovr > 0:
                barback_hours -= self.barback_sub_ovr
            cloak_hours += EventReception.calculate_cloack_team_time(event_start, event_end)
            if self.cloakroom_add_ovr > 0:
                cloak_hours += self.cloakroom_add_ovr
            elif self.cloakroom_sub_ovr > 0:
                cloak_hours -= self.cloakroom_sub_ovr

            duration = EventReception.event_duration(event_start, event_end)    

            event = EventReception(event_name, event_type, guests, event_start, event_end, food_staff_hours, wine_staff_hours, bartender_hours, barback_hours, cloak_hours)

            # Add to list
            self.events_name_list.append(event_name)
            self.event_type_list.append(event_type)
            self.event_durations_list.append(duration)
            self.event_date_list.append(event_date)
            self.guests_list.append(guests)

            # Add to sub overview list
            self.reception_events_name_list.append(event_name)
            self.reception_event_type_list.append(event_type)
            self.reception_event_durations_list.append(duration)
            self.reception_event_date_list.append(event_date)
            self.reception_guests_list.append(guests)

            # number of staff
            num_food_staff = event.num_food_staff

            num_clearing_staff = event.num_clearing_staff
            num_wine_staff = event.num_wine_staff
            num_bartenders_staff = event.num_bartenders_staff
            num_barback_staff = event.num_barback_staff
            num_cloakroom_staff = event.num_cloakroom_staff

            total_staff_combined = event.total_staff_combined
            self.event_staff_total_count_list.append(total_staff_combined)
            self.reception_event_staff_total_count_list.append(total_staff_combined)


            self.total_food_service_staff_combined += num_food_staff
            self.total_clearing_staff_combined += num_clearing_staff
            self.total_wine_waiters_staff_combined += num_wine_staff        
            self.total_bartender_staff_combined += num_bartenders_staff
            self.total_barback_staff_combined += num_barback_staff
            self.total_cloakroom_staff_combined += num_cloakroom_staff

            # Calculate total staffing cost by category
            food_service_staff_cost = event.food_service_staff_cost
            wine_waiters_staff_cost = event.wine_waiters_staff_cost
            bartenders_staff_cost = event.bartenders_staff_cost
            barback_staff_cost = event.barback_staff_cost
            cloakroom_staff_cost = event.cloakroom_staff_cost

            total_staff_cost = event.total_staff_cost
            self.event_total_cost_list.append( "£" + str(total_staff_cost))
            self.reception_event_total_cost_list.append(total_staff_cost)

            # update sub overview totals list
            self.total_reception_guests_list = sum(self.reception_guests_list)
            self.total_reception_event_staff_total_count_list = sum(self.reception_event_staff_total_count_list)
            self.total_reception_event_total_cost_list = sum(self.reception_event_total_cost_list)

            self.total_food_service_staff_cost += food_service_staff_cost
            self.total_wine_waiters_staff_cost += wine_waiters_staff_cost
            self.total_bartender_staff_cost += bartenders_staff_cost
            if num_barback_staff == 0:
                self.total_barback_staff_cost += 0
            else:
                self.total_barback_staff_cost += barback_staff_cost
            self.total_cloakroom_staff_cost += cloakroom_staff_cost

            #total staff combined and cost for all events
            self.total_staff_combined_for_all_events += total_staff_combined

            self.total_staff_cost_for_all_events += total_staff_cost

            self.total_guests_combined += guests

            #Allocation variables
            food_waiter_AL = num_food_staff - num_clearing_staff
            clearing_AL = num_clearing_staff

            # Ovr hrs column
            food_ovr_hrs_column = 0
            wine_ovr_hrs_column = 0
            bartender_ovr_hrs_column = 0
            barback_ovr_hrs_column = 0
            cloakroom_ovr_hrs_column = 0

            if self.food_add_ovr > 0:
                food_ovr_hrs_column += self.food_add_ovr
            elif self.food_sub_ovr > 0:
                food_ovr_hrs_column -= self.food_sub_ovr
            if self.wine_add_ovr > 0:
                wine_ovr_hrs_column += self.wine_add_ovr
            elif self.wine_sub_ovr > 0:
                wine_ovr_hrs_column -= self.wine_sub_ovr
            if self.bar_add_ovr > 0:
                bartender_ovr_hrs_column += self.bar_add_ovr
            elif self.bar_sub_ovr > 0:
                bartender_ovr_hrs_column -= self.bar_sub_ovr
            if self.barback_add_ovr > 0:
                barback_ovr_hrs_column += self.barback_add_ovr
            elif self.barback_sub_ovr > 0:
                barback_ovr_hrs_column -= self.barback_sub_ovr
            if self.cloakroom_add_ovr > 0:
                    cloakroom_ovr_hrs_column += self.cloakroom_add_ovr
            elif self.cloakroom_sub_ovr > 0:
                    cloakroom_ovr_hrs_column -= self.cloakroom_sub_ovr

            #---------------------------------------------------------------- Reception OUTPUT --------------------------------------------------------------------------------------------------
            self.output_text.insert(tk.END, f'---------------------------------------------------------------------------------- RECEPTION ------------------------------------------------------------------------------------\n','orange')
            event_data = [
                ["Event Name", "Event Type", "Number of Guests", "Start Time", "End Time", "Duration", "Date"],
                [event_name, event_type, guests, event_start, event_end, str(duration) + "Hrs", event_date]
            ]

            staff_data = [
                ["Type of Staff", "Number of Staff", "Rates Per Hour","Hours", "Ovr Hrs", "Total Cost"],
                ["Food Waiter", num_food_staff,'£' + str(staff_rates['food_waiter']), food_staff_hours, food_ovr_hrs_column, '£' + str(food_service_staff_cost)],
                ["Wine Waiter", num_wine_staff,'£' + str(staff_rates['wine_waiter']), wine_staff_hours, wine_ovr_hrs_column, '£' + str(wine_waiters_staff_cost)],
                ["Bartender", num_bartenders_staff,'£' + str(staff_rates['bartender']), bartender_hours, bartender_ovr_hrs_column, '£' + str(bartenders_staff_cost)],
                ["Barback", num_barback_staff,'£' + str(staff_rates['barback']), barback_hours, barback_ovr_hrs_column, '£' + str(barback_staff_cost)],
                ["Cloakroom", num_cloakroom_staff, '£' + str(staff_rates['cloakroom']),cloak_hours, cloakroom_ovr_hrs_column, '£' + str(cloakroom_staff_cost)],
                ["Total", total_staff_combined,"", "", "", '£' + str(total_staff_cost)]
            ]
            staff_time_rules = [["Staff", "In", "Out"],
                                ["Food Waiter", "1.5 hrs before event", "1 hr after the event"],
                                ["Wine Waiter", "1.5 hrs before event", "1 hr after the event"],
                                ["Wartender", "2 hrs before the event", "2 hrs after the event"],
                                ["Barback", "1 hr before event", "2 hrs after the event"],
                                ["Cloakroom", "1.5 hrs before event", "1 hr after the event"],]
            event_table = tabulate(event_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*6) + "\n\n"
            self.output_text.insert(tk.END, event_table)
            staff_table = tabulate(staff_data, headers="firstrow", tablefmt='fancy_grid')
            staff_time_rules_table = tabulate(staff_time_rules, headers="firstrow", tablefmt='fancy_grid')  + "\n\n"
            
            # Split table strings into rows
            staff_table_rows = staff_table.split("\n")
            staff_time_rules_table_rows = staff_time_rules_table.split("\n")
            # Combine rows element-wise
            combined_rows = [row1 + " " + row2 for row1, row2 in zip(staff_table_rows, staff_time_rules_table_rows)]
            # Join combined rows into a single string
            combined_table_str = "\n".join(combined_rows)
            
            self.output_text.insert(tk.END, combined_table_str)

            food_waiter_allocation_data = [["Food Waiter", "Allocations"],
                                        ["Food", food_waiter_AL],
                                        ["Clearing", clearing_AL]]
            food_waiter_allocation_table = tabulate(food_waiter_allocation_data, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", colalign=("center",)*2) + "\n\n"
            self.output_text.insert(tk.END, "\n\n" + food_waiter_allocation_table )

            # Clear entry fields
            self.event_name_entry.delete(0, tk.END)
            self.guests_entry.delete(0, tk.END)
            self.event_time_start_entry.delete(0, tk.END)
            self.event_time_end_entry.delete(0, tk.END)
            self.event_time_lunchdinner_entry.delete(0, tk.END)
            self.event_date_entry.delete(0, tk.END)

            # Reset Override hours
            self.AM_food_add_ovr = 0
            self.PM_food_add_ovr = 0
            self.food_add_ovr = 0
            self.wine_add_ovr = 0
            self.bar_add_ovr = 0
            self.barback_add_ovr = 0
            self.cloakroom_add_ovr = 0
            self.hostess_add_ovr = 0
            self.porter_add_ovr = 0

            self.AM_food_sub_ovr = 0
            self.PM_food_sub_ovr = 0
            self.food_sub_ovr = 0
            self.wine_sub_ovr = 0
            self.bar_sub_ovr = 0
            self.barback_sub_ovr = 0
            self.cloakroom_sub_ovr = 0
            self.hostess_sub_ovr = 0
            self.porter_sub_ovr = 0
        

    #---------------------------------------------------------------- OVERVIEW OUTPUT --------------------------------------------------------------------------------------------------
    def overview_reports(self):

            self.output_text.insert(tk.END, f'---------------------------------------------------------------------------------- OVERVIEW -------------------------------------------------------------------------------------\n','orange')
            events_info_data = zip(self.events_name_list, self.event_type_list,self.guests_list, self.event_staff_total_count_list, self.event_durations_list, self.event_date_list, self.event_total_cost_list)
            totals_data = [["Totals", "", self.total_guests_combined, self.total_staff_combined_for_all_events, "", "", "£" +  str(round(self.total_staff_cost_for_all_events, 2))]]
            combined_data = list(events_info_data) + totals_data
            combined_table_str = tabulate(combined_data, headers=["Event Name", "Type of Event", "Number of Guests", "Number of Staff", "Duration", "Date", "Cost"], tablefmt='fancy_grid')
            self.output_text.insert(tk.END, combined_table_str)
            
            self.output_text.insert(tk.END, f'\n\n------------------------------------------------------------------------------- COST BREAK DOWN ---------------------------------------------------------------------------------\n', 'yellow')

            
            totals_data = [
                    ["Staff", "Number of Staff ", "Cost"],
                    ["Food waiter", self.total_food_service_staff_combined, "£" + str(round(self.total_food_service_staff_cost, 2))],
                    ["Wine waiter", self.total_wine_waiters_staff_combined, "£" + str(round(self.total_wine_waiters_staff_cost, 2))],
                    ["Bartender", self.total_bartender_staff_combined, "£" + str(round(self.total_bartender_staff_cost, 2))],
                    ["Barback", self.total_barback_staff_combined, "£" + str(round(self.total_barback_staff_cost, 2))],
                    ["Cloakroom", self.total_cloakroom_staff_combined, "£" + str(round(self.total_cloakroom_staff_cost, 2))],
                    ["Porter", self.total_porter_staff_combined, "£" + str(round(self.total_porter_staff_cost, 2))],
                    ["Hostess", self.total_hostess_staff_combined, "£" + str(round(self.total_hostess_staff_cost, 2))],
                    ["Total", self.total_staff_combined_for_all_events, "£" + str(round(self.total_staff_cost_for_all_events, 2))]
                    ]

            totals_table = tabulate(totals_data, headers="firstrow", tablefmt="fancy_grid") + "\n\n"
            self.output_text.insert(tk.END, totals_table)
    
            # plt.barh(self.x, self.y, color = 'r', height=0.1)
            # plt.title('Total Cost Per Event') 
            # plt.show()
    
    #-------------------------------------------------------------- SUB OVERVIEW OUTPUT -------------------------------------------------------------------------------------------------
    def suboverview_reports(self):
            
            sub_overview_var = self.sub_overview_var.get().upper()

            if sub_overview_var == "DDR BOWL":
                self.output_text.insert(tk.END, f'------------------------------------------------------------------------------ DDR BOWL OVERVIEW --------------------------------------------------------------------------------\n','orange')
                events_info_data = zip(self.ddr_bowl_events_name_list, self.ddr_bowl_event_type_list,self.ddr_bowl_guests_list, self.ddr_bowl_event_staff_total_count_list, self.ddr_bowl_event_durations_list, self.ddr_bowl_event_date_list, self.ddr_bowl_event_total_cost_list)
                totals_data = [["Totals", "", self.total_ddr_bowl_guests_list, self.total_ddr_bowl_event_staff_total_count_list, "", "", "£" +  str(round(self.total_ddr_bowl_event_total_cost_list, 2))]]
                combined_data = list(events_info_data) + totals_data
                combined_table_str = tabulate(combined_data, headers=["Event Name", "Type of Event", "Number of Guests", "Number of Staff", "Duration", "Date", "Cost"], tablefmt='fancy_grid') + "\n\n"
                self.output_text.insert(tk.END, combined_table_str)

            elif sub_overview_var == "DDR BUFFET":
                self.output_text.insert(tk.END, f'----------------------------------------------------------------------------- DDR BUFFET OVERVIEW -------------------------------------------------------------------------------\n','orange')
                events_info_data = zip(self.ddr_buffet_events_name_list, self.ddr_buffet_event_type_list,self.ddr_buffet_guests_list, self.ddr_buffet_event_staff_total_count_list, self.ddr_buffet_event_durations_list, self.ddr_buffet_event_date_list, self.ddr_buffet_event_total_cost_list)
                totals_data = [["Totals", "", self.total_ddr_buffet_guests_list, self.total_ddr_buffet_event_staff_total_count_list, "", "", "£" +  str(round(self.total_ddr_buffet_event_total_cost_list, 2))]]
                combined_data = list(events_info_data) + totals_data
                combined_table_str = tabulate(combined_data, headers=["Event Name", "Type of Event", "Number of Guests", "Number of Staff", "Duration", "Date", "Cost"], tablefmt='fancy_grid') + "\n\n"
                self.output_text.insert(tk.END, combined_table_str)
            
            elif sub_overview_var == "DINNER":
                self.output_text.insert(tk.END, f'------------------------------------------------------------------------------- DINNER OVERVIEW ---------------------------------------------------------------------------------\n','orange')
                events_info_data = zip(self.dinner_events_name_list, self.dinner_event_type_list,self.dinner_guests_list, self.dinner_event_staff_total_count_list, self.dinner_event_durations_list, self.dinner_event_date_list, self.dinner_event_total_cost_list)
                totals_data = [["Totals", "", self.total_dinner_guests_list, self.total_dinner_event_staff_total_count_list, "", "", "£" +  str(round(self.total_dinner_event_total_cost_list, 2))]]
                combined_data = list(events_info_data) + totals_data
                combined_table_str = tabulate(combined_data, headers=["Event Name", "Type of Event", "Number of Guests", "Number of Staff", "Duration", "Date", "Cost"], tablefmt='fancy_grid') + "\n\n"
                self.output_text.insert(tk.END, combined_table_str)
            
            elif sub_overview_var == "DINNER NOBU MENU":
                self.output_text.insert(tk.END, f'-------------------------------------------------------------------------- DINNER NOBU MENU OVERVIEW ----------------------------------------------------------------------------\n','orange')
                events_info_data = zip(self.dinner_nm_events_name_list, self.dinner_nm_event_type_list,self.dinner_nm_guests_list, self.dinner_nm_event_staff_total_count_list, self.dinner_nm_event_durations_list, self.dinner_nm_event_date_list, self.dinner_nm_event_total_cost_list)
                totals_data = [["Totals", "", self.total_dinner_nm_guests_list, self.total_dinner_nm_event_staff_total_count_list, "", "", "£" +  str(round(self.total_dinner_nm_event_total_cost_list, 2))]]
                combined_data = list(events_info_data) + totals_data
                combined_table_str = tabulate(combined_data, headers=["Event Name", "Type of Event", "Number of Guests", "Number of Staff", "Duration", "Date", "Cost"], tablefmt='fancy_grid') + "\n\n"
                self.output_text.insert(tk.END, combined_table_str)

            elif sub_overview_var == "RECEPTION":
                self.output_text.insert(tk.END, f'------------------------------------------------------------------------------ RECEPTION OVERVIEW -------------------------------------------------------------------------------\n','orange')
                events_info_data = zip(self.reception_events_name_list, self.reception_event_type_list,self.reception_guests_list, self.reception_event_staff_total_count_list, self.reception_event_durations_list, self.reception_event_date_list, self.reception_event_total_cost_list)
                totals_data = [["Totals", "", self.total_reception_guests_list, self.total_reception_event_staff_total_count_list, "", "", "£" +  str(round(self.total_reception_event_total_cost_list, 2))]]
                combined_data = list(events_info_data) + totals_data
                combined_table_str = tabulate(combined_data, headers=["Event Name", "Type of Event", "Number of Guests", "Number of Staff", "Duration", "Date", "Cost"], tablefmt='fancy_grid') + "\n\n"
                self.output_text.insert(tk.END, combined_table_str)
            
root = tk.Tk()
app = App(root)
root.mainloop()