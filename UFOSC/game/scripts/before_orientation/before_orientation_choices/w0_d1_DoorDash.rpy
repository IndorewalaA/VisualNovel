label w0_d1_DoorDash:
    mc "I passed Chipotle like fifteen times on the way here, I bet I can order some for delivery…"
    "*15 minutes later*"
    mc "This driver sucks! I ordered this 30 minutes ago and he still hasn't picked it up!!!"
    "*20 minutes later*"
<<<<<<< HEAD
    mc "Uuuugggghhhhh. I'm so hungry. Can this loser hurry up? It isn't that hard to deliver food."
    "*20 more minutes later, there is a knock at the door*"
    u "Here you go."
    mc "*Upset/Annoyed/Stern* What took you so long."
    u "*Sigh* Orientation is tomorrow, everyone is ordering food."

    menu w0_d1_DoorDashTip:
        mc "Whatever, at least you finally got here."
=======
    "[mc]" "Uuuugggghhhhh. I'm so hungry. Can this loser hurry up? It isn't that hard to deliver food."
    "*20 more minutes later, there is a knock at the door*"
    "[u]" "Here you go."
    "[mc]" "*Upset/Annoyed/Stern* What took you so long."
    "[u]" "*Sigh* Orientation is tomorrow, everyone is ordering food."

    menu w0_d1_DoorDashTip:
        "[mc]" "Whatever, at least you finally got here."
>>>>>>> origin/main

        "Tip driver":
            u "Your total is $30."
            mc "*Hands over $35*"
            mc "Keep the change I guess, have a good one."
            u "Mhm. *Leaves*"
            mc "*Shouts* You're welcome!"
            mc "*To themselves* Some people are just awful…"
            mc "*Closes the door*"
            
        "Don't tip driver":
<<<<<<< HEAD
            u "Your total is $30."
            mc "*Hands over $30*"
            mc "Here"   
            u "What? No tip? Are you kidding me?"
            mc "You took eight years to get me my food."
            mc "Get lost old man."
            mc "*Closes the door*"
=======
            "[u]" "Your total is $30."
            "[mc]" "*Hands over $30*"
            "[mc]" "Here"   
            "[u]" "What? No tip? Are you kidding me?"
            "[mc]" "You took eight years to get me my food."
            "[mc]" "Get lost old man."
            "[mc]" "*Closes the door*"
>>>>>>> origin/main
            
    mc "*Looks inside the chipotle bag*"
    mc "*Shocked and angry* WHERE ARE MY CHIPS AND QUESO????"

jump w0_d1_End