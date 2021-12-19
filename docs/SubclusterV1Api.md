# openapi_client.SubclusterV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_dbname_subclusters_delete**](SubclusterV1Api.md#v1_vaas_databases_dbname_subclusters_delete) | **DELETE** /v1/vaas/databases/{dbname}/subclusters | 
[**v1_vaas_databases_dbname_subclusters_post**](SubclusterV1Api.md#v1_vaas_databases_dbname_subclusters_post) | **POST** /v1/vaas/databases/{dbname}/subclusters | 


# **v1_vaas_databases_dbname_subclusters_delete**
> InlineResponse2001 v1_vaas_databases_dbname_subclusters_delete(dbname, body=body)



Terminates instances and drops an existing subcluster.

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
    api_instance = openapi_client.SubclusterV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject20() # InlineObject20 |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_subclusters_delete(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubclusterV1Api->v1_vaas_databases_dbname_subclusters_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject20**](InlineObject20.md)|  | [optional] 

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
**200** | Delete subcluster request accepted |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_databases_dbname_subclusters_post**
> InlineResponse2001 v1_vaas_databases_dbname_subclusters_post(dbname, body=body)



Provisions new instances and creates a new subcluster

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
    api_instance = openapi_client.SubclusterV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject19() # InlineObject19 |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_subclusters_post(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubclusterV1Api->v1_vaas_databases_dbname_subclusters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject19**](InlineObject19.md)|  | [optional] 

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
**200** | Create subcluster request accepted |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

