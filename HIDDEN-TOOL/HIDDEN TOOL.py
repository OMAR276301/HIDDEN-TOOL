def main():

	import os 
	import sys
	import colorama
	from colorama import Back, Fore, Style
	import time
	import platform
	import signal



	os.system('clear')

	def sigint_handler(signal, frame):
	    os.system('clear')
	    os.system("./banner.sh")
	    print('\n')
	    print('\n')  
	    print(Fore.BLUE +      ' THANKS FOR USING THE TOOL ')
	    time.sleep(6)
	    os.system('clear') 
	    sys.exit(0)
	signal.signal(signal.SIGINT, sigint_handler)
		                                                                 #(DISCLAIMR)


	if platform.uname()[0] == "Windows":
	    print("\n This Tool Only Works On Linux Distributions\n")
	    exit()
	else:
	    pass


	root = os.environ.get('USER')
	if root != "root":
	    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

	os.system("clear")
	os.system("./banner.sh")
	print('\n')
	print('\n')
	print(Fore.RED +'1: This tool is for informational and educational purpose only')
	print('\n')
	print(Fore.RED +'2: Do not attempt to violate the law with anything contained here. If you planned to use the tool for illegal purpose, then please exit this tool immediately! We will not be responsible for your any illegal actions.')
	print('\n')
	print(Fore.RED +'3: You shall not use the tool to gain unauthorised access. However you may try out this tool on your own computer at your own risk. Performing hack attempts (without permission) on computers that you do not own is illegal.')
	print('\n')


	choice = input('\033[31mDO YOU AGREE WITH TERMS ? \033[34m(y/n); ').lower()


	if choice == "n":
		print('\n')
		print('\033[34mSORRY YOU MUST AGREE WITH THE TERMS BYE :)')
		time.sleep(4)
		os.system("clear")
		sys.exit()



	elif choice == "y":
		pass
		
		
	else:
		print('\n')
		print('WRONG INPUT );')
		time.sleep(3)
		os.system("clear")
		sys.exit()


		                                                                 #(HIDDENTOOL)
		                                                                 


	os.system('sudo apt install steghide')
	os.system('clear')
	os.system("./banner.sh") 



	print('\n')
	print('\n')

	colorama.init(autoreset=True)
	print(Fore.BLUE +      ' {1}--EMBED A FILE ')
	print('\n')
	print(Fore.BLUE +      ' {2}--EXTRACT A FILE ')
	print('\n')
	print(Fore.BLUE +      ' {3}--EXIT ')
	print('\n')
	print('\n')

	choice = input(Fore.RED +' HIDDEN TOOL ~# ')
	print('\n')
	if choice == "1":
		hide = input(' \033[0;35m{1}--FILE YOU WANT TO HIDE ----> ')
		coverpic = input(' \033[0;35m{2}--THE COVER OF THE FILE YOU WANT TO HIDE ----> ')
		password = input(' \033[0;35m{3}--PASSWORD FOR THE FILE YOU WANT TO HIDE ----> ')
		mbed = (' steghide embed -ef ' )
		cover = (' -cf ')
		pas= (' -p ')
		time.sleep(3)
		os.system(mbed + hide + cover + coverpic + pas + password)


	elif choice == "2":
		extract = input(' \033[0;35m{1}--FILE YOU WANT TO EXTRACT ----> ')
		passof = input(' \033[0;35m{2}--PASSWORD OF SECRET FILE ----> ')
		output = input(' \033[0;35m{3}--OUTPUT FOR THE NEW FILE ----> ')
		hidden = (' steghide extract -sf ' )
		p = (' -p ')
		out = (' -xf ')
		time.sleep(3)
		os.system(hidden + extract + p + passof + out + output )
		
	elif choice == "3":
		print('\n')
		print("\033[0;35mTHANKS FOR USING THE TOOL BYE :)")
		time.sleep(3)
		os.system("clear")
		exit()
		
	else:
		print("\033[34mHIDDEN TOOL ~#  \033[31m{ WRONG INPUT }")
		
	print('\n')
	print('\n')

	time.sleep(2)	
	restart = input(' \033[34mHIDDEN TOOL ~#  \033[31mDO YOU WANT TO START AGAIN ? ("y/n") ----> ').lower()
	if restart == "y":
	 print('\n')
	 print("\033[35m{OK STARTING THE TOOL} ---->")
	 time.sleep(3)
	 main()

	else:
		print('\n')
		print(" \033[35mTHANKS FOR USING THE TOOL BYE :)")
		time.sleep(3)
		os.system("clear")
		exit()

main()

