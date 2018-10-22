import discord
import asyncio
import random
import time
import datetime
import requests
import json
import wikipedia
wikipedia.exceptions
import io
import os
import pyfiglet

tempo = []

try:
    from urllib.request import urlretrieve
except Exception as e:
    pass

players = {}
COR = 0xF7FE2E

COR =0x690FC3
msg_id = None
msg_user = None

COR = 0x9910CD

client = discord.Client()

#comandos para deixar o bot online

@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ MUNDO')
    print(client.user.name)
    print(client.user.id)
    print('-----PNS------')
    print('O bot foi executado com sucesso e está Online no momento')


    await client.change_presence(game=discord.Game(name="Não sabe meus Comandos? Digite: gb!ajuda", type=1, url='https://www.twitch.tv/gamebotbr'),
                       status='streaming')




@client.event
async def on_message(message):
    if message.content.lower().startswith('gb!cmd1'):
        await client.send_message(message.channel,"```O servidor entrará em manutenção```")


    if message.content.lower().startswith('gb!gamelist'):
        Embed = discord.Embed(color=0x000000, description="Ok, aqui esta seus comandos!")
        Embed.add_field(name='gb!crossfire', value="CrossFire", inline=False)
        Embed.add_field(name='gb!minecraft', value="Minecraft", inline=False)
        Embed.add_field(name='gb!fortnite', value="Fortnite", inline=False)
        Embed.add_field(name='gb!rainbowsix', value="RainbowSix", inline=False)
        Embed.add_field(name='gb!freefire', value="FreeFire", inline=False)
        Embed.add_field(name='gb!pubg', value="PLAYERUNKNOWN'S BATTLEGROUNDS", inline=False)
        Embed.add_field(name='gb!lol', value="League of Legends", inline=False)
        Embed.add_field(name='gb!eurotruck', value="Euro Truck Simulator", inline=False)
        Embed.add_field(name='gb!farcry', value="FarCry", inline=False)
        Embed.add_field(name='gb!gta', value="Grand Theft Auto", inline=False)
        await client.send_message(message.channel, embed=Embed)
##############################################################################################
    if message.content.startswith("gb!pubg"):
        embed = discord.Embed(color=0x191970, description = "")
        embed.set_image(url="https://http2.mlstatic.com/playerunknowns-battlegrounds-pubg-original-steam-pc-D_NQ_NP_7217"
                            "25-MLB26563476758_122017-F.jpg")
        embed.add_field(name="PUBG", value="PlayerUnknown's Battlegrounds, ou somente Battlegrounds, é um jogo eletrônic"
                                           "o multiplayer desenvolvido pela PUBG Corp., subsidiária da produtora coreana"
                                           " Bluehole, utilizando o motor de jogo Unreal Engine 4.", inline=False)
        await client.send_message(message.channel, embed=embed)
############################################################################################################
    if message.content.startswith("gb!minecraft"):
        embed = discord.Embed(color=0x191970, description="")
        embed.set_image(
            url="https://minecraft.net/static/pages/img/index-hero-og.088fb7996b03.jpg")
        embed.add_field(name="Minecraft",
                        value="Minecraft é um jogo eletrônico tipo sandbox e independente de mundo aberto que permite a" 
                              " construção usando blocos dos quais o mundo é feito. Foi criado por Markus Notch Persson." 
                              "O desenvolvimento de Minecraft começou por volta do dia 10 de maio de 2009"
                              ". ", inline=False)
        await client.send_message(message.channel, embed=embed)
###########################################################################################
    if message.content.startswith("gb!fortnite"):
        embed = discord.Embed(color=0x191970, description="")
        embed.set_image(
            url="https://cdn2.unrealengine.com/Fortnite%2Fbattle-royale%2Fseason6-social-1920x1080-0a72ec2f35dfe5be6cf8a77ec16063cca4db7046.jpg")
        embed.add_field(name="Fortnite",
                        value="Fortnite é um jogo eletrônico online criado em 2017, desenvolvido pela Epic Games, e lançado como diferentes pacotes de software com diferentes modos de jogo que compartilham a mesma jogabilidade e motor gráfico de jogo.  ", inline=False)
        await client.send_message(message.channel, embed=embed)
########################################################################################################################
    if message.content.startswith("gb!lol"):
        embed = discord.Embed(color=0x191970, description="")
        embed.set_image(
            url="https://digitalks.com.br/wp-content/uploads/2017/07/league-of-legends.png")
        embed.add_field(name="League of Legends",
                        value="League of Legends é um jogo eletrônico do gênero multiplayer online battle arena, desenvo"
                              "lvido e publicado pela Riot Games para Microsoft Windows e Mac OS X. É um jogo gratuito "
                              "para jogar e inspirado no modo Defense of the Ancients de Warcraft III: "
                              "The Frozen Throne.", inline=False)
        await client.send_message(message.channel, embed=embed)
############################################################
    prefixo = "gb!"
    if message.content.startswith(prefixo+'wiki'):
        try:
            a = len(prefixo) + 5
            query = message.content[a:]
            q = wikipedia.page(query)
            summary = wikipedia.summary(query, sentences=5)
            wikipedia.set_lang('pt')
            embed = discord.Embed(title='Wikipedia:', description=f'{summary} \n\nPara mais informações [**clique aqui**]({q.url})', color=0x002eff)
            await client.send_message(message.channel, embed=embed)
        except wikipedia.exceptions.PageError:
            await client.send_message(message.channel, "Não consegui achar nada com esse nome :/")
        except IndexError:
            return await client.send_message(message.channel, "Oque eu deverei procurar ?")
#############################################################################################

##########################################################################
    if message.content.lower().startswith('gb!userinfo'):
        try:
            user = message.mentions[0]
            server = message.server
            embedinfo = discord.Embed(title='Informações do usuário', color=0x03c3f5)
            embedinfo.set_thumbnail(url=user.avatar_url)
            embedinfo.add_field(name='Usuário:', value=user.name, inline=True)
            embedinfo.add_field(name='Apelido', value=user.nick, inline=True)
            embedinfo.add_field(name='ID:', value=user.id, inline=True)
            embedinfo.add_field(name='Entrou em:', value=user.joined_at.strftime("%d %b %Y às %H:%M"), inline=True)
            embedinfo.add_field(name='Server criado em:', value=server.created_at.strftime("%d %b %Y %H:%M"),
                                inline=True)
            embedinfo.add_field(name='Jogando:', value=user.game, inline=True)
            embedinfo.add_field(name="Status:", value=user.status, inline=True)
            embedinfo.add_field(name='Cargos:', value=([role.name for role in user.roles if role.name != "@everyone"]),
                                inline=True)

            embedinfo.set_footer(
                text="GameBot © 2018"


            )

            await client.send_message(message.channel, embed=embedinfo)
        except ImportError:
            await client.send_message(message.channel, 'Buguei!')
        except:
            await client.send_message(message.channel, '| Mencione um usuário válido!')
        finally:
            pass
