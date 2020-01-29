def cep_json_xml(cep, formato):
    cepEntrada = cep
    tipoCep =""
    cepTemp =""
    metodo ="buscarCep"
    formato = formato.lower()
    url = "http://m.correios.com.br/movel/buscaCepConfirma.do"
    post_data_dictionary = {
        'cepEntrada': cepEntrada,
        'tipoCep': tipoCep,
        'cepTemp': cepTemp,
        'metodo': metodo
    }

    post_data_encoded = urllib2.urlencode(post_data_dictionary)
    try:
        request_object = urllib2.Request(url,post_data_encoded)
        response = urllib2.urlopen(request_object)
        result = response.read()
        soup = BeautifulSoup(result)
        values = soup.select(".caixacampobranco span.respostadestaque")

        if len(values) > 2:
            resultado = 1
            resultado_txt = "Sucesso cep completo"

            logradouro = (values[0].text.strip()).split('-')
            logradouro = logradouro[0]

            bairro = values[1].text.strip()
            cidade_estado = values[2].text.split()
            cidade = cidade_estado[0]
            estado = cidade_estado[1].strip('/')
            cep = values[3].text.strip()
        elif len(values) < 2:
            resultado = 2
            resultado_txt = "Sucesso cep unico"
            logradouro = ""
            bairro = ""
            cidade_estado = values[0].get_text().split()
            cidade = cidade_estado[0]
            estado = cidade_estado[1].split('/')
            cep = values[1].get_text().split()
        else:
            resultado_txt = "Serviço indisponivel ou cep invalido"
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file = exc_tb.tb_frame.f_code.co_filename
        retorno = json.dumps({
            'msg': 'type:%s, error: %s,file: %s,line: %s' % (exc_type,exc_obj,file,exc_tb.tb_lineno)
        })
        return retorno,formato
    dict_json = {
            'resultado':resultado,
            'resultado_txt':resultado_txt,
            'logradouro':logradouro,
            'bairro':bairro,
            'cidade':cidade,
            'uf': estado,
            'cep': cep
    }

    if formato == 'json':
        retorno = json.dumps(dict_json)
    elif formato == 'xml':
        retorno = open(os.path.join(os.path.dirname(__file__), 'cep.xml'),'r').read()%dict_json
    else:
        retorno = "Opção não existe"
    return retorno,formato