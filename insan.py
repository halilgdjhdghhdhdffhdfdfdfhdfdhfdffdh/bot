import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/öneri'):
        await message.channel.send(""""İşte evde ürettikleri atik miktarini azaltmak isteyen ancak nereden başlayacaklarini bilmeyen gençler
         ve yetişkinler için bazi yararli ipuçlari:
                                                                            Plastik bardak ve şişe gibi tek kullanimlik ürünleri kullanmaktan kaçinin

                                                                            Kağit tüketimini azaltmak için e-okuyuculara geçiş yapin

                                                                         Mümkün olduğunca az ambalajli market ürünlerini ve atiştirmaliklari tercih edin, yiyecekleri ağirliklarina göre (ambalajsiz) satin alin ve yeniden kullanilabilir poşetlere geçmeye çalişin

                                                                            Geri dönüştürmeye çalişin. Geri dönüştürülebilir ürünler için bir çöp kutusu ayirin ve dolduğunda geri dönüşüm istasyonuna taşiyin""")

client.run("MTE2MzkxMzI4NDEyNzI5MzUyMQ.GE-Dgs.dIQ8xo-dlIADIXxQfjTeareOE-4P_vwar-6jqE")