########################################################################################################################

    if message.content.lower().startswith('gb!ping'):
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping_embed = discord.Embed(title="🏓 Pong!", color=0x000000,
                                   description='Calculei aqui e é: `{}ms`!'.format(round((t2 - t1) * 1000)))
        await client.send_message(message.channel, f"{message.author.mention}", embed=ping_embed)
########################################################################################################
    if message.content.startswith("gb!contagem"):
        mensagem = "**5**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**4**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**3**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**2**"
        await client.send_message(message.channel, mensagem)
        await asyncio.sleep(1)
        mensagem = "**1**"
        await client.send_message(message.channel, mensagem)

    if message.content.lower().startswith("gb!gb"):
        sn = random.choice('abcd')
        if sn == 'a':
            await client.send_message(message.channel, '{0.author.mention} Claro'.format(message))
            await client.add_reaction(message, '👍')
        if sn == 'b':
            await client.send_message(message.channel, '{0.author.mention} Nem ferrando'.format(message))
            await client.add_reaction(message, '👿')
        if sn == 'c':
            await client.send_message(message.channel, '{0.author.mention} Talvez'.format(message))
            await client.add_reaction(message, '😶')
        if sn == 'd':
            await client.send_message(message.channel, '{0.author.mention} https://permita.me/?q=Como+usar+o+Google?'.format(message))
            await client.add_reaction(message, '🤔')

    if message.content.lower().startswith('gb!mute'):
        try:
            if not message.author.server_permissions.administrator:
                return await client.send_message(message.channel,
                                                 '**Parsa TÁ FICANDO LOKO?, você não tem permissão pra fazer isso!!!**')
            author = message.author.mention
            user = message.mentions[0]
            motivo = message.content[29:]
            cargo = discord.utils.get(message.author.server.roles, name='</Mute/>')
            await client.add_roles(user, cargo)
            await client.send_message(message.channel,
                                      '*__O usuário: {} foi mutado pelo Administrador__*: {} pelo motivo: {}.'.format(
                                          user.mention, author, motivo))
        except:
            await client.send_message(message.channel, "**__Ou, se nao selecionou ninguem para mutar.__**")

    if message.content.lower().startswith('gb!unmute'):
        try:
            if not message.author.server_permissions.administrator:
                return await client.send_message(message.channel,
                                                 ' Bro,se tá pensando que vai dar Un-mute em alguém?Tá enganado.')
            author = message.author.mention
            user = message.mentions[0]
            motivo = message.content[29:]
            cargo = discord.utils.get(message.author.server.roles, name='</Mute/>')
            await client.remove_roles(user, cargo)
            await client.send_message(message.channel,
                                      'O usuário: {} foi desmutado pelo Administrador: {} pelo motivo: {}.'.format(
                                          user.mention, author, motivo))
        except:
            await client.send_message(message.channel, "Olha bem, você não selecionou ninguém pra desmutar.")


#####################################################################
    if message.content.lower().startswith('gb!moeda'):
        escolha = random.randint(1, 2)
        if  escolha == 1:
            await client.add_reaction(message, '😀')
            await client.send_message(message.channel, "Cara!")
        if escolha == 2:
            await client.add_reaction(message, '👑')
            await client.send_message(message.channel, "Coroa!")
#################################################################################################################
    if message.content.lower().startswith('gb!bavatar'):
        if message.author.id == '296428519947370499':
            try:
                link = message.content[11:].strip()
                urlretrieve(link, 'pp.jpg')
                with open("pp.jpg", "rb") as imageFile:
                    file = imageFile.read()
                bytelike = bytearray(file)
                await client.edit_profile(avatar=bytelike)
                await client.send_message(message.channel, 'Beleza véi!')
                await client.delete_message(message)
            except:
                await client.send_message(message.channel, 'Confere o Link aí parsa, por que tem algo errado!')
        else:
            await client.send_message(message.channel, 'Você não tem permissões para fazer isso, só o Mestre Punisher '
                                                       'pode!')
#################################################################################################

############################################################################################################
    if message.content.lower().startswith('gb!vote'):
        votee = message.content[8:].strip()
        votee = await client.send_message(message.channel,
                                          message.author.mention + " **Iniciou uma votação Top **\n\n``" + votee + "``")
#############################################################################################################
        await client.delete_message(message)
        await client.add_reaction(votee, '👍')
        await client.add_reaction(votee, '👎')
########################################################################################################
    if message.content.lower().startswith("gb!sorteio"):  # esse comandos sorteia um memebro
        if message.author.server_permissions.administrator:
            n = random.choice(list(message.server.members))
            n1 = '{}'.format(n.name)
            m1 = discord.utils.get(message.server.members, name="{}".format(n1))
            embed = discord.Embed(
                title="Sorteiar membro",
                colour=0xab00fd,
                description="Membro sorteado foi {}".format(m1.mention)
            )
            hh = await client.send_message(message.channel, "{}".format(m1.mention))
            await client.delete_message(hh)
            await client.send_message(message.channel, embed=embed)
        else:
            await client.send_message(message.channel,"{} você não tem permissão de executar esse comando!".format(message.author.mention))
############################################################################
    if message.content.lower().startswith('gb!cargo'):
        if message.author.server_permissions.manage_roles:
            try:
                a = message.mentions[0]
                b = str(message.content).split()
                c = b[2]
                d = discord.Object(id="{}".format(int(str(c).strip("<>@&"))))
                await client.add_roles(a, d)
                await client.send_message(message.channel, "O cargo {} foi adiciona no(a) {}".format(c, a.mention))
            except:
                await client.send_message(message.channel, "{} o comando esta faltando o usuario ou o cargo".format(
                    message.author.mention))
        else:
            await client.send_message(message.channel,
                                      "{} Você não tem permissão de usar esse comando".format(message.author))
##############################################################################
    if message.content.startswith('gb!hora'):
        # importe o time e datetime
        horario = datetime.datetime.now().strftime("%H:%M:%S")
        await client.send_message(message.channel,
                                  "**Quer saber a  hora local atual"
                                  ", tão tá né então toma o horário do {} **{}".format(message.server.region, horario))
        await client.send_message(message.channel,
                                  "**Esta hora e de acordo com a localização do servidor, no caso desse servidor a loca"
                                  "lização dele e** {}".format(
                                      message.server.region))

    if message.content.startswith('gb!denunciar'):
        await client.send_message(message.author,
                                  '**Qual úsuario você deseja denunciar? {}**'.format(message.author.mention))
        jogador = await client.wait_for_message(author=message.author)
        await client.send_message(message.author, '**Qual o motivo da denuncia? {}**'.format(message.author.mention))
        motivo = await client.wait_for_message(author=message.author)
        await client.send_message(message.author, '**Que dia aconteceu isso? {}**'.format(message.author.mention))
        dia = await client.wait_for_message(author=message.author)
        await  client.send_message(message.author, '**Prova já hospedada senhor {}:**'.format(message.author.mention))
        prova = await client.wait_for_message(author=message.author)
        canal = client.get_channel('495028044986187788')
        embed = discord.Embed(colour=0xF0000,
                              description="O Úsuario: {} acabou de denunciar!".format(message.author.mention))
        embed.add_field(name='?Motivo:', value=motivo.content)
        embed.add_field(name='??Data do ocorrido:', value=dia.content)
        embed.add_field(name='??Prova:', value=prova.content)
        embed.add_field(name='??Úsuario denunciado:', value=jogador.content)
        await client.send_message(canal, embed=embed)
