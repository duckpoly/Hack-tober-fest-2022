 while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low #or high 
        feedback=input((f'Is {guess} too high(h), too low(l), or correct(c)'))
        if feedback == 'h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
