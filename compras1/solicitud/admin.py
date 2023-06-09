from django.contrib import admin
from django import forms

# Register your models here.

from solicitud.models import SedesCompra, Staff, Usuarios, TiposCompra, EstadosValidacion,EstadosAlmacen, Presentacion, DescripcionCompra, Proveedores, Areas, Solicitudes, SolicitudesDetalle, OrdenesCompra, Articulos
#from solicitud.models import SedesCompra, Staff, Usuarios, TiposCompra, EstadosValidacion,EstadosAlmacen, Presentacion, DescripcionCompra, Proveedores, Areas, Solicitudes, SolicitudesDetalle, OrdenesCompra, Articulos
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(SedesCompra)
class sedesCompraAdmin(admin.ModelAdmin):
    list_display = ("id", "codreg_sede", "nom_sede", "codreg_ips", "direccion", "telefono", "departamento", "municipio")
    search_fields = (
    "id", "codreg_sede", "nom_sede", "codreg_ips", "direccion", "telefono", "departamento", "municipio")
    # Filtrar

    list_filter = ("id", "codreg_sede", "nom_sede", "codreg_ips", "direccion", "telefono", "departamento", "municipio")

    def has_delete_permission(self, request, obj=None):
        return False


    def get_actions(self, request):
        actions = super(sedesCompraAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Usuarios)
class usuariosAdmin(admin.ModelAdmin):
    list_display =( "num_identificacion" ,"nom_usuario","carg_usuario","sede","estadoreg" )
    search_fields = ( "num_identificacion" ,"nom_usuario","carg_usuario","sede_id__nom_sede","estadoreg" )

    list_filter = ( "num_identificacion" ,"nom_usuario","carg_usuario","sede","estadoreg" )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Staff)
class staffAdmin(admin.ModelAdmin):
    list_display =( "num_identificacion" ,"nom_usuario","carg_usuario","sede","estadoreg" )
    search_fields = ( "num_identificacion" ,"nom_usuario","carg_usuario","sede_id__nom_sede","estadoreg" )

    list_filter = ( "num_identificacion" ,"nom_usuario","carg_usuario","sede","estadoreg" )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TiposCompra)
class tiposCompraAdmin(admin.ModelAdmin):

    list_display = ("nombre", "descripcion", "estadoreg")
    search_fields = ("nombre", "descripcion", "estadoreg")
    list_filter = ("nombre", "descripcion", "estadoreg")

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(EstadosValidacion)
class estadosValidacionAdmin(admin.ModelAdmin):

    list_display = ("nombre", "estadoreg")
    search_fields = ("nombre", "estadoreg")
    list_filter = ("nombre", "estadoreg")

    def has_delete_permission(self, request, obj=None):
        return False



    def has_change_permission(self, request, obj=None):
        return False

@admin.register(EstadosAlmacen)
class estadosAlmacenAdmin(admin.ModelAdmin):
        list_display = ("nombre", "estadoreg")
        search_fields = ("nombre", "estadoreg")
        list_filter = ("nombre", "estadoreg")

        def has_delete_permission(self, request, obj=None):
            return False



        def has_change_permission(self, request, obj=None):
            return False

@admin.register(Presentacion)
class presentacionAdmin(admin.ModelAdmin):

    list_display = ("nombre", "descripcion", "estadoreg")
    search_fields = ("nombre", "descripcion", "estadoreg")
    list_filter = ("nombre",  "descripcion","estadoreg")

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(DescripcionCompra)
class descripcionCompraAdmin(admin.ModelAdmin):

    list_display = ("nombre", "descripcion", "estadoreg")
    search_fields = ("nombre", "descripcion", "estadoreg")
    list_filter = ("nombre",  "descripcion","estadoreg")

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Proveedores)
class proveedoresAdmin(admin.ModelAdmin):

    list_display = ("codreg_proveedor", "proveedor","nit","direccion", "telefono", "correo", "estadoreg")
    search_fields = ("codreg_proveedor", "proveedor","nit","direccion", "telefono", "correo", "estadoreg")
    list_filter = ("codreg_proveedor", "proveedor","nit","direccion", "telefono", "correo", "estadoreg")

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Areas)
class areasAdmin(admin.ModelAdmin):

    list_display = ("sede", "area", "estadoreg")
    search_fields = ( "area","sede_id__nom_sede", "estadoreg")
    list_filter = ("sede", "area", "estadoreg")

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Articulos)
class articulosAdmin(admin.ModelAdmin):

    list_display = ("codregArticulo", "articulo", "estadoreg")
    search_fields = ("codregArticulo", "articulo", "estadoreg")
    list_filter = ("codregArticulo", "articulo", "estadoreg")

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Solicitudes)
class solicitudesAdmin(admin.ModelAdmin):

    list_display = ("id", "fecha", "usuarios", "area", "estadoreg")
    search_fields = ("id", "fecha","area_id__area",  "estadoreg")
    list_filter = ("id", "fecha", "usuarios", "area", "estadoreg")

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(SolicitudesDetalle)
class solicitudesDetalleAdmin(admin.ModelAdmin):

    list_display = ("id", "solicitud", "item", "descripcion", "tiposCompra","cantidad","presentacion","producto","justificacion","estadosSolicitud","usuarioResponsableValidacion","especificacionesTecnicas","estadosValidacion","observacionesCompras")
    search_fields = ["id", "item", "descripcion_id__nombre", "tiposCompra_id__nombre","cantidad","presentacion_id__nombre","producto","justificacion","especificacionesTecnicas","observacionesCompras"]
    list_filter = ("id","solicitud", "item", "descripcion", "tiposCompra","cantidad","presentacion","producto","justificacion","estadosSolicitud","usuarioResponsableValidacion","especificacionesTecnicas","estadosValidacion","observacionesCompras")

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(OrdenesCompra)
class ordenesCompraAdmin(admin.ModelAdmin):

    list_display = ("id", "fechaElab", "fechaRevi", "fechaApro","estadoOrden","observaciones")
    search_fields = ("id", "fechaElab", "fechaRevi", "fechaApro","estadoOrden","observaciones")
    list_filter = ("id", "fechaElab", "fechaRevi", "fechaApro","estadoOrden","observaciones")

    readonly_fields = ["elaboro", "aprobo", "revizo","area"]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False