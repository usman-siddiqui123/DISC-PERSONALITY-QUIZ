# def run_quiz():
   
#     questions = [
#         {"question": "When I hear from a college coach, I want them to:", "options": [
#             "Be direct and tell me where I stand. ",
#             "Make it exciting and energetic. ",
#             "Be friendly, genuine, and take their time.",
#             "Provide all the info I need to make a smart decision."
#         ]},
        
#         {"question": "The thing that matters most in a program is:", "options": [
#             "How competitive and successful it is.",
#             "The vibe, relationships, and culture.",
#             "Feeling like I belong and will be supported.",
#             "The structure, development plan, and academic strength."
#         ]},
        
#         {"question": "When a coach visits or calls me, I prefer they:", "options": [
#             "Cut to the chase and talk about what they can offer me.",
#             "Connect with me and make the conversation fun.",
#             "Ask about me and show they care about more than just sports.",
#             "Come prepared and explain everything clearly."
#         ]},
        
#         {"question": "I usually make decisions by:", "options": [
#             "Trusting my gut and taking action fast.",
#             "Talking it out with others and going with what feels right.",
#             "Taking time to think and talk with my family.",
#             "Doing research and comparing all the options."
#         ]},
        
#         {"question": "In conversations with coaches, I respond best when they:", "options": [
#             "Speak confidently and set clear expectations.",
#             "Joke around, smile, and keep it real.",
#             "Listen carefully and don't rush me.",
#             "Are professional, thoughtful, and organized."
#         ]},
        
#         {"question": "When visiting a campus, I care most about:", "options": [
#             "Seeing how serious and competitive the team is.",
#             "Meeting players and feeling the energy.",
#             "Feeling like I'd be part of a close-knit team.",
#             "Getting a full breakdown of facilities, academics, and the daily schedule."
#         ]},
        
#         {"question": "The kind of coach I respond to best is:", "options": [
#             "Strong, driven, and holds people accountable.",
#             "High-energy, positive, and fun to be around.",
#             "Supportive, calm, and approachable.",
#             "Knowledgeable, methodical, and well-prepared."
#         ]},
        
#         {"question": "When I feel pressure in the recruiting process, I:", "options": [
#             "Push through and make quick decisions. ",
#             "Stay upbeat and talk to people I trust. ",
#             "Get a little quiet and need time to process. ",
#             "Slow down and try to organize everything. "
#         ]},
        
#         {"question": "I like coaches who:", "options": [
#             "Are confident and challenge me to level up. ",
#             "Are personable and make things fun.",
#             "Are steady, loyal, and consistent.",
#             "Are structured, smart, and precise."
#         ]},
        
#         {"question": "When it comes to choosing a school, I am:", "options": [
#             "Focused on winning and advancing to the next level.",
#             "Looking for a team and experience I'll enjoy.",
#             "Wanting a place that feels like family.",
#             "Analyzing what will set me up long-term, both in and out of sports."
#         ]}
#     ]
    
    
#     score = {"D": 0, "I": 0, "S": 0, "C": 0}
    
   
#     for i, q in enumerate(questions):
#         print(f"\nQuestion {i+1}: {q['question']}")
#         for idx, option in enumerate(q['options']):
#             print(f"{idx+1}. {option}")
        
#         while True:
#             try:
#                 answer = int(input("Please select an option (0-4): "))  
#                 if 0 <= answer <= 4:  
#                     selected_option = q['options'] [answer - 1] 
#                     selected_letter = selected_option.split(" ")[-1].strip("()") 
#                     score[selected_letter] += 1 
#                     break  
#                 else:
#                     print("Invalid input. Please select a number between 1 and 4.")  
#             except ValueError:
#                 print("Invalid input. Please enter a number.")
        

        
#     print(f"\nYour score distribution: {score}")

    
#     full_names = {
#         "D": "Dominance",
#         "I": "Influence",
#         "S": "Steadiness",
#         "C": "Conscientiousness"
#     }

    
#     dominant_letter = max(score, key=score.get)
#     dominant_score = score[dominant_letter]

   
#     if dominant_score >= 7:
#         level = "High"
#     elif dominant_score >= 3:
#         level = "Moderate"
#     else:
#         level = "Low"

   
#     dominant_category = full_names[dominant_letter]
#     print(f"\nYou Are: {dominant_category} - {level}")

         

   


#     # max_score = max(score.values())  # Find the highest score
#     # if max_score >= 7:
#     #     result = "High"
#     # elif 3 <= max_score < 7:
#     #     result = "Moderate"
#     # else:
#     #     result = "Low"
    
#     # # Find the category with the highest score
#     # winner = [k for k, v in score.items() if v == max_score]
    
