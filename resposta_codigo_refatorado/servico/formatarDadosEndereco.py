from ..modelo.endereco import Endereco

class FormatarDadosEndereco:
    def __init__(self, dados):
        self.dados = dados
        self.endereco = Endereco()
    
    def cepCompleto(self):
        listDeLogradouros = (self.dados[0].text.strip()).split('-')
        self.endereco.logradouro = listDeLogradouros[0]

        self.endereco.bairro = self.dados[1].text.strip()
        cidade_estado = self.dados[2].text.split()
        this.formatarCidadeEEstado(cidade_estado)
        self.endereco.cep = self.dados[3].text.strip()

        return self.endereco

    def cepUnico(self):
        cidade_estado = self.dados[0].get_text().split()
        this.formatarCidadeEEstado(cidade_estado)
        self.endereco.cep = self.dados[1].get_text().split()
        return self.endereco

    def formatarCidadeEEstado(self,cidade_estado):
        self.endereco.cidade = cidade_estado[0]
        self.endereco.estado = cidade_estado[1].split('/')
