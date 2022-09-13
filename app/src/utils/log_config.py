

import traceback

def registrar_log(codigo_log, mensagem, nivel="INFO", exception=None):
    log_message = f"{codigo_log} - {nivel} - {mensagem}"
    if exception:
        trace_message = traceback.format_exc()
        log_message = f"{log_message} - {trace_message} - {str(exception)}"
    print(log_message)