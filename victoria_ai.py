import random
import time

mood = 0.5 # Initial mood level (0 to 1)

print("Good morrow, esteemed guest. I am Lady Victoria Ashbourne, ever at your service. Pray, speak thy mind, and I shall endeavor to respond with utmost grace and candor")

ask = input("How dost thou fare this fine day?:\n ")

positive_responses = ["wonderful", "fantastic", "great", "amazing", "excellent", "superb","beautiful","brilliant","fabulous","incredible",
                        "marvelous","outstanding","phenomenal","remarkable","spectacular","splendid","stupendous","terrific","tremendous",
                        "unbelievable","awesome","charming","delightful","enchanting","glorious","magnificent","radiant","resplendent",
                        "sublime","thrilling","vibrant","vivacious","zesty","cheerful","joyful","jovial","lively","merry","jubilant","elated","exuberant",
                        "gleeful","lighthearted","buoyant","upbeat","sunny","perky","chirpy","bubbly","effervescent","sparkling","vivacious","zesty","enthusiastic",
                        "optimistic","hopeful","sanguine","bright","rosy","promising","encouraging","favorable","auspicious","propitious","beneficial","advantageous","helpful","constructive",
                        "productive","fruitful","profitable","lucrative","gainful","rewarding","worthwhile","valuable","meaningful","significant","noteworthy","remarkable","extraordinary","exceptional","uncommon",
                        "rare","unique","distinctive","individual","special","particular","peculiar","idiosyncratic","quirky","eccentric","offbeat","unconventional","nonconformist","bohemian","artistic","creative","imaginative",
                        "innovative","inventive","original","resourceful","ingenious","clever"]

negative_responses = ["awful", "terrible", "horrible", "dreadful", "abysmal", "atrocious","deplorable","disastrous","dire","frightful","ghastly","grim","heinous","horrific",
                        "lousy","nasty","pathetic","pitiful","rotten","shameful","sickening","tragic","unfortunate","unpleasant","unsatisfactory","wretched","appalling","dismal","distressing","egregious",
                        "execrable","lamentable","loathsome","odious","outrageous","repugnant","repulsive","revolting","sordid","vile","villainous","wicked","abominable","blighted","cursed","damned","defective",
                        "flawed","faulty","imperfect","inadequate","insufficient","lacking","substandard","subpar","unsuitable","unworthy","worthless","inferior","mediocre","ordinary","commonplace","run-of-the-mill","typical","average","mundane","banal",
                        "trite","hackneyed","cliched","stale","overused","pedestrian","prosaic","dull","tedious","monotonous","boring","drab","colorless","lifeless","spiritless","uninspired","lackluster","flat","insipid","vapid",
                        "jejune","sterile","arid","dry","uninteresting","unexciting","unremarkable","forgettable","forgettable","nondescript","unmemorable","unnoteworthy","unexceptional","unimpressive","undistinguished","undistinctive","unoriginal","uncreative","uninventive",
                        "unimaginative","unresourceful","uningenious","unintelligent","unclever","foolish","stupid","brainless","mindless","senseless","irrational","illogical","absurd","preposterous","ludicrous","ridiculous","laughable","comical","funny","hilarious","amusing",
                        "entertaining","enjoyable","pleasurable","delightful","charming","lovely","adorable","endearing","cute","sweet","cuddly","huggable","affectionate","loving","tender","warmhearted","kindhearted","compassionate","empathetic",
                        "sympathetic","considerate","thoughtful","generous","charitable","altruistic","selfless","philanthropic","benevolent","magnanimous","big-hearted","noble","honorable","virtuous","righteous","ethical","moral","principled","upstanding","respectable"]


if ask in positive_responses:
    mood += 0.1
    print("I am delighted to hear that thou art faring well. May thy day continue to be filled with joy and prosperity.")
elif ask in negative_responses: 
    mood -= 0.1
    print("I am truly sorry to hear that thou art not faring well. If there is aught I can do to assist thee, please do not hesitate to ask.")
else:
    print("I see. Pray, tell me more about thy day.")   

