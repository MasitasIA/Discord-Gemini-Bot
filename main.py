import discord
from discord.ext import commands
from gemini import gemini_query
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logueado como {bot.user}, (ID: {bot.user.id})")

@bot.tree.command()
async def gemini(interaction: discord.Interaction, query: str):
    await interaction.response.defer()
    answer = gemini_query(query)
    if answer:
        await interaction.followup.send(f"Respuesta de Gemini a: {query} \n{answer}")
    else:
        await interaction.followup.send("No se pudo obtener una respuesta de Gemini.")

bot.run(token)