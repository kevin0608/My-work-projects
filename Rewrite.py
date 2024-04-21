import tkinter as tk

class EventDDR:
    def __init__(self, event_name, event_type, guests, food_hours, cloakroom_hours, food_rate, cloakroom_rate, ddr_meeting_rooms):
        self.event_name = event_name
        self.event_type = event_type
        self.guests = guests
        self.food_hours = food_hours
        self.cloakroom_hours = cloakroom_hours
        self.food_rate = food_rate
        self.cloakromm_rate = cloakroom_rate
        self.ddr_meeting_rooms = ddr_meeting_rooms

    def calculate_staff(self):
        self.num_food_staff = 0
        self.num_cloakroom_staff = 0
        self.num_food_staff += self.ddr_meeting_rooms

        if self.guests <= 80:
            self.num_food_staff += 4
            self.num_cloakroom_staff += 1
            if self.event_type == "DDR BOWL":
                self.num_food_staff += 1
                self.num_food_staff += round(self.guests / 30)
            elif self.event_type == "DDR BUFFET":
                self.num_food_Staff += 2

        elif self.guests > 80 and self.guests <= 100:
            self.num_food_staff += 7
            self.num_cloakroom_staff += 1
            if self.event_type == "DDR BOWL":
                self.num_food_staff += 1
                self.num_food_staff += round(self.guests / 30)
            elif self.event_type == "DDR BUFFET":
                self.num_food_staff += 3

        elif self.guests > 100 and self.guests <= 150:
            self.num_food_staff += 6
            if self.guests > 100:
                self.num


