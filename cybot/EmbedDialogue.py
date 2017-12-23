from discord import Embed, Colour, errors
from discord import reaction as d_reaction
from asyncio import sleep
from math import ceil

class EmbedDialogue:

    # Dialogue Constants
    E_EXIT = 0
    E_REFRESH = 1

    def __init__(self, items: dict, max_per_page=6, timeout=30):
        """
        Creates a new dialogue object

        :param items: items to appear on dialogue
        :param max_per_page: amount of items per page
        :param timeout: idle timeout in seconds
        """

        # Dialogue fields
        self.items = items
        self.max_per_page = max_per_page
        self.timeout = timeout
        self.page = 1
        self.reactions = {}
        self.user = None
        self.max_page = max(1, ceil(len(items) / max_per_page)) # If you're using this bot, please do not change max_per_page to 0, I'm not responsible for your shenagians

        # Embed fields
        self.message = None
        self.embed = None
        self.title = ''
        self.description = ''
        self.color = Colour.default()
        self.thumbnail = None

    def generate_embed(self):
        """
        Generates an embed object
        :return: embed obect
        """

        embed = Embed(title=self.title, description=self.description, color=self.color)
        embed.set_footer(text="Page %d/%d" % (self.page, self.max_page))

        if self.thumbnail is not None:
            embed.set_thumbnail(url=self.thumbnail)

        # Get page messages
        init_index = (self.page - 1) * self.max_per_page
        for i in range(init_index, init_index + min(len(self.items) - init_index,self.max_per_page)):
            item = list(self.items.keys())[i]
            value = self.items[item]

            embed.add_field(name="**{0}**".format(item), value="{0} {1}".format(item, value), inline=False)

        return embed

    async def create(self, client, channel):
        """
        Creates an instance of the dialogue
        :param client: client
        :param channel: channel callback
        """

        # If dialogue instance already exists
        if self.message is not None:
            return

        # Create new embed if there's none
        if self.embed is None:
            self.embed = self.generate_embed()

        self.message = await client.send_message(channel, embed=self.embed)

        for reaction in self.reactions:
            await client.add_reaction(self.message, reaction)
            await sleep(0.1)

    async def update(self, client):
        """
        Updates the dialogue
        :param client: Client
        """

        if not self.message:
            return

        # wait for interaction with any user
        async def wait_for_interaction():
            return await client.wait_for_reaction(timeout=self.timeout, message=self.message)

        interaction = await wait_for_interaction()
        while interaction is not None:
            reaction, user = interaction
            # Checks if user issuer is the command issuer
            if user == self.user:
                if reaction.emoji in self.reactions:
                    value = self.reactions[reaction.emoji](self)
                    if value is EmbedDialogue.E_EXIT:
                        break

                    if value is EmbedDialogue.E_REFRESH:
                        self.embed = self.generate_embed()
                        await client.edit_message(self.message, embed=self.embed)

            # Ignore and delete non-bots reactions
            if user is not client.user:
                await client.remove_reaction(self.message, reaction.emoji, user)

            # repeat procedure
            interaction = await wait_for_interaction()

        try:
            print("TIME TO DELETE")
            await client.delete_message(self.message)
        except errors.Forbidden:
            pass
        except errors.HTTPException:
            pass


    @staticmethod
    def exit_dialogue(instance):
        """
        dialogue exit function

        :param instance: Dialogue isntance
        :return: dialogue exit opcode
        """

        return EmbedDialogue.E_EXIT

    @staticmethod
    def go_back(instance):
        """
        Moves one page backward
        :param istance: Dialogue instance
        :return: Refresh opcode
        """
        if instance.page > 1:
            instance.page -= 1
            return EmbedDialogue.E_REFRESH

    @staticmethod
    def go_forward(instance):
        """
        Movess one page forward
        :param istance: Dialogue instance
        :return: Refresh opcode
        """

        if instance.page < instance.max_page:
            instance.page += 1
            return EmbedDialogue.E_REFRESH

    @staticmethod
    def first_page(instance):
        """
        Moves to the first page
        :param instance: Dialogue instance
        :return: Refresh opcode
        """

        instance.page = 1
        return EmbedDialogue.E_REFRESH

    @staticmethod
    def last_page(instance):
        """

        :param instance:
        :return:
        """

        instance.page = instance.max_page
        return EmbedDialogue.E_REFRESH

    def add_reaction(self, emoji, func):
        """
        Adds an emoji with a function reference
        :param emoji: Emoji appearance
        :param func: function to callback on
        """

        if emoji not in self.reactions:
            self.reactions[emoji] = func

