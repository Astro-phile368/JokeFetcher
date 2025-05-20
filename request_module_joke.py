import requests
#print(r)
while True:
   try:
        r = requests. get('https://official-joke-api.appspot.com/jokes/random')
        if r. status_code == 200:
            print('connected to joke \n')       
            pr = r. json()
            jock= pr['setup']
            ans=pr['punchline']        
            print(f'joke :-  {jock}')
            input('press enter to see answer')
            print(f'ans:- {ans}')
            print()
            a= input(f'need another joke yes[y]/no[n] ;-'). strip(). lower()
            if a!= 'y':
                print('bye')
                break
        else:
            print('failed to connected pls restart')   
            break 
           
   except:     
       print('unable to connect pls check your internet connection')                        
       break