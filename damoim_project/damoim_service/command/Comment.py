from dataclasses import dataclass


@dataclass
class CreateCommentCommand:
    user_id: int
    comment: str
