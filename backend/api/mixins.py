from .permissions import IsStaffEditor
from rest_framework.permissions import IsAdminUser

class IsStaffEditorMixin():
    permission_class = [IsStaffEditor, IsAdminUser]


class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff:
            return qs
        return qs.filter(**lookup_data)

