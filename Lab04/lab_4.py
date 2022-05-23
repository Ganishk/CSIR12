#!/usr/bin/env python3

class Question:
    def __init__(obj, question=None,options=None,answer=None,solution=None):
        """ question is expected to be an string object
        while options should be a dict
        and answer should be an int str index of options"""
        obj.__question = question;
        obj.__options = options;
        obj.__answer = answer;
        obj.__solution = solution;

    def set_answer(self,answer): self.__answer = answer
    def set_question(self,question): self.__question= question;
    def set_options(self,options): self.__options = options;
    def get_answer(self): return self.__options[int(self.__answer)]
    def is_answer(self,option): return True if self.__answer==option else False
    def get_solution(self): return self.__solution
    def show_question(self,question_number,/):
        print(f"""
{question_number:{'0'}2d}. {self.__question}
    1.  {self.__options[1]}
    2.  {self.__options[2]}
    3.  {self.__options[3]}
    4.  {self.__options[4]}
Enter your option[1-4]: """,end='')

    @staticmethod
    def parse_question(qString,*,sep):
        """Question, Options, Answer.
        Expected qString format
        qString_template = "{0};{1:{1}, 2:{2}, 3:{3}, 4:{4}}; {5}; {6}"
        """
        q = list(map(str.strip,qString.split(sep)))
        ARGS = 4
        if len(q) != ARGS: raise(TypeError("Expected "+str(ARGS)+" arguments but given "+str(len(q))));
        q[1] = eval(q[1])
        return tuple(q)

"""Here the questions are classified as list of string of Easy, Medium and Hard Questions.
The reason for this is that, it can be useful when we read the questions from a external file with a delimitter"""
#################################################################################################################
E_QUESTIONS = [
    "How many connectors or flow lines are linked to the diamond of flowchart of a conditional statement?;{1:3, 2:2, 3:0, 4:1};1;Conditional statement has three connectors in its flow chart. Squential flow, True or False statement flow based on the decision that was made.",

    "How many connectors or flow lines are linked to the diamond symbol of flowchart of a loop statment?;{1:3,2:2,3:4,4:1};3; In addition to the conditional checking there is a feedback arrow to the decision to form a loop.",

    "In python, what is the general form of if...else... construct as in C-family?; {1:'if CONDITION:\\n\\t\\tStatements\\n\\telse if CONDTION:\\n\\t\\tStatements',2:'if CONDITION:\\n\\t\\tStatements\\n\\telif CONDTION:\\n\\t\\tStatements',3:'if CONDITION: Statements',4:'else CONDTION: Statements'};2;In python, else if blended as elif",
]

M_QUESTIONS = [
    "Assume that you'll choose to eat idly if dosa is unavailable. Choose a statment from below which narrates the same to your robot which understands python, assume the words are named meaning fully.; {1: 'if food.isAvailable(dosa): eat(food.dosa)\\n\\telse: eat(food.idly)',2:'if not food.isAvailable(dosa): eat(food.dosa) \\n\\telse: eat(food.idly)',3:'if food.isAvailable(idly): eat(food.dosa)\\n\\telse: eat(food.idly)',4:'for food in foods if food==Food.dosa: food.eat()'};1; Last option is a loop which is not needed here and also not a correct syntax. First option is logically correct.",

    "You have given mysterious box which contains many keys to the next door, you have to check all the keys in a short amount of time as possible. Luckily you've hacked one of the enemies bots which understands python and you can use it check the correct key. Which of the following statement is appropriate?;{1:'for key in box_of_keys do robot.check_key(key)\\n\\t\\tif True: break',2:'for key in box_of_keys:\\n\\t\\tif robot.check_key(key): break',3:'for key in box_of_keys:\\n\\t\\tif robot.check_key(key): continue',4:'while key in box_of_keys:\\n\\t\\tif robot.check_key(key): continue'};2;Only the 2nd option follows the correct syntax and it in optimized way of time.",
]

H_QUESTIONS = [
    "Now, you're in the Boss battle with Java, but our ally C had betrayed us. You can only our citizens by slaying both of them, but once you slayed C as a CPython you'll be dead. Choose your movements wisely. If the attacked part is lang for then he'll be dead and libc for C;{1:'while True:\\n\\t  if java.isAlive():\\n\\t\\tif attack().part==\"lang\": java.life=0\\n\\t  else:\\n\\t\\tif not attack().part==\"libc\": c.life=0',2:'while True:\\n\\t  if java.isAlive():\\n\\t\\tif attack().part!=\"lang\": java.life=0\\n\\t  else:\\n\\t\\tif attack().part==\"libc\": c.life=0',3:'for x in range(40):\\n\\t  if java.isAlive():\\n\\t\\tif attack().part==\"lang\": java.life=0\\n\\t  else:\\n\\t\\tif attack().part==\"libc\": c.life=0',4:'while True:\\n\\t  if java.isAlive():\\n\\t\\tif attack().part==\"lang\": java.life=0\\n\\t  else:\\n\\t\\tif attack().part==\"libc\": c.life=0'};4;Think patiently and cast a good spell.",
]
#################################################################################################################

def take_questions(qList):
    a = []
    for question in qList:
        a.append(Question(*Question.parse_question(question,sep=";")))
    return a

def ask_questions(questions,Q_SCORE):
    score = 0
    qNum = 0
    for question in questions:
        qNum+=1
        while True:
            question.show_question(qNum)
            try:
                ans = input().strip();
                if not 0<int(ans)<5: raise ValueError
                if question.is_answer(ans):
                    print("Correct. Move ahead.")
                    score+=Q_SCORE
                else:
                    print("Wrong answer\n")
                    print("Correct Answer:\t",question.get_answer())
                    print("Solution:",question.get_solution())
                break
            except:
                print("Please enter a valid option[1-4]")
    return score


if __name__=="__main__":
    E_SCORE = 10;
    M_SCORE = 25;
    H_SCORE = 40;
    score = 0;
    eQuestions = take_questions(E_QUESTIONS)
    mQuestions = take_questions(M_QUESTIONS)
    hQuestions = take_questions(H_QUESTIONS)
    print("Hi, CPython, our world is invaded by Java. He make our people Jython. You're assigned a task to defeat them. Solve the mysteries along the way and bring honour to our CPython community.\n(Press Enter to start this level)")
    input()
    print("\n")
    score+=ask_questions(eQuestions, E_SCORE)
    print("__________________________________")
    print("Level Ended")
    print("Current Score:",score)

    print("\n\nNow, Jython is standing in our way towards Java, use the power of C to show him the taste of defeat.\n(Press Enter to start this level)")
    input()
    print("\n")
    score+=ask_questions(mQuestions, M_SCORE)
    print("__________________________________")
    print("Level Ended")
    print("Current Score:",score)

    print("Now our final target Java is ahead.\n(Press Enter to start this level)")
    input()
    print("\n")
    score+=ask_questions(hQuestions, H_SCORE)
    print("__________________________________")
    print("Game was Ended")
    print("The war was over and we remain victorius, our history shall always remind of you. At the end you are now counting your last minutes which results in the defeat of C")
    print("\n\nCongratulations! You Completed the game with the score of",score)
