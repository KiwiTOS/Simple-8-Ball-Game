import random, time, os, colorama
from colorama import Fore

while True:
    os.systen('clear') 

    print(f"""
  ______{Fore.MAGENTA}___.          .__  .__   {Fore.RESET}
 /  __  \{Fore.MAGENTA}_ |__ _____  |  | |  |  {Fore.RESET}
 >      <{Fore.MAGENTA}| __ \\__  \ |  | |  |  {Fore.RESET}
/   --   \{Fore.MAGENTA} \_\ \/ __ \|  |_|  |__{Fore.RESET}
\______  /{Fore.MAGENTA}___  (____  /____/____/{Fore.RESET}
       \/ {Fore.MAGENTA}   \/     \/           {Fore.RESET}
    """)

    menu = input(f"""{Fore.BLUE}
   -----------------------------------------------
   | (1): Enter a Question and Shake the 8 Ball  |
   | (2): See 8 Ball Responses                   |
   -----------------------------------------------\n{Fore.RESET}
    >>> """)
    if menu == "1":
        question = input("\nWhat is your question? > ")
        time.sleep(0.5)
        print("\nShaking Magic 8 Ball...\n")

        responses = [
            "🟢 It is certain.",
            "🟢 It is decidedly so.",
            "🟢 Without a doubt.",
            "🟢 Yes definitely.",
            "🟢 You may rely on it.",
            "🟢 As I see it, yes.",
            "🟢 Most likely.",
            "🟢 Outlook good.",
            "🟢 Yes.",
            "🟢 Signs point to yes.",
            "🟡 Reply hazy, try again.",
            "🟡 Ask again later.",
            "🟡 Better not tell you now.",
            "🟡 Cannot predict now.",
            "🟡 Concentrate and ask again.",
            "🔴 Don't count on it.",
            "🔴 My reply is no.",
            "🔴 My sources say no.",
            "🔴 Outlook not so good.",
            "🔴 Very doubtful."
    ]

        time.sleep(0.5)
        print(f"Question - {question}")
        time.sleep(1.0)
        print(f"Result - {random.choice(responses)}\n")
        time.sleep(1.0)
        return1 = input("Press Enter to Return to Main Menu. > ")
        if return1 == "x":
            os.systen('clear') 
    
    if menu == "2":
        print(f"""
            {Fore.BLUE}--------------------
            |-8 BALL RESPONSES-|
            --------------------{Fore.RESET}

            🟢 It is certain.
            🟢 It is decidedly so.
            🟢 Without a doubt.
            🟢 Yes definitely.
            🟢 You may rely on it.
            🟢 As I see it, yes.
            🟢 Most likely.
            🟢 Outlook good.
            🟢 Yes.
            🟢 Signs point to yes.
            🟡 Reply hazy, try again.
            🟡 Ask again later.
            🟡 Better not tell you now.
            🟡 Cannot predict now.
            🟡 Concentrate and ask again.
            🔴 Don't count on it.
            🔴 My reply is no.
            🔴 My sources say no.
            🔴 Outlook not so good.
            🔴 Very doubtful.\n
        """)
        time.sleep(1.0)
        return2 = input("Press Enter to Return to Main Menu. > ")
        if return2 == "x":
            os.systen('clear') 
