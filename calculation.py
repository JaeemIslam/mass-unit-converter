from MassUnitConverter import present_unit, value_of_mass, convertion_unit

# Equantions for metric ton(ton) to kg/lb/oz/g/CT/mg convertion
ton_to_kg = round(value_of_mass * 1000,4)
ton_to_lb = round(value_of_mass * 2204.623,4)
ton_to_oz = round(value_of_mass * 35273.96,4)
ton_to_g = round(value_of_mass * 10**6,4)
ton_to_CT = round(value_of_mass * (5*10**6),4)
ton_to_mg = round(value_of_mass * 10**9,4)

# Equantions for kilogram(kg) to ton/lb/oz/g/CT/mg convertion
kg_to_ton = round(value_of_mass / 1000,4)
kg_to_lb = round(value_of_mass * 2.204623,4)
kg_to_oz = round(value_of_mass * 35.27396,4)
kg_to_g = round(value_of_mass * 1000,4)
kg_to_CT = round(value_of_mass * 5000,4)
kg_to_mg = round(value_of_mass * 10**6,4)

# Equantions for pound(lb) to ton/kg/oz/g/CT/mg convertion
lb_to_ton = round(value_of_mass / 2204.623,4)
lb_to_kg = round(value_of_mass / 2.204623,4)
lb_to_oz = round(value_of_mass * 16,4)
lb_to_g = round(value_of_mass * 453.5924,4)
lb_to_CT = round(value_of_mass * 2267.962,4)
lb_to_mg = round(value_of_mass * 453592.4,4)

# Equantions for ounce(oz) to ton/kg/lb/g/CT/mg convertion
oz_to_ton = round(value_of_mass / 35273.96,4)
oz_to_kg = round(value_of_mass / 35.27396,4)
oz_to_lb = round(value_of_mass / 16,4)
oz_to_g = round(value_of_mass * 28.34952,4)
oz_to_CT = round(value_of_mass * 141.7476,4)
oz_to_mg = round(value_of_mass * 28349.52,4)

# Equantions for gram(g) to ton/kg/lb/oz/CT/mg convertion
g_to_ton = round(value_of_mass / 10**6,4)
g_to_kg = round(value_of_mass / 1000,4)
g_to_lb = round(value_of_mass / 453.5924,4)
g_to_oz = round(value_of_mass / 28.34952,4)
g_to_CT = round(value_of_mass * 5,4)
g_to_mg = round(value_of_mass * 1000,4)

# Equantions for carat(CT) to ton/kg/lb/oz/g/mg convertion
CT_to_ton = round(value_of_mass / (5*10**6),4)
CT_to_kg = round(value_of_mass / 5000,4)
CT_to_lb = round(value_of_mass / 2267.962,4)
CT_to_oz = round(value_of_mass / 141.7476,4)
CT_to_g = round(value_of_mass / 5,4)
CT_to_mg = round(value_of_mass * 200)

# Equantions for milligram(mg) to ton/kg/lb/oz/g/CT convertion
mg_to_ton = round(value_of_mass / 10**9,4)
mg_to_kg = round(value_of_mass / 10**6,4)
mg_to_lb = round(value_of_mass / 453592.4,4)
mg_to_oz = round(value_of_mass / 28349.52,4)
mg_to_g = round(value_of_mass / 1000,4)
mg_to_CT = round(value_of_mass / 200)