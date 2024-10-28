import os
import random
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar claves de API
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Configurar el bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    """
    Imprime cuando el bot está listo
    """
    print(f'Bot {bot.user} está listo y conectado a Discord!')


@bot.command()
async def hola(ctx):
    """
    Imprime un hola.
    """
    await ctx.send('¡Hola! ¿Cómo estás?')


@bot.command()
async def bien(ctx):
    """
    Imprime una respuesta
    """
    await ctx.send('Bueno, me chupa un reverendo re mil huevo, ¡putaaaaaaaaa!')


@bot.command()
async def puto(ctx):
    """
    Comando para unirse al canal de voz y reproducir un audio aleatorio
    """
    # Revisa si el usuario está en un chat de voz
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()

        # Usar una carpeta absoluta para los audios
        audio_folder = r'C:\Users\TT\Desktop\Stuff\PROGRAMACIÓN PRÁCTICAS\Python\Repositorio\pador\audios'
        print("CARGADO!")

        # Comprobar si la carpeta de audios existe
        if not os.path.exists(audio_folder):
            await ctx.send(f'La carpeta de audios no existe en la ruta: {audio_folder}')
            await voice_client.disconnect()
            return

        # Seleccionar un archivo de audio aleatorio de la carpeta raíz
        audio_files = [f for f in os.listdir(audio_folder) if f.endswith(
            ('.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a', '.wma'))]
        if not audio_files:
            await ctx.send('No se encontraron archivos de audio compatibles en la carpeta.')
            await voice_client.disconnect()
            return

        audio_file = random.choice(audio_files)
        audio_path = os.path.join(audio_folder, audio_file)

        # Reproducir el audio
        voice_client.play(discord.FFmpegPCMAudio(audio_path),
                          after=lambda e: print(f'Reproducción finalizada: {e}'))

        # Esperar a que termine la reproducción
        while voice_client.is_playing():
            await asyncio.sleep(1)

        # Desconectarse del canal de voz
        await voice_client.disconnect()
    else:
        await ctx.send('¡Debes estar en un canal de voz para usar este comando!')

# Ejecutar el bot
bot.run(DISCORD_TOKEN)