#     # # Display the final result
#     # print(f"\nYour score distribution: {score}")
#     # print(f"\nThe dominant category is: {', '.join(winner)} with {result} result")
 
    

#     # winner = max(score, key=score.get)
    
    
#     # print(f"\nYour score distribution: {score}") 
#     # # print(f"\nWinner is: {winner} (based on your responses)")  
#     # for key, value in score.items():
#     #     if 3 <= value <= 7:
#     #         print(f"{key}: You are High")
#     #     elif 1 <= value < 3:
#     #         print(f"{key}: You are Moderate")
#     #     else:
#     #         print(f"{key}:You are  Low")
#     #     print(f"{key} :{score}")

# run_quiz()  

def run_quiz():
    questions = [
        {"question": "When I hear from a college coach, I want them to:", "options": [
            ("Be direct and tell me where I stand.", "D"),
            ("Make it exciting and energetic.", "I"),
            ("Be friendly, genuine, and take their time.", "S"),
            ("Provide all the info I need to make a smart decision.", "C")
        ]},
        {"question": "The thing that matters most in a program is:", "options": [
            ("How competitive and successful it is.", "D"),
            ("The vibe, relationships, and culture.", "I"),
            ("Feeling like I belong and will be supported.", "S"),
            ("The structure, development plan, and academic strength.", "C")
        ]},
        {"question": "When a coach visits or calls me, I prefer they:", "options": [
            ("Cut to the chase and talk about what they can offer me.", "D"),
            ("Connect with me and make the conversation fun.", "I"),
            ("Ask about me and show they care about more than just sports.", "S"),
            ("Come prepared and explain everything clearly.", "C")
        ]},
        {"question": "I usually make decisions by:", "options": [
            ("Trusting my gut and taking action fast.", "D"),
            ("Talking it out with others and going with what feels right.", "I"),
            ("Taking time to think and talk with my family.", "S"),
            ("Doing research and comparing all the options.", "C")
        ]},
        {"question": "In conversations with coaches, I respond best when they:", "options": [
            ("Speak confidently and set clear expectations.", "D"),
            ("Joke around, smile, and keep it real.", "I"),
            ("Listen carefully and don't rush me.", "S"),
            ("Are professional, thoughtful, and organized.", "C")
        ]},
        {"question": "When visiting a campus, I care most about:", "options": [
            ("Seeing how serious and competitive the team is.", "D"),
            ("Meeting players and feeling the energy.", "I"),
            ("Feeling like I'd be part of a close-knit team.", "S"),
            ("Getting a full breakdown of facilities, academics, and the daily schedule.", "C")
        ]},
        {"question": "The kind of coach I respond to best is:", "options": [
            ("Strong, driven, and holds people accountable.", "D"),
            ("High-energy, positive, and fun to be around.", "I"),
            ("Supportive, calm, and approachable.", "S"),
            ("Knowledgeable, methodical, and well-prepared.", "C")
        ]},
        {"question": "When I feel pressure in the recruiting process, I:", "options": [
            ("Push through and make quick decisions.", "D"),
            ("Stay upbeat and talk to people I trust.", "I"),
            ("Get a little quiet and need time to process.", "S"),
            ("Slow down and try to organize everything.", "C")
        ]},
        {"question": "I like coaches who:", "options": [
            ("Are confident and challenge me to level up.", "D"),
            ("Are personable and make things fun.", "I"),
            ("Are steady, loyal, and consistent.", "S"),
            ("Are structured, smart, and precise.", "C")
        ]},
        {"question": "When it comes to choosing a school, I am:", "options": [
            ("Focused on winning and advancing to the next level.", "D"),
            ("Looking for a team and experience I'll enjoy.", "I"),
            ("Wanting a place that feels like family.", "S"),
            ("Analyzing what will set me up long-term, both in and out of sports.", "C")
        ]}
    ]

    score = {"D": 0, "I": 0, "S": 0, "C": 0}

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for idx, (text, _) in enumerate(q['options']):
            print(f"{idx + 1}. {text}")
        
        while True:
            try:
                answer = int(input("Please select an option (1-4): "))
                if 1 <= answer <= 4:
                    _, letter = q['options'][answer - 1]
                    score[letter] += 1
                    break
                else:
                    print("Invalid input. Please select a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    print(f"\nYour score distribution: {score}")

    full_names = {
        "D": "Dominance",
        "I": "Influence",
        "S": "Steadiness",
        "C": "Conscientiousness"
    }

    dominant_letter = max(score, key=score.get)
    dominant_score = score[dominant_letter]

    if dominant_score >= 7:
        level = "High"
    elif dominant_score >= 3:
        level = "Moderate"
    else:
        level = "Low"

    dominant_category = full_names[dominant_letter]
    print(f"\nYou Are: {dominant_category} - {level}")

