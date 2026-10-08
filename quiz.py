
questions = [
    {
        'question': 'What is the capital of Poland?', 
        'answer': 'Warsaw'
    },
    {
        'question': 'How many fingers are on a human hand?', 
        'answer': '10'
    },
    {
        'question': 'Who is the BASS GOD?', 
        'answer': 'Che'
    },
]

points = 0


for question in questions:
    print(f'Question: {question['question']}')
    user_input = input()
    if user_input.upper() == question['answer'].upper():
        print('You are absolutely right!')
        print(f'The answer is "{user_input}"')
        points += 1
    else:
        print('Unfortunately, you were wrong!')
        print(f'It\'s not "{user_input}" but "{question['answer']}"')

print(f'Your result is {points}/{len(questions)}')
