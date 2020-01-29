class FormatarResposta:
    def __init__(self):

    def retornarResultadoFormatado(resultado, resultado_txt, endereco):
        dict_json = {
            'resultado':resultado,
            'resultado_txt':resultado_txt,
            'logradouro':endereco.logradouro,
            'bairro':endereco.bairro,
            'cidade':endereco.cidade,
            'uf': endereco.estado,
            'cep': endereco.cep
        }

        if formato == 'json':
            return json.dumps(dict_json)
        elif formato == 'xml':
            return open(os.path.join(os.path.dirname(__file__), 'cep.xml'),'r').read()%dict_json
        else:
            return "Opção não existe"