## If conditions 
if True:
    print('bioinfo conditions are good')
if False:
    print('bioinfo conditions are good')

## if-else conditions
code_lang = 'python'
if code_lang == 'java':
    print('Yeah, its python!')
else: 
    print('no, its not')

## if-elif-else conditions
bioinformatics_stats_lang = 'R'
if bioinformatics_stats_lang == 'pyhton': 
    print('no, not true')
    
elif bioinformatics_stats_lang == 'perl':
    print('still wrong')
elif bioinformatics_stats_lang == 'bashscript':
    print('nope')
else: 
    print('the answer is R programming for getting the best statistic outputs for bioinformatics analyses')

## booleans conditions using if-elif-else 
user = 'rukaiya'
bioinformatician = True
if user == 'rukaiya' and bioinformatician == False:
    print('career will be content creator')
elif user == 'zeenat' or bioinformatician == False:
    print('thats not me')
elif user == 'rukaiya' and not bioinformatician == True:
        print('career will be educational content creator')
elif user == 'rukaiya' and bioinformatician == True:
    print('dream career')
else: 
    print('career is a gone case')




