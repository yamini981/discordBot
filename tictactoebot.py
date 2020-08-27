import os, discord, time
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD GUILD')

bot = commands.Bot(command_prefix='%')
def inHouseBoardChange(move, array, chip):
    if (move == '1'):
        array[0][0] = chip
    elif (move == '2'):
        array[0][1] = chip
    elif (move == '3'):
        array[0][2] = chip
    elif (move == '4'):
        array[1][0] = chip
    elif (move == '5'):
        array[1][1] = chip
    elif (move == '6'):
        array[1][2] = chip
    elif (move == '7'):
        array[2][0] = chip
    elif (move == '8'):
        array[2][1] = chip
    elif (move == '9'):
        array[2][2] = chip

def winCheck(array, chip, p1name, p2name):
    fullBoard = True #at the moment we assume the board is full. Then, we will go through each element and check if it is empty
    for row in array:
        for e in row:
            fullBoard = fullBoard and e != "" #if at any point, an element is empty, then fullBoard will be set to false

    if array[0][0] == chip and array[0][1] == chip and array[0][2] == chip: #horizontal 1
        if (chip == "X"):
            finalMessage = "```[P1] " + p1name + " has won the game on the top row!\nType %play to play again!```"
        else:
            finalMessage = "```[P2] " + p2name + " has won the game on the top row!\nType %play to play again!```"
        return True, finalMessage
    elif array[1][0] == chip and array[1][1] == chip and array[1][2] == chip: #horizontal 2
        if (chip == "X"):
            finalMessage = "```[P1] " + p1name + " has won the game on the middle row!\nType %play to play again!```"
        else:
            finalMessage = "```[P2] " + p2name + " has won the game on the middle row!\nType %play to play again!```"
        return True, finalMessage
    elif array[2][0] == chip and array[2][1] == chip and array[2][2] == chip: #horizontal 3
        if (chip == "X"):
            finalMessage = "```[P1] " + p1name + " has won the game on the bottom row!\nType %play to play again!```"
        else:
            finalMessage = "```[P2] " + p2name + " has won the game on the bottom row!\nType %play to play again!```"
        return True, finalMessage
    elif array[0][0] == chip and array[1][0] == chip and array[2][0] == chip: #vertical 1
        if (chip == "X"):
            finalMessage = "```[P1] " + p1name + " has won the game on the first column!\nType %play to play again!```"
        else:
            finalMessage = "```[P2] " + p2name + " has won the game on the first column!\nType %play to play again!```"
        return True, finalMessage
    elif array[0][1] == chip and array[1][1] == chip and array[2][1] == chip: #vertical 2
        if (chip == "X"):
            finalMessage = "```[P1] " + p1name + " has won the game on the second column!\nType %play to play again!```"
        else:
            finalMessage = "```[P2] " + p2name + " has won the game on the second column!\nType %play to play again!```"
        return True, finalMessage
    elif array[0][2] == chip and array[1][2] == chip and array[2][2] == chip: #vertical 3
        if (chip == "X"):
            finalMessage = "```[P1] " + p1name + " has won the game on the third column!\nType %play to play again!```"
        else:
            finalMessage = "```[P2] " + p2name + " has won the game on the third column!\nType %play to play again!```"
        return True, finalMessage
    elif array[0][0] == chip and array[1][1] == chip and array[2][2] == chip: #diagonal 1
        if (chip == "X"):
            finalMessage = "```[P1] " + p1name + " has won the game on a diagonal!\nType %play to play again!```"
        else:
            finalMessage = "```[P2] " + p2name + " has won the game on a diagonal!\nType %play to play again!```"
        return True, finalMessage
    elif array[2][0] == chip and array[1][1] == chip and array[0][2] == chip: #diagonal 2
        if (chip == "X"):
            finalMessage = "```[P1] " + p1name + " has won the game on a diagonal!\nType %play to play again!```"
        else:
            finalMessage = "```[P2] " + p2name + " has won the game on a diagonal!\nType %play to play again!```"
        return True, finalMessage
    elif fullBoard:
        finalMessage = "```Looks like you held the game to a tie...\nType %play to play again!```"
        return True, finalMessage
    else: 
        return False, ""
        
@bot.event
async def on_ready(): #when the bot is activated this code will run 
    for guild in bot.guilds: #loop goes through all guilds that the bot is in (only one) and when guild.name is equal to the actual 
        #GUILD environment variable, it will stop going through the loop so that we can then say that we connected to the correct server
        if guild.name == GUILD:
            break

    print( #prints bot name, server name, and server id
        f'{bot.user} is connected to the following server:\n'
        f'{guild.name} (id: {guild.id})'
    )


@bot.command(name='play', help ='Start a game of tic-tac-toe')
async def tictactoeGame(ctx):
    blank = ""
    board = [[blank, blank, blank], [blank, blank, blank], [blank, blank, blank]]

    numpad ="\
      |     |     \n\
   1  |  2  |  3  \n\
______|_____|_____\n\
      |     |     \n\
   4  |  5  |  6  \n\
______|_____|_____\n\
      |     |     \n\
   7  |  8  |  9  \n\
      |     |     \n"

    await ctx.send("```Welcome to tic-tac-toe!\n\nPlayer 1 Please say 'ready'```")

    def checkReady(msg):
        return msg.content == 'ready'

    p1ready = await bot.wait_for('message', check = checkReady)
    Player1 = p1ready.author

    await ctx.send("```Player 1 is " + Player1.name + ".\n\nPlayer 2 Please say 'ready'```")

    p2ready = await bot.wait_for('message', check = checkReady)
    Player2 = p2ready.author

    await ctx.send("```Player 2 is " + Player2.name + ".\n\n\
Here is the board:\n"\
+ numpad + "\n\
Each square has an associated number.```")

    def checkMove(validMove):
        returnVal = False
        for x in availableMoves:
            returnVal = (validMove.content == x)
            if validMove.content == x:
                break
        if (turn == 'X'):
            return returnVal and validMove.author == Player1
        elif (turn == 'O'):
            return returnVal and validMove.author == Player2
    
    availableMoves = ['1','2','3','4','5','6','7','8','9']
    partingMessage = ""
    turn = 'O' #it is currently the X player's turn
    switch = True #Makes it easy to switch between turn 'X' and 'O'
    condition = False
    while (not condition):
        if switch:
            turn = 'X'
            switch = False
        else:
            turn = 'O'
            switch = True
        if not switch:
            await ctx.send("```[P1] " + Player1.name + ", please make your move (choose 1, 2, 3, etc.)```")
        else:
            await ctx.send("```[P2] " + Player2.name + ", please make your move (choose 1, 2, 3, etc.)```")
        move = await bot.wait_for('message', check = checkMove)
        availableMoves.remove(move.content)
        numpad = numpad.replace(move.content, turn)
        inHouseBoardChange(move.content, board, turn)
        await ctx.send("```" + numpad + "```")
        condition, partingMessage = winCheck(board, turn, Player1.name, Player2.name)

    await ctx.send(partingMessage)
        

@bot.command(name='howtoplay', help='Useless command')
async def guide(ctx):
    await ctx.send("```Dude it's tic-tac-toe you should know how to play lol```")

bot.run(TOKEN)