import time
import random

import azure.functions as func
import azure.durable_functions as df

myApp = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# An HTTP-triggered function with a Durable Functions client binding
@myApp.route(route="orchestrators/hello_orchestrator")
@myApp.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    # Hardcode the orchestrator function name to match the defined orchestrator
    function_name = "hello_orchestrator"
    instance_id = await client.start_new(function_name)
    response = client.create_check_status_response(req, instance_id)
    return response

# Orchestrator
@myApp.orchestration_trigger(context_name="context")
def hello_orchestrator(context):
    result1 = yield context.call_activity("hello", "Seattle")
    result2 = yield context.call_activity("hello", "Tokyo")
    result3 = yield context.call_activity("hello", "London")

    return [result1, result2, result3]

# Activity
@myApp.activity_trigger(input_name="city")
def hello(city: str):
    
    sleep_seconds = random.randint(60, 85)
    time.sleep(sleep_seconds)
    
    return f"Hello {city}"