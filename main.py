# One Stop Insurance Company needs a program to enter and
# calculate new insurance policy information for its customers.
# Author: A F Singleton. Start: 2022-11-22 End:

#############################################################
# This file Calls Functions from other files to do the work
# for him & he displays a menu
#############################################################
# IMPORTS
import datetime

#############################################################
# DEFAULT VALUES LIST
DATE = datetime.datetime.now().strftime("%Y-%m-%d")
file = open('OSICDef.dat', 'r')  # open file
defVals = []  # initialize list for default vals
line = file.readline()  # read the first line of file
while line != '':  # this loop appends the file's line contents until one returns a blank
    defVals.append(line.strip())
    line = file.readline()
file.close()  # close file. variable file now unassigned
DATE = datetime.datetime.now().strftime("%Y-%m-%d")


#############################################################
# FUNCTIONS
def Receipt():
    # begin display.
    # Defaults
    XTR_LBLTY_CVRG = defVals[3]
    GLASS_CVRG = defVals[4]
    LONR_CAR_CVRG = defVals[5]
    PRCSSNG_FEE = defVals[7]  # The Processing Fee for Monthly Payments

    # open costs file and copy values
    file = open('OSICCosts.dat', 'r')
    line = file.readline()
    COSTS = []
    POLNUMS = []
    while line != "":
        COSTS.append(line.split(','))
        POLNUMS.append(COSTS[-1][0])
        line = file.readline()
    file.close()

    # open policy file and copy values
    file = open('OSICPolicy.dat', 'r')
    line = file.readline()
    POLICYS = []
    while line != "":
        POLICYS.append(line.split(','))
        line = file.readline()
    file.close()

    # display stored policies
    run = True
    while run:
        if not len(POLICYS) > 0:
            print('')
            input('There are no Policyies to display. press enter to continue...')
            print('')
            break
        else:
            print(f"""
        {'One Stop Insurance Comp.':^80}
        {'Policies stored on hand':<40}{f'Date: {DATE}':>40}
{"Pol."}    {'    '}    {'extra':^11}         {'Glass':^8}     {'Loaner'}      {'Payment':^12}        {'Date':^7}
{"Num."}    {'cars'}    {'liabilities'}         {'coverage'}     {'car':^6}     {'Schedule':^12}        {'Entered'}  
        ================================================================================""")
            for policy in POLICYS:
                print(f'{policy[0]}    {policy[9]:^4}    {policy[10]:^12}        {policy[11]:^8}     {policy[12]:^6}      {policy[13].strip():^12}     {policy[8]:>10}')
            print('        ================================================================================')
            input("        End of File. Press Enter to continue...")
            print('')

            # which policy does the user want to print?
            # assign the index based on the policy number
            # find the corresponding index value to math policies to policy costs
            while True:
                PolNum = input("Which policy would you like to print (enter policy number): ")
                if len(PolNum) != 4:
                    print("Policy number is a four digit code. ex 1944 - please re-enter value")
                elif not set(PolNum).issubset('1234567890'):
                    print("Invalid characters used in policy number - please re-enter.")
                else:
                    for IDS in POLNUMS:
                        if IDS == PolNum:
                            PASS = True
                            break
                        else:
                            PASS = False
                    if not PASS:
                        input("Enter valid Policy ID from table - press enter to continue...")
                        print("")
                        break
                    else:
                        # use Policy Number to identify which list the policy we want to print is in
                        for Index in range(len(POLICYS)):
                            ID = POLICYS[Index][0]
                            if ID == PolNum:
                                INDEX = Index
                                break
                            else:
                                continue

                        # print receipt
                        print(f"""
        {'One Stop Insurance Comp.':^45}
        {'Receipt of Transaction':<22}{f'Issued: {POLICYS[INDEX][8]}':>23}
        =============================================
        Customer {f'{POLICYS[INDEX][1][0]}. {POLICYS[INDEX][2]}':<35}
                 {POLICYS[INDEX][3]:^14}
                 {POLICYS[INDEX][4]:^14}, {POLICYS[INDEX][5]:2} {POLICYS[INDEX][6]:7}
                 {POLICYS[INDEX][7]:<12}
        =============================================
        Policy {POLICYS[INDEX][0]+'-'+POLICYS[INDEX][1][0]+POLICYS[INDEX][2][0]:^7}                           Per
        Number of cars on policy: {POLICYS[INDEX][9]:}             Car $""")
                    # Extra liabilities
                    if POLICYS[INDEX][10] == '0.0':
                        print(f"            Extra Liability:  No ----------- {f'${float(XTR_LBLTY_CVRG):,.2f}':>8}")
                    else:
                        print(f"            Extra Liability: Yes ----------- {f'${float(XTR_LBLTY_CVRG):,.2f}':>8}")
                        print(f"            Up to: {POLICYS[INDEX][10]:<11}")

                    # Glass Coverage
                    if POLICYS[INDEX][11] == "Y":
                        print(f"            Glass Coverage: Yes ------------ {f'${float(GLASS_CVRG):,.2f}':>8}")
                    else:
                        print(f"            Glass Coverage:  No ------------ {f'${float(GLASS_CVRG):,.2f}':>8}")

                    # loaner Car
                    if POLICYS[INDEX][12] == "Y":
                        print(f"            Loaner Car: Yes ---------------- {f'${float(LONR_CAR_CVRG):.2f}' :>8}")
                    else:
                        print(f"            Loaner Car:  No ---------------- {f'${float(LONR_CAR_CVRG):.2f}' :>8}")

                    # print total
                    if str(POLICYS[INDEX][-1]).strip() == "M":
                        print(f"            Processing fee ----------------- {f'${float(PRCSSNG_FEE):.2f}' :>8}")
                        print(f"    {f'payment schedule: Monthly':^45}")
                        print(f'    {f"Monthly payment: ${float(COSTS[INDEX][-3]):,.2f}":^45}')
                    else:
                        print(f"     {f'payment schedule:    Full':^45}")
                    print(f"""        =============================================
        Transaction
        
            Premium
            Premium First Car ------------ {f'${float(COSTS[INDEX][1]):,.2f}':>10}
            Premium Additional Cars ------ {f'${float(COSTS[INDEX][-6]):,.2f}':>10}
            Total Premium Charge --------- {f'${float(COSTS[INDEX][-5]):,.2f}':>10}
            
            Additional options
            Extra Liability Charge ------- {f'${float(COSTS[INDEX][2]):,.2f}':>10}
            Glass Coverage Charge -------- {f'${float(COSTS[INDEX][3]):,.2f}':>10}
            Loaner car Coverage Charge --- {f'${float(COSTS[INDEX][4]):,.2f}':>10}
            Additional options total ----- {f'${float(COSTS[INDEX][-4]):,.2f}':>10}
            -------------------------------------
            Total before HST ------------- {f'${float(COSTS[INDEX][-2]):,.2f}':>10}
                                          -----------
            HST -------------------------- {f'${float(COSTS[INDEX][-1]):,.2f}':>10}
            -------------------------------------
            Total after HST -------------- {f'${float(COSTS[INDEX][-2].strip("$"))+float(COSTS[INDEX][-1]):,.2f}':>10}
        =============================================
                Thanks for Trusting OSIC """)



                    # Closing
                    print("")
                    input("Press Enter to continue...")
                    print("")

                    while True:
                        tmp = input('print another receipt (Y/N): ').upper()
                        if not set(tmp).issubset("YN"):
                            print("Invalid character. Use Y or N - please re-enter")
                        elif len(tmp) != 1:
                            print("Input must only be one character Y or N - please re-enter")
                        else:
                            break
                    if tmp == 'Y':
                        pass
                    else:
                        run = False
                        break
                break

