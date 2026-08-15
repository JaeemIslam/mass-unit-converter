from calculation import *

# Print the converted mass value according to conditions

match present_unit:
    case "ton":
        match convertion_unit:
            case "ton":
                print(f"\n\n\33[1mMass(ton) = {value_of_mass}")
            case "kg":
                print(f"\n\n\33[1mMass(kg) = {ton_to_kg}")
            case "lb":
                print(f"\n\n\33[1mMass(lb) = {ton_to_lb}")
            case "oz":
                print(f"\n\n\33[1mMass(oz) = {ton_to_oz}")
            case "g":
                print(f"\n\n\33[1mMass(g) = {ton_to_g}")
            case "CT":
                print(f"\n\n\33[1mMass(CT) = {ton_to_CT}")
            case "mg":
                print(f"\n\n\33[1mMass(mg) = {ton_to_mg}")

    case "kg":
        match convertion_unit:
            case "kg":
                print(f"\n\n\33[1mMass(kg) = {value_of_mass}")
            case "ton":
                print(f"\n\n\33[1mMass(ton) = {kg_to_ton}")
            case "lb":
                print(f"\n\n\33[1mMass(lb) = {kg_to_lb}")
            case "oz":
                print(f"\n\n\33[1mMass(oz) = {kg_to_oz}")
            case "g":
                print(f"\n\n\33[1mMass(g) = {kg_to_g}")
            case "CT":
                print(f"\n\n\33[1mMass(CT) = {kg_to_CT}")
            case "mg":
                print(f"\n\n\33[1mMass(mg) = {kg_to_mg}")

    case "lb":
        match convertion_unit:
            case "lb":
                print(f"\n\n\33[1mMass(lb) = {value_of_mass}")
            case "ton":
                print(f"\n\n\33[1mMass(ton) = {lb_to_ton}")
            case "kg":
                print(f"\n\n\33[1mMass(kg) = {lb_to_kg}")
            case "oz":
                print(f"\n\n\33[1mMass(oz) = {lb_to_oz}")
            case "g":
                print(f"\n\n\33[1mMass(g) = {lb_to_g}")
            case "CT":
                print(f"\n\n\33[1mMass(CT) = {lb_to_CT}")
            case "mg":
                print(f"\n\n\33[1mMass(mg) = {lb_to_mg}")

    case "oz":
        match convertion_unit:
            case "oz":
                print(f"\n\n\33[1mMass(oz) = {value_of_mass}")
            case "ton":
                print(f"\n\n\33[1mMass(ton) = {oz_to_ton}")
            case "kg":
                print(f"\n\n\33[1mMass(kg) = {oz_to_kg}")
            case "lb":
                print(f"\n\n\33[1mMass(lb) = {oz_to_lb}")
            case "g":
                print(f"\n\n\33[1mMass(g) = {oz_to_g}")
            case "CT":
                print(f"\n\n\33[1mMass(CT) = {oz_to_CT}")
            case "mg":
                print(f"\n\n\33[1mMass(mg) = {oz_to_mg}")

    case "g":
        match convertion_unit:
            case "g":
                print(f"\n\n\33[1mMass(g) = {value_of_mass}")
            case "ton":
                print(f"\n\n\33[1mMass(ton) = {g_to_ton}")
            case "kg":
                print(f"\n\n\33[1mMass(kg) = {g_to_kg}")
            case "lb":
                print(f"\n\n\33[1mMass(lb) = {g_to_lb}")
            case "oz":
                print(f"\n\n\33[1mMass(oz) = {g_to_oz}")
            case "CT":
                print(f"\n\n\33[1mMass(CT) = {g_to_CT}")
            case "mg":
                print(f"\n\n\33[1mMass(mg) = {g_to_mg}")

    case "CT":
        match convertion_unit:
            case "CT":
                print(f"\n\n\33[1mMass(CT) = {value_of_mass}")
            case "ton":
                print(f"\n\n\33[1mMass(ton) = {CT_to_ton}")
            case "kg":
                print(f"\n\n\33[1mMass(kg) = {CT_to_kg}")
            case "lb":
                print(f"\n\n\33[1mMass(lb) = {CT_to_lb}")
            case "oz":
                print(f"\n\n\33[1mMass(oz) = {CT_to_oz}")
            case "g":
                print(f"\n\n\33[1mMass(g) = {CT_to_g}")
            case "mg":
                print(f"\n\n\33[1mMass(mg) = {CT_to_mg}")

    case "mg":
        match convertion_unit:
            case "mg":
                print(f"\n\n\33[1mMass(mg) = {value_of_mass}")
            case "ton":
                print(f"\n\n\33[1mMass(ton) = {mg_to_ton}")
            case "kg":
                print(f"\n\n\33[1mMass(kg) = {mg_to_kg}")
            case "lb":
                print(f"\n\n\33[1mMass(lb) = {mg_to_lb}")
            case "oz":
                print(f"\n\n\33[1mMass(oz) = {mg_to_oz}")
            case "g":
                print(f"\n\n\33[1mMass(g) = {mg_to_g}")
            case "CT":
                print(f"\n\n\33[1mMass(CT) = {mg_to_CT}")