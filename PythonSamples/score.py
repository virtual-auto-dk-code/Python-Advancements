print("--------------------------------------------------------------------")
print("--- Grace Score Program ---")
print("--------------------------------------------------------------------")
print("--- Provide Original Score ---")
ise = int(input("Enter ISE :"))      # 0 Pass
ese = int(input("Enter ESE :"))      # 20 Pass
total = ise + ese   # Original Total
print("--------------------------------------------------------------------")
print("--- Given Original Score ---")
print("Given ISE : " + str(ise))
print("Given ESE : " + str(ese))
print("Given ISE + ESE as Original Total : " + str(total))
print("--------------------------------------------------------------------")

ese_grace = 0
total_grace = 0

revised_ese = 0
revised_total = 0

if (17 <= ese < 20) and total >= 40:    # ESE Failed in 17 to 20 but Total above 40
    ese_grace = 20 - ese
    revised_ese = ese + ese_grace
    revised_total = ise + revised_ese
    total = revised_total
    print("Failed in ESE and Total more than 40 hence ESE Grace given ... ")
    print("ESE Grace : " + str(ese_grace))
    print("Revised ESE : " + str(revised_ese))
    print("Revised Total : " + str(total))
elif ese >= 20 and (37 <= total < 40): # ESE Passed but Total Failed in 37 to 40
    total_grace = 40 - total
    revised_ese = ese + total_grace
    revised_total = ise + revised_ese
    total = revised_total
    print("Failed in Total and ESE more than 20 hence added grace to ESE ... ")
    print("Total Grace : " + str(total_grace))
    print("Revised ESE : " + str(revised_ese))
    print("Revised Total : " + str(total))
elif (17 <= ese < 20) and (37 <= total < 40): # ESE Failed in 17 to 20 and also Total Failed in 37 to 40
    ese_grace = 20 - ese
    revised_ese = ese + ese_grace
    revised_total = ise + revised_ese
    total = revised_total
    print("Failed in Total and ESE hence added grace to ESE ... ")
    print("ESE Grace : " + str(ese_grace))
    print("Total Grace : " + str(total_grace))
    print("Revised ESE : " + str(revised_ese))
    print("Revised Total : " + str(total))
else:                                       # No condition of Grace
    print("No Grace condition identified ... Hence Original Score is ...")
    print("ISE : " + str(ise))
    print("ESE : " + str(ese))
    print("ISE + ESE as Original Total : " + str(total))

print("--------------------------------------------------------------------")
