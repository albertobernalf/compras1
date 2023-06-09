# Generated by Django 3.2 on 2023-04-18 15:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(default='', max_length=80)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codregArticulo', models.CharField(max_length=30, unique=True)),
                ('articulo', models.CharField(blank=True, max_length=300, null=True)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='DescripcionCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='EstadosAlmacen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='EstadosValidacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenesCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaElab', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaRevi', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('fechaApro', models.DateTimeField(default=django.utils.timezone.now)),
                ('estadoOrden', models.CharField(choices=[('V', 'Vigente'), ('C', 'Caduca')], default='A', max_length=1)),
                ('contacto', models.CharField(default='', max_length=120)),
                ('entregarEn', models.CharField(default='', max_length=120)),
                ('telefono', models.CharField(default='', max_length=30)),
                ('opciones', models.CharField(choices=[('C', 'Contra entrega'), ('A', 'Anticipo'), ('N', 'Noventa dias')], default='A', max_length=1)),
                ('valorBruto', models.DecimalField(decimal_places=2, max_digits=20)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=20)),
                ('valorParcial', models.DecimalField(decimal_places=2, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=20)),
                ('valorTotal', models.DecimalField(decimal_places=2, max_digits=20)),
                ('observaciones', models.CharField(default='', max_length=300)),
                ('estadoReg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codreg_proveedor', models.CharField(max_length=50, unique=True)),
                ('proveedor', models.CharField(max_length=80, unique=True)),
                ('nit', models.CharField(default='', max_length=30, unique=True)),
                ('direccion', models.CharField(default='', max_length=80)),
                ('telefono', models.CharField(default=0, max_length=30)),
                ('correo', models.EmailField(max_length=200)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='SedesCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codreg_sede', models.CharField(default='', max_length=30)),
                ('nom_sede', models.CharField(default='', max_length=30)),
                ('codreg_ips', models.CharField(default='', max_length=30)),
                ('direccion', models.CharField(default='', max_length=200)),
                ('telefono', models.CharField(default='', max_length=120)),
                ('departamento', models.CharField(default='', max_length=120)),
                ('municipio', models.CharField(default='', max_length=120)),
                ('zona', models.CharField(default='', max_length=120)),
                ('sede', models.CharField(default='', max_length=120)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
            options={
                'unique_together': {('codreg_sede', 'nom_sede')},
            },
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aareasSolicitudes', to='solicitud.areas')),
            ],
        ),
        migrations.CreateModel(
            name='TiposCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_identificacion', models.CharField(max_length=30)),
                ('nom_usuario', models.CharField(max_length=150)),
                ('clave_usuario', models.CharField(max_length=20)),
                ('carg_usuario', models.CharField(max_length=80)),
                ('perfil', models.CharField(choices=[('C', 'Compras'), ('A', 'Almacen'), ('V', 'Validacion'), ('S', 'Solicitud')], default='S', max_length=1)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('sede', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ssedesCompra', to='solicitud.sedescompra')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_identificacion', models.CharField(max_length=30)),
                ('nom_usuario', models.CharField(max_length=150)),
                ('clave_usuario', models.CharField(max_length=20)),
                ('carg_usuario', models.CharField(max_length=80)),
                ('perfil', models.CharField(choices=[('G', 'Gerencia')], default='S', max_length=1)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('sede', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ssedesCompra7', to='solicitud.sedescompra')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudesDetalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('producto', models.CharField(default='', max_length=30)),
                ('justificacion', models.CharField(default=0, max_length=250)),
                ('especificacionesTecnicas', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('especificacionesAlmacen', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('solicitadoAlmacen', models.IntegerField(default=0)),
                ('entregadoAlmacen', models.IntegerField(default=0)),
                ('adjuntoCompras', models.FileField(blank=True, null=True, upload_to='Uploaded Files/')),
                ('observacionesCompras', models.CharField(default='', max_length=300)),
                ('solicitadoOrdenCantidad', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('recibidoOrdenCantidad', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('valorUnitario', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('solicitadoOrdenValor', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('recibidoOrdenValor', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('estadoreg', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('descripcion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ddescripcion', to='solicitud.descripcioncompra')),
                ('estadosAlmacen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='eestadosAlmacen', to='solicitud.estadosalmacen')),
                ('estadosCompras', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='eestadosCompras', to='solicitud.estadosvalidacion')),
                ('estadosSolicitud', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='eestadosSolicitud', to='solicitud.estadosvalidacion')),
                ('estadosValidacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='eestadosValidacion', to='solicitud.estadosvalidacion')),
                ('ordenCompra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='oordenesCompra', to='solicitud.ordenescompra')),
                ('presentacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ppresentacion', to='solicitud.presentacion')),
                ('solicitud', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ssolicitudes', to='solicitud.solicitudes')),
                ('tiposCompra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ttipoCompra', to='solicitud.tiposcompra')),
                ('usuarioResponsableAlmacen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuariosResponsableAlmacen', to='solicitud.usuarios')),
                ('usuarioResponsableCompra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuariosResponsableCompra', to='solicitud.usuarios')),
                ('usuarioResponsableValidacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuariosResponsable', to='solicitud.usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='solicitudes',
            name='usuarios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuarios', to='solicitud.usuarios'),
        ),
        migrations.AddField(
            model_name='ordenescompra',
            name='aprobo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuariosaPROBO', to='solicitud.usuarios'),
        ),
        migrations.AddField(
            model_name='ordenescompra',
            name='aproboCompraStaff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sstaff', to='solicitud.staff'),
        ),
        migrations.AddField(
            model_name='ordenescompra',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aareasoRDENES', to='solicitud.areas'),
        ),
        migrations.AddField(
            model_name='ordenescompra',
            name='elaboro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuariosElaboro', to='solicitud.usuarios'),
        ),
        migrations.AddField(
            model_name='ordenescompra',
            name='entragaMercancia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuariosEntrega', to='solicitud.usuarios'),
        ),
        migrations.AddField(
            model_name='ordenescompra',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pproveedores', to='solicitud.proveedores'),
        ),
        migrations.AddField(
            model_name='ordenescompra',
            name='recibeMercancia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuariosRecibe', to='solicitud.usuarios'),
        ),
        migrations.AddField(
            model_name='ordenescompra',
            name='responsableCompra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuariosResp', to='solicitud.usuarios'),
        ),
        migrations.AddField(
            model_name='ordenescompra',
            name='revizo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uusuariosrEVIZO', to='solicitud.usuarios'),
        ),
        migrations.AddField(
            model_name='areas',
            name='sede',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ssedesArea', to='solicitud.sedescompra'),
        ),
    ]
