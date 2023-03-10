from final_checkbook_functions import *



def run_atm():
    inquiry = True
    while inquiry:
        question = input("What would you like to do? \n\n"
                         "1) View current balance\n"
                         "2) Record a debit (withdraw)\n"
                         "3) Record a credit (deposit)\n"
                         "4) More options\n"
                         "5) exit\n")
        if question == '1':
            clear_terminal()
            view()
        elif question == '2':
            balance = get_balance()
            clear_terminal()
            if balance == "0.00" or balance == '0.0':
                print(f"You can't withdraw with a balance of: {balance}\n")
            else:
                descript = description("Withdraw")
                amount = input("How much would you like to withdraw? ")
                if check_input(amount):
                    withdraw(float(amount), descript)
                else:
                    clear_terminal()
                    print("Please put input a number\n")
        elif question == '3':
            clear_terminal()
            descript = description("Deposit")
            amount = (input("How much would you like to deposit? "))
            if check_input(amount):
                deposit(float(amount), descript)
            else:
                clear_terminal()
                print("Please put input a number\n")

        elif question == '4':
            clear_terminal()
            more = more_options()
            if more == "1":
                clear_terminal()
                get_history()
            elif more == "2":
                search("Deposit")
            elif more == "3":
                search("Withdraw")
            elif more == "4":
                search("date")
            else:
                print('Not a valid option\n')
        elif question == '5':
            clear_terminal()
            inquiry = exit_checkbook()
        else:
            clear_terminal()
            print("Not a valid option, please try again")
            pass


run_atm()
