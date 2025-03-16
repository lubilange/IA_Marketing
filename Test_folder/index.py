import random 

numbers = random.randint(1, 100)


computer_choice = numbers


while True :

     try :

             human_choice = int(input("Devinez le nombre choisi par l'ordinateur 🤖, il se situe entre 1 et 100: "))

             if human_choice == computer_choice :
                 print("vous avez gagné ✅ !!!")
                
             elif abs(human_choice - computer_choice) == 2 :
                 print("proche 😬!")
             elif human_choice < computer_choice :
                 print("trop bas ⛔!")
             else :
                 print("trop haut ⛔ !")

     except ValueError :
         print("Veuillez entrer un nombre valide")