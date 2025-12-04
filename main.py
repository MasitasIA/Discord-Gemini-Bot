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
        try:
            full_response = f"Respuesta de Gemini a: {query} \n{answer}"
            if len(full_response) > 2000:
                await interaction.followup.send("No puedo responder a esa pregunta porque el texto es demasiado largo.")
            else:
                await interaction.followup.send(full_response)
        except Exception:
            await interaction.followup.send("No puedo responder a esa pregunta.")
    else:
        await interaction.followup.send("No se pudo obtener una respuesta de Gemini.")

bot.run(token)