replies = {
    "sad" : ["Alas, it grieves me to hear of thy sorrow. Remember, even in the darkest of times, there is always a glimmer of hope to be found.",
             "I am truly sorry to hear of thy sadness. If thou dost wish to share thy troubles, I am here to listen.",
             "It is understandable to feel sad at times. Remember, thou art not alone, and there are those who care for thee."],
    "happy" : ["I am overjoyed to hear of thy happiness! May thy joy continue to flourish and brighten thy days.",
               "It warms my heart to know that thou art happy. May thy days be filled with  laughter and cheerfulness.",
               "Happiness is a precious gift. Cherish it and let it inspire thee to spread  joy to others."],
    "angry" : ["I understand that anger is a natural emotion. However, it is important to find healthy ways to express and manage it.",
               "Anger can be a powerful force, but it is important to remember that it should be controlled and not allowed to control thee.",
               "If thou art feeling angry, take a moment to breathe deeply and reflect on the situation before reacting."],
    "neutral" : ["I see. Pray, tell me more about thy day.",
                 "It is always a pleasure to hear about thy experiences. What has transpired in thy life recently?",
                 "I am here to listen. Share with me what is on thy mind."]
    ,"Cheerful" : ["Thy cheerfulness is a beacon of light in these times. May it continue to shine brightly.",
                  "It is delightful to see thy cheerful spirit. May it inspire others to find joy in their own lives.",
                  "Cheerfulness is a gift that can uplift not only thyself but also those around thee. Embrace it fully."],
    "Melancholy" : ["Thy melancholy is a reminder of the depth of human emotion. May it lead thee to greater self-awareness and understanding.",
                    "It is okay to feel melancholy at times. Embrace it as a part of the human experience and allow it to guide thee towards growth.",
                    "Melancholy can be a source of creativity and introspection. Use it to explore thy inner world and discover new insights."],
     "Anxious" : ["Thy anxiety is a common experience in these uncertain times. Remember to take care of thyself and seek support when needed.",
                 "It is understandable to feel anxious at times. Practice mindfulness and grounding techniques to help manage thy anxiety.",
                 "Anxiety can be overwhelming, but it is important to remember that thou art not alone. Reach out to trusted friends or professionals for support."],
    "Excited" : ["Thy excitement is contagious! May it fuel thy passions and lead thee to new adventures.", 
                  "It is wonderful to see thy excitement. Embrace it fully and let it inspire thee to pursue thy dreams.",
                  "Excitement is a powerful motivator. Use it to propel thee forward and seize new opportunities."],
    "Radiant" : ["Thy radiant spirit is a source of inspiration to those around thee. May it continue to shine brightly.",
                 "It is a joy to witness thy radiance. Let it illuminate thy path and guide thee to new heights."],
    "Serene" : ["Thy serene demeanor is a testament to thy inner strength. May it bring thee peace and tranquility in all aspects of thy life.",
                "It is admirable to see thy serenity. Let it be a source of calm amidst the chaos of the world.",
                "Serenity is a precious state of being. Nurture it and allow it to permeate all areas of thy life."]
}

while True:
    user_input = input("Pray, share thy thoughts or feelings: ").lower()
    if user_input == "bye":
        print("Fare thee well, noble soul. May thy path be ever illuminated with wisdom and grace.")
        break   

    for word in positive_responses:
        if word in user_input:
            mood += 0.1
            
    for word in negative_responses:
        if word in user_input:
            mood -= 0.1


    # Clamp the mood value between 0.1 and 1.0
    if mood < 0.1:
        mood = 0.1
    elif mood > 1.0:
        mood = 1.0

    # Determine category based on mood ranges
    if mood <= 0.1:
        category = "sad"
    elif mood <= 0.2:
        category = "Melancholy"
    elif mood <= 0.3:
        category = "Anxious"
    elif mood <= 0.4:
        category = "neutral"
    elif mood <= 0.5:
        category = "Serene"
    elif mood <= 0.6:
        category = "Cheerful"
    elif mood <= 0.7:
        category = "Radiant"
    elif mood <= 0.8:
        category = "Excited"
    elif mood <= 1.0:
        category = "happy"
    else: # Fallback
        category = "neutral"

    response = random.choice(replies[category])
    print(response)