# creates datafiles for policy & policy costs
def CreatePolicy():

    # Default values
    POLICY_NUMBER = defVals[0]  # Policy Number
    BASIC_PREMIUM = defVals[1]  # Basic Premium Charge
    DSCNT_4_ADD_CAR = defVals[2]  # Discount For Adding additional cars to policy
    XTR_LBLTY_CVRG = defVals[3]  # Extra Liabilities Coverage charge
    XTR_LBLTY_LMT = 1000000.00  # Limit for XTR_LBLTY_CVRG
    GLASS_CVRG = defVals[4]  # The Cost Of Glass Coverage
    LONR_CAR_CVRG = defVals[5]  # Loner Car Coverage (loaning your car to someone else?).
    HST_RATE = defVals[6]  # Tax Rate. Not Tax Total
    PRCSSNG_FEE = defVals[7]  # The Processing Fee for Monthly Payments

    #Main loop
    run = True
    while run:

        # Customer Information
        # Name
        # first and program Shutdown.
        while True:
            # validate first name
            frstName = input('First Name ("End" to stop entering policies): ').title()
            if frstName == "":
                print("First name cannot be blank - please re-enter.")
            elif not set(frstName).issubset("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'"):
                print("First Name contains invalid characters - please re-enter")
            elif frstName == "End":
                # run becomes false and program shuts down if triggered.
                run = False
                break
            else:
                break

        if not run:
            break
        else:
            pass

        # last
        while True:
            # validate Last name
            lstName = input('Last Name: ').title()
            if lstName == "":
                print("Last name cannot be blank - please re-enter.")
            elif not set(lstName).issubset("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'"):
                print("Last Name contains invalid characters - please re-enter")
            else:
                break

        # Address
        while True:
            addrss = input("Address: ")
            if addrss == "":
                print("Address cannot be left blank - Please re-enter")
            elif not set(addrss).issubset("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890,'-."):
                print("Address contains invalid characters. - please re-enter ")
            else:
                break

        # City
        while True:
            city = input("City: ")
            if city == "":
                print("City cannot be left blank - Please re-enter")
            elif not set(city).issubset("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,'-."):
                print("City contains invalid characters. - please re-enter ")
            else:
                break

        # Province
        while True:
            prvnc = input("Province(ex AB for alberta): ").upper()
            if prvnc == "":
                print("Province cannot be left blank - Please re-enter")
            elif len(prvnc) != 2:
                print("Province must be a two character representation - please re-enter")
            elif not set(prvnc).issubset("ABCDEFGHIJKLMONPQRSTUVWXYZ"):
                print("Province contains invalid characters. - please re-enter ")
            else:
                break

        # Postal Code
        while True:
            postCode = input("Postal Code format A1A 3B6: ")
            if len(postCode) != 7:
                error = "Postal code invalid length."
                print(error, "format A1A 3B6 - please re-enter")
            elif postCode[3] != " ":
                print("postal code invalid format. format A1A 3B6 - please re-enter")
            else:
                num = [postCode[1], postCode[4], postCode[6]]
                let = [postCode[0], postCode[2], postCode[5]]
                PASS = ''
                for i in range(3):
                    if not num[i].isdigit():
                        print("postal code invalid Character. format A1A 3B6 - please re-enter")
                        PASS = False
                        break
                    elif not let[i].isalpha():
                        print("postal code invalid Character. format A1A 3B6 - please re-enter")
                        PASS = False
                        break
                    else:
                        PASS = True
                        continue
                if PASS:
                    postCode = f"{postCode[0].upper()}{postCode[1]}{postCode[2].upper()}-{postCode[4]}{postCode[5].upper()}{postCode[6]}"
                    break
                else:
                    continue

        # Phone Number
        # stored in order as a list of length 3.
        while True:
            temp = input("Customer phone number format 123 456-7890: ")
            customerPhNum = temp.split()  # split by space
            if not len(temp) == 12:
                print('Invalid length - please re-input in format "123 456-7890"')
            elif not temp[3] == " ":
                print('Needs space as fourth character - please re-input in format "123 456-7890"')
            elif not temp[7] == "-":
                print('Needs "-" as seventh character - please re-input in format "123 456-7890"')
            elif temp == "":
                print('Phone cannot be blank - please re-input in format "123 456-7890"')
            elif not len(customerPhNum) > 1:
                print('Invalid input - please re-input in format "123 456-7890"')
            else:  # check number only contains numbers
                # split XXX-XXXX into ['XXX','XXXX']
                temp = customerPhNum.pop(1)
                customerPhNum.append(temp.split("-")[0])
                customerPhNum.append(temp.split("-")[1])
                for index in range(len(customerPhNum)):
                    if not set(customerPhNum[index]).issubset("1234567890"):
                        print('Phone number must only contain digits - please re-input in format "000 000-0000"')
                        break
                    elif index == 2:
                        break
                Phone = str(customerPhNum[0]).strip() + " " + str(customerPhNum[1]).strip() + "-" + str(customerPhNum[2]).strip()
                break


        # Policy Information
        # Number of cars
        while True:
            try:
                cars = int(input("Number of cars on policy: "))
            except:
                print("Cars on policy must be a valid integer Ex. 2 - please re-enter value.")
            else:
                break

        # Option for extra liability (up to limit)
        while True:
            tmp = input("Extra Liability (Y/N): ").upper()
            if not set(tmp).issubset("YN"):
                print("Invalid character. Use Y or N - please re-enter")
            elif len(tmp) != 1:
                print("Input must only be one character Y or N - please re-enter")
            elif tmp == 'Y':
                while True:
                    try:
                        xtraLiabilityCovered = float(input("Extra Liability amount: "))
                    except:
                        print("Extra liability amount must be a number - please re-enter")
                    else:
                        if xtraLiabilityCovered > XTR_LBLTY_LMT:
                            print(f"Amount exceeds limit. must be under {XTR_LBLTY_LMT}. - please re-enter")
                        else:
                            break
                break
            else:
                xtraLiabilityCovered = 0.0
                break

        # glass coverage
        while True:
            tmp = input("Glass Coverage (Y/N): ").upper()
            if not set(tmp).issubset("YN"):
                print("Invalid character. Use Y or N - please re-enter")
            elif len(tmp) != 1:
                print("Input must only be one character Y or N - please re-enter")
            else:
                glssCoverage = tmp
                break

        # loaner car option
        while True:
            tmp = input("Loaner Car (Y/N): ").upper()
            if not set(tmp).issubset("YN"):
                print("Invalid character. Use Y or N - please re-enter")
            elif len(tmp) != 1:
                print("Input must only be one character Y or N - please re-enter")
            else:
                loanerCar = tmp
                break

        # pay in full or monthly
        while True:
            tmp = input("Pay monthly or in full (M/F): ").upper()
            if not set(tmp).issubset("FM"):
                print("Invalid character. use F or M - please re-enter")
            elif len(tmp) != 1:
                print("Input must only be one character F or M - please re-enter")
            else:
                paymntSchdl = tmp
                break

        # Store Policy data
        file = open('OSICPolicy.dat', 'a')
        file.write(
            f"{POLICY_NUMBER},{frstName},{lstName},{addrss},{city},{prvnc},{postCode},{Phone},{DATE},{cars},"
            f"{'${:.2f}'.format(xtraLiabilityCovered)},{glssCoverage},{loanerCar},{paymntSchdl}\n")
        file.close()

        ####################################################
            # CALCULATIONS & UPDATING FILES
        ####################################################
        # create policy cost data
        premTotal = 0.0
        addOptnTotal = 0.0

        # cars
        discount = (float(BASIC_PREMIUM)*(float(DSCNT_4_ADD_CAR)))
        addCarCost = float(BASIC_PREMIUM) - discount
        CarCost = float(BASIC_PREMIUM)
        CarTotalCost = CarCost+((int(cars)-1) * addCarCost)
        if not cars > 1:                    # only one car
            premTotal += CarCost
        else:                               # more than one car
            premTotal += CarTotalCost

        # extra liabilities
        if xtraLiabilityCovered > 0.0:
            xtraLiabilityCost = float(XTR_LBLTY_CVRG) * cars
            addOptnTotal += xtraLiabilityCost
        else:
            xtraLiabilityCost = 0.0
            pass

        # Glass Coverage
        if glssCoverage == 'Y':
            glassCost = float(GLASS_CVRG) * cars
            addOptnTotal += glassCost
        else:
            glassCost = 0.0
            pass

        # Loaner car
        if loanerCar == 'Y':
            loanerCost = float(LONR_CAR_CVRG) * cars
            addOptnTotal += loanerCost
        else:
            loanerCost = 0.0
            pass

        # Total Cost of policy before tax
        TOTAL = addOptnTotal + premTotal

        # HST
        HST = TOTAL * float(HST_RATE)

        # monthly payment
        monthlyCost = (TOTAL + float(PRCSSNG_FEE)) / 8   # eight monthly payments

        # Store Costs Data
        file = open('OSICCosts.dat', 'a')
        file.write(f"{POLICY_NUMBER},{'{:.2f}'.format(CarCost)},{'{:.2f}'.format(xtraLiabilityCost)},"
                   f"{'{:.2f}'.format(glassCost)},{'{:.2f}'.format(loanerCost)},{'{:.2f}'.format(CarTotalCost)},"
                   f"{'{:.2f}'.format(addCarCost)},{'{:.2f}'.format(premTotal)},{'{:.2f}'.format(addOptnTotal)},"
                   f"{'{:.2f}'.format(monthlyCost)},{'{:.2f}'.format(TOTAL)},{'{:.2f}'.format(HST)}\n")
        file.close()

        # update Policy number
        POLICY_NUMBER = str(int(POLICY_NUMBER) + 1)

        # UPDATING DEFAULT VALUES
        file = open('OSICDef.dat', 'w')
        file.write(f"{POLICY_NUMBER}\n")
        file.write(f"{BASIC_PREMIUM}\n")
        file.write(f"{DSCNT_4_ADD_CAR}\n")
        file.write(f"{XTR_LBLTY_CVRG}\n")
        file.write(f"{GLASS_CVRG}\n")
        file.write(f"{LONR_CAR_CVRG}\n")
        file.write(f"{HST_RATE}\n")
        file.write(f"{PRCSSNG_FEE}\n")
        file.close()

        input(f"Policy & Customer Data Saved for {frstName[0]} {lstName}. Press enter to continue...")


#############################################################
# PROCESS
while True:
    print("""
    Hello, Welcome to the OSIC database.
    Functions we offer: 
    1. Create Policies
    2. Display a Policy Receipt
    3. Exit Program""")

    tmp = input("Enter the numerical value associated with your choice: ")
    if not set(tmp).issubset("123"):
        print("Invalid input - please re-enter")
    elif len(tmp) != 1:
        print('Input must be One character - please re-enter')
    else:
        if tmp == '1':
            CreatePolicy()

        elif tmp == '2':
            Receipt()

        else:
            break

input("Program closing, thank you for using OSIC. Press Enter to continue...")