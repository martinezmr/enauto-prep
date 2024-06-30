import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="MerakiWebhook")
## req is the trigger, msg is the output
def MerakiWebhook(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> str:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sharedSecret = req_body.get('sharedSecret')

    if sharedSecret == 'foo':
        msg.set(json.dumps(req_body))
        return func.HttpResponse(body=json.dumps(req_body,
                                                 status_code=200,
                                                 headers={"Content-Type": "application/json"}))
    else:
        return func.HttpResponse(
             "Please supply correct shared secret.",
             status_code=401
        )