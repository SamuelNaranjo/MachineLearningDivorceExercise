from tkinter import *
import os
from math import exp
from tkinter import messagebox


root = Tk()
root.title('COUPLES COUNSELING QUIZ A01205900')
root.geometry("650x800")


frame = LabelFrame(root,text='Instructions',padx=10,pady=10)
frame.pack(padx=10,pady=10)
Label(frame,text='PLEASE READ THE INSTRUCTIONS VERY CAREFULLY',fg='red').pack()
Label(frame,text='Answer the following 54 questions using a scale of numbers from 0 to 4').pack()
Label(frame,text='"0" being I TOTALLY DISAGREE and "4 being I TOTALLY AGREE"').pack()
Label(frame,text='Insert your answers in the space below WITHOUT ANY SPACES then click "GET RESULTS" button').pack()
#Label(frame,text='Example of how your answer MUST be written: 000122341110000212330011').pack()
Label(frame,text='Please make sure you write all 54 numbers to get an accurate result').pack()
Label(frame,text='To start the quiz click the "START TEST" button (you can scroll down to see all the questions)').pack()
Label(frame,text='Example of how your answer MUST be written: 000122341110000212330011').pack()

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

#resultweights = [-0.4116168406477664, 0.16127135722674943, 0.09392306875528937, 0.08618336486073931, 0.15152198981452428, 0.112703007177662, 0.09959435925096392, 0.046355238009921, 0.07832970277182749, 0.1836059310339804, -0.24645953615853497, 0.20736758532548907, -0.09141524522943613, -0.33106967241217106, 0.20042007088344801, 0.07067972542319356, 0.11203971486413962, 0.1513019592977353, 0.249451549661633, 0.21923144895804722, 0.3024432014526723, 0.06627392598204146, -0.02249979099215653, 0.040515874905737055, -0.10073100325790932, -0.008230154392166785, 0.29973765817792886, 0.07517029761985991, 0.30134673260176326, 0.2496979705662934, 0.23966672815913084, 0.0035239384305774967, -0.058214625848810424, 0.1320518147992346, 0.01833260356721795, 0.12684862249311699, 0.3399070197900843, -0.125114022801525, 0.14989888969506993, 0.25294460479916175, 0.5965257732108006, 0.08870670902543579, 0.009971131483531721, -0.36162818986095663, 0.2805272368921549, -0.31313838310813547, -0.2678994086095123, -0.14067947785693713, -0.49842841526547793, 0.13607361389923087, -0.09895543666501327, -0.4526281227044454, 0.06730245486533827, -0.0755428416317035, -0.14057230786197902]
global multiplication

def start():
    question=Text(root)
    for i in questionaire:
        question.insert(END,i+'\n')
        question.pack()
      
        
def exitest():
    root.destroy()
sbutton = Button(root,text="START TEST",command=start,fg='green',padx=5,pady=5).pack(pady=10)


    
e = Entry(root,width=54,borderwidth=5)
e.pack()  
global result
#global data

def next():
    data = []
    multiplication = []
    
    num = e.get()
    lab = Label(root,text='Your answers were:'+ num)
    lab.pack()
    datalist = map(int,num)
    data = list(datalist)
    e.delete(0,END)
    #print(data)
    resultweights = [-0.17547863415369358, 0.059018922327791594, 0.0181765637956597, -0.020397176024057728, 0.06789372505576953, 0.10256608365465662, 0.01283211412535286, 0.04004000232195386, 0.09134242405329114, 0.12140232590316545, -0.020665310715920166, 0.10082966765473729, 0.01472736815557992, -0.05691641220236317, 0.07470425095434967, 0.0699380677736943, 0.07289779428699286, 0.10777230284922278, 0.12729614688828209, 0.12091930141092565, 0.12393038740755126, 0.07590670921008617, 0.061722063163815934, 0.08712043700051933, 0.03698941536033841, 0.04932576728217898, 0.11025432711936563, 0.08827577315671686, 0.11662480872248286, 0.1297924783915819, 0.09002846500396253, -0.02523927755460061, -0.029074462288015974, 0.07991667065532584, 0.01105526336468964, 0.11666205523268677, 
0.15604021645641192, -0.018754168491839262, 0.08441709376772338, 0.060595870573288295, 0.1747923201208717, 0.05113261419863296, -0.016499219080672825, -0.17421145669806545, 0.09181143303464898, -0.15936016887955332, -0.1877077114531733, -0.06753746125527527, -0.26732838142438786, -0.04737395988481654, -0.10826147529009138, -0.20030454333251402, -0.088880313450971, -0.07944533853802352, -0.0017274421195360207]
  
    for num1, num2 in zip(data, resultweights):
        multiplication.append(num1 * num2)

    finalvalue = sum(multiplication)
    result = 1.0 / (1.0 + exp(-finalvalue))
    print(multiplication) 
    print(finalvalue)
    print(result)
        
                     
    if(round(result) == 1):

        #Label(root,text='Couples with similar results tend to work out their differences with the help of counseling').pack()
        #Label(root,text='If you work toghether you will get through this!!').pack()
        messagebox.showinfo('Results','Couples with similar results tend to work out their differences with the help of counseling\n\nIf you work toghether you will get through this!!')
   
            
    else:
        #Label(root,text='Couples with similar results tend to part ways. ').pack()
        #Label(root,text='Sorry bro :(').pack() 
        messagebox.showinfo('Results','Couples with similar results tend to part ways.\n\nSorry bro :(')
        







#result = 1.0 / (1.0 + exp(-finalvalue))

#finish=Button(root,text='END',command = finisht).pack()

nextb = Button(root,text="GET RESULTS",command = next,padx=5,pady=5).pack()
exitbutton=Button(root,text='EXIT',command = exitest,fg='red',padx=5,pady=5).pack()

#messagebox.showinfo('Instructions','PLEASE READ THE INSTRUCTIONS VERY CAREFULLY\n\nAnswer the following 54 questions using a scale of numbers from 0 to 4\n"0" being I TOTALLY DISAGREE and "4 being I TOTALLY AGREE"\nInsert your answers in the space below WITHOUT ANY SPACES then click "GET RESULTS" button\nExample of how your answer MUST be written: 000122341110000212330011\nPlease make sure you write all 54 numbers to get an accurate result')




root.mainloop()





             

