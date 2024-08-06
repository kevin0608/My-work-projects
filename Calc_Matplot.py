import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

class EventDDR:
    def __init__(self, ddr_meeting_rooms, event_name, event_type, guests, food_hours, food_rate, cloakroom_hours, cloakroom_rate):
        self.room = ddr_meeting_rooms
        self.name = event_name
        self.type = event_type
        self.guests = guests
        self.food_hours = food_hours
        self.food_rate = food_rate
        self.cloakroom_hours = cloakroom_hours
        self.cloakroom_rate = cloakroom_rate
        ddr_meeting_rooms = 0
        self.calculate_staff()
        self.calculate_staff_cost()

    def calculate_staff(self):
        self.num_food_staff = 0
        self.num_cloakroom_staff = 0
        self.num_food_staff += self.room

        self.hot_food_staff = round(self.guests / 30)

        if self.guests <= 80:
            self.num_food_staff += 4
            self.num_cloakroom_staff += 1
            if self.type == 'DDR BOWL':
                self.num_food_staff += 1
                self.num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.num_food_staff += 2

        elif self.guests > 80 and self.guests <= 100:
            self.num_food_staff += 7
            self.num_cloakroom_staff += 1
            if self.type == 'DDR BOWL':
                self.num_food_staff += 1
                self.num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.num_food_staff += 3

        elif self.guests > 100 and self.guests <= 150:
            self.num_food_staff += 6
            if self.guests > 100:
                self.num_food_staff += 2
            elif self.guests == 150:
                self.num_food_staff += 3
            self.num_cloakroom_staff += 1
            if self.type == 'DDR BOWL':
                self.num_food_staff += 2
                self.num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.num_food_staff += 4

        elif self.guests > 150 and self.guests <= 200:
            self.num_food_staff += 6
            if self.guests >= 150:
                self.num_food_staff += 3
            elif self.guests == 200:
                self.num_food_staff += 4
            self.num_cloakroom_staff += 2
            if self.type == 'DDR BOWL':
                self.num_food_staff += 2
                self.num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.num_food_staff += 4

        elif self.guests > 200:
            self.num_food_staff += 13
            if self.guests > 200:
                self.num_cloakroom_staff += 2
            elif self.guests > 250 and self.guests <= 300:
                self.num_cloakroom_staff += 3
            if self.type == 'DDR BOWL':
                self.num_food_staff += 3
                self.num_food_staff += round(self.guests / 30)
            elif self.type == 'DDR BUFFET':
                self.num_food_staff += 5

        self.ddr_total_staff_combined = sum([self.num_food_staff, self.num_cloakroom_staff])

    def calculate_staff_cost(self):

        self.food_service_staff_cost = round(self.num_food_staff * self.food_rate * self.food_hours, 2)
        self.cloakroom_staff_cost = round(self.num_cloakroom_staff * self.cloakroom_rate * self.cloakroom_hours, 2)
        self.total_staff_cost = round(sum([self.food_service_staff_cost, self.cloakroom_staff_cost]), 2)