##################################################################################################
    if message.content.startswith('gb!feed'):
        msg = message.content[6:]
        member = message.author
        server = message.server
        channel = client.get_channel('495032687518547989')

        embed = discord.Embed(title='FeedBack')
        embed.add_field(name='Info',
            value=f'? Server: {server.name}\n ServerID: {server.id}\n Usuario: {member.name}\n UsuarioID: {member.id}')
        embed.add_field(name='Feed', value=f'{msg}', inline=False)
        await client.send_message(channel, embed=embed)

    if message.content.lower().startswith('gb!botinfo'):
        await client.delete_message(message)
        embedbot = discord.Embed(
            title='** Informações do Bot**',
            color=0x00a3cc,
            description='\n'
        )
        embedbot.set_thumbnail(
            url="https://i.imgur.com/2GHenCV.png")  # Aqui você coloca a url da foto do seu bot!
        embedbot.add_field(name=' |🔵 Nome', value=client.user.name, inline=True)
        embedbot.add_field(name=' |🔴 Id bot', value=client.user.id, inline=True)
        embedbot.add_field(name=' |🗓 Criado em', value=client.user.created_at.strftime("%d %b %Y %H:%M"))
        embedbot.add_field(name=' |🏷 Tag', value=client.user)
        embedbot.add_field(name=' |🎨 Avatar', value=f'Clique [aqui](https://www.mediafire.com/convkey/db4a/sjc4fbjqwfwxp6d7g.jpg)')
        embedbot.add_field(name=' |📂 Servidores', value=len(client.servers))
        embedbot.add_field(name=' |🌎 Usuarios', value=len(list(client.get_all_members())))
        embedbot.add_field(name=' |<:heroku:500708290356051983> Hospedagem', value='Heroku')
        embedbot.add_field(name=' |⚠ Prefixo', value='gb!')
        embedbot.add_field(name=' |🗺️Região  ', value = str(message.server.region).title(), inline = True)
        embedbot.add_field(name=' |🌐 Status ', value=message.server.get_member(client.user.id).status)
        embedbot.add_field(name=' |<:python:500701558271377419> Linguagem', value='Python')
        embedbot.add_field(name=' |<:pycharm:500720469431812096> Programa', value='Pycharm')
        embedbot.add_field(name=' |👨‍💻 Programador', value="`Punisher`")# Aqui você coloca seu nome/discord
        embedbot.add_field(name=' |✉ Adicionar Bot', value=f'Clique [aqui](https://discordapp.com/oauth2/authorize?client_id=491061703493156875&scope=bot&permissions=8)')
        embedbot.add_field(name=' |Python  |<:python:500701558271377419> Version',
                           value="`3.6.6`")  # Aqui você coloca a versão do python que você está utilizando!
        embedbot.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)

        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        embedbot.add_field(name="🏓 Ping!", value='Meu tempo de resposta é `{}ms`!'.format(round((t2 - t1) * 1000)),
                        inline=True)

        await client.send_message(message.channel, embed=embedbot)
###############################################################################

    if message.content.lower().startswith('gb!news'):
        reqnews = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=globo&apiKey=6888a62938c744a79d4dec22809ba3d1')
        lernews = json.loads(reqnews.text)
        authornews = (str(lernews['articles'][0]['author']))
        titulonews = (str(lernews['articles'][0]['title']))
        descriptionnews = (str(lernews['articles'][0]['description']))
        urlnews = (str(lernews['articles'][0]['url']))
        datanews = (str(lernews['articles'][0]['publishedAt']))
        imgnews = (str(lernews['articles'][0]['urlToImage']))
        embednews = discord.Embed(color=0x65ff00)
        embednews.add_field(name='Autor Da notícia:', value="{}".format(authornews))
        embednews.add_field(name='Título:', value="{}".format(titulonews))
        embednews.add_field(name='Descrição:', value="{}".format(descriptionnews))
        embednews.add_field(name='Link da noticia:', value="{}".format(urlnews))
        embednews.set_footer(text='Data da noticia: ' + datanews)
        embednews.set_thumbnail(url=imgnews)
        await client.send_message(message.channel, embed=embednews)
#################################################################################################
    if message.content.startswith('gb!tempo'):
       x = message.author.id
       if not x in tempo:
          await client.send_message(message.channel, 'testado')
          tempo.append(x)
          await asyncio.sleep(5)
          tempo.remove(x)
       else:
         await client.send_message(message.channel, '**Você tem que aguarda 5 segundos mano!!**')
########################################################################################################################
    if message.content.lower().startswith('gb!ajuda'):
        Embed = discord.Embed(color=0x191970, description="**Ok, aqui esta todos os comandos do Servidor**!")
        Embed.add_field(name='gb!gamelist', value="Lista de códigos de **jogos**.", inline=False)
        Embed.add_field(name='gb!wiki', value="Você consegue pesquisar na **Wikipédia!!**", inline=False)
        Embed.add_field(name='gb!userinfo', value="**Informações** do Usuário", inline=False)
        Embed.add_field(name='gb!ping', value="Quer ver seu **Ping?**Tá aí!!!", inline=False)
        Embed.add_field(name='gb!contagem', value="O Bot irá **Contar até CINCO**", inline=False)
        Embed.add_field(name='gb!gb', value="Responde sua pergunta com **mensagens** gravadas!!!", inline=False)
        Embed.add_field(name='gb!mute', value="Alguém está de irritando?**Toma Mute!!!**", inline=False)
        Embed.add_field(name='gb!unmute', value="Ficou com dó?**Ele desmuta!!!**", inline=False)
        Embed.add_field(name='gb!say', value="Quer que eu diga algo?**Toma-lhe Say**", inline=False)
        Embed.add_field(name='gb!moeda', value="**Cara ou coroa?**Temos esse Comando também!!!", inline=False)
        Embed.add_field(name='gb!limpar', value="Serve para **limpar as conversas** acumulantes!!", inline=False)
        Embed.add_field(name='gb!vote', value="**Inicia uma votação** maneira!!!", inline=False)
        Embed.add_field(name='gb!sorteio', value="**Sorteia membros** IRADOS", inline=False)
        Embed.add_field(name='gb!cargo', value="Preguiça de colocar cargo?Não se preocupe, existe"
                                                  "GameBot!!! ** ", inline=False)
        Embed.add_field(name='gb!hora', value="Quer **ver a hora**?Ok!", inline=False)
        Embed.add_field(name='gb!denunciar', value="Quer **denunciar alguém?**Ai está!!!", inline=False)
        Embed.add_field(name='gb!feed', value="Quer **dar um Feedback? **Ai está!!!", inline=False)
        Embed.add_field(name='gb!botinfo', value="Quer **saber sobre o Bot?**Então tá né, quer saber de mim, OK!!!",
                           inline=False)
        Embed.add_field(name='gb!news', value="Quer **ver uma notícia? **Dá esse comando que é bala!!!",
                           inline=False)
        Embed.add_field(name='gb!juntarnomes', value="Quer **juntar nomes? **Falo nada!!!", inline=False)
        Embed.add_field(name='gb!servers', value="Quer **em quais Servers estou? **Preciso falar?!", inline=False)
        Embed.add_field(name='gb!incrivelist',
                           value="Quer **ver os Comandos incríveis?**Desculpa cansei, mas você sabe né?", inline=False)
        await client.send_message(message.author, embed=Embed)
        await client.send_message(message.channel, embed=Embed)

           ################################################################
    if message.content.startswith('gb!incrível'):
        await client.send_message(message.channel, 'Quem é incrível? Digite **gb!nome** @NomeDoUsuario')
        def check(msg):
            return msg.content.startswith('gb!nome')
        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('gb!nome'):].strip()
        await client.send_message(message.channel, '{} **Realmente, é muito incrível!!!**'.format(name))
