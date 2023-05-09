from rest_framework.permissions import BasePermission
class IsInGroup_ahmashim(BasePermission):
    def has_permission(self, request, view):
        groups = self.get_groups(view)
        if not groups:
            return True
        user_groups = request.user.groups.values_list('name', flat=True)
        return bool(set(groups).intersection(user_groups))

    def get_groups(self, view):
        return getattr(view, 'allowed_groups', ['Ahmashim'])

class IsInGroup_tehnaim(BasePermission):
    def has_permission(self, request, view):
        groups = self.get_groups(view)
        if not groups:
            return True
        user_groups = request.user.groups.values_list('name', flat=True)
        return bool(set(groups).intersection(user_groups))

    def get_groups(self, view):
        return getattr(view, 'allowed_groups', ['Tehnaim','Ahmashim'])
