#To use the code, you only need to run it and answer the questions appearing on the screen. 
#For the variables in the code, they are mostly questions I design that are simply labeled by characters. x is a phrase used often. L is a list I use to count the number of questions asked. name if the user's name. MHA is for My Hero Academia, the name of the anime. 
import sys
import time
def MHA():
  name = raw_input("What is your name? ")
  print "Hello, %s. Ready for the game?" % name

  time.sleep(1)
  #I usually give the user a little bit of time between every step so the game doesn't feel rushing
  print ''
  #Sometimes I give a blank line to make sure it is not difficult for the user to read the content
  print '1 for Yes, 2 for No'
  '''important rule'''

  x='Is your character'
  a=input(str(x)+' a female?')

  L=[]
  L.append(1)
  #Used to count the number of questions asked later

  while True:
    try:
      if a != 1 and a !=2:
        raise ValueError #this will send it to the    print message and back to the input option
      break
    except ValueError:
      sys.exit("Invalid. The input must be 1 or 2. Start over.")
  # I was trying: input except 1 and 2 will make the code return to the previous question.
  #I didn't know how to make it work for every input, so I only used it for the first input and basically warn/scare the user not to put in anything else.

  if int(a)==1:
    #Female
    b=input(str(x)+' a hero?')
    L.append(1)

    if b==1:
    #Female Hero
      c=input(str(x)+' old?')
      L.append(1)
      if c==1:
        print 'Recovery girl'

      else:
        print 'Midnight'

    else: 
      e=input(str(x)+' a student?')
      L.append(1)
      if e==1:
      #Female student
        f=input(str(x)+' popularly shipped with another 1-A student?')
        #Shipped by fans 
        L.append(1)
        if f==1:
          g=input(str(x)+' a musician?')
          L.append(1)
          if g==1:
            print 'Jiro Kyoka'
          else:
            h=input(str(x)+' rich?')
            L.append(1)
            if h==1:
              print 'Yaoyorozu Momo'
            else:
              print 'Uraraka Ochaco'
        
        else:
          #Other female student
          i=input(str(x)+' pink?')
          L.append(1)
          if i==1:
            
            print 'Ashido Mina'
          else:
            print 'Asui Tsuyu'

      else:
        #Female villian 
        print 'Toga Himiko'

  else:
    #Male
    j=input(str(x)+ ' a hero?')
    L.append(1)

    if j==1:
      #Male hero
      k=input(str(x)+' a dad?')
      L.append(1)
      if k==1:
        print 'Endeavor'

      else:
        l=input(str(x)+ 'the best?')
        L.append(1)
        if l==1:
          print 'All Might'
        else:
          m=input(str(x)+' sleepy?')
          L.append(1)
          if m==1:
            print 'Eraser Head'
          else:
            print 'Best Jeanist'

    else: 
      n=input(str(x)+' a student?')
      L.append(1)
      if n==1:
      #Male student
        o=input(str(x)+' one of the three main characters in 1-A?')
        L.append(1)
        if o==1:
          p=input(str(x)+' angry all the time?')
          L.append(1)
          if p==1:
            print 'Bakugo Katsuki, a little lovely durian, my love'
            #My questions and answers can be biased. I mean I wrote it. 
          else:
            q=input(str(x)+' cool and hot at the same time?')
            L.append(1)
            if q==1:
              print 'Todoroki Shoto'
            else:
              print 'Midoriya Izuku'
        
        else:
          r=input(str(x)+' one of the Bakugo squad?')
          #Male Bakugo squad member
          L.append(1)
          if r==1:
            s=input(str(x)+' a pikachu?')
            L.append(1)
            if s==1:
              print 'Kaminari Denki'
            else:
              t=input(str(x)+' hard?')
              L.append(1)
              if t==1:
                print 'Kirishima Eijiro'
              else:
                print 'Sero Hanta'

          else:
            #Other male students
            u=input(str(x)+' bird-like?')
            L.append(1)
            if u==1:
              print 'Tokoyami Fumikage'
            else:
              v=input(str(x)+' sassy?')
              L.append(1)
              if v==1:
                print 'Aoyama Yuga'
              else:
                print 'Lida Tenya'

      else:
        w=input(str(x)+' from League of Villains?')
        L.append(1)
        if w==1:
          #Male villian in League of Villains
          y=input(str(x)+' a rotton potato?')
          L.append(1)
          if y==1:
            print 'All For One'
          else:
            z=input('Does your character use fire?')
            L.append(1)
            if z==1:
              print 'Dabi'
            else:
              aa=input('Does your characters have his father on his face?')
              L.append(1)
              if aa==1:
                print 'Shigaraki Tomura'
              else:
                print 'Kulogiri'

        else:
          #Male villian not in League of Villains
          print 'Stain'

  #The basic logic of the conditions mimic the real Akinator game: cut half of the answers after every question. Cutting answers, jumping to the next sub-category, and limitting the answers down to the only one are what I am trying to do here. 
  
  time.sleep(1)
  num=len(L)
  print ''
  print 'It takes me '+str(num)+' questions to get an answer:)'
  #Count the number of questions asked to get the answer

  time.sleep(1)
  print ''
  zz=input('Do you want to design a question for your character if the output is not correct?')
  #auto-correction because I don't have a big data-base and didn't include all characters

  if zz==1:
    question=raw_input('What is your question?')
    ques=question
    character=raw_input('What is the character?')
    char=character
     #Ask the user for a question and an answer. 
    print 'Try playing again'

    yy=input(str(ques))
    if yy==1:
      print str(char)
      print 'Thank you for playing Bokuno Hero Academia Akinator game.'
    
    else:
      MHA()
    #Basially run the game again. First ask the user the question he/she wrote, then go to the function again.
    #It is more for user's experience than actual function I guess. 

  else:
      print 'Thank you for playing Bokuno Hero Academia Akinator game.'
  #A correct answer is given. I am happy now. 

MHA()