###########################################################
    if message.content.startswith('gb!chato'):
        await client.send_message(message.channel, 'Eita! Quem é chato? Digite **gb!nome** @NomeDoUsuario')
        def check(msg):
            return msg.content.startswith('gb!nome')
        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('gb!nome'):].strip()
        await client.send_message(message.channel, '{} ```**Vish, vai dar treta, mas sou programado pra falar: É, '
                                                   'realmente.**``` '.format(name))
#########################################################
    if message.content.startswith('gb!linda'):
        await client.send_message(message.channel, 'Opaa!! Quem é Lindo (a) ?? Digite **gb!nome** @NomeDoUsuario')
        def check(msg):
            return msg.content.startswith('gb!nome')
        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('gb!nome'):].strip()
        await client.send_message(message.channel, '{} **É verdade, muito Linda (o), concordo. Passa WhatsApp ?**'
                                                   ' '.format(name))
###################################################
    if message.content.lower().startswith('gb!juntarnomes'):
        try:
            cont = message.mentions[0].name
            cont2 = message.mentions[1].name
            cont3 = len(cont2)
            cont4 = cont3 - 4
            cont5 = cont[0:4]
            cont6 = cont2[cont4:cont3]
            cont7 = cont5 + cont6
            await client.send_message(message.channel,
                                      "Junção do nome de {} com {} = **{}**".format(message.mentions[0].mention,
                                                                                    message.mentions[1].mention, cont7))
        except IndexError:
            await client.send_message(message.channel,
                                      "{} Você não mencionou dois usuarios".format(message.author.mention))

    if message.content.startswith("gb!kick"):
        if not message.author.server_permissions.kick_members:
            return await client.send_message(message.channel,
                                             "**Você não tem permissão para executar esse comando bobinho(a)!**")
        try:
            user = message.mentions[0]
            await client.send_message(message.channel,
                                      "**O usuário(a) <@{}> foi kickado com sucesso do servidor.HAHAHAHA"
                                      "**".format(user.id))
            await client.kick(user)
        except:
            await client.send_message(message.channel, "**Você deve especificar um usuario para kickar!**")
##################################################
    if message.content.startswith("gb!servers"):
            servidores = '\n'.join([s.name for s in client.servers])
            embe = discord.Embed(title="Estou online em " + str(len(client.servers)) + " servidores com " + str(
                len(set(client.get_all_members()))) + " membros!",
                                color=COR,
                                description=servidores)
            await client.send_message(message.channel, embed=embe)