class Event:
    def __init__(self, event_name, event_type, guests, food_hours, food_rate, wine_hours, wine_rate, bartender_hours, bartender_rate, cloakroom_hours, cloakroom_rate):
        self.name = event_name
        self.type = event_type
        self.guests = guests
        self.food_hours = food_hours
        self.food_rate = food_rate
        self.wine_hours = wine_hours
        self.wine_rate = wine_rate
        self.bartender_hours = bartender_hours
        self.bartender_rate = bartender_rate
        self.cloakroom_hours = cloakroom_hours
        self.cloakroom_rate = cloakroom_rate
        self.staff_ratios = {'food_service' : 25, 'clearing' : 50, 'wine_waiters' : 30, 'bartenders' : 50, 'cloakroom': 100}
        self.calculate_staff()
        self.calculate_staff_cost()

    def calculate_staff(self):
            
            self.num_food_staff = 0
            self.num_cloakroom_staff = 0
        
            if self.food_hours == 0:
                self.num_food_staff = 0
            else:
                self.num_food_staff = round(self.guests / self.staff_ratios['food_service'])  

            self.num_food_staff += round(self.guests / self.staff_ratios['clearing'])
            self.num_clearing_staff = round(self.guests / self.staff_ratios['clearing'])

            if self.wine_hours == 0:
                self.num_wine_staff = 0
            else:
                self.num_wine_staff = round(self.guests / self.staff_ratios['wine_waiters'])
            if self.bartender_hours == 0:
                self.num_bartenders_staff = 0
            else:
                self.num_bartenders_staff = round(self.guests /self.staff_ratios['bartenders'])

            remainder = self.guests % 100
            cloakroom_rounded = self.guests - remainder + 100

            if self.cloakroom_hours == 0:
                self.num_cloakroom_staff = 0
            else:
                if remainder >= 50:
                    self.num_cloakroom_staff += (cloakroom_rounded // self.staff_ratios['cloakroom'])
                else:
                    self.num_cloakroom_staff += (self.guests // self.staff_ratios['cloakroom'])

            self.total_staff_combined = sum([self.num_food_staff, 
                                         self.num_wine_staff, self.num_bartenders_staff, 
                                         self.num_cloakroom_staff])

    def calculate_staff_cost(self):
        
            self.food_service_staff_cost = round(self.num_food_staff * self.food_rate * self.food_hours, 2)
            self.wine_waiters_staff_cost = round(self.num_wine_staff * self.wine_rate * self.wine_hours, 2)
            self.bartenders_staff_cost = round(self.num_bartenders_staff * self.bartender_rate * self.bartender_hours, 2)
            self.cloakroom_staff_cost = round(self.num_cloakroom_staff * self.cloakroom_rate * self.cloakroom_hours, 2)
            self.total_staff_cost = round(sum([self.food_service_staff_cost,
                                        self.wine_waiters_staff_cost, self.bartenders_staff_cost,
                                        self.cloakroom_staff_cost]), 2)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Events Agency Calculator')
        self.create_widgets()
        self.events = []
        root.config(bg='#333333')

         # Varialbes for total staff in category
        self.total_food_service_staff_combined = 0
        self.total_clearing_staff_combined = 0
        self.total_wine_waiters_staff_combined = 0
        self.total_bartender_staff_combined = 0
        self.total_cloakroom_staff_combined = 0

         # Variables for total staffing cost by category
        self.total_food_service_staff_cost = 0
        self.total_clearing_staff_cost = 0
        self.total_wine_waiters_staff_cost = 0
        self.total_bartender_staff_cost = 0
        self.total_cloakroom_staff_cost = 0

        #total staff combined and cost for all events
        self.total_staff_combined_for_all_events = 0
        self.total_staff_cost_for_all_events = 0

        #list for event names, cost, number of staff for plotting
        self.events_name_list = []
        self.events_cost_list = []
        self.events_staff_list = []

        self.output_text.insert(tk.END, "The 'event type' must be one of the following to ensure correct calculation based on specific conditions:\n \t\t\tReception, DDR bowl, DDR buffet\nFor ddr 'event type', only fill in the necessary entry fields: Food waiter, Cloakroom and DDR Meeting Rooms\n\n", "orange")


    def clear_fields(self):
        
        
        self.event_name_entry.delete(0, tk.END)
        self.guests_entry.delete(0, tk.END)
        self.food_hours_entry.delete(0, tk.END)
        self.wine_hours_entry.delete(0, tk.END)
        self.bartender_hours_entry.delete(0, tk.END)
        self.cloakroom_hours_entry.delete(0, tk.END)

        self.food_rate_entry.delete(0, tk.END)
        self.wine_rate_entry.delete(0, tk.END)
        self.bartender_rate_entry.delete(0, tk.END)
        self.cloakroom_rate_entry.delete(0, tk.END)

        self.ddr_meeting_rooms_entry.delete(0, tk.END)


        self.output_text.delete(1.0, tk.END)

         # Varialbes for total staff in category
        self.total_food_service_staff_combined = 0
        self.total_wine_waiters_staff_combined = 0
        self.total_bartender_staff_combined = 0
        self.total_cloakroom_staff_combined = 0

         # Variables for total staffing cost by category
        self.total_food_service_staff_cost = 0
        self.total_wine_waiters_staff_cost = 0
        self.total_bartender_staff_cost = 0
        self.total_cloakroom_staff_cost = 0

        #total staff combined and cost for all events
        self.total_staff_combined_for_all_events = 0
        self.total_staff_cost_for_all_events = 0

        self.events_name_list = []


        self.output_text.insert(tk.END, "The event type must be one of the following to ensure correct calculation based on specific conditions:\n \t\t\tReception, DDR bowl, DDR buffet\nFor ddr 'event type', only fill in the necessary entry fields: Food waiter, Cloakroom and DDR Meeting Rooms\n\n", "orange")




    def create_widgets(self):   

        # Labels and entries for each event 
        self.event_frame = tk.Frame(self.root)
        self.event_frame.grid(rowspan= 2, columnspan=2)

        # Event type option menu
        self.event_types = ["Reception", "DDR Bowl", "DDR Buffet"]

        self.event_type_label = tk.Label(self.event_frame, text="Event Type:")
        self.event_type_label.grid(row=1, column=0)
        self.event_type_var = tk.StringVar(root)
        self.event_type_var.set(self.event_types[0])
        self.event_type_dropdown = tk.OptionMenu(self.event_frame, self.event_type_var, *self.event_types)
        self.event_type_dropdown.grid(row=1, column=1)

        #Phasu credit label
        self.Phasu = tk.Label(self.event_frame, text="Credits to Phasu")
        self.Phasu.grid(row=8, column=4)

         # Meeting rooms

        self.ddr_meeting_rooms_entry = tk.Label(self.event_frame, text="DDR Meeting Rooms:")
        self.ddr_meeting_rooms_entry.grid(row=2, column=4)

        self.ddr_meeting_rooms_entry = tk.Entry(self.event_frame, width=5)
        self.ddr_meeting_rooms_entry.grid(row=3, column=4)

        self.event_name_label = tk.Label(self.event_frame, text="Events Name:")
        self.event_name_label.grid(row=0, column=0)
        self.event_name_entry = tk.Entry(self.event_frame, width=15)
        self.event_type_dropdown.config(width=12)
        self.event_name_entry.grid(row=0, column=1, columnspan=1)
   
        self.guests_label = tk.Label(self.event_frame, text="Number of Guests:")
        self.guests_label.grid(row=2, column=0)
        self.guests_entry = tk.Entry(self.event_frame, width=15)
        self.guests_entry.grid(row=2, column=1)

        # Rate per hour label
        self.rates_label = tk.Label(self.event_frame, text="Rate Per Hour")
        self.rates_label.grid(row=2, column=2)

        self.food_hours_label = tk.Label(self.event_frame, text="Food Waiter Hours:")
        self.food_hours_label.grid(row=3, column=0)
        self.food_hours_entry = tk.Entry(self.event_frame, width=15)
        self.food_hours_entry.grid(row=3, column=1)

        self.food_rate_entry = tk.Entry(self.event_frame, width=5)
        self.food_rate_entry.grid(row=3, column=2)

        self.wine_hours_label = tk.Label(self.event_frame, text="Wine Waiter Hours:")
        self.wine_hours_label.grid(row=5, column=0)
        self.wine_hours_entry = tk.Entry(self.event_frame, width=15)
        self.wine_hours_entry.grid(row=5, column=1)

        self.wine_rate_entry = tk.Entry(self.event_frame, width=5)
        self.wine_rate_entry.grid(row=5, column=2)

        self.bartender_hours_label = tk.Label(self.event_frame, text="Bartender Hours:")
        self.bartender_hours_label.grid(row=6, column=0)
        self.bartender_hours_entry = tk.Entry(self.event_frame, width=15)
        self.bartender_hours_entry.grid(row=6, column=1)

        self.bartender_rate_entry = tk.Entry(self.event_frame, width=5)
        self.bartender_rate_entry.grid(row=6, column=2)

        self.cloakroom_hours_label = tk.Label(self.event_frame, text="Cloakroom Staff Hours:")
        self.cloakroom_hours_label.grid(row=7, column=0)
        self.cloakroom_hours_entry = tk.Entry(self.event_frame, width=15)
        self.cloakroom_hours_entry.grid(row=7, column=1)

        self.cloakroom_rate_entry = tk.Entry(self.event_frame, width=5)
        self.cloakroom_rate_entry.grid(row=7, column=2) 

         # Button to calcul
        self.add_events_button = tk.Button(self.event_frame, text="Calculate", command=self.calculate_expenses)
        self.add_events_button.grid(row=0, column=3)

        # Button to clear fields
        self.clear_button = tk.Button(self.event_frame, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=0, column=5)

         # Button to clear fields
        self.total_button = tk.Button(self.event_frame, text="Calculate Totals", command=self.total_reports)
        self.total_button.grid(row=0, column=4)

        # Button to display graph 
        self.graph_button = tk.Button(self.event_frame, text="Total Report Graph", command=self.total_reports_graph)
        self.graph_button.grid(row=7, column=4)


        # Output text box
        output_label = tk.Label(root, text="")
        output_label.grid(row=1, column=0, sticky="w")

        self.output_text = tk.Text(root,height=40, width=60, font=("Helvetica", 14), bg="#1e1e1e")
        self.output_text.grid(row=2, column=0, columnspan=6, sticky='nsew')

        # Scrollbar
        self.scrollbar = tk.Scrollbar(root, command=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=2, column=6, sticky='ns')


        self.output_text.tag_configure("green", foreground="green")
        self.output_text.tag_configure("red", foreground="red")
        self.output_text.tag_configure("yellow", foreground="yellow")
        self.output_text.tag_configure("purple", foreground="purple")
        self.output_text.tag_configure("orange", foreground="orange")
        
    
    
    def calculate_expenses(self):   
        
        
        event_name = self.event_name_entry.get().upper()
        event_type = self.event_type_var.get().upper()
            
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
            
        if event_type == 'DDR BOWL' or event_type == 'DDR BUFFET':
            try:
                guests_entry = self.guests_entry.get()
                if not guests_entry:
                    raise ValueError("Guests entry is missing")
                guests = validate_numeric_input(guests_entry)
                if guests is None:
                    raise ValueError("Guests must be numeric")
                
                food_hours_entry = self.food_hours_entry.get()
                if not food_hours_entry:
                    raise ValueError("Food hours entry is missing")
                food_hours = validate_numeric_input(food_hours_entry)
                if food_hours is None:
                    raise ValueError("Food hours must be numeric")
                
                cloakroom_hours_entry = self.cloakroom_hours_entry.get()
                if not cloakroom_hours_entry:
                    raise ValueError("Cloakroom hours entry is missing")
                cloakroom_hours = validate_numeric_input(cloakroom_hours_entry)
                if cloakroom_hours is None:
                    raise ValueError("Cloakroom hours must be numeric")
                
                # Rates
                food_rate_entry = self.food_rate_entry.get()
                if not food_rate_entry:
                    raise ValueError("Food rate entry is missing")
                food_rate = validate_numeric_input(food_rate_entry)
                if food_rate is None:
                    raise ValueError("Food rate must be numeric")

                cloakroom_rate_entry = self.cloakroom_rate_entry.get()
                if not cloakroom_rate_entry:
                    raise ValueError("Cloakroom rate entry is missing")
                cloakroom_rate = validate_numeric_input(cloakroom_rate_entry)
                if cloakroom_rate is None:
                    raise ValueError("Cloakroom rate must be numeric")

                ddr_meeting_rooms_entry = self.ddr_meeting_rooms_entry.get()
                if not ddr_meeting_rooms_entry:
                    raise ValueError("DDR meeting rooms entry is missing")
                ddr_meeting_rooms = validate_numeric_input(ddr_meeting_rooms_entry)
                if ddr_meeting_rooms is None:
                    raise ValueError("DDR meeting rooms must be numeric")
                        
            except ValueError as e:
                self.output_text.insert(tk.END, f'Error: {e} "\n', "red")
            
            
        
            event = EventDDR(ddr_meeting_rooms, event_name, event_type, guests, food_hours, food_rate, cloakroom_hours, cloakroom_rate)

            # Add event to list
            self.events_name_list.append(event_name)

            #DDR Variables
            hot_food_staff = event.hot_food_staff

            # Calculate total staffing by category  
            num_food_staff = event.num_food_staff   
            num_cloakroom_staff = event.num_cloakroom_staff

            total_staff_combined = event.ddr_total_staff_combined

            #add to total stall list
            self.events_staff_list.append(event.ddr_total_staff_combined)

            self.total_food_service_staff_combined += num_food_staff
            self.total_cloakroom_staff_combined += num_cloakroom_staff

            # Calculate total staffing cost by category
            food_service_staff_cost = event.food_service_staff_cost
            cloakroom_staff_cost = event.cloakroom_staff_cost

            total_staff_cost = event.total_staff_cost

            #add cost to the list
            self.events_cost_list.append(event.total_staff_cost)

            self.total_food_service_staff_cost += food_service_staff_cost
            self.total_cloakroom_staff_cost += cloakroom_staff_cost

            #total staff combined and cost for all events
            self.total_staff_combined_for_all_events += event.ddr_total_staff_combined

            self.total_staff_cost_for_all_events += total_staff_cost

            # Clear entry fields
            self.event_name_entry.delete(0, tk.END)
            self.guests_entry.delete(0, tk.END)
            self.food_hours_entry.delete(0, tk.END)
            self.wine_hours_entry.delete(0, tk.END)
            self.bartender_hours_entry.delete(0, tk.END)
            self.cloakroom_hours_entry.delete(0, tk.END)

            self.food_rate_entry.delete(0, tk.END)
            self.wine_rate_entry.delete(0, tk.END)
            self.bartender_rate_entry.delete(0, tk.END)
            self.cloakroom_rate_entry.delete(0, tk.END)

            self.ddr_meeting_rooms_entry.delete(0, tk.END)

            #---------------------------------------------------------------- OUTPUT ------------------------------------------------------------------------------

            self.output_text.insert(tk.END, f'---------------------------------- DETAILS ---------------------------------\n', 'orange')       
            self.output_text.insert(tk.END, f'Event Name: {event_name}\n', 'orange')
            self.output_text.insert(tk.END, f'Event Type: {event_type}\n', 'orange')
            self.output_text.insert(tk.END, f'Number of Guests: {guests_entry}\n', 'orange')
            self.output_text.insert(tk.END, f'Food Waiter Hours: {food_hours} @ £ {food_rate}\n','orange')
            self.output_text.insert(tk.END, f'Cloakroom Staff Hours: {cloakroom_hours} @ £ {cloakroom_rate}\n\n','orange')
            self.output_text.insert(tk.END, f'Meeting Rooms: {ddr_meeting_rooms}\n\n','orange')

            self.output_text.insert(tk.END, f'--------------- NUMBER OF STAFF ---------------\n\n', 'green')

            self.output_text.insert(tk.END, f'Food Waiter: {num_food_staff}\n', 'green')
            self.output_text.insert(tk.END, f'Cloakroom: {num_cloakroom_staff}\n\n', 'green')
            self.output_text.insert(tk.END, f'Total: {event.ddr_total_staff_combined}\n\n', 'green')

            #--------------------------------------------------- DDR allocation conditioning ------------------------------------------------------

            self.output_text.insert(tk.END, f'--------------- Allocations ---------------\n\n', 'orange')

            if guests <= 80:
                self.output_text.insert(tk.END, "Coffee Station: 1 \nBuffet Station: 1 \nWater Station: 1 \nClearing: 1 \nCloakroom: 1\n", 'orange')
                self.output_text.insert(tk.END, f"Meeting Rooms: {ddr_meeting_rooms} \n\n", 'orange')
                if event_type == "DDR BOWL":
                    self.output_text.insert(tk.END, f"----- Bowl Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Additional Clearing: 1\n", 'orange')
                    self.output_text.insert(tk.END, f"Hot Food: {hot_food_staff}\n\n", 'orange')

                elif event_type == "DDR BUFFET":
                    self.output_text.insert(tk.END, f"----- Buffet Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Buffet Food Runners: 2\n\n", 'orange')

            elif guests > 80 and guests <= 100:
                self.output_text.insert(tk.END, "Coffee Station: 2 \nBuffet Station: 2 \nWater Station: 1 \nClearing: 2 \nCloakroom: 1\n", 'orange')
                self.output_text.insert(tk.END, f"Meeting Rooms: {ddr_meeting_rooms} \n\n", 'orange')
                if event_type == "DDR BOWL":
                    self.output_text.insert(tk.END, f"----- Bowl Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Additional Clearing: 1\n", 'orange')
                    self.output_text.insert(tk.END, f"Hot Food: {hot_food_staff}\n\n", 'orange')

                elif event_type == "DDR BUFFET":
                    self.output_text.insert(tk.END, f"----- Buffet Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Buffet Food Runners: 3\n\n", 'orange')

            elif guests > 100 and guests <= 150:
                self.output_text.insert(tk.END, "Coffee Station: 2\nCoffee Runner: 1 \nBuffet Station: 2 \nWater Station: 1 \nCloakroom: 2\n", 'orange')
                if guests > 100:
                    self.output_text.insert(tk.END, f"Clearing: 2 \n", 'orange')
                elif guests == 150:
                    self.output_text.insert(tk.END, f"Clearing: 3 \n", 'orange')
                self.output_text.insert(tk.END, f"Meeting Rooms: {ddr_meeting_rooms} \n\n", 'orange')
                if event_type == "DDR BOWL":
                    self.output_text.insert(tk.END, f"----- Bowl Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Additional Clearing: 2\n", 'orange')
                    self.output_text.insert(tk.END, f"Hot Food: {hot_food_staff}\n\n", 'orange')

                elif event_type == "DDR BUFFET":
                    self.output_text.insert(tk.END, f"----- Buffet Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Buffet Food Runners: 4\n\n", 'orange')

            elif guests > 150 and guests <= 200:
                self.output_text.insert(tk.END, "Coffee Station: 2\nCoffee Runner: 1 \nBuffet Station: 2 \nWater Station: 1 \nCloakroom: 2\n", 'orange')
                if guests >= 150:
                    self.output_text.insert(tk.END, f"Clearing: 3 \n", 'orange')
                elif guests == 200:
                    self.output_text.insert(tk.END, f"Clearing: 4 \n", 'orange')
                self.output_text.insert(tk.END, f"Meeting Rooms: {ddr_meeting_rooms} \n\n", 'orange')
                if event_type == "DDR BOWL":
                    self.output_text.insert(tk.END, f"----- Bowl Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Additional Clearing: 2\n", 'orange')
                    self.output_text.insert(tk.END, f"Hot Food: {hot_food_staff}\n\n", 'orange')

                elif event_type == "DDR BUFFET":
                    self.output_text.insert(tk.END, f"----- Buffet Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Buffet Food Runners: 4\n\n", 'orange')

            elif guests > 200:
                self.output_text.insert(tk.END, "Coffee Station: 3\nCoffee Runner: 1 \nBuffet Station: 3 \nWater Station: 2 \nClearing: 4\n", 'orange')
                if guests > 200:
                    self.output_text.insert(tk.END, f"Cloakroom: 2 \n", 'orange')
                elif guests >= 250 and guests <= 300:
                    self.output_text.insert(tk.END, f"Cloakroom: 3 \n", 'orange')
                self.output_text.insert(tk.END, f"Meeting Rooms: {ddr_meeting_rooms} \n\n", 'orange')
                if event_type == "DDR BOWL":
                    self.output_text.insert(tk.END, f"----- Bowl Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Additional Clearing: 3\n", 'orange')
                    self.output_text.insert(tk.END, f"Hot Food: {hot_food_staff}\n\n", 'orange')

                elif event_type == "DDR BUFFET":
                    self.output_text.insert(tk.END, f"----- Buffet Lunch -----\n", 'orange')
                    self.output_text.insert(tk.END, f"Buffet Food Runners: 5\n\n", 'orange')        
                
                    

            self.output_text.insert(tk.END, f'--------------- STAFF COST ---------------\n\n', 'red')

            self.output_text.insert(tk.END, f'Food Waiter: £ {food_service_staff_cost}\n', 'red')
            self.output_text.insert(tk.END, f'Cloakroom: £ {cloakroom_staff_cost}\n\n', 'red')

            self.output_text.insert(tk.END, f"Total: £ {total_staff_cost}\n\n",'red')

        #---------------------------------------------------------------- Reception event type ------------------------------------------------------------------------------

        elif event_type == 'RECEPTION':
            try:
                guests_entry = self.guests_entry.get()
                if not guests_entry:
                    raise ValueError("Guests entry is missing")
                guests = validate_numeric_input(guests_entry)
                if guests is None:
                    raise ValueError('Guests must be numeric')
                
                food_hours_entry = self.food_hours_entry.get()
                if not food_hours_entry:
                    raise ValueError("Food hours entry is missing")
                food_hours = validate_numeric_input(food_hours_entry)
                if food_hours is None:
                    raise ValueError('Food_hours must be numeric')
                
                wine_hours_entry = self.wine_hours_entry.get()
                if not wine_hours_entry:
                    raise ValueError("Wine rate entry is missing")
                wine_hours = validate_numeric_input(wine_hours_entry)
                if wine_hours is None:
                    raise ValueError("Wine rate must be numeric")

                bartender_hours_entry = self.bartender_hours_entry.get()
                if not bartender_hours_entry:
                    raise ValueError("Bartender rate entry is missing")
                bartender_hours = validate_numeric_input(bartender_hours_entry)
                if bartender_hours is None:
                    raise ValueError("Bartender rate must be numeric")

                cloakroom_hours_entry = self.cloakroom_hours_entry.get()
                if not cloakroom_hours_entry:
                    raise ValueError("Cloakroom rate entry is missing")
                cloakroom_hours = validate_numeric_input(cloakroom_hours_entry)
                if cloakroom_hours is None:
                    raise ValueError("Cloakroom rate must be numeric")
                
                # Rates
                food_rate_entry = self.food_rate_entry.get()
                if not food_rate_entry:
                    raise ValueError("Food rate entry is missing")
                food_rate = validate_numeric_input(food_rate_entry)
                if food_rate is None:
                    raise ValueError("Food rate must be numeric")

                wine_rate_entry = self.wine_rate_entry.get()
                if not wine_rate_entry:
                    raise ValueError("Wine rate entry is missing")
                wine_rate = validate_numeric_input(wine_rate_entry)
                if wine_rate is None:
                    raise ValueError("Wine rate must be numeric")

                bartender_rate_entry = self.bartender_rate_entry.get()
                if not bartender_rate_entry:
                    raise ValueError("Bartender rate entry is missing")
                bartender_rate = validate_numeric_input(bartender_rate_entry)
                if bartender_rate is None:
                    raise ValueError("Bartender rate must be numeric")

                cloakroom_rate_entry = self.cloakroom_rate_entry.get()
                if not cloakroom_rate_entry:
                    raise ValueError("Cloakroom rate entry is missing")
                cloakroom_rate = validate_numeric_input(cloakroom_rate_entry)
                if cloakroom_rate is None:
                    raise ValueError("Cloakroom rate must be numeric")
            except ValueError as e:
                self.output_text.insert(tk.END, f'Error: {e} "\n', "red")
                
            event = Event(event_name, event_type, guests, food_hours, food_rate, wine_hours, wine_rate, bartender_hours, bartender_rate, cloakroom_hours, cloakroom_rate)

            self.events_name_list.append(event_name)

            #number of staff
            num_food_staff = event.num_food_staff
            num_clearing_staff = event.num_clearing_staff
            num_wine_staff = event.num_wine_staff
            num_bartenders_staff = event.num_bartenders_staff
            num_cloakroom_staff = event.num_cloakroom_staff

            total_staff_combined = event.total_staff_combined

            #add to total stall list
            self.events_staff_list.append(event.total_staff_combined)

            self.total_food_service_staff_combined += num_food_staff
            self.total_clearing_staff_combined += num_clearing_staff
            self.total_wine_waiters_staff_combined += num_wine_staff        
            self.total_bartender_staff_combined += num_bartenders_staff 
            self.total_cloakroom_staff_combined += num_cloakroom_staff

            # Calculate total staffing cost by category
            food_service_staff_cost = event.food_service_staff_cost
            wine_waiters_staff_cost = event.wine_waiters_staff_cost
            bartenders_staff_cost = event.bartenders_staff_cost
            cloakroom_staff_cost = event.cloakroom_staff_cost

            total_staff_cost = event.total_staff_cost

            #add to total cost list
            self.events_cost_list.append(event.total_staff_cost)


            self.total_food_service_staff_cost += food_service_staff_cost
            self.total_wine_waiters_staff_cost += wine_waiters_staff_cost
            self.total_bartender_staff_cost += bartenders_staff_cost
            self.total_cloakroom_staff_cost += cloakroom_staff_cost

            #total staff combined and cost for all events
            self.total_staff_combined_for_all_events += total_staff_combined

            self.total_staff_cost_for_all_events += total_staff_cost

            #Allocation variables
            food_waiter_AL = num_food_staff - num_clearing_staff
            clearing_AL = num_clearing_staff
        

            # Clear entry fields
            self.event_name_entry.delete(0, tk.END)
            self.guests_entry.delete(0, tk.END)
            self.food_hours_entry.delete(0, tk.END)
            self.wine_hours_entry.delete(0, tk.END)
            self.bartender_hours_entry.delete(0, tk.END)
            self.cloakroom_hours_entry.delete(0, tk.END)

            self.food_rate_entry.delete(0, tk.END)
            self.wine_rate_entry.delete(0, tk.END)
            self.bartender_rate_entry.delete(0, tk.END)
            self.cloakroom_rate_entry.delete(0, tk.END)

            self.ddr_meeting_rooms_entry.delete(0, tk.END)

            #---------------------------------------------------------------- OUTPUT ------------------------------------------------------------------------------

            self.output_text.insert(tk.END, f'---------------------------------- DETAILS ---------------------------------\n', 'orange')
            self.output_text.insert(tk.END, f'Event Name: {event_name}\n', 'orange')
            self.output_text.insert(tk.END, f'Event Type: {event_type}\n', 'orange')
            self.output_text.insert(tk.END, f'Number of Guests: {guests}\n', 'orange')
            self.output_text.insert(tk.END, f'Food Waiter Hours: {food_hours} @ £ {food_rate}\n','orange')
            self.output_text.insert(tk.END, f'Wine Waiter Hours: {wine_hours} @ £ {wine_hours}\n', 'orange')
            self.output_text.insert(tk.END, f'Bartender Hours: {bartender_hours}  @ £ {bartender_rate}\n', 'orange')
            self.output_text.insert(tk.END, f'Cloakroom Staff Hours: {cloakroom_hours} @ £ {cloakroom_rate}\n\n','orange')

            self.output_text.insert(tk.END, f'--------------- NUMBER OF STAFF ---------------\n\n', 'green')

            self.output_text.insert(tk.END, f'Food Waiter: {num_food_staff}\n', 'green')
            self.output_text.insert(tk.END, f'Wine Waiter: {num_wine_staff}\n', 'green')
            self.output_text.insert(tk.END, f'Bartender: {num_bartenders_staff}\n', 'green')
            self.output_text.insert(tk.END, f'Cloakroom: {num_cloakroom_staff}\n\n', 'green')

            self.output_text.insert(tk.END, f'Total: {total_staff_combined}\n\n', 'green')

            self.output_text.insert(tk.END, f'--------------- Food Waiter Allocations ---------------\n\n', 'orange')

            self.output_text.insert(tk.END, f'Food Waiter: {food_waiter_AL}\n', 'orange')
            self.output_text.insert(tk.END, f'Clearing: {clearing_AL}\n\n', 'orange')


            self.output_text.insert(tk.END, f'--------------- STAFF COST ---------------\n\n', 'red')

            self.output_text.insert(tk.END, f'Food Waiter: £ {food_service_staff_cost}\n', 'red')
            self.output_text.insert(tk.END, f'Wine Waiter: £ {wine_waiters_staff_cost}\n', 'red')
            self.output_text.insert(tk.END, f'Bartender: £ {bartenders_staff_cost}\n', 'red')
            self.output_text.insert(tk.END, f'Cloakroom: £ {cloakroom_staff_cost}\n\n', 'red')

            self.output_text.insert(tk.END, f"Total: £ {total_staff_cost}\n\n",'red')

       
    def total_reports(self):

            # Varialbes for total staff in category
        
        self.output_text.insert(tk.END, f'----------------------------------------------------------------------------\n', 'orange')
        self.output_text.insert(tk.END, f'******* TOTALS *******\n\n','red')
        self.output_text.insert(tk.END, f'Events: {self.events_name_list}\n\n', 'orange')

        self.output_text.insert(tk.END, f'***** TOTAL NUMBER OF STAFF *****\n\n','green')
        self.output_text.insert(tk.END, f'Total Food Waiter Staff: {self.total_food_service_staff_combined}\n','green')
        self.output_text.insert(tk.END, f'Total Wine Waiter Staff: {self.total_wine_waiters_staff_combined}\n','green')
        self.output_text.insert(tk.END, f'Total Bartender Staff: {self.total_bartender_staff_combined}\n','green')
        self.output_text.insert(tk.END, f'Total Cloakroom: {self.total_cloakroom_staff_combined}\n\n','green')

        self.output_text.insert(tk.END, f"Total Staff For All Events: {self.total_staff_combined_for_all_events}\n",'green')

        self.output_text.insert(tk.END, f'\n***** TOTAL STAFF COST *****\n\n','red')

        self.output_text.insert(tk.END, f'Total Food Waiter: £ {self.total_food_service_staff_cost}\n','red')
        self.output_text.insert(tk.END, f'Total Wine Waiter: £ {self.total_wine_waiters_staff_cost}\n','red')
        self.output_text.insert(tk.END, f'Total Bartender Staff: £ {self.total_bartender_staff_cost}\n','red')
        self.output_text.insert(tk.END, f'Total Cloakroom: £ {self.total_cloakroom_staff_cost}\n\n','red')   

        self.output_text.insert(tk.END, f"Total Staffing Cost For All Events: £ {self.total_staff_cost_for_all_events}\n\n",'red')

    def total_reports_graph(self):
        self.x1 = np.array(self.events_name_list)
        self.y1 = np.array(self.events_cost_list)
        self.x2 = np.array(self.events_name_list)
        self.y2 = np.array(self.events_staff_list)

        plt.subplot(2,1,1)
        plt.barh(self.x1, self.y1, color = 'r', height=0.1)
        plt.title('Total Cost Per Event')
        plt.subplot(2,1,2)
        plt.title('Total Number of Staff per Event')
        plt.barh(self.x2, self.y2, color = 'g', height=0.1)
        plt.subplots_adjust(hspace=0.5)

        plt.show()


root = tk.Tk()
app = App(root)
root.mainloop()