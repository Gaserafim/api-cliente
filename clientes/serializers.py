from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


    def validate(self, data):
        if not cpf_valido(data["cpf"]):
            raise serializers.ValidationError({"cpf": "Digite um CPF válido!"})

        if not nome_valido(data["nome"]):
            raise serializers.ValidationError(
                {"nome": "Impossível inserir números neste campo!"}
            )

        if not rg_valido(data["rg"]):
            raise serializers.ValidationError({"rg": "O RG deve conter 9 digítos!"})

        if not celular_valido(data["celular"]):
            raise serializers.ValidationError(
                {"celular": "O celular deve conter 11 digítos, considerando o modelo: xx xxxxx-xxxx."}
            )

        return data
