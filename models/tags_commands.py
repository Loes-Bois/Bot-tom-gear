import discord
def help():
	embed=discord.Embed(title="Help", description="This is the help command.", color=0x100dc9)
	embed.set_author(name="Bot-Tom-Gear", icon_url="https://cdn.discordapp.com/avatars/759261058698706976/36481f81386257f8434c7bcea1f8590c.webp?size=1024")
	embed.add_field(name="tag create [c] tagname content", value="Create a tag with your specified name and with your specified content", inline=False)
	embed.add_field(name="tag [t | tags] tagname", value="Shows you the tag with the specified name", inline=False)
	embed.add_field(name="tag help", value="Shows you all the commands with description", inline=False)
	return embed

def nocommand():
	embed = help()
	embed.set_footer(text="Please pick a command.")
	return embed

def notagfound():
	embed=discord.Embed(title="No Tag Fouund", description="No tag was found. Please select another tag", color=0xe10e0e)
	embed.set_author(name="Bot-Tom-Gear", icon_url="https://cdn.discordapp.com/avatars/759261058698706976/36481f81386257f8434c7bcea1f8590c.webp?size=1024")
	return embed