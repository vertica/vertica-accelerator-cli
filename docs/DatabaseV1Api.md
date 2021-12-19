# openapi_client.DatabaseV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_get**](DatabaseV1Api.md#v1_vaas_databases_get) | **GET** /v1/vaas/databases | 
[**v1_vaas_databases_post**](DatabaseV1Api.md#v1_vaas_databases_post) | **POST** /v1/vaas/databases | 


# **v1_vaas_databases_get**
> InlineResponse200 v1_vaas_databases_get(brief=brief)



Returns a list of databases, their properties, instances, and current status.

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
    api_instance = openapi_client.DatabaseV1Api(api_client)
    brief = True # bool | If unset or set to true, only database names will be returned. (optional)

    try:
        api_response = api_instance.v1_vaas_databases_get(brief=brief)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseV1Api->v1_vaas_databases_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brief** | **bool**| If unset or set to true, only database names will be returned. | [optional] 

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

# **v1_vaas_databases_post**
> InlineResponse2001 v1_vaas_databases_post(body=body)



Provisions instances and creates a new database.

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
    api_instance = openapi_client.DatabaseV1Api(api_client)
    body = openapi_client.InlineObject8() # InlineObject8 |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_post(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseV1Api->v1_vaas_databases_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject8**](InlineObject8.md)|  | [optional] 

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
**200** | Success |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