######################################################################
    if message.content.startswith('gb!help'):
        ajuda = discord.Embed(title="Comandos do GameBot!", description="Todos os comandos disponiveis do GameBot", color=0x660066)
        ajuda.set_author(name="E ai, beleza?Sou GameBot! ", icon_url="https://imgur.com/a/R2L4g0a.png")
        ajuda.set_thumbnail(url="https://imgur.com/a/R2L4g0a.png")
        ajuda.add_field(name="gb!gamelist", value="Lista de comandos de Jogos", inline=False)
        ajuda.add_field(name="gb!lista1", value="A Lista 1, a lista da Zoeira!", inline=False)
        ajuda.add_field(name="gb!lista2", value="Lista 2 , a lista de coisas inúteas!", inline=False)
        ajuda.add_field(name="gb!lista3", value="Lista 3 , para Moderadores e Administradores", inline=False)
        ajuda.set_image(url="https://imgur.com/a/R2L4g0a")
        ajuda.set_footer(
            text=">>Clique no ❌ para fechar<<             1/3")  ## icon_url="https://i.imgur.com/rdm3W9t.png")

        botmsghelp = await client.send_message(message.channel, embed=ajuda)

        await client.add_reaction(botmsghelp, "⏮")
        await client.add_reaction(botmsghelp, "⏪")
        await client.add_reaction(botmsghelp, "⏹")
        await client.add_reaction(botmsghelp, "⏩")
        await client.add_reaction(botmsghelp, "⏭")
        await client.add_reaction(botmsghelp, "❌")  # fecha mensagem

        msg_id = botmsghelp.id
        msg_user = message.author

        @client.event
        async def on_reaction_add(reaction, user):
            msg = reaction.message
            if reaction.emoji == "❌" and msg.id == msg_id and user == msg_user:
                await client.delete_message(msg)
                await asyncio.sleep(0.2)
                await client.send_message(msg.channel, "{} **Fechou a Mensagem**".format(msg_user.mention))
                print("remove")

            if reaction.emoji == "⏩" and msg.id == msg_id and user == msg_user:
                ajuda = discord.Embed(title="Comandos novos do GameBot", description="Todos os comandos disponiveis do Bot",
                                      color=0x660066)
                ajuda.set_author(name="E ai, denovo, beleza? 💜", icon_url="https://imgur.com/a/R2L4g0a.png")
                ajuda.set_thumbnail(url="https://imgur.com/a/R2L4g0a.png")
                ajuda.add_field(name="m!uptime", value="Mostra o tempo que o bot esta Online", inline=False)
                ajuda.add_field(name="m!Ping", value="Ping do Bot", inline=False)
                ajuda.add_field(name="m!serverinfo", value="Veja algumas informações do server", inline=False)
                ##ajuda.set_image(url="")
                ajuda.set_footer(
                    text=">>Clique no ❌ para fechar<<             2/3")  ## icon_url="https://i.imgur.com/rdm3W9t.png")
                await client.edit_message(msg, embed=ajuda)

            if reaction.emoji == "⏪" and msg.id == msg_id and user == msg_user:
                ajuda = discord.Embed(title="Comandos do bot", description="Todos os comandos disponiveis do BOT",
                                      color=0x660066)
                ajuda.set_author(name="olá eu sou Mitsu 💜", icon_url="https://i.imgur.com/5R1LPwv.jpg")
                ajuda.set_thumbnail(url="https://i.imgur.com/mntKcWT.jpg")
                ajuda.add_field(name="m!uptime", value="Mostra o tempo que o bot esta Online", inline=False)
                ajuda.add_field(name="m!Ping", value="Ping do Bot", inline=False)
                ajuda.add_field(name="m!serverinfo", value="Veja algumas informações do server", inline=False)
                ##ajuda.set_image(url="")
                ajuda.set_footer(
                    text=">>Clique no ❌ para fechar<<             2/3")  ## icon_url="https://i.imgur.com/rdm3W9t.png")
                await client.edit_message(msg, embed=ajuda)
            if reaction.emoji == "⏮" and msg.id == msg_id and user == msg_user:
                ajuda = discord.Embed(title="Comandos do bot", description="Todos os comandos disponiveis do BOT",
                                      color=0x660066)
                ajuda.set_author(name="olá eu sou Mitsu 💜", icon_url="https://i.imgur.com/5R1LPwv.jpg")
                ajuda.set_thumbnail(url="https://i.imgur.com/mntKcWT.jpg")
                ajuda.add_field(name="m!elo", value="Selecionar o seu elo no lolzinho", inline=False)
                ajuda.add_field(name="m!lane", value="Selecionar a sua lane favorita no lolzinho", inline=False)
                ajuda.add_field(name="m!eco", value="Aumenta sua mengagem não use sempre", inline=False)
                ajuda.add_field(name="m!flipc", value="Joguinho de cara ou coroa", inline=False)
                ##ajuda.set_image(url="")
                ajuda.set_footer(
                    text=">>Clique no ❌ para fechar<<             1/3")  ## icon_url="https://i.imgur.com/rdm3W9t.png")
                await client.edit_message(msg, embed=ajuda)
            if reaction.emoji == "⏭" and msg.id == msg_id and user == msg_user:
                ajuda = discord.Embed(title="Comandos do bot", description="Todos os comandos disponiveis do BOT",
                                      color=0x660066)
                ajuda.set_author(name="olá eu sou Mitsu 💜", icon_url="https://i.imgur.com/5R1LPwv.jpg")
                ajuda.set_thumbnail(url="https://i.imgur.com/mntKcWT.jpg")
                ajuda.add_field(name="m!", value="indisponivel", inline=False)
                ajuda.add_field(name="m!", value="indisponivel", inline=False)
                ajuda.add_field(name="m!", value="indisponivel", inline=False)
                ajuda.add_field(name="m!", value="indisponivel", inline=False)
                ##ajuda.set_image(url="")
                ajuda.set_footer(
                    text=">>Clique no ❌ para fechar<<             3/3")  ## icon_url="https://i.imgur.com/rdm3W9t.png")
                await client.edit_message(msg, embed=ajuda)



    if message.content.lower().startswith('gb!lista1'):
        Embed = discord.Embed(color=0x000000, description="Ok, aqui esta a Lista 1, a lista da Zoeira!")
        Embed.add_field(name='gb!incrível', value=". . .", inline=False)
        Embed.add_field(name='gb!chato', value=". . .", inline=False)
        Embed.add_field(name='gb!linda', value=". . .", inline=False)
        Embed.add_field(name='gb!moeda', value=". . .", inline=False)
        Embed.add_field(name='gb!juntarnomes', value=". . .", inline=False)
        Embed.add_field(name='gb!say', value=". . .", inline=False)
        Embed.add_field(name='gb!gb', value=". . .", inline=False)
        await client.send_message(message.channel, embed=Embed)

    if message.content.lower().startswith('gb!lista2'):
        Embed = discord.Embed(color=0x000000, description="Tá aí, lista 2 , a lista de coisas inúteas!")
        Embed.add_field(name='gb!hora', value=". . . ", inline=False)
        Embed.add_field(name='gb!news', value=". . .", inline=False)
        Embed.add_field(name='gb!wiki', value=". . .", inline=False)
        await client.send_message(message.channel, embed=Embed)

    if message.content.lower().startswith('gb!lista3'):
        Embed = discord.Embed(color=0x000000, description="Lista séria, para Moderadores e Administradores!!!")
        Embed.add_field(name='gb!mute', value=". . .", inline=False)
        Embed.add_field(name='gb!unmute', value=". . .", inline=False)
        Embed.add_field(name='gb!kick', value=". . .", inline=False)
        Embed.add_field(name='gb!limpar', value=". . .", inline=False)
        Embed.add_field(name='gb!vote', value=". . .", inline=False)
        Embed.add_field(name='gb!cargo', value=". . .", inline=False)
        Embed.add_field(name='gb!sorteio', value=". . .", inline=False)
        await client.send_message(message.channel, embed=Embed)

    if message.content.lower().startswith('gb!lista4'):
        Embed = discord.Embed(color=0x000000, description="Outros")
        Embed.add_field(name='gb!denunciar', value=". . .", inline=False)
        Embed.add_field(name='gb!feed', value=". . .", inline=False)
        Embed.add_field(name='gb!bug', value=". . .", inline=False)
        Embed.add_field(name='gb!botinfo', value=". . .", inline=False)
        Embed.add_field(name='gb!userinfo', value=". . .", inline=False)
        Embed.add_field(name='gb!wiki', value=". . .", inline=False)
        await client.send_message(message.channel, embed=Embed)

    if message.content.lower().startswith(prefixo + 'anunciar'):
        if message.author.server_permissions.manage_messages:
            try:
                prefixo = 'gb!'
                msg = str(message.content).replace(prefixo + "anunciar", "")
                embed = discord.Embed(title="Anúncios e Novidades", description=msg, color=0xFFFF00)
                await client.send_message(message.channel, embed=embed)
                await client.delete_message(message)
            except IndexError:
                await client.send_message(message.channel, "Digite algo para um anúncio!")
        else:
            await client.send_message(message.channel, "Você não tem permissão para usar esse comando, ManoBrow !")


    if message.content.lower().startswith("gb!girl"):
        sn = random.choice('abcdefg')
        if sn == 'a':
            await client.send_message(message.channel, '{0.author.mention} Julia'.format(message))
            await client.add_reaction(message, '👍')
        if sn == 'b':
            await client.send_message(message.channel, '{0.author.mention} Fernanda'.format(message))
            await client.add_reaction(message, '👿')
        if sn == 'c':
            await client.send_message(message.channel, '{0.author.mention} Roberta  '.format(message))
            await client.add_reaction(message, '😶')
        if sn == 'd':
            await client.send_message(message.channel, '{0.author.mention} Maria'.format(message))
            await client.add_reaction(message, '🤔')
        if sn == 'e':
            await client.send_message(message.channel, '{0.author.mention} Maria'.format(message))
            await client.add_reaction(message, '🤔')
        if sn == 'f':
            await client.send_message(message.channel, '{0.author.mention} **Ninguém**'.format(message))
            await client.add_reaction(message, '🤔')
        if sn == 'g':
            await client.send_message(message.channel, '{0.author.mention} Jubiscléida'.format(message))
            await client.add_reaction(message, '🤔')


    if message.content.lower().startswith("gb!randomcorrida"):  # esse comandos sorteia um memebro
        if message.author.server_permissions.administrator:
            n = random.choice(list(message.server.members))
            n1 = '{}'.format(n.name)
            m1 = discord.utils.get(message.server.members, name="{}".format(n1))
            embed = discord.Embed(
                title="Corrida Random!!!",
                colour=0xab00fd,
                description="O membro que ganhou a corrida foi : {}".format(m1.mention)

            )
            hh = await client.send_message(message.channel, "{}".format(m1.mention))
            await client.delete_message(hh)
            await client.send_message(message.channel, embed=embed)
        else:
            await client.send_message(message.channel,"{} você não tem permissão de executar esse comando".format(message.author.mention))
