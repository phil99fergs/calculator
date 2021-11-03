#Varbutibu kalkulators
# Autors: X
# Datums: 03.11.2021 V2V

def statistiska():
    #Ja 𝑘 neatkarīgos mēģinājumos notikums 𝐴 iestājas 𝑚 reizes,
    # tad 𝑚 sauc par 𝐴 absolūto biežumu,
    # bet attiecību 𝑊(𝐴)=𝑚/𝑘 par notikuma 𝐴 relatīvo biežumu. Rezultātu izsaki procentos

    #lietotāja vertibu ievade
    # aprekins
    #izvade
    #Piemērs - 10 / 20. Relatīvais biežums būs 50%.
    a = float(input("Ievadiet [A notikuma] kopējo reižū skaitu: "))
    b = float(input("Ievadiet [A notikuma] cik reizes notika notikums?: "))
    x = b / a
    c = x * 100
    if a < 0:
        return print("Skaitlis nevar būt negatīvs,mēģiniet velreiz -> (Startejat kodu atkal)")
    elif b < 0:
        return print("Skaitlis nevar būt negatīvs,mēģiniet velreiz -> (Startejat kodu atkal)")

    print("Tātad, ka no" , a , "notikumu notiks" , b , "reizes ir : ")
    print("Tas ir jūsu absolūtais,relatīvais biežums: " , c , "%")


def geometriksa():
    #Šis varbūtību aprēķināšanas likums ir spēkā arī telpiskiem ķermeņiem.
    # Pieņemsim, ka telpā doti ģeometriski ķermeņi 𝐺 un 𝑔,
    # pie kam, ķermenis 𝐺 ietver sevī ķermeni 𝑔.
    # Uz labu laimi izvēlas punktu no ķermeņa 𝐺.
    # Varbūtība, ka izvēlētais punkts piederēs arī ķermenim 𝑔, ir 𝑃(𝐴)=𝑉(𝑔)/𝑉(𝐺)

    # lietotāja vertibu ievade
    # aprekins
    # izvade

    a = float(input("Ievadiet pirmā ķermeņa,figuras [G] laukumu(tikai skaitlis) : "))
    b = float(input("Ievadiet otrā ķermeņa,figuras [g] laukumu(tikai skaitlis): "))
    x = b / a
    c = x * 100


    if a < 0:
        return print("Skaitlis nevar būt negatīvs,mēģiniet velreiz. -> (Startejat kodu atkal)")
    elif b < 0:
        return print("Skaitlis nevar būt negatīvs,mēģiniet velreiz. -> (Startejat kodu atkal)")
    elif a == b:
        return print("Skaitļi nevar būt vienādi,mēģiniet velreiz. -> (Startejat kodu atkal)")


    print("Tā ir varbūtība, ka izvēlētais punkts piederēs arī kermenim,figurai [g] : ", c, "%")



def klasiska():
    #P(A) = (labvēlīgo notikumu skaits) / (visu notikumu kopskaits)

    # lietotāja vertibu ievade
    # aprekins
    # izvade

    a = float(input("Ievadiet labvēlīgo notikumu skaitu: "))
    b = float(input("Ievadiet visu notikumu kopskaitu: "))
    x = a / b
    c = x * 100

    if a < 0:
        return print("Skaitlis nevar būt negatīvs,mēģiniet velreiz -> (Startejat kodu atkal)")
    elif b < 0:
        return print("Skaitlis nevar būt negatīvs,mēģiniet velreiz -> (Startejat kodu atkal)")

    print("Tātad, ka no", b, "notikumu var notikt", a, "reizes ir :", c, "%")

    print("Pagaidām atbildi var iegūt tikai %, strādājam pie tā.")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choice = input("Kada veida varbutibas aprekini Tev sodien padoma? \n"
                   "Ievadi burtu:\n-K klasiska metode n no n\n"
                   "-G geometriksa varbutiba\n"
                   "-S statiska varbutiba k m reizes\n")
    if choice.lower() == 'k':
        klasiska()
    if choice.lower() == 'g':
        geometriksa()
    if choice.lower() == 's':
        statistiska()
    else:
        exit(0)
