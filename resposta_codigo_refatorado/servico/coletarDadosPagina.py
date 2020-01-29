from ..modelo.cep import Cep

class ColetarDadosPagina:
    def __init__(self, cep, url):
        self.cep = cep
        self.url = url

    def formatarDados(self):
        return {
        'cepEntrada': self.cep.cepEntrada,
        'tipoCep': self.cep.tipoCep,
        'cepTemp': self.cep.cepTemp,
        'metodo': self.cep.metodo
    }

    def dadosCodificados(self):
        return urllib2.urlencode(this.formatarDados())

    def dadosDaPagina(self):
        request_object = urllib2.Request(self.url,dadosCodificados)
        response = urllib2.urlopen(request_object)
        return result = response.read()
    
    def obterValoresDaPagina(self):
        soup = BeautifulSoup(this.dadosDaPagina)
        values = soup.select(".caixacampobranco span.respostadestaque")
        return values

    