############################################################################
    if message.content.lower().startswith("gb!banneds"):
        x = await client.get_bans(message.server)
        xx = '\n'.join([y.name for y in x])
        embedban = discord.Embed(title="***Banidos do Servidor:***", description=xx, color=0xdb709e)
        return await client.send_message(message.channel, embed=embedban)
###########################################################
    if message.content.startswith(client.user.mention):
        await client.send_message(message.channel, "<:gamebot_br:496815652359897112>| Escreva gb!help para ver todo os meus Códigos!")

    # Facil mais perca de Tempo
    if message.content.startswith("491061703493156875"):
        await client.send_message(message.channel, "Oi")
##################
    if message.content.lower().startswith("gb!emojis"):
        if len(message.server.emojis) == 0:
            return await client.send_message(message.channel,
                                             message.author.mention + ", **esse servidor não possui nenhum emoji!**")

        emojis = ""
        mostrando = 0
        for emoji in message.server.emojis:
            if len(str(emoji)) + 1 + len(emojis) <= 1024:
                emojis += str(emoji) + " "
                mostrando += 1

        em = discord.Embed(colour=0x00FFFF, description="**Mostrando `{}` de `{}`**\n\n".format(mostrando, len(
            message.server.emojis)) + emojis)
        em.set_author(name=message.server.name, icon_url=message.server.icon_url)
        em.set_footer(text="Requisitado por " + str(message.author), icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=em)
######################################
    if message.content.lower().startswith("gb!fechar"):
        membro = discord.utils.find(lambda r: r.name == "</Coordenador/>", message.server.roles)
        fechado = discord.PermissionOverwrite()
        fechado.read_messages = False
        fechado.send_messages = False
        await client.edit_channel_permissions(message.channel, membro, fechado)
        await client.send_message(message.channel, "O canal foi fechado para membros, satisfeito?!")
###############################################################################################


    ########################################################################################################################
    prefix = "gb!"
    if message.content.startswith(prefix + "ban"):
        if not message.author.server_permissions.ban_members:
            return await client.send_message(message.channel,
                                             "**Você não tem permissão para executar esse comando bobinho(a)!**")
        try:
            a = len(prefix) + 4
            userid = message.content[a:]
            user = message.server.get_member(userid)
            await client.send_message(message.channel,
                                      "**O usuário(a) {} foi banido com sucesso do servidor.**".format(user.id))
            await client.ban(user, delete_message_days=1)
        except IndexError:
            await client.send_message(message.channel, "**Você deve especificar um usuario para banir!**")
        except discord.Forbidden:
            await client.send_message(message.channel,
                                      "**Não posso banir o usuário, o cargo dele está acima de mim ou não tenho permissão para banir membros**")
        finally:
            pass

    if message.content.lower().startswith('gb!8ball'):
        try:
            respostas = ['Sim', 'Não', 'Talvez', 'Nunca', 'Claro']
            resposta = random.choice(respostas)
            mensagem = message.content[7:]
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name="Pergunta:", value='{}'.format(mensagem), inline=False)
            embed.add_field(name="Resposta:", value=resposta, inline=False)
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except:
            await client.send_message(message.channel, 'Você precisa perguntar alguma coisa!')

    if message.content.startswith('gb!bug'):
        await client.send_message(message.author,
                                  '**Vish, qual Bug estou tendo?  {}**'.format(message.author.mention))
        await client.delete_message(message)
        jogador = await client.wait_for_message(author=message.author)
        await client.send_message(message.author, '**Escreva o Comando, ou meu Erro (Sem print) {}**'.format(message.author.mention))
        motivo = await client.wait_for_message(author=message.author)
        await client.send_message(message.author, '**Que dia aconteceu isso? {}**'.format(message.author.mention))
        dia = await client.wait_for_message(author=message.author)
        await  client.send_message(message.author, '**Ok, vou falar com o Mestre Punisher! {}:**'.format(message.author.mention))
        prova = await client.wait_for_message(author=message.author)
        canal = client.get_channel('497962169984614411')
        embed = discord.Embed(colour=0xF0000,
                              description="O Úsuario: {} acabou de relatar um Bug".format(message.author.mention))
        embed.add_field(name='Comando:', value=motivo.content)
        embed.add_field(name='Dia:', value=dia.content)

        embed.add_field(name='Bug:', value=jogador.content)
        await client.send_message(canal, embed=embed)

##########################################################################################################

    if message.content.lower().startswith("gb!eval"):
        await client.delete_message(message)
        admin = '296428519947370499'
        if not message.author.id == admin:
            await client.delete_message(message)
            await client.send_message(message.channel,
                                      'Você não tem permissão para executar esse comando bobinho (a) .')
        try:
            await client.send_message(message.channel, str(eval(message.content[7:])))
        except Exception as e:
            await client.send_message(message.channel, repr(e))
