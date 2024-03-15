from django.db import models



class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    valor = models.IntegerField()
    data_validade = models.DateField()
    estoque = models.IntegerField()


    def __str__(self):
        return self.nome



class Dados_Usuario(models.Model):
        endereco = models.CharField(max_length=200)
        numero = models.IntegerField()
        rua = models.CharField(max_length=100)
        cidade = models.CharField(max_length=100)
        bairro = models.CharField(max_length=100)
        estado = models.CharField(max_length=2)
        cpf = models.IntegerField()

        def __str__(self):
            return self.rua


class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.IntegerField()

    def __str__(self):
        return self.nome


