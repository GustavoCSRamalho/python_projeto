from .modelo.cep  import Cep
from .servico.coletarDadosPagina import ColetarDadosPagina
from .servico.formatarDadosEndereco import FormatarDadosEndereco
from .servico.manipuladorDeErros import ManipuladorDeErros
from .servico.formatarResposta import FormatarResposta

def cep_json_xml(cep, formato):
    cep = Cep(cep,"","","buscarCep")
    formato = formato.lower()
    coletarDadosPagina = ColetarDadosPagina(cep,"http://m.correios.com.br/movel/buscaCepConfirma.do")
    try:
        values = coletarDadosPagina.obterValoresDaPagina()
        formatarDadosEndereco = FormatarDadosEndereco(values)
        if len(values) > 2:
            resultado = 1
            resultado_txt = "Sucesso cep completo"
            endereco = formatarDadosEndereco.cepCompleto()
        elif len(values) < 2:
            resultado = 2
            resultado_txt = "Sucesso cep unico"
            endereco = formatarDadosEndereco.cepUnico()
        else:
            resultado_txt = "Serviço indisponivel ou cep invalido"
    except:
        retorno = ManipuladorDeErros().manipularDeErros()
        return retorno,formato

    formatarResposta = FormatarResposta() 
    retorno = formatarResposta.retornarResultadoFormatado(resultado,resultado_txt,endereco)

    return retorno,formato