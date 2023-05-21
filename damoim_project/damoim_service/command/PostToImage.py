from dataclasses import dataclass

from django.utils import timezone

from damoim_service.models import Post


@dataclass
class CreatePostToImageCommand:
    post_id: Post
    image_url: str = None
