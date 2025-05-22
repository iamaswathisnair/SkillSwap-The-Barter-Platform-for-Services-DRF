from rest_framework.permissions import BasePermission

class IsCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'company_owner'

class IsLegalTeam(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'legal_team'

class IsInvestigator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'investigator'

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'employee'
