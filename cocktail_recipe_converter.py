import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

passionfruitmartini = {'Vanilla Vodka' : 40, 'Passionfruit Juice' : 50, 'Passao' : 15, 'Vanilla Syrup' : 15, 'Lime Juice' : 5}

shinjuku = {'Bourbon': 40, 
  'Noilly Prat': 20,
            'Cherry Syrup': 15, 
  'Cherry Bitters': 0.45,
            'Angostura Bitters': 0.45}

mojito = {'White Rum': 50, 
  'Syrup': 20, 'Lime Juice': 25}

Umi = {'Dark Rum': 50, 
'Curacao Syrup': 15, 
'Citrus Cordial': 15}

pandan = {'Vodka': 40, 
'Pandan': 40,
'Citric Cordial': 10,
'Cherry Bitters': 0.45,}

oishii = {'Tequila': 40,
'Rose Syrup': 40,
'Vanilla bitters': 0.45,}

ringo = {'Gin': 45,
'Apple Syrup' : 25,
'Saline solution': 1}

negroni= {'Gin': 25,
'Campari' : 25,
'Puntemes': 25}

vodkapassao = {'Vanilla Vodka': 40,
              'Passao Liqueur': 15}

spirit_volume = 700
carton_juice = 1000
bitters = 200
lime_juice = 1000
lemon_juice = 1000

#*******************************************************************************************************************

def convert_cocktail_to_recipe():
#user inputs
    
      cocktail_name = cocktail_entry.get().lower()
      if cocktail_name == 'passionfruit martini':
          cocktail = passionfruitmartini
      elif cocktail_name == 'shinjuku':
           cocktail = shinjuku
      elif cocktail_name == 'umi':
           cocktail = Umi
      elif cocktail_name == 'pandan':
           cocktail_name = pandan
      elif cocktail_name == 'oishii':
           cocktail = oishii
      elif cocktail_name == 'ringo':
           cocktail = ringo
      elif cocktail_name == 'negroni':
           cocktail = negroni
      elif cocktail_name == 'vodka passao':
           cocktail = vodkapassao
      elif cocktail_name == 'library':
        output_textbox.insert("end", "------------- LIBRARY ------------\n")
        output_textbox.insert("end", "passionfruit martini \nshinjuku \numi \npandan \noishii \nringo \nnegroni \nvodka passao\n")
        cocktail_entry.delete(0, 'end')
        return
    
      else:
          output_textbox.insert("end", 'Invalid cocktail name. Please try again.\n')
      try:
        num_bottles = float(bottles_entry.get())
      except ValueError:
         output_textbox.insert("end", 'Invalid number of bottles. Please try again.\n')
         return
      
      stock = 750 * num_bottles
      cocktail_volume = sum(cocktail.values())
      ml_converter = stock / cocktail_volume

#defining an empty dictionary "recipe"
      recipe = {}
  #loops over the cocktail ingridients and passing over to the new variable named "ingridient for the key and the amount for the value"
      for ingredient, amount in cocktail.items():
      #adds key to the empty recipe dictionary and converts the value of the key by ml_converter and multiply the amount
        recipe[ingredient] = ml_converter * amount
#prints the ingridients and amount in ml.
      output_textbox.insert("end",'\n---------- RECIPE TO ML ----------\n')
      output_textbox.insert("end", f'Cocktail name:  {cocktail_name}\n\n', 'yellow')
      for ingredient, volume in recipe.items():
        output_textbox.insert("end", f"{ingredient}: {round(volume, 1)} ml\n")
      output_textbox.insert("end", '\n---------- ML TO BOTTLES ----------\n')
      for ingredient, volume in recipe.items():
           if ingredient == "Passionfruit Juice":
                bottle = volume / 1000
           elif volume < 150:
                bottle = volume / 200
           elif ingredient == "Rose Syrup":
                syrup = volume / 450
                syrup = syrup * 350
                bottle = syrup / 700
           else:
                bottle = volume / 700
           output_textbox.insert("end", f"{ingredient}: {round(bottle, 1)} bottles\n")
      cocktail_entry.delete(0, "end")
      bottles_entry.delete(0, "end")
      
        

#*******************************************************************************************************************

