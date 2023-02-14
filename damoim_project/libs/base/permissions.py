from rest_framework.permissions import BasePermission

class DamoimUser(BasePermission):
    def has_permission(self, request, view):
        """
        Todo 유저인지 아닌지 확인하는 조건문 필요
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Todo 유저인지 아닌지 확인하는 조건문 필요
        """
        return True

class DamoimGroupManager(BasePermission):
    def has_permission(self, request, view):
        """
        Todo 그룹에 가입되어 있는 사람들 중에서 방장인지 아닌지 확인하는 조건문 필요
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Todo 그룹에 가입되어 있는 사람들 중에서 방장인지 아닌지 확인하는 조건문 필요
        """
        return True

class DamoimBankingPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Todo 로그인한 유저가 접근하는 계좌의 소유주인지 확인하는 로직 필요
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Todo 로그인한 유저가 접근하는 계좌의 소유주인지 확인하는 로직 필요
        """
        return True

