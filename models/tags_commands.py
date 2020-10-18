import discord
def help():
	embed=discord.Embed(title="Help", description="This is the help command.", color=0x100dc9)
	embed=set_author(embed) 
	embed.add_field(name="tag create [c] tagname content", value="Create a tag with your specified name and with your specified content", inline=False)
	embed.add_field(name="tag [t | tags] tagname", value="Shows you the tag with the specified name", inline=False)
	embed.add_field(name="tag help", value="Shows you all the commands with description", inline=False)
	return embed

def nocommand():
	embed = help()
	embed.set_footer(text="Please pick a command.")
	return embed

def notagfound():
	embed=discord.Embed(title="No Tag Fouund", description="No tag was found. Please select another tag.", color=0xe10e0e)
	embed=set_author(embed) 
	return embed

def taginuse():
	embed=discord.Embed(title="Tag is already taken", description="Tag is already in use, please use a different name.", color=0xe10e0e)
	embed=set_author(embed) 
	return embed

def tagerror():
	embed=discord.Embed(title="Error", description="An occured while your tag erry nice.", color=0xe10e0e)
	embed=set_author(embed) 
	return embed

def tagsucceed():
	embed=discord.Embed(title="Tag created", description="Errry Nice, You created your tag!! :D", color=0x07ed58)
	embed=set_author(embed) 
	return embed

def tagdelete():
	embed=discord.Embed(title="Tag deleted", description="Errry Nice, You deleted your tag!! :D", color=0x07ed58)
	embed=set_author(embed) 
	return embed

def notagdelete():
	embed=discord.Embed(title="Tag was not deleted", description="Tag could not be found or you do not own it", color=0xe10e0e)
	embed=set_author(embed) 
	return embed

def notenoughargs():
	embed=discord.Embed(title="Please enter a tagname", description="Enter a tag name to complete the command", color=0xe10e0e)
	embed=set_author(embed) 
	return embed

def set_author(embed):
	embed.set_author(name="Bot-Tom-Gear", icon_url="https://cdn.discordapp.com/avatars/759261058698706976/36481f81386257f8434c7bcea1f8590c.webp?size=1024")
	return embed


