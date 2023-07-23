from damoim_service.command.Post import CreatePostCommand
from Repository.spi import PostToImageRepository, PostRepository
from damoim_service.command.PostToImage import CreatePostToImageCommand
from Repository.api.s3.s3 import AWSS3


def create_post(command: CreatePostCommand):
    post_instance = None
    post_instance = PostRepository.create_post(command=command)
    image_list = []
    for i in command.image_contents:
        image_list.append(AWSS3().upload_file_s3(i))

    post_image_command = CreatePostToImageCommand(post_id=post_instance, image_url="")
    PostToImageRepository.create(post_image_command)
    return post_instance
