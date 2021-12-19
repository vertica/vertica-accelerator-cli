# openapi_client.DatabaseDetailV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_dbname_delete**](DatabaseDetailV1Api.md#v1_vaas_databases_dbname_delete) | **DELETE** /v1/vaas/databases/{dbname} | 
[**v1_vaas_databases_dbname_get**](DatabaseDetailV1Api.md#v1_vaas_databases_dbname_get) | **GET** /v1/vaas/databases/{dbname} | 
[**v1_vaas_databases_dbname_put**](DatabaseDetailV1Api.md#v1_vaas_databases_dbname_put) | **PUT** /v1/vaas/databases/{dbname} | 


# **v1_vaas_databases_dbname_delete**
> InlineResponse2001 v1_vaas_databases_dbname_delete(dbname)



Terminates instances and Drops an existing database.

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
    api_instance = openapi_client.DatabaseDetailV1Api(api_client)
    dbname = 'dbname_example' # str | 

    try:
        api_response = api_instance.v1_vaas_databases_dbname_delete(dbname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseDetailV1Api->v1_vaas_databases_dbname_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 

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
**200** | Delete request accepted |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_databases_dbname_get**
> InlineResponse200 v1_vaas_databases_dbname_get(dbname)



Returns the instance states and details about a specific database including subclusters.

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
    api_instance = openapi_client.DatabaseDetailV1Api(api_client)
    dbname = 'dbname_example' # str | 

    try:
        api_response = api_instance.v1_vaas_databases_dbname_get(dbname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseDetailV1Api->v1_vaas_databases_dbname_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 

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

# **v1_vaas_databases_dbname_put**
> InlineResponse200 v1_vaas_databases_dbname_put(dbname, body=body)



Starts instances and then starts the database. Stops instances and then stops the database.

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
    api_instance = openapi_client.DatabaseDetailV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject11() # InlineObject11 |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_put(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseDetailV1Api->v1_vaas_databases_dbname_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject11**](InlineObject11.md)|  | [optional] 

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
**202** | Success updated |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

