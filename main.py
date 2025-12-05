import discord
from discord.ext import commands
from gemini import gemini_query
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!")

# --- CLASE PARA EL FORMULARIO EMERGENTE (MODAL) ---
class PreguntaModal(discord.ui.Modal, title="Nueva Consulta a Gemini"):
    pregunta_input = discord.ui.TextInput(
        label="¿Qué quieres saber?",
        style=discord.TextStyle.paragraph,
        placeholder="Escribe tu pregunta aquí...",
        required=True,
        max_length=500
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()
        
        pregunta = self.pregunta_input.value
        answer = gemini_query(pregunta)
        
        if answer:
            embed = discord.Embed(
                title="Respuesta de Gemini",
                description=f"**Pregunta:** {pregunta}\n\n**Respuesta:** {answer}",
                color=0x4D8BD3,
                timestamp=datetime.now()
            )
            embed.set_thumbnail(url="https://registry.npmmirror.com/@lobehub/icons-static-png/1.75.0/files/dark/gemini-color.png")
            
            await interaction.followup.send(embed=embed, view=BotonReintentar())
        else:
            await interaction.followup.send("No se pudo obtener una respuesta.")

# --- CLASE PARA EL BOTÓN DE REINTENTAR ---
class BotonReintentar(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Preguntar otra cosa", style=discord.ButtonStyle.primary)
    async def boton_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(PreguntaModal())

# --- EVENTOS DEL BOT ---
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logueado como {bot.user}, (ID: {bot.user.id})")

# --- COMANDOS DE BARRA ---
@bot.tree.command(name="gemini", description="Consulta a la IA de Gemini.")
async def gemini(interaction: discord.Interaction, pregunta: str):
    await interaction.response.defer()
    answer = gemini_query(pregunta)
    if answer:
        full_response = f"Respuesta de Gemini a: {pregunta} \n{answer}"
        if len(full_response) <= 2000:
            await interaction.followup.send(full_response)
        else:
            await interaction.followup.send("Respuesta demasiado larga.")
    else:
        await interaction.followup.send("Error al obtener respuesta.")

# --- COMANDO DE BARRA CON EMBED ---
@bot.tree.command(name="gemini_embed", description="Consulta a la IA de Gemini en un embed.")
async def gemini_embed(interaction: discord.Interaction, pregunta: str):
    await interaction.response.defer()
    answer = gemini_query(pregunta)
    
    if answer:
        embed = discord.Embed(
            title="Respuesta de Gemini",
            description=f"**Pregunta:** {pregunta}\n\n**Respuesta:** {answer}",
            color=0x4D8BD3,
            timestamp=datetime.now()
        )
        embed.set_thumbnail(url="https://registry.npmmirror.com/@lobehub/icons-static-png/1.75.0/files/dark/gemini-color.png")
        
        await interaction.followup.send(embed=embed, view=BotonReintentar())
    else:
        await interaction.followup.send("No se pudo obtener una respuesta de Gemini.")

#--- TOKEN ---
bot.run(token)