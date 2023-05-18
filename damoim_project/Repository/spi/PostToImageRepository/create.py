from damoim_service.command.PostToImage import CreatePostToImageCommand


def create(form: CreatePostToImageCommand):
    from damoim_service.models import PostToImage

    return PostToImage.objects.create(
        post_id=form.post_id,
        image_url=form.image_url,
    )
