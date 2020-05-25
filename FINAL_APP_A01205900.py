from tkinter import *
import os
from math import exp
from tkinter import messagebox


root = Tk()
root.title('COUPLES COUNSELING QUIZ A01205900')
root.geometry("650x800")



Label(root,text='PLEASE READ THE INSTRUCTIONS VERY CAREFULLY').pack()
Label(root,text='Answer the following 54 questions using a scale of numbers from 0 to 4').pack()
Label(root,text='"0" being I TOTALLY DISAGREE and "4 being I TOTALLY AGREE"').pack()
Label(root,text='Insert your answers in the space below WITHOUT ANY SPACES then click "GET RESULTS" button').pack()
Label(root,text='Example of how your answer MUST be written: 000122341110000212330011').pack()
Label(root,text='Please make sure you write all 54 numbers to get an accurate result').pack()
Label(root,text='To start the quiz click the "START TEST" button (you can scroll down to see all the questions)').pack()
Label(root,text='Example of how your answer MUST be written: 000122341110000212330011').pack()

questionaire = ['1. If one of us apologizes when our discussion deteriorates, the discussion ends ',
'2. I know we can ignore our differences, even if things get hard sometimes ',
'3. When we need it, we can take our discussions with my spouse from the beginning and correct it ',
'4. When I discuss with my spouse, to contact him will eventually work ',
'5. The time I spent with my wife is special for us ',
'6. We dont have time at home as partners',
'7. We are like two strangers who share the same environment at home rather than family ',
'8. I enjoy our holidays with my wife',
'9. I enjoy traveling with my wife',
'10. Most of our goals are common to my spouse. ',
'11. I think that one day in the future, when I look back, I see that my spouse and I have been in harmony with each other. ',
'12. My spouse and I have similar values in terms of personal freedom. ',
'13. My spouse and I have similar sense of entertainment. ',
'14. Most of our goals for people children, friends, etc., are the same. ',
'15. Our dreams with my spouse are similar and harmonious. ',
'16. We are compatible with my spouse about what love should be. ',
'17. We share the same views about being happy in our life with my spouse ',
'18. My spouse and I have similar ideas about how marriage should be ',
'19. My spouse and I have similar ideas about how roles should be in marriage ',
'20. My spouse and I have similar values in trust. ',
'21. I know exactly what my wife likes. ',
'22. I know how my spouse wants to be taken care of when she/he sick. ',
'23. I know my spouses favorite food. ',
'24. I can tell you what kind of stress my spouse is facing in her/his life. ',
'25. I have knowledge of my spouses inner world. ',
'26. I know my spouses basic anxieties. ',
'27. I know what my spouses current sources of stress are. ',
'28. I know my spouses hopes and wishes. ',
'29. I know my spouse very well. ',
'30. I know my spouses friends and their social relationships. ',
'31. I feel aggressive when I argue with my spouse. ',
'32. When discussing with my spouse, I usually use expressions such as ‘you always’ or ‘you never’ . ',
'33. I can use negative statements about my spouses personality during our discussions. ',
'34. I can use offensive expressions during our discussions. ', 
'35. I can insult my spouse during our discussions.',
'36. I can be humiliating when we discussions. ',
'37. My discussion with my spouse is not calm. ',
'38. I hate my spouses way of open a subject. ',
'39. Our discussions often occur suddenly. ',
'40. We are just starting a discussion before I know whats going on. ',
'41. When I talk to my spouse about something, my calm suddenly breaks. ',
'42. When I argue with my spouse, ı only go out and I dont say a word. ', 
'43. I mostly stay silent to calm the environment a little bit. ',
'44. Sometimes I think its good for me to leave home for a while. ',
'45. I would rather stay silent than discuss with my spouse. ',
'46. Even if I am right in the discussion, I stay silent to hurt my spouse. ',
'47. When I discuss with my spouse, I stay silent because I am afraid of not being able to control my anger. ',
'48. I feel right in our discussions. ',
'49. I have nothing to do with what Ihave been accused of. ',
'50. I am not actually the one who is guilty about what I am accused of. ',
'51. I am not the one who is wrong about problems at home. ',
'52. I would not hesitate to tell my spouse about her/his inadequacy. ',
'53. When I discuss, I remind my spouse of her/his inadequacy. ',
'54. I am not afraid to tell my spouse about her/his incompetence. ']


def start():
    question=Text(root)
    for i in questionaire:
        question.insert(END,i+'\n')
        question.pack()
      
        
def exitest():
    root.destroy()
sbutton = Button(root,text="START TEST",command=start).pack(pady=10)


    
e = Entry(root,width=54)
e.pack()  
global result
global data
data = []
def next():
    for _ in range(1):
        num = e.get()
        lab = Label(root,text='Your answers were:'+ num)
        lab.pack()
        datalist = map(int,num)
        data = list(datalist)
        e.delete(0,END)
        print(data)
        resultweights = [-0.4116168406477664, 0.16127135722674943, 0.09392306875528937, 0.08618336486073931, 0.15152198981452428, 0.112703007177662, 0.09959435925096392, 0.046355238009921, 0.07832970277182749, 0.1836059310339804, -0.24645953615853497, 0.20736758532548907, -0.09141524522943613, -0.33106967241217106, 0.20042007088344801, 0.07067972542319356, 0.11203971486413962, 0.1513019592977353, 0.249451549661633, 0.21923144895804722, 0.3024432014526723, 0.06627392598204146, -0.02249979099215653, 0.040515874905737055, -0.10073100325790932, -0.008230154392166785, 0.29973765817792886, 0.07517029761985991, 0.30134673260176326, 0.2496979705662934, 0.23966672815913084, 0.0035239384305774967, -0.058214625848810424, 0.1320518147992346, 0.01833260356721795, 0.12684862249311699, 0.3399070197900843, -0.125114022801525, 0.14989888969506993, 0.25294460479916175, 0.5965257732108006, 0.08870670902543579, 0.009971131483531721, -0.36162818986095663, 0.2805272368921549, -0.31313838310813547, -0.2678994086095123, -0.14067947785693713, -0.49842841526547793, 0.13607361389923087, -0.09895543666501327, -0.4526281227044454, 0.06730245486533827, -0.0755428416317035, -0.14057230786197902]
        for num1, num2 in zip(data, resultweights):
            multiplication.append(num1 * num2)
            finalvalue = sum(multiplication)
            print(multiplication)
            print(finalvalue)
            result = 1.0 / (1.0 + exp(-finalvalue)) 
            print(result)
    
    if(round(result) == 1):
        Label(root,text='Couples with similar results tend to work out their differences with the help of counseling').pack()
        Label(root,text='If you work toghether you will get through this!!').pack()
        
        
    else:
        Label(root,text='Couples with similar results tend to part ways. ').pack()
        Label(root,text='Sorry bro :(').pack() 

          
 

global multiplication
multiplication = []



#result = 1.0 / (1.0 + exp(-finalvalue))

#finish=Button(root,text='END',command = finisht).pack()

nextb = Button(root,text="GET RESULTS",command = next).pack()
exitbutton=Button(root,text='EXIT',command = exitest).pack()

#messagebox.showinfo('Instructions','PLEASE READ THE INSTRUCTIONS VERY CAREFULLY\n\nAnswer the following 54 questions using a scale of numbers from 0 to 4\n"0" being I TOTALLY DISAGREE and "4 being I TOTALLY AGREE"\nInsert your answers in the space below WITHOUT ANY SPACES then click "GET RESULTS" button\nExample of how your answer MUST be written: 000122341110000212330011\nPlease make sure you write all 54 numbers to get an accurate result')




root.mainloop()





             

