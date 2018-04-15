

from collections import namedtuple

# UserSummary = namedtuple('UserSummary', ['nickname', 'beans', 'send_receive'])


class UserSummary:
    @classmethod
    def user(cls, user):
        return dict(
            nickname=user.nickname,
            beans=user.beans,
            email=user.email,
            send_receive=str(user.send_counter) + '/' + str(user.receive_counter)
        )
