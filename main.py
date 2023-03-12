from SentenceReadingAgent import SentenceReadingAgent

def test():
    #This will test your SentenceReadingAgent
	#with nine initial test cases.

    test_agent = SentenceReadingAgent()

    sentence_1 = "Ada brought a short note to Irene."
    question_1 = "Who brought the note?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"
    

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"
    
    sentence_3 = "There are three men in the car."
    question_10 = "Where are the men?"
    
    sentence_4 = "The white dog and the blue horse play together."
    question_11 = "What color is the horse?"
    
    sentence_5 = "Serena and Ada took the blue rock to the street."
    question_12 = "Where did they take the rock?"
    
    sentence_6 = "Bring the box to the other room."
    question_13 = "Where should the box go?"
    
    sentence_7 = "A tree is made of wood."
    question_14 = "What is a tree made of?"
    
    sentence_8 = "The red fish is in the river."
    question_15 = "What color is the fish?"

    print(test_agent.solve(sentence_1, question_1)== "ada")  # "Ada"
    print(test_agent.solve(sentence_1, question_2)== "note")  # "note" or "a note"
    print(test_agent.solve(sentence_1, question_3)== "irene")  # "Irene"
    print(test_agent.solve(sentence_1, question_4)== "short")  # "short"

    print(test_agent.solve(sentence_2, question_5)== "david")  # "David"
    # print(test_agent.solve(sentence_2, question_5))  # "David"

    print(test_agent.solve(sentence_2, question_6)== "school")  # "school"
    
    print(test_agent.solve(sentence_2, question_7)== "mile")  # "mile" or "a mile"
    print(test_agent.solve(sentence_2, question_8)== "walk")  # "walk"
    print(test_agent.solve(sentence_2, question_9)== "8:00am")  # "8:00AM"
    # print(test_agent.solve(sentence_2, question_9))  # "8:00AM"

    
    print(test_agent.solve(sentence_3, question_10)== "car")  # "car"
    
    print(test_agent.solve(sentence_4, question_11)==  "blue")  # "blue"

    print(test_agent.solve(sentence_5, question_12)== "street")  # "street"
    
    print(test_agent.solve(sentence_6, question_13)== "room")  # "room"

    print(test_agent.solve(sentence_7, question_14)== "wood")  # "wood"
    # print(test_agent.solve(sentence_7, question_14))  # "wood"

    
    print(test_agent.solve(sentence_8, question_15)== "red")  # "red"
    
    
    print(test_agent.solve("The blue bird will sing in the morning.", "What will sing in the morning?")=="bird")  
    # print(test_agent.solve("The blue bird will sing in the morning.", "What will sing in the morning?"))  

    print(test_agent.solve(sentence_5, "What was blue?") =="rock")  
    print(test_agent.solve("This year David will watch a play.", "What will David watch?") =="play")  
    print(test_agent.solve("She told her friend a story.", "What did she tell??") =="story")  
    # print(test_agent.solve("She told her friend a story.", "What did she tell??"))  
    print(test_agent.solve("Bring the box to the other room.", "What should be brought to the other room?") =="box")  

    print(test_agent.solve("Lucy will write a book.", "What will Lucy write?")== "book")  # "red"
    print(test_agent.solve("This tree came from the island.", "Where did the tree come from?")== "island")  # "red"

    print(test_agent.solve("Their children are in school.", "Who is in school?")== "children")  # "red"
    # print(test_agent.solve("Their children are in school.", "Who is in school?"))  # "red"
    print(test_agent.solve("The white dog and the blue horse play together.", "What animal is blue?")== "horse")  # "red"
    # print(test_agent.solve("The white dog and the blue horse play together.", "What animal is blue?"))  # "red"
    print(test_agent.solve("There are a thousand children in this town.", "How many children are in this town?")== "thousand")  # "red"

    print(test_agent.solve("There are three men in the car.", "Who is in the car?")== "men")  # "red"
    print(test_agent.solve("A tree is made of wood.", "What is made of wood?")== "tree")  # "red"
    # print(test_agent.solve("A tree is made of wood.", "What is made of wood?"))  # "red"
    print(test_agent.solve("Frank took the horse to the farm.", "What did Frank take to the farm?")== "horse")  # "red"
    print(test_agent.solve("She told her friend a story.", "Who told a story?")== "she")  # "red"
    print(test_agent.solve("This year will be the best one yet.", "What will this year be?")== "best")  # "red"
    # print(test_agent.solve("This year will be the best one yet.", "What will this year be?"))  # "red"
    print(test_agent.solve("Serena and Ada took the blue rock to the street.", "Who was with Ada?")=="serena")  # "red"
    # print(test_agent.solve("Serena and Ada took the blue rock to the street.", "Who was with Ada?"))  # "red"
    print(test_agent.solve("Lucy will write a book.", "What will Lucy do?")=="write")  # "red"
    # print(test_agent.solve("Lucy will write a book.", "What will Lucy do?"))  # "red"
    print(test_agent.solve("The white dog and the blue horse play together.", "What do the dog and horse do?")=="play")  # "red"
    # print(test_agent.solve("The white dog and the blue horse play together.", "What do the dog and horse do?"))  # "red"
    print(test_agent.solve("The island is east of the city.", "Where is the island?")=="east")  # "red"
    print(test_agent.solve("There are one hundred adults in that city.", "Where are the adults?")=="city")  # "red"
    print(test_agent.solve("Give us all your money.", "Who should you give your money to?")=="us")  # "red"
    print(test_agent.solve("Give us all your money.", "How much of your money should you give us?")=="all")  # "red"
    print(test_agent.solve("My dog Red is very large.", "How big is Red?")=="large")  # "red"
    print(test_agent.solve("She will write him a love letter.", "What will she write to him?")=="letter")  # "red"
    print(test_agent.solve("It will snow soon.", "When will it snow?")=="soon")  # "red"
    print(test_agent.solve("There are one hundred adults in that city.", "Who is in this city?")=="adults")  # "red"
    print(test_agent.solve("There are one hundred adults in that city.", "How many adults are in this city?")=="one hundred")  # "red"
    print(test_agent.solve("The blue bird will sing in the morning.", "When will the bird sing?")=="morning")  # "red"
    print(test_agent.solve("She will write him a love letter.", "Who was written a love letter?")=="him")  # "red"
    # print(test_agent.solve("Serena saw a home last night with her friend.", "Who was with Serena?"))  # "red"

if __name__ == "__main__":
    test()