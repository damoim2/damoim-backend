from damoim_service.command.Post import CreatePostCommand
from Repository.spi import PostToImageRepository, PostRepository
from damoim_service.command.PostToImage import CreatePostToImageCommand
from Repository.api.s3.s3 import AWSS3


def create_post(command: CreatePostCommand):
    post_instance = None
    post_instance = PostRepository.create_post(command=command)
    # image_url=AWSS3().upload_file_s3(request.FILE)

    image_url = None
    if image_url is not None:
        post_image_command = CreatePostToImageCommand(
            post_id=post_instance, image_url=image_url
        )
        PostToImageRepository.create(post_image_command)
    return post_instance