############################################################################################
    if message.content.lower().startswith('gb!say'):
        if message.author.server_permissions.administrator:
            try:
                msg = str(message.content).replace("gb!say", "")
                await client.send_message(message.channel, msg)
                await client.delete_message(message)
            except:
                await  client.send_message(message.channel, "Digite algo!")
        else:
            await client.send_message(message.channel, "Sem permissão!")

    if message.channel == client.get_channel('498142537517891594'):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")

    if message.content.lower().startswith('gb!confirmar'):
        await client.delete_message(message)
        await client.send_message(message.channel, f"Ok, pelo Pedido de confirmação do {message.author.mention}iremos  enviar para o Mestre <@!296428519947370499>")

    prefix = "gb!"  # digite o prefixo
    if message.content.lower().startswith(prefix + "gif"):
        prefi = len(prefix) + 6
        tag = message.content[prefi:]
        apikey = "KCqwu9zw4HQru1UoKErfzyJJB7P6A1bx"  # copie e cole sua api key aqui
        url = "http://api.giphy.com/v1/gifs/random?tag={}&api_key={}&rating=g".format(tag, apikey)
        r2 = json.loads(requests.get(url).text)
        link = r2['data']['images']['downsized_large']['url']
        imagem = requests.get(link, stream=True)  ## Caso queira colocar em uma Embed apague essa linha e a de baixo
        # e apague o import io.
        await client.send_file(message.channel, io.BytesIO(imagem.raw.read()), filename="Giphy.gif")

    if message.content.startswith('gb!atacar'):
        if len(message.content) > 9:
            user = message.mentions[0]
            author = message.author.mention
            Embed = discord.Embed(color=COR, description='** O usuário {} atacou o(a) 🔫🔫🔫{} **'.format(author, user.mention))
            await client.send_message(message.channel, embed=Embed)
        else:
            Embed = discord.Embed(color=COR, description='**Você não mencionou um usuário para atacar**')
            Embed.set_footer(text="Nossa, a treta vai comer!🔫⚔⚔⚔")
            await client.send_message(message.channel, embed=Embed)

    if message.content.lower().startswith('gb!abraçar'):
        try:
            hugimg = ['http://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705',
                      'http://media1.tenor.com/images/949d3eb3f689fea42258a88fa171d4fc/tenor.gif?itemid=4900166',
                      'http://media1.tenor.com/images/11889c4c994c0634cfcedc8adba9dd6c/tenor.gif?itemid=5634578',
                      'http://media1.tenor.com/images/d7529f6003b20f3b21f1c992dffb8617/tenor.gif?itemid=4782499',
                      'https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935',
                      'https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788',
                      'https://media1.tenor.com/images/3c83525781dc1732171d414077114bc8/tenor.gif?itemid=7830142']
            hug = random.choice(hugimg)
            hugemb = discord.Embed(title='Abraço :heart:',
                                   description='**{}** recebeu um abraço de **{}**! TOP DEMAIS! :heart_eyes: '
                                   .format(message.mentions[0].name, message.author.name), color=0xff6e00)
            hugemb.set_image(
                url=hug)
            hugemb.set_footer(text="GameBot © 2018")
            await client.send_message(message.channel, embed=hugemb)
        except IndexError:
            await client.send_message(message.channel, 'Você precisa mencionar um usuário específico para abraçar!')

    if message.content.lower().startswith('gb!botinutil'):
        await client.send_message(message.channel, "Não sou não, você que é viu!")

    if message.content.lower().startswith('gb!roletarussa'):
        escolha = random.randint(1, 2)
        if escolha == 1:
            await client.add_reaction(message, '🔫')
            await client.send_message(message.channel, "O tiro foi certeiro, você morreu!")
        if escolha == 2:
            await client.add_reaction(message, '😲')
            await client.send_message(message.channel, "Você está com sorte, a bala não foi disparada.")

    if message.content.lower().startswith('gb!tirada'):
        escolha = random.randint(1,6)
        if escolha == 1:
            await client.add_reaction(message, '😎')
            await client.send_message(message.channel, "**-Amigo, o seu pneu está careca?\n"
                                                        "-Não não, é que ele ainda está muito novo e não nasceram os pelos ainda.**")
        if escolha == 2:
            await client.add_reaction(message, '😎')
            await client.send_message(message.channel, "**-Vamos viver a vida...\n"
                                                       "-Amigo, se tiver como viver a morte me avise!**")
        if escolha == 3:
            await client.add_reaction(message, '😎')
            await client.send_message(message.channel, "**O financeiro do banco liga para você: \n"
                                                       "-Senhor, gostaria de informar que o boleto venceu semana passada.\n"
                                                       "-Que maravilha, eu estava torcendo por ele!**")

        if escolha == 4:
            await client.add_reaction(message, '😎')
            await client.send_message(message.channel, "**A mulher abre a porta para o convidado e pergunta:\n"
                                                       "-Você veio?\n"                                                       
                                                       "-Não, não sou eu! É outro, vou vir mais tarde!**")

        if escolha == 5:
            await client.add_reaction(message,'😎')
            await client.send_message(message.channel, "**Na fila da padaria o cara pergunta pra mulher: \n"
                                                       "-Você está na fila?\n"
                                                       "Não, pisei em um chiclete e estou grudada!**")





    if message.content.startswith('gb!teste'):
        embed = discord.Embed(colour=0xFF0000, description='Olá Mundo, estou vivo!')
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("gb!changegame"):
        await client.delete_message(message)
        gameName = message.content.replace("gb!changegame", "")
        if message.author.server_permissions.administrator:
            await client.change_presence(game=discord.Game(name=gameName))
            await client.send_message(message.channel, "`Presence alterada para: {}`".format(gameName))
        else:
            await client.send_message(message.channel, "⚄1�7  Assim, só admin pode mudar minha Presence, ok?.")




    if message.content.lower().startswith('gb!notificar'):
        try:
            cargo = discord.utils.get(message.server.roles, name ='</Notificado/>') #Crie um cargo com o nome de Notificação e coloque Dentro dos parênteses.
            await client.add_roles(message.author, cargo)

            embed = discord.Embed(title="🔔 Você ativou as notificações!", description="Cada vez que tiver uma novidade você será notificado.", color=0x2A6EED)
            await client.send_message(message.channel, embed=embed)
        except:
            await client.send_message(message.channel, "Você talvez digitou o comando errado , ou não tem esse cargo.")

    if message.content.lower().startswith("gb!ascii"):
        f = Figlet(font='avatar')
        mensagem = message.content.lower().replace(".ascii", "")
        texto = f.renderText(mensagem)
        await client.send_message(message.channel, "`{}`".format(texto))


