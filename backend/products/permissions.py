from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        print(request.user.get_all_permissions())
        if request.user.is_staff:
            return True
        return False
