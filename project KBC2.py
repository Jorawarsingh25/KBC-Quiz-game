questions=[
['What is the national animal of India?','cow','got','monkey','tiger',4],
['Who is known as the "Father of the Nation" in India?','pandit jawaharlal neharu','mahatma ghandhi','sardarvallabh bhai patel','subhash chandra boss',2],
['What is the capital of India?','new delhi','mathura','gajiyabad','ajmer',1],
['Which river is considered the holiest in Hinduism and is also known as the Ganga?','yamuna','saraswati','ganga','mahi',3],
['What is the national flower of India?','gulab','kamal','suryamukhi','none',2],
['ho was the first Prime Minister of India?','dhirendra shastri','P.jawahar lal neharu','bhagat singh','mahatma ghandhi',2],
['What is the national currency of India?','doller','rupees','both of you','none',2],
['Which monument in India is also known as the "Symbol of Love"?','taj hotel','ram mandir','tajmahal','kutumbinar',3],
['What is the national sport of India?','cricket','hokey','football','kho kho',2],
['Which Indian festival is known as the Festival of Lights?','holi','sakranti','Diwali','ram navami',3]
]
levels=[1000,2000,4000,8000,14000,20000,40000,100000,240000,500000]
money=0
for i in range(len(questions)):
    question=questions[i]
    print(f'your question amount Rs.{levels[i]}')
    print(f'{question[0]}')
    print(f'A. {question[1]}                  B. {question[2]}')
    print(f'C. {question[3]}                  D. {question[4]}')
    
    user=int(input('enter your answer in option (1-4) and you are quit in 0: '))
    if user ==0:
        print('Your choose a 0 mean quit the game...')
        break
    if user==question[-1]:
        print(f'your answer is correct and you won a Rs{levels[i]}\n')

        if user==4:
            money=8000
        elif user==6:
            money=20000
        elif user==9:
            money=240000
        else:
            money +=levels[i]
            print(f'your current amout Rs{levels[i]}\n')
    else:
        print('Wrong Answer!!')
        break
    
print(f'your take home money {money}')