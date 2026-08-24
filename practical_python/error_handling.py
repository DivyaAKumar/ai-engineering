try:
    user_input = input("Enter a positive number: ")

    number = int(user_input)

    if number <= 0:
        raise ValueError("Number must be positive.")

    result = 100 / number

except ValueError as e:
        if not user_input.lstrip("-").isdigit():
            print(f'Invalid number: "{user_input}" is not a number')
        else:
            print(f"Invalid number: {e}")


except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Execution finished.")
#raise- to create a exception


class InsufficientBalanceError(Exception):

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        super().__init__(
            f"Your balance is {balance}, and the amount requested for withdrawal is {amount}."
        )


def withdraw(balance: float, amount: float) -> float:

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    if amount > balance:
        raise InsufficientBalanceError(balance, amount)

    return balance - amount


try:
    balance = 1000
    amount = 1500

    new_balance = withdraw(balance, amount)

except InsufficientBalanceError as e:
    print(f"Transaction failed: {e}")

except ValueError as e:
    print(f"Invalid input: {e}")

else:
    print(f"New balance: {new_balance}")

finally:
    print("Transaction process completed.")