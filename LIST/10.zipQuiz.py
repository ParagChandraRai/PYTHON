questions = ['What is the capital of France?', 'What is the currency of Japan?', 'What is the largest desert in the world?']
answers = ['Paris', 'Yen', 'Sahara']

for question, answer in zip(questions, answers):
    response = input(f"{question}: ")
    if response.strip().lower() == answer.lower():
        print("Correct!")
    else:
        print(f"Incorrect! The answer is {answer}")
