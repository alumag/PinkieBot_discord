import time

from discord import Embed, Message

from cybot import utils, client
from cybot.db import RunCommand

_time_between_karma = 60 * 30  # half an hour, in seconds


def get_karma_embed(member, karma):
    em = Embed(title="karma balance", color=0x0080ff)
    _url = member.avatar_url
    if _url is None:
        _url = member.default_avatar

    em.set_thumbnail(url=_url)
    em.add_field(name="User: %s" % member.name, value="karma: %d" % karma, inline=False)

    return em


def set_karma_embed(member, karma):
    em = Embed(color=0x00ff40)

    _url = member.avatar_url
    if _url is None:
        _url = member.default_avatar

    em.set_author(name="%s#%s" % (member.name, member.discriminator), icon_url=_url)
    em.set_footer(text="User was given %d karma points!" % karma)

    return em


@utils.register_command(name='give1')
async def add_karma_cmd(message: Message, args: [str]):
    """
    give @USER: give 1 karma to a user
    """
    try:
        sender_id = message.author.id
        target_id = message.mentions[0].id
        user_nick = message.mentions[0].nick
        if user_nick is None:
            user_nick = message.mentions[0].name
    except:
        return await client.send_message(message.channel, 'No user specified!')

    if target_id == sender_id:
        return await client.send_message(message.channel, "4ril??")

    eligible_to_give = _eligible_to_give(sender_id)
    if not eligible_to_give[1]:
        return await client.send_message(message.channel, 'You can give karma to %s again in more %d minutes' %
                                         (user_nick,
                                          eligible_to_give[0] / 60))
    _add_karma(sender_id, target_id)
    _update_time(sender_id)
    await client.send_message(message.channel, '%s has %s karma' % (user_nick, _get_karma(target_id)))


def _update_time(user_id):
    RunCommand.update_row(table="karma",
                          expression=f"user = '{user_id}'",
                          set=f"last_karma_gave = {int(time.time())}")


def _eligible_to_give(sender_id):
    _last_karma_time = RunCommand.select_row(table="karma",
                                             fields=["last_karma_gave"],
                                             expression=f"user = '{sender_id}'")
    if not _last_karma_time: return 0, True
    _last_karma_time = _last_karma_time[0]
    _time = int(time.time()) - _last_karma_time
    return _time, _time >= _time_between_karma


def _add_karma(target_id, num=1):
    karma = RunCommand.select_row(table="karma",
                                  fields=["karma"],
                                  expression=f"user = '{target_id}'")
    if not karma:
        RunCommand.add_row(table="karma",
                           values=[f"'{target_id}'", f"-{num}", f"{int(time.time())}"]
                           )

    RunCommand.update_row(table="karma",
                          expression=f"user = '{target_id}'",
                          set=f"karma = {karma+num}")


def _set_karma(target_id, num=1):
    karma = RunCommand.select_row(table="karma",
                                  fields=["karma"],
                                  expression=f"user = '{target_id}'")
    if not karma:
        RunCommand.add_row(table="karma",
                           values=[f"'{target_id}'", f"{num}", f"{int(time.time())}"]
                           )

    RunCommand.update_row(table="karma",
                          expression=f"user = '{target_id}'",
                          set=f"karma = {num}")


def _dec_karma(target_id, num=1):
    karma = RunCommand.select_row(table="karma",
                                  fields=["karma"],
                                  expression=f"user = '{target_id}'")
    if not karma:
        RunCommand.add_row(table="karma",
                           values=[f"'{target_id}'", f"-{num}", f"{int(time.time())}"]
                           )

    RunCommand.update_row(table="karma",
                          expression=f"user = '{target_id}'",
                          set=f"karma = {karma-num}")


def _get_karma(user_id):
    karma = RunCommand.select_row(table="karma",
                                  fields=["karma"],
                                  expression=f"user = '{user_id}'")
    if not karma:
        RunCommand.add_row(table="karma",
                           values=[f"'{user_id}'", "0", f"{int(time.time())}"]
                           )
        return 0
    return karma[0]
