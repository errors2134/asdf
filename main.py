import discord
import asyncio
import os

client = discord.Client()

token = "ODg5MTE5ODg1OTk5ODkwNTIy.YUcnaw.a99z-_2MIJwy4u933tR7mlbNYcg"

@client.event
async def on_ready():

    print(client.user.name)
    print("성공적으로 봇이 실행되었습니다")
    game = discord.Game('오아앙')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "!테스트":
        await message.channel.send("asdf")

    if message.content == "asdf":
        await message.channel.send("성공")

    if message.content == "저게 임베드라는거래요":
        embed = discord.Embed(title="이미지 임베드", description="image embed, color=0x00ff00")
        embed.set_thumbnail(url="https://search.naver.com/search.naver?where=image&sm=tab_niv&query=%EB%8B%AC%20%EC%82%AC%EC%A7%84&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall#imgId=image_sas%3Ablog140042483%7C6%7C222483902141_2139223213&vType=rollout")
        await message.channel.send(embed=embed)

    if message.content == "이건 뭐에 쓰는거지":
        embed = discord.Embed(title="여기에 쓰는 거", description="이건 또 뭐고", color=0x00ff00)
        embed.add_field(name="오아앙", value="ㅁㄴㅇㄻㄴㅇㄹ",inline=True)
        embed.add_field(name="뉴아아아ㅏㅇ", value="ㅁ빼앵ㅇ",inline=True)
        embed.set_footer(text="ㅁㄴㅇㄹ")
        await message.channel.send(embed=embed)



access_token = os.environ['BOT_TOKEN"]
client.run(access_token) 
