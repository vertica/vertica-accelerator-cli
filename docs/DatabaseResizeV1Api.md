# openapi_client.DatabaseResizeV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_dbname_resize_decrease_put**](DatabaseResizeV1Api.md#v1_vaas_databases_dbname_resize_decrease_put) | **PUT** /v1/vaas/databases/{dbname}/resize/decrease | 
[**v1_vaas_databases_dbname_resize_increase_put**](DatabaseResizeV1Api.md#v1_vaas_databases_dbname_resize_increase_put) | **PUT** /v1/vaas/databases/{dbname}/resize/increase | 


# **v1_vaas_databases_dbname_resize_decrease_put**
> InlineResponse2001 v1_vaas_databases_dbname_resize_decrease_put(dbname, body=body)



Decrease the number of nodes for the database.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatabaseResizeV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject16() # InlineObject16 |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_resize_decrease_put(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseResizeV1Api->v1_vaas_databases_dbname_resize_decrease_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject16**](InlineObject16.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resize request accepted |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_databases_dbname_resize_increase_put**
> InlineResponse2001 v1_vaas_databases_dbname_resize_increase_put(dbname, body=body)



Increase the number of nodes for the database.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatabaseResizeV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject17() # InlineObject17 |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_resize_increase_put(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseResizeV1Api->v1_vaas_databases_dbname_resize_increase_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject17**](InlineObject17.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resize request accepted |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

