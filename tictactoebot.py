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

def winCheck(array, chip):
    #TODO: Check if there is a win (also check if board is full if there is a tie) on the internal board array (var name is board)
    if array[0][0] == chip and array[0][1] == chip and [0][2] == chip: #horizontal 1
        return True
    elif array[1][0] == chip and array[1][1] == chip and array[1][2] == chip: #horizontal 2
        return True
    elif array[2][0] == chip and array[2][1] == chip and array[2][2] == chip: #horizontal 3
        return True
    elif array[0][0] == chip and array[1][0] == chip and array[2][0] == chip: #vertical 1
        return True
    elif array[0][1] == chip and array[1][1] == chip and array[2][1] == chip: #vertical 2
        return True
    elif array[0][2] == chip and array[1][2] == chip and array[2][2] == chip: #vertical 3
        return True
    elif array[0][0] == chip and array[1][1] == chip and array[2][2] == chip: #diagonal 1
        return True
    elif array[2][0] == chip and array[1][1] == chip and array[0][2] == chip: #diagonal 2
        return True
    else: 
        return False
        
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
    blank = " "
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

    await ctx.send("```Welcome to tic-tac-toe!\nPlayer 1 Please say 'ready'```")

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
Each square has an associated number.\n[P1] " + Player1.name + ", choose what number you want to make your first move on (1, 2, 3, etc.)```")

    availableMoves = ['1','2','3','4','5','6','7','8','9']
    
    def checkP1Move(validMove):
        returnVal = False
        for x in availableMoves:
            returnVal = (validMove.content == x)
            print(returnVal)
            if validMove.content == x:
                availableMoves.remove(x)
                break
        return returnVal and validMove.author == Player1
    
    p1move1 = await bot.wait_for('message', check = checkP1Move)
    print (p1move1.content)
    numpad = numpad.replace(p1move1.content, 'X')
    print(board)
    inHouseBoardChange(p1move1.content, board, 'X')
    print(board)

    await ctx.send("```" + numpad + "\nPlayer 2 choose your move.```")

    #TODO: Make second player turn and make loop that goes thru each turn? or figure out how to find end etc.



@bot.command(name='howtoplay', help='Useless command')
async def guide(ctx):
    await ctx.send("```Dude it's tic-tac-toe you should know how to play lol```")

bot.run(TOKEN)