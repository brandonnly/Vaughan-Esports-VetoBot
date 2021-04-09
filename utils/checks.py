def playerCheck(ctx):
    def func(message):
        """Checks if a player said 'me' """
        return message.content.lower() == 'me' \
               and message.channel == ctx.channel

    return func


def stageCheck(ctx, match):
    """
    Check if the stage name is valid
    :param ctx: discord context to check for channel
    :param match: match to check stagelist and game from
    :return:
    """

    def func(message):
        return message.content in match.games[match.current_game].stagelist \
               and message.channel == ctx.channel

    return func