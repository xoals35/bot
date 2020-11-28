import discord
import captcha
import time
import asyncio
import datetime
import random
import os

client = discord.Client()


@client.event
async def on_ready():
    print('봇이준비됌')
    print('client.user.id')
    game = discord.Game('케테르서버공식봇')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("/서버 on"):
        embed=discord.Embed(title='서버 on', color =0x00ff56)
        await message.channel.send(embed=embed)

    if message.content.startswith("/서버 off"):
        embed=discord.Embed(title='서버 off', color=0xff0000)
        await message.channel.send(embed=embed)

    if message.content.startswith('!청소'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨', colour=discord.Colour.green()))
                await asyncio.sleep(100000000000000000000000000000000000000000)
                await message.delete()
            else:
                await message.channel.send('``명령어 사용권한이 없습니다.``')
        except:
            pass
    
    if message.content.startswith("/help"):
        embed=discord.Embed(title="/help", description="명령어 설명서입니다", color=0x00ff56)
        embed.set_author(name="당신은 /help명령어를치셨습니다.", url="https://blog.naver.com/huntingbear21", icon_url="https://ifh.cc/g/El8fbu.jpg")
        embed.set_thumbnail(url="https://ifh.cc/g/El8fbu.jpg")
        embed.add_field(name="말대로 역할인증명령어입니다.", value="/인증", inline=True)
        embed.add_field(name="말그대로 채팅청소명령어입니다.", value="/청소 (원하는수)", inline=True)
        embed.add_field(name="없음", value="없음", inline=True)
        embed.add_field(name="없음", value="없음", inline=True)
        embed.set_footer(text="이것은 임베드라는것입니다")
        await message.channel.send(embed=embed)

    if message.content.startswith("/케테르"):
        embed=discord.Embed(title="/help", description="명령어 설명서입니다", color=0x00ff56)
        embed.set_author(name="당신은 /케테르명령어를치셨습니다.", url="https://blog.naver.com/huntingbear21", icon_url="https://ifh.cc/g/El8fbu.jpg")
        embed.set_thumbnail(url="https://ifh.cc/g/El8fbu.jpg")
        embed.add_field(name="케테르", value="나이:13살", inline=True)
        embed.add_field(name="케테르", value="초등학교6학년", inline=True)
        embed.add_field(name="케테르", value="scpsl서버장", inline=True)
        embed.add_field(name="케테르", value="일을잘하면서 가끔식 권남도함", inline=True)
        embed.set_footer(text="케테르서버공식봇초대링크(복사해서 쓰세용):https://discord.com/oauth2/authorize?client_id=782242908648112138&scope=bot")
        await message.channel.send(embed=embed)
    
    if(message.content == "!시간"):
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))

   
    if message.content == "!핑":
        la = client.latency
        await message.channel.send(f'{str(round(la * 1000))}ms')

    

access_token = os.environ["BOT_TOKEN"]
client.run('NzgyMjQyOTA4NjQ4MTEyMTM4.X8JWeg.K2z6K-GEKx1lsmpkUdJRZn66fx8')


    
