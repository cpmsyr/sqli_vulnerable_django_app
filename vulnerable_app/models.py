from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
        id = models.BigAutoField(primary_key=True)
        group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
        permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

        class Meta:
            managed = False
            db_table = 'auth_group_permissions'
            unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
                name = models.CharField(max_length=255)
                content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
                codename = models.CharField(max_length=100)

                class Meta:
                    managed = False
                    db_table = 'auth_permission'
                    unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boat(models.Model):
    hid = models.CharField(primary_key=True, max_length=12)
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    displacement = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('BoatType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'boat'


class BoatType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boat_type'


class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    invoice_date = models.DateField(blank=True, null=True)
    cid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class Motor(models.Model):
    hid = models.OneToOneField(Boat, models.DO_NOTHING, db_column='hid', primary_key=True)
    engine_type = models.CharField(max_length=50, blank=True, null=True)
    cylinders = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'motor'


class Part(models.Model):
    part_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    heavy_use = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part'


class RepairJob(models.Model):
    repair_id = models.IntegerField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, blank=True, null=True)
    repair_description = models.CharField(max_length=100, blank=True, null=True)
    hours_labor = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hid = models.ForeignKey(Boat, models.DO_NOTHING, db_column='hid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_job'


class RepairParts(models.Model):
    sequence_id = models.IntegerField(primary_key=True)
    repair = models.ForeignKey(RepairJob, models.DO_NOTHING, blank=True, null=True)
    part = models.ForeignKey(Part, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_parts'


class Row(models.Model):
    hid = models.OneToOneField(Boat, models.DO_NOTHING, db_column='hid', primary_key=True)
    oars = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'row'


class Sail(models.Model):
    hid = models.OneToOneField(Boat, models.DO_NOTHING, db_column='hid', primary_key=True)
    mast_height = models.IntegerField(blank=True, null=True)
    sail_area = models.IntegerField(blank=True, null=True)
    draft = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sail'


class Vendors(models.Model):
    vendor_id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=20, blank=True, null=True)
    part_number = models.ForeignKey(Part, models.DO_NOTHING, db_column='part_number', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendors'

