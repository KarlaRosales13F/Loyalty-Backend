# loyaltee/serializers/user.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from loyaltee.models import UserProfile, PuntosFidelizacion


class RegisterSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    telefono = serializers.CharField(max_length=30, required=False, allow_blank=True)
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(write_only=True)
    rol = serializers.CharField(max_length=30, default='cliente')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este email ya está registrado.')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Las contraseñas no coinciden.'})
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        telefono = validated_data.pop('telefono', '')
        rol = validated_data.pop('rol', 'cliente')
        nombre = validated_data.pop('nombre')
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=nombre,
            password=validated_data['password'],
            is_staff=(rol != 'cliente'),
        )
        UserProfile.objects.create(user=user, telefono=telefono, rol=rol)
        PuntosFidelizacion.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    # Campos mapeados para compatibilidad con Android
    username = serializers.CharField(source='email', read_only=True)
    nombre = serializers.CharField(source='first_name', read_only=True)
    apellido = serializers.CharField(source='last_name', read_only=True)
    correo = serializers.CharField(source='email', read_only=True)
    firstName = serializers.CharField(source='first_name', read_only=True)
    lastName = serializers.CharField(source='last_name', read_only=True)
    telefono = serializers.SerializerMethodField()
    rol = serializers.SerializerMethodField()
    fecha_registro = serializers.DateTimeField(source='date_joined', read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    num_orders = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'nombre', 'apellido', 'correo',
            'firstName', 'lastName', 'telefono', 'rol', 'fecha_registro',
            'date_joined', 'is_staff', 'is_active', 'num_orders',
        ]
        read_only_fields = fields

    def get_telefono(self, obj):
        return getattr(getattr(obj, 'profile', None), 'telefono', '')

    def get_rol(self, obj):
        return getattr(getattr(obj, 'profile', None), 'rol', 'cliente')

    def get_num_orders(self, obj):
        # Contar compras del usuario si la relación existe
        if hasattr(obj, 'compras'):
            return obj.compras.count()
        return 0


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['telefono', 'rol']
        read_only_fields = ['rol']


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(min_length=8, write_only=True)
    new_password2 = serializers.CharField(write_only=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('La contraseña actual es incorrecta.')
        return value

    def validate(self, data):
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': 'Las contraseñas no coinciden.'})
        validate_password(data['new_password'])
        return data
