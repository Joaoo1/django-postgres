from django.contrib import admin

from .models import Role, Service, Employee, Feature


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'createdAt', 'updatedAt')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'createdAt', 'updatedAt')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'active', 'createdAt', 'updatedAt')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'active', 'createdAt', 'updatedAt')
