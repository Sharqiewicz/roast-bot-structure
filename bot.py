import discord
import random
import json
from discord.ext import commands

data = json.load(open('roasts.json', 'r'))


client = commands.Bot(command_prefix = ".!.")




async def kick(author):
    await author.kick(reason="reason")

async def ban(author):
    await author.ban(reason="reason")

async def roulette(ctx, user):
    if random.randint(0, 10) < 3:
        await user.edit(voice_channel=None)
    if random.randint(0,30) == 0:
        await kick(user)
    if random.randint(0, 200) == 4:
        await ban(user)

async def extreme_roulette(ctx, user):
    tmp = random.randint(0,1)
    if tmp == 0:
        await ctx.send('Goodbye')
        await user.edit(voice_channel=None)
    else:
        await ctx.send("Ale udało ci się uniknać kary skubańcu!")


@client.event
async def on_ready():
    print('Bot is ready!')

@client.command(aliases=['roastme', 'play'])
async def roast(ctx):
    await roulette(ctx, ctx.author)
    answer = random.choice(data['roasts'])
    await ctx.send(answer)

@client.command(aliases=["roastfelek", "roastcarisma", "feliks", "felek"])
async def roastfeliks(ctx):
    await roulette(ctx, ctx.author)
    answer = random.choice(data['feliks'])
    await ctx.send(answer)

@client.command(aliases=["mieczkowski","roastkamil", "roastmieczyk", "mieczyk"])
async def roastmieczkowski(ctx):
    await roulette(ctx, ctx.author)
    answer = random.choice(data['mieczkowski'])
    await ctx.send(answer)

@client.command(aliases=["wiktor","wito", "vito", "polo", "vitopolo"])
async def polak(ctx):
    await roulette(ctx, ctx.author)
    answer = random.choice(data['wiktor'])
    await ctx.send(answer)

@client.command(aliases=["DJ", "dj"])
async def janczyk(ctx):
    await roulette(ctx, ctx.author)
    answer = random.choice(data['janczyk'])
    await ctx.send(answer)

@client.command(aliases=["czy", "dlaczego"])
async def pytanie(ctx, *, question):
    await roulette(ctx, ctx.author)
    say = random.choice(data['question_answers'])
    await ctx.send(f'Pytanie: {question}? Odpowiedz: {say}')

@client.command()
async def losu(ctx):
    await roulette(ctx, ctx.author)
    author = ctx.author.name
    say = random.choice(data['losy'])
    await ctx.send(f'{author} to {say}')

@client.command()
async def jestem(ctx):
    await roulette(ctx, ctx.author)
    author = ctx.author
    nickname = random.choice(data['losy'])
    await author.edit(nick=nickname)




@client.command(aliases=["black", "b", "c"])
async def czarny(ctx, *, count):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_currency(users, ctx.author)

    if await check_amount(users,ctx.author, count):
        los_bet = los_bet = await get_color()
        await ctx.send(f'Wylosowany kolor: {los_bet}')
        if(los_bet == 'czarny'):
            await add_currency(users, ctx.author, count)
            await ctx.send(f'Wygrałeś!')
            await ctx.send(await get_amount(users, ctx.author))
        else:
            await erase_currency(users,ctx.author, count)
            await extreme_roulette(ctx, ctx.author)
            await ctx.send(await get_amount(users, ctx.author))

        with open('users.json', 'w') as f:
            json.dump(users, f)
    else:
        await ctx.send('Nie masz hajsu pipko')


@client.command(aliases=["red", "r", "cz"])
async def czerwony(ctx, *, count):

    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_currency(users, ctx.author)

    if await check_amount(users,ctx.author, count):
        los_bet = los_bet = await get_color()
        await ctx.send(f'Wylosowany kolor: {los_bet}')
        if(los_bet == 'czerwony'):
            await add_currency(users, ctx.author, count)
            await ctx.send(f'Wygrałeś!')
            await ctx.send(await get_amount(users, ctx.author))
        else:
            await erase_currency(users,ctx.author, count)
            await extreme_roulette(ctx, ctx.author)
            await ctx.send(await get_amount(users, ctx.author))

        with open('users.json', 'w') as f:
            json.dump(users, f)
    else:
        await ctx.send('Nie masz hajsu pipko')



@client.command(aliases=["green", "g", "z"])
async def zielony(ctx, *, count):

    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_currency(users, ctx.author)

    if await check_amount(users,ctx.author, count):
        los_bet = await get_color()
        await ctx.send(f'Wylosowany kolor: {los_bet}')
        if(los_bet == 'zielony'):
            await add_currency(users, ctx.author, ( int(count) * 14 ))
            await ctx.send(f'Wygrałeś!')
            await ctx.send(await get_amount(users, ctx.author))
        else:
            await erase_currency(users,ctx.author, count)
            await extreme_roulette(ctx, ctx.author)
            await ctx.send(await get_amount(users, ctx.author))

        with open('users.json', 'w') as f:
            json.dump(users, f)
    else:
        await ctx.send('Nie masz hajsu pipko')



@client.command(aliases=["hajs", 'szmal', 'siano', 'forsa', 'mamona', 'konto', 'pieniadze', 'account', 'stan', 'ziemniaki', 'szekle', 'PLN', 'dolce'])
async def money(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        await ctx.send(await get_amount(users, ctx.author))

@client.command(aliases=["board", "tabela", "gra", "tablea", "tbalea"])
async def leaderboard(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        await ctx.send('--------------------------------LEADERBOARD-----------------------------')
        for attr, value in users.items():
            await ctx.send("Gracz: " + str(attr) + " --- Szekle: " + str(value['money']))
        await ctx.send('------------------------------------------------------------------------')

@client.command()
async def earn(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
    if random.choice([True, False, True]):
        tmp = random.choice([1,2,3,4,5])
        await ctx.send('Trzymaj biedaku ' + str(tmp) + " Szekli")
        await add_currency(users, ctx.author, tmp)
        await ctx.send(await get_amount(users, ctx.author))
    else:
        await ctx.send("Nie i chuj")
    with open('users.json', 'w') as f:
        json.dump(users, f)



async def get_color():
    tmp = random.randint(0,100)
    if tmp <= 3:
        color = 'zielony'
    elif tmp >= 53:
        color = 'czerwony'
    elif tmp <= 52:
        color = 'czarny'
    return color

async def check_amount(users, user, count):
    return ( users[user.name]['money'] > 0 and users[user.name]['money'] >= int(count) )


async def update_currency(users, user):
    if not user.name in users:
        users[user.name] = {}
        users[user.name]['money'] = 269

async def add_currency(users, user, money):
    users[user.name]['money'] += int(money)

async def erase_currency(users,user,money):
    users[user.name]['money'] -= int(money)

async def get_amount(users, user):
    await update_currency(users, user)
    mn = users[user.name]['money']
    return f'@{user.name} Na koncie masz {mn}'




client.run('TOKEN')
