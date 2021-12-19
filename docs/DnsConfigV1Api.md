# openapi_client.DnsConfigV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_dns_dbname_delete**](DnsConfigV1Api.md#v1_vaas_dns_dbname_delete) | **DELETE** /v1/vaas/dns/{dbname} | 
[**v1_vaas_dns_dbname_get**](DnsConfigV1Api.md#v1_vaas_dns_dbname_get) | **GET** /v1/vaas/dns/{dbname} | 
[**v1_vaas_dns_dbname_post**](DnsConfigV1Api.md#v1_vaas_dns_dbname_post) | **POST** /v1/vaas/dns/{dbname} | 


# **v1_vaas_dns_dbname_delete**
> InlineResponse200 v1_vaas_dns_dbname_delete(dbname, body=body)



Delete a single DNS (A) record by name.

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
    api_instance = openapi_client.DnsConfigV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject23() # InlineObject23 |  (optional)

    try:
        api_response = api_instance.v1_vaas_dns_dbname_delete(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsConfigV1Api->v1_vaas_dns_dbname_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject23**](InlineObject23.md)|  | [optional] 

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
**200** | Successfully deleted |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_dns_dbname_get**
> InlineResponse200 v1_vaas_dns_dbname_get(dbname, dnsname=dnsname)



List DNS records of the vertica clusters.

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
    api_instance = openapi_client.DnsConfigV1Api(api_client)
    dbname = 'dbname_example' # str | 
dnsname = 'dnsname_example' # str | DNS name to get particular record. (optional)

    try:
        api_response = api_instance.v1_vaas_dns_dbname_get(dbname, dnsname=dnsname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsConfigV1Api->v1_vaas_dns_dbname_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **dnsname** | **str**| DNS name to get particular record. | [optional] 

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
**404** | Not Found |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_dns_dbname_post**
> InlineResponse200 v1_vaas_dns_dbname_post(dbname, body=body)



Creates or Updates DNS (A) record for the cluster(s).

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
    api_instance = openapi_client.DnsConfigV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject22() # InlineObject22 |  (optional)

    try:
        api_response = api_instance.v1_vaas_dns_dbname_post(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsConfigV1Api->v1_vaas_dns_dbname_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject22**](InlineObject22.md)|  | [optional] 

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
**201** | Successfully Created |  -  |
**400** | Bad Request |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

