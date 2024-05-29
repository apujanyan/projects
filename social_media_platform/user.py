from __future__ import annotations
from utils.validators import String, Email
from operations import UserOperations
from datetime import datetime


class User(UserOperations):
    name = String()
    contact_info = Email()
    profile_info = String()

    def __init__(
            self,
            name: str,
            contact_info: str,
            profile_info: str
    ) -> None:
        self.name = name
        self.contact_info = contact_info
        self.profile_info = profile_info

    def create_post(
            self,
            post_type: str,
            date: datetime,
            content: str,
    ) -> Post | None:
        if post_type == 'Audio':
            post = AudioPost(self, content, date)
        elif post_type == 'Text':
            post = TextPost(self, content, date)
        else:
            return
        return post

    def view_post(
            self,
            post: Post
    ) -> None:
        print(f'Viewing post by {post.user.name}: {post.content}. ')

    def leave_comment(
            self,
            post: Post,
            content: str
    ) -> Comment:
        comment = Comment(self, post, content)
        return comment


from posts import Post, AudioPost, TextPost
from comment import Comment