####################################################################################
    if message.content.lower().startswith("gb!corrida"):
        await client.send_message(message.channel,
                                  "**Marque o Player que deseja Desafiar**")
        msg = await client.wait_for_message(author=message.author)
        user = msg.mentions[0]
        vel1 = random.randint(1, 100)
        vel2 = random.randint(1, 100)
        if vel1 > vel2:
            await client.send_message(message.channel,
                                      "O Usuario {} Ganhou a Corrida Marcando {}m/s".format(message.author.name,
                                                                                            str(vel1)))
        elif vel2 > vel1:
            await client.send_message(message.channel,
                                      "O Usuario {} Ganhou a Corrida Marcando {}m/s".format(user.name, str(vel2)))
        else:
            await client.send_message(message.channel,
                                      "Os 2 Usuarios empataram a  Corrida Marcando o total de {}m/s".format(
                                          message.author, str(vel1)))

    if message.content.lower().startswith("gb!serverinfo"):
        horario = datetime.datetime.now().strftime("%H:%M:%S")
        embed = discord.Embed(title="\n", color=0x00a3cc,
                              description="Abaixo está as informaçoes principais do servidor!")
        embed.set_image(url='http://www.imagensanimadas.com/data/media/562/linha-imagem-animada-0538.gif')
        embed.set_thumbnail(url=message.server.icon_url)
        embed.set_footer(text="{} • {}".format(message.author, horario))
        embed.add_field(name="Nome:", value=message.server.name, inline=True)
        embed.add_field(name="Dono:", value=message.server.owner.mention)
        embed.add_field(name="ID:", value=message.server.id, inline=True)
        embed.add_field(name="Cargos:", value=str(len(message.server.roles)), inline=True)
        embed.add_field(name="Canais de texto:", value=str(
            len([c.mention for c in message.server.channels if c.type == discord.ChannelType.text])),
                        inline=True)
        embed.add_field(name="Canais de voz:", value=str(
            len([c.mention for c in message.server.channels if c.type == discord.ChannelType.voice])),
                        inline=True)
        embed.add_field(name="Membros:", value=str(len(message.server.members)), inline=True)
        embed.add_field(name="Bots:",
                        value=str(len([a for a in message.server.members if a.bot])),
                        inline=True)
        embed.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"),
                        inline=True)
        embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)
        await client.send_message(message.channel, embed=embed)

        a = await client.send_message(message.channel, '**GameBot © 2018**')
        await client.add_reaction(a, "🐧")




    if message.content.startswith('gb!roleinfo'):
        a = message.content[12:]
        nome = discord.utils.get(message.server.roles, name=a)
        embed = discord.Embed(color=0xFF0000, description='**Informações do cargo:**')
        embed.add_field(name='`📋 | Nome:`', value=str(nome))
        embed.add_field(name='`💻 | ID:`', value=str(nome.id))
        embed.add_field(name='`🌈 | Cor:`', value=str(nome.colour))
        embed.add_field(name='`📅 | Criado:`', value=str(nome.created_at))
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith("gb!twitch"):
        embed = discord.Embed(colour=0x00a3cc, description='__Quer saber minha Twitch?__ \n'
                                                           'Ok!\n'
                                                           '__Aqui está:__ \n'
                                                           '**gamebotbr**')
        await client.send_message(message.channel, embed=embed)



    if message.content.startswith('gb!divulgar'):
        if "</Anunciar/>" in [r.name for r in message.author.roles if r.name != "</Youtubers/>"] or "</Youtubers/>" in [r.name for r in message.author.roles if r.name != "@everyone"] or "</Youtubers/>" in [r.name for r in message.author.roles if r.name != "@everyone"] or "Coordenador" in [r.name for r in message.author.roles if r.name != "@everyone"] or "Developer" in [r.name for r in message.author.roles if r.name != "@everyone"] or "Gerente" in [r.name for r in message.author.roles if r.name != "@everyone"] or "Fundador" in [r.name for r in message.author.roles if r.name != "@everyone"]:
                x = message.author.id
                if not x in tempo:
                    canal2= client.get_channel('501829076902739969')
                    del3=await client.send_message(message.channel,
                                                                    "**__Olá {}! você receberá uma mensagem, na onde deverar responde-la para Divulgar seu video__**".format(message.author.name))

                    await client.send_message(message.author, "Qual será o titulo para sua divulgação?")
                    titulo = await client.wait_for_message(author=message.author)
                    await client.send_message(message.author, "Qual o nome do canal que postou o vídeo?")
                    canal1 = await client.wait_for_message(author=message.author)
                    await client.send_message(message.author, "Qual o link do vídeo?")
                    link = await client.wait_for_message(author=message.author)
                    embeddivul=discord.Embed(title="GameBot:",description="O {} {} acaba de divulgar um novo vídeo!\n\n 📝 Titulo:\n{}\n\n📫 Enviado pelo(a):\n{}\n\nPara acessar o vídeo [Clique aqui]({})".format(message.author.top_role.name, message.author.name, titulo.content, canal1.content, link.content), color=0xFFFFFF)
                    embeddivul.set_author(name='Punisher Divulgações!!!', icon_url=message.author.avatar_url)
                    embeddivul.set_thumbnail(url="https://www.youtube.com/yts/img/yt_1200-vfl4C3T0K.png")
                    await client.send_message(canal2, embed=embeddivul)
                    tempo.append(x)
                    await asyncio.sleep(1)
                    tempo.remove(x)
                else:
                    await client.send_message(message.channel, "{} você só poderá divulgar outro vídeo após ``24 horas.``".format(message.author.mention))
        else:
            await client.send_message(message.channel, "Olá {}, você precisa do cargo <@&501827476763181056> ou estar no Cargo: <@&501836273284284416> .".format(message.author.mention))

    if message.content.startswith('gb!convite'):
        embed = discord.Embed(colour=0x00a3cc, description='**|📨 Ok, aqui está o Convite do Servidor:** \n'
                                                           
                                                           'https://discord.gg/Y5dbtcp')
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('?img'):
        embed = discord.Embed(color=COR)
        embed.set_image(url="https://1.bp.blogspot.com/-g30feZDV5Zk/TbsiI9A4sFI/AAAAAAAAONw/ZX0ELuiCiqc/s1600/datena-ibagens.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("gb!dado"):
        await client.delete_message(message)
        choice = random.randint(1, 6)
        embeddad = discord.Embed(title='🎲 Dado', description=' Joguei o dado, o resultado foi :   {}'.format(choice),
                                 colour=0x000000)
        await client.send_message(message.channel, embed=embeddad)

    if message.content.lower().startswith('gb!tabuada'):

        while True:
            a = input()
            num = 1
            while num != 11:
                print(f'{a} x {num} = {int(a) * num}')
                num += 1

    if message.content.lower().startswith('gb!gerarinvite'):
        crt = message.content[14:]
        link = f'https://discordapp.com/oauth2/authorize?client_id=491061703493156875{crt}&scope=bot&permissions=8'
        embed2 = discord.Embed(title="Gerando...",
                               description="✅ | Verifique o resultado em seu privado.",
                               color=5675432)
        embed2.set_footer(icon_url=message.server.icon_url, text="Gerador de Invite")
        await client.send_message(message.channel, embed=embed2)
        embed = discord.Embed(title="Aqui está o invite do bot.",
                              description=f"[Clique aqui.]({link})",
                              color=5675432)
        embed.set_thumbnail(url= message.server.icon_url)
        embed.set_footer(icon_url=message.server.icon_url, text="Gerador de Invite")
        await client.send_message(message.author, embed=embed)

    if message.content.lower().startswith('gb!ppt'):
        escolha = random.randint(1,4)

        if escolha == 1:
            await client.send_message(message.channel, "**Empate!**")
            await client.add_reaction(message, '🆗')

        if escolha == 2:
            await client.send_message(message.channel, "**Papel!**")
            await client.add_reaction(message, '📄')

        if escolha == 3:
            await client.send_message(message.channel, "**Pedra!**")
            await client.add_reaction(message, '💎')

        if escolha == 4:
            await client.send_message(message.channel, "**Tesoura!**")
            await client.add_reaction(message, '✂')

    if message.content.startswith('gb!teste'):
        embed = discord.Embed(colour=0xFF0000, description='GitHub!')
        await client.send_message(message.channel, embed=embed)

################     ###################
#                    #                 #
#                    #                 #
#     ##########     #                 #
#              #     ###################
#              #     #                 #
#              #     #                 #
################     ###################

client.run(os.environ.get("HEROKU.TOKEN"))


