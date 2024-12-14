#program that says hello and then asks and displays your name aswell as your age

print('what is your name? ')
name = input( )
print('nice to meet you',name)
print('the length of your name is', len(name),'charectors')
print('how old are you?')
age = input()
print('you are '+ age +' years old, you will be '+ str(int(age)+1)+' next')