import discord
from discord.ext import commands


class Main(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ping(self, ctx):
		embed = discord.Embed(
			title = ctx.guild.name,
			description = "clickbedrock Топ!",
			colour = ctx.author.color
		)

		embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = ctx.guild.icon_url)
		embed.add_field(name = "Скоро...", value = "Global Update!", inline = True)

		await ctx.send(embed = embed)


	@commands.command()
	@commands.has_permissions(administrator = True)
	async def clear(self, ctx, amount: int):
		if amount == int:
			await ctx.channel.purge(limit = amount + 1)
			await ctx.send(f"Я удалил {amount} сообщений!", delete_after = 3)
		else:
			await ctx.send("Правильное использование: **!clear Количество**")


	@commands.command()
	@commands.has_permissions(ban_members = True)
	@commands.guild_only()
	async def ban(self, ctx, member: discord.Member, *, reason = "Без причины"):
		await ctx.channel.purge(limit = 1)
		if member != ctx.author:
			await member.ban(reason=reason)
			emb = discord.Embed(
				title = f"{ctx.author} забанил пользователя {member}",
				description = f"Причина: {reason}",
				colour = discord.Color.red()
			)
			await ctx.send(embed = emb)
		else:
			await ctx.send("Зачем банить себя..?", delete_after = 3)



	@commands.Cog.listener()
	async def on_member_join(self, member):
		member.add_roles(967679450227556382)
		msg = f"{member.name} присоединился к серверу!"

		await self.bot.get_channel(998161850028007494).send(msg)

	@commands.Cog.listener()
	async def on_message_edit(self, before, after):

		emb = discord.Embed(
			title = "clickbedrock | Логи | Текстовый Чат",
			description = "Изменения сообщения",
			colour = discord.Color.orange()
		)

		emb.add_field(name = "До изменения:", value = f"{before.content}", inline = True)
		emb.add_field(name = "После изменения:", value = f"{after.content}", inline = True)
		emb.set_author(name = before.author.nick)

		await self.bot.get_channel(998162064260485212).send(embed = emb)

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		emb = discord.Embed(
			title = "clickbedrock | Логи | Текстовый Чат",
			description = f"Удаление сообщения в {message.channel}",
			colour = discord.Color.red()
		)

		emb.add_field(name = "Сообщение:", value = f"{message.content}", inline = True)
		emb.set_author(name = message.author.nick)

		await self.bot.get_channel(998162064260485212).send(embed = emb)

	@commands.Cog.listener()
	async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
		emb = discord.Embed(
			title = "clickbedrock | Логи | Голосовой канал",
			description = "Вход/Выход из голосового канала.",
			colour = discord.Color.blue()
		)
		if before.channel is None:
			emb.add_field(name = f"{member.display_name} присоединился к каналу", value = f"{after.channel.mention}", inline = True)
			await self.bot.get_channel(998162064260485212).send(embed = emb)
		elif after.channel is None:
			emb.add_field(name = f"{member.display_name} покинул канал", value = f"{before.channel.mention}", inline = True)
			await self.bot.get_channel(998162064260485212).send(embed = emb)
		elif before.channel != after.channel:
			emb.add_field(name = f"{member.display_name} перешёл из канала в канал", value = f"{before.channel.mention} > {after.channel.mention}", inline = True)
			await self.bot.get_channel(998162064260485212).send(embed = emb)


def setup(bot):
	bot.add_cog(Main(bot))