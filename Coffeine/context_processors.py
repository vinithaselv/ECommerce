from .models import userModel

def user_context(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = userModel.objects.get(id=user_id)
            return {
                'username': user.username,
                'user_img': user.user_img.url if user.user_img else None
                }
        except userModel.DoesNotExist:
            return {
                'username': None,
                'user_img': None
                }
    return {
        'username': None,
        'user_img': None
        }