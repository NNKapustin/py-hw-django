from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.is_superuser: # оставлена проверка на суперпользователя, т.к.
        # по условию задания нужно проверять на админа, но группы мы не назначали, ниже вариант с группами
        # if request.user.groups.filter(name='admin').exists():
            return True
        return request.user == obj.creator
