from __future__ import annotations
from utils.validators import String, CustomValidator


class Comment:
    content = String()

    def __init__(
            self,
            user: User,
            post: Post,
            content: str
    ) -> None:
        self.user = user
        self.post = post
        self.content = content


from user import User
from posts import Post
