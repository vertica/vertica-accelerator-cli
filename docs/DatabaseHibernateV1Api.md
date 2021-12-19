# openapi_client.DatabaseHibernateV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_dbname_hibernate_put**](DatabaseHibernateV1Api.md#v1_vaas_databases_dbname_hibernate_put) | **PUT** /v1/vaas/databases/{dbname}/hibernate | 


# **v1_vaas_databases_dbname_hibernate_put**
> InlineResponse2001 v1_vaas_databases_dbname_hibernate_put(dbname)



Hibernates the database.

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
    api_instance = openapi_client.DatabaseHibernateV1Api(api_client)
    dbname = 'dbname_example' # str | 

    try:
        api_response = api_instance.v1_vaas_databases_dbname_hibernate_put(dbname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseHibernateV1Api->v1_vaas_databases_dbname_hibernate_put: %s\n" % e)
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
**200** | Hibernate request accepted |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

