# Print the name of the app
print("\n                                                 \33[1mMass Unit Converter\33[m\n")


# Print the purpose of this app
print("\33[1mAbout\33[m")
print("""This app will convert Mass and Weight values in between Metric Tons(ton), Kilograms(kg),
Pounds(lb), Ounces(oz), Grams(g), Carats(CT) and Milligrams(mg).\n\n""")


# Take input of the present unit, the mass value and the covertion unit
present_unit = input("\33[1mEnter Mass Unit(ton/kg/lb/oz/g/CT/mg):\33[m ")
value_of_mass = float(input("\n\33[1mEnter Mass Value:\33[m "))
convertion_unit = input("\n\33[1mEnter Convertion Unit(ton/kg/lb/oz/g/CT/mg):\33[m ")