def stock_counter():
  cocktail = cocktail_stock_entry.get().lower()
  if cocktail == 'library':
     output2_textbox.insert("end", "------------- LIBRARY ------------\n")
     output2_textbox.insert("end", "passionfruit martini \nshinjuku \numi \noishii \nringo \nnegroni \nmojito\n")
     cocktail_stock_entry.delete(0, 'end')
     return
  try:
     portion = int(portion_entry.get())
  except ValueError:
     output2_textbox.insert("end", 'Invalid number of portions. Please try again.\n')
     return
  recipe = {}
  cocktail = cocktail_stock_entry.get().lower()
  if cocktail == 'passionfruit martini':
    
    for ingredient, volume in passionfruitmartini.items():
      if ingredient == 'Vanilla Vodka':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Passionfruit Juice':
        recipe[ingredient] = volume * portion / carton_juice
      elif ingredient == 'Passao':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Vanilla Syrup':
        recipe[ingredient] = volume * portion / spirit_volume
      else:
        recipe[ingredient] = volume * portion / lime_juice

  elif cocktail == 'shinjuku':
    for ingredient, volume in shinjuku.items():
      if ingredient == 'Bourbon':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Noilly Prat':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Cherry Syrup':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Cherry Bitters':
        recipe[ingredient] = volume * portion / bitters

  elif cocktail == 'umi':
    for ingredient, volume in Umi.items():
      if ingredient == 'Dark Rum':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Curacao Syrup':
        recipe[ingredient] = volume * portion / spirit_volume

  elif cocktail == 'oishii':
    for ingredient, volume in oishii.items():
      if ingredient == 'Tequila':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Rose Syrup':
        volume = volume - 8.8
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Vanilla bitters':
        recipe[ingredient] = volume * portion / bitters

  elif cocktail == 'ringo':
    for ingredient, volume in ringo.items():
      if ingredient == 'Gin':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Apple Syrup':
        recipe[ingredient] = volume * portion / spirit_volume

  elif cocktail == 'negroni':
    for ingredient, volume in negroni.items():
      recipe[ingredient] = volume * portion / spirit_volume

  elif cocktail == 'mojito':
    for ingredient, volume in mojito.items():
      if ingredient == 'White Rum':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Syrup':
        recipe[ingredient] = volume * portion / spirit_volume
      elif ingredient == 'Lime Juice':
        recipe[ingredient] = volume * portion / lime_juice
  else:
       output2_textbox.insert("end", "Invalid cocktail name\n")
       return

  output2_textbox.insert("end",'\n------------ QUANTITY ------------\n')
  for ingredient, volume in recipe.items():
    output2_textbox.insert("end",f' {ingredient} : {round(volume, 1)} Btls\n')
  if cocktail == 'mojito':
    output2_textbox.insert("end",f" Soda water\n Freshmint")

  cocktail_stock_entry.delete(0, "end")
  portion_entry.delete(0, "end")

def clear():
   output_textbox.delete("1.0", "end")

def clear2():
   output2_textbox.delete("1.0", "end")

root = customtkinter.CTk()
root.geometry("800x400")
root.title("Beverage Tool")

frame = customtkinter.CTkFrame(master=root)
frame.pack(side="left", pady=5, padx=0, fill="both", expand=True)
frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(side="right", pady=5, padx=0, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Cocktail Batch Converter", font=("Arial", 12, "bold"))
label.pack(pady=5, padx=0)
label2 = customtkinter.CTkLabel(master=frame2, text="Stock Counter", font=("Arial", 12, "bold"))
label2.pack(pady=5, padx=0)

cocktail_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Cocktail Name")
cocktail_entry.pack(pady=5, padx=10)
bottles_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Number of Bottles")
bottles_entry.pack(pady=5, padx=10)

cocktail_stock_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Cocktail Name")
cocktail_stock_entry.pack(pady=5, padx=10)
portion_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Portion")
portion_entry.pack(pady=5, padx=10)

enter_button = customtkinter.CTkButton(master=frame, text="Enter", command=convert_cocktail_to_recipe)
enter_button.pack(pady=5, padx=10)
enter2_button = customtkinter.CTkButton(master=frame2, text="Enter", command=stock_counter)
enter2_button.pack(pady=5, padx=10)

clear_button = customtkinter.CTkButton(master=frame, text="Clear", command=clear)
clear_button.pack(pady=5, padx=10)
clear2_button = customtkinter.CTkButton(master=frame2, text="Clear", command=clear2)
clear2_button.pack(pady=5, padx=10)

output_textbox = customtkinter.CTkTextbox(master=frame, width=350, height=300, font=("Arial", 12))
output_textbox.pack(pady=5, padx=5)
output2_textbox = customtkinter.CTkTextbox(master=frame2, width=350, height=300, font=("Arial", 12))
output2_textbox.pack(pady=5, padx=5)

root.mainloop()


  

  