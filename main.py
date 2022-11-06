print("Choose equation:\n(1) E_osc^anh = ṽ_e(v+1/2)-xṽ_e(v+1/2)^2\n(2) ΔE_osc^anh = ṽ_e[1-2x(v+1)]"
      "\nx-anharmonicity coefficient\nṽ_e-equilibrium value of oscillations\nv[1/s], ṽ_e-[1/cm], ΔE_osc^anh-[1/cm] E_osc^anh-[1/cm]")
choose = int(input("Type 1 or 2: "))

if choose == 1:
    print("what value you want to find: 1.(E_osc^anh), 2.(ṽ_e), 3.(v), 4.(x)")
    choose_value = int(input("Type 1, 2, 3 or 4: "))
    if choose_value == 1:
        v_e = float(input("insert value of ṽ_e: "))
        v = float(input("insert value of v: "))
        x = float(input("insert value of x: "))
        equal = v_e * (v + 1/2)-x*v_e*(v+1/2)**2
        print("E_osc ^ anh = "+str(equal))
    elif choose_value == 2:
        E_osc = float(input("insert value of E_osc ^ anh: "))
        v = float(input("insert value of v: "))
        x = float(input("insert value of x: "))
        equal = E_osc/((v+1/2)-x*(v+1/2)**2)
        print("ṽ_e = " + str(equal))
    elif choose_value == 3:
        E_osc = float(input("insert value of E_osc ^ anh: "))
        v_e = float(input("insert value of ṽ_e: "))
        x = float(input("insert value of x: "))
        equal_1 = -((v_e*x-v_e)+((v_e-v_e*x)**2+4*v_e*x*(v_e/2-v_e*x/4))**(1/2))/(2*v_e*x)
        equal_2 = -((v_e*x-v_e)-((v_e-v_e*x)**2+4*v_e*x*(v_e/2-v_e*x/4))**(1/2))/(2*v_e*x)
        print("v = " + str(equal_1)+" or "+str(equal_2))
    elif choose_value == 4:
        E_osc = float(input("insert value of E_osc ^ anh: "))
        v = float(input("insert value of v: "))
        v_e = float(input("insert value of v_e: "))
        equal = (v_e*(v+1/2)-E_osc)/(v_e*(v+1/2)**2)
        print("x = " + str(equal))
    else:
        print("choose valid value")
        pass

elif choose == 2:
    print("what value you want to find: 1.(ΔE_osc^anh), 2.(ṽ_e), 3.(v), 4.(x)")
    choose_value = int(input("Type 1, 2, 3 or 4: "))
    if choose_value == 1:
        v_e = float(input("insert value of ṽ_e: "))
        v = float(input("insert value of v: "))
        x = float(input("insert value of x: "))
        equal = v_e*(1-2*x*(v+1))
        print("ΔE_osc^anh = " + str(equal))
    elif choose_value == 2:
        E_osc = float(input("insert value of E_osc ^ anh: "))
        v = float(input("insert value of v: "))
        x = float(input("insert value of x: "))
        equal = E_osc/(1-2*x*(v+1))
        print("ṽ_e = " + str(equal))
    elif choose_value == 3:
        E_osc = float(input("insert value of E_osc ^ anh: "))
        v_e = float(input("insert value of ṽ_e: "))
        x = float(input("insert value of x: "))
        equal = (E_osc - v_e +2*x*v_e) /(-2*x*v_e)
        print("v = " + str(equal))
    elif choose_value == 4:
        E_osc = float(input("insert value of E_osc ^ anh: "))
        v = float(input("insert value of v: "))
        v_e = float(input("insert value of v_e: "))
        equal = (E_osc-v_e)/(-2*v_e*(v+1))
        print("x = " + str(equal))
    else:
        print("choose valid value")
        pass

else:
    print("give valid value")