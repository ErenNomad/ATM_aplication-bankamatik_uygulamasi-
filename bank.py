#ATM application
user1_account = {
    'name' : 'user1Name user1Surname',
    'accountNum' : '12345',
    'balance' : 5000,
    'adAccount' : 3000
}
user2_account = {
    'name' : 'user2Name user2Surname',
    'accountNum' : '31621',
    'balance' : 5000,
    'adAccount' : 500
}
user3_account = {
    'name':'user3Name user3Surname',
    'accountNum': '69310',
    'balance': 200,
    'adAccount': 600
}
def withdrawMoney(account,amount):
    print(f"Hoşgeldiniz {account['name']} ")
    if (account['balance']>= amount):
        newBalance = account['balance']-amount
        print(f"Paranızı alabilirsiniz.\nKalan bakiyeniz\n-Ana hesapta {newBalance}TL\t-Ek hesap limitiniz ise {account['adAccount']}TL")
    else:
        total = account['balance']+ account['adAccount']
        if total >= amount :
            adAccountUsing = input("Ek hesap kullanılsın mı ?(e/h)")
            if adAccountUsing == "e":
                availableBalance = total-int(amount)
                print(f"Paranızı alabilirsiniz kalan bakiyeniz {total}TL dir")
            else:
                print(f"Sayın {account['name']} {account['accountNum']} nolu hesabınızda {account['balance']}TL bulunmaktadır ve "
                      f"ek limitiniz ise {account['adAccount']}TL dir ")
        else:
            print("Üzgününüz bakiyeniz yetersiz")


withdrawMoney(user1_account,300)
print(70*'-')
withdrawMoney(user2_account,5000)
print(70*'-')
withdrawMoney(user3_account,250)
