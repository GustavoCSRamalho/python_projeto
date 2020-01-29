class ManipuladorDeErros:
    def __init__(self):

    def manipularDeErros():
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file = exc_tb.tb_frame.f_code.co_filename
        return json.dumps({
            'msg': 'type:%s, error: %s,file: %s,line: %s' % (exc_type,exc_obj,file,exc_tb.tb_lineno)
        })