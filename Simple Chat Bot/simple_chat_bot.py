def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    question = "What does the keyword return do?"
    print(question)
    answers = ["1. after the function call, it returns all the arguments",
               "2. return invokes the function",
               "3. return stops the function execution and/or sends back "
               "a value resulted from the function call"]
    counter = 0
    while counter < len(answers):
        print(answers[counter])
        counter += 1
    right_answer = 3
    user_answer = int(input())
    while user_answer != right_answer:
        print("Please, try again.")
        user_answer = int(input())


def end():
    print('Congratulations, have a nice day!')


greet('Ball', '2024')  
remind_name()
guess_age()
count()
test()
end()
