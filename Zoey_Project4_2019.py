import sys
def MHA():
  print '1 for Yes, 2 for No'

  x='Is your character'
  a=input(str(x)+' a female?')

  while True:
    try:
      if a != 1 and a !=2:
        raise ValueError #this will send it to the print message and back to the input option
      break
    except ValueError:
      sys.exit("Invalid. The input must be 1 or 2. Start over.")

  if int(a)==1:
    b=input(str(x)+' a hero?')

    if b==1:
      c=input(str(x)+' old?')
      if c==1:
        return 'Recovery girl'

      else:
        return 'Midnight'

    else: 
      e=input(str(x)+' a student?')
      if e==1:
        f=input(str(x)+' popularly shipped with another 1-A student?')
        if f==1:
          g=input(str(x)+' a musician?')
          if g==1:
            return 'Jiro Kyoka'
          else:
            h=input(str(x)+' rich?')
            if h==1:
              return 'Yaoyorozu Momo'
            else:
              return 'Uraraka Ochaco'
        
        else:
          i=input(str(x)+' pink?')
          if i==1:
            return 'Ashido Mina'
          else:
            return 'Asui Tsuyu'

      else:
        return 'Toga Himiko'

  else:
    j=input(str(x)+ ' a hero?')

    if j==1:
      k=input(str(x)+' a dad?')
      if k==1:
        return 'Endeavor'

      else:
        l=input(str(x)+ 'the best?')
        if l==1:
          return 'All Might'
        else:
          m=input(str(x)+' sleepy?')
          if m==1:
            return 'Eraser Head'
          else:
            return 'Best Jeanist'

    else: 
      n==input(str(x)+' a student?')
      if n==1:
        o=input(str(x)+' one of the three main characters in 1-A?')
        if o==1:
          p=input(str(x)+' angry all the time?')
          if p==1:
            return 'Bakugo Katsuki, a little lovely durian, my love'
          else:
            q=input(str(x)+' cool and hot at the same time?')
            if q==1:
              return 'Todoroki Shoto'
            else:
              return 'Midoriya Izuku'
        
        else:
          r=input(str(x)+' one of the Bakugo squad?')
          if r==1:
            s=input(str(x)+' a pikachu?')
            if s==1:
              return 'Kaminari Denki'
            else:
              t=input(str(x)+' hard?')
              if t==1:
                return 'Kirishima Eijiro'
              else:
                return 'Sero Hanta'

          else:
            u=input(str(x)+' bird-like?')
            if u==1:
              return 'Tokoyami Fumikage'
            else:
              v=input(str(x)+' sassy?')
              if v==1:
                return 'Aoyama Yuga'
              else:
                return 'Lida Tenya'

      else:
        w=input(str(x)+' from League of Villains?')
        if w==1:
          y=input(str(x)+' a rotton potato?')
          if y==1:
            return 'All For One'
          else:
            z=input('Does your character use fire?')
            if z==1:
              return 'Dabi'
            else:
              aa=input('Does your characters have his father on his face?')
              if aa==1:
                return 'Shigaraki Tomura'
              else:
                return 'Kulogiri'

        else:
          return 'Stain'


MHA()


