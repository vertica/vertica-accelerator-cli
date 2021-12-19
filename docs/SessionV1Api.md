# openapi_client.SessionV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_sessions_dbname_delete**](SessionV1Api.md#v1_vaas_sessions_dbname_delete) | **DELETE** /v1/vaas/sessions/{dbname} | 
[**v1_vaas_sessions_dbname_get**](SessionV1Api.md#v1_vaas_sessions_dbname_get) | **GET** /v1/vaas/sessions/{dbname} | 


# **v1_vaas_sessions_dbname_delete**
> InlineResponse200 v1_vaas_sessions_dbname_delete(dbname, body=body)



Delete session with specific seesion id.

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
    api_instance = openapi_client.SessionV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject25() # InlineObject25 |  (optional)

    try:
        api_response = api_instance.v1_vaas_sessions_dbname_delete(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SessionV1Api->v1_vaas_sessions_dbname_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject25**](InlineObject25.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success deleted |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_sessions_dbname_get**
> InlineResponse200 v1_vaas_sessions_dbname_get(dbname, node_name=node_name)



Get a list of sessions from certain database.

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
    api_instance = openapi_client.SessionV1Api(api_client)
    dbname = 'dbname_example' # str | 
node_name = 'all' # str |  (optional) (default to 'all')

    try:
        api_response = api_instance.v1_vaas_sessions_dbname_get(dbname, node_name=node_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SessionV1Api->v1_vaas_sessions_dbname_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **node_name** | **str**|  | [optional] [default to &#39;all&#39;]